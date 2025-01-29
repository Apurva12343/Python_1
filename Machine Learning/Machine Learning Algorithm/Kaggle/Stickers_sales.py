import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_percentage_error, make_scorer
# Load data
train_df = pd.read_csv('/train.csv')
def extract_date_features(df):
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['day_of_week'] = df['date'].dt.dayofweek
    df['week_of_year'] = df['date'].dt.isocalendar().week
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    df['quarter'] = df['date'].dt.quarter
    return df.drop(columns=['date'])

train_df = extract_date_features(train_df)
train_df = train_df.dropna(subset=['num_sold'])

X = train_df.drop(columns=['num_sold', 'id'])
y = train_df['num_sold']
# Preprocessing
numerical_features = ['year', 'month', 'day', 'day_of_week', 'week_of_year', 'is_weekend', 'quarter']
categorical_features = ['country', 'store', 'product']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', numerical_features),
        ('cat', OrdinalEncoder(), categorical_features)
    ])
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', TransformedTargetRegressor(
        regressor=lgb.LGBMRegressor(
            objective='mae',
            random_state=42,
            n_jobs=2, 
            verbose=-1
        ),
        func=np.log,
        inverse_func=np.exp))
])
param_grid = {
    'regressor__regressor__n_estimators': [300, 500],
    'regressor__regressor__learning_rate': [0.05, 0.1],
    'regressor__regressor__max_depth': [5, 7],
    'regressor__regressor__num_leaves': [31, 63],
    'regressor__regressor__subsample': [0.8],
}
scorer = make_scorer(mean_absolute_percentage_error, greater_is_better=False)
grid_search = GridSearchCV(
    model,
    param_grid,
    cv=3,  
    scoring=scorer,
    n_jobs=1,  
    verbose=2
)
best_model = grid_search.fit(X, y)
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X)
mape = mean_absolute_percentage_error(y, y_pred)
print(f"Best Model MAPE: {mape:.4f}")
def process_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['day_of_week'] = df['date'].dt.dayofweek
    df['week_of_year'] = df['date'].dt.isocalendar().week
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    df['quarter'] = df['date'].dt.quarter
df = pd.read_csv("D:\Python\Machine Learning\Machine Learning Algorithm\Kaggle\test.csv")
test_df = process_data(df)
test_predictions = best_model.predict(test_df)
test_df['num_sold'] = test_predictions
submission = test_df[['id', 'num_sold']]
submission.to_csv("Submission_file_Apurva.csv", index=False)
print("Predictions saved to 'Submission_Apurva.csv'.")