import pymongo
client = pymongo.MongoClient("mongodb+srv://iamapurvaaryan:Apurva@cluster0.lzgwt20.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.test
print(db)
db = client['ApurvaAryan']
data = {"name":"Apurva","class":"Data Science","friend":"Anjali"}
coll_Apurva = db["my_record"]
coll_Apurva.insert_one(data)
data1 = {"mail":"apurva.aryan@outlook.com","phonenumber":"7366018523"}
coll_Apurva.insert_one(data1)
for i in coll_Apurva.find():
    print(i)