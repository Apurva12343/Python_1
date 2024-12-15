from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])
def math_operation():
    if request.method == 'POST':
        operation = request.form['operation']  # Match 'operation' from the form
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        
        if operation == 'add':
            r = num1 + num2
            result = f'The sum of {num1} and {num2} is {r}'
        elif operation == 'subtract':
            r = num1 - num2
            result = f'The difference between {num1} and {num2} is {r}'
        elif operation == 'multiply':
            r = num1 * num2
            result = f'The product of {num1} and {num2} is {r}'
        elif operation == 'divide':
            if num2 != 0:
                r = num1 / num2
                result = f'The division of {num1} by {num2} is {r}'
            else:
                result = "Division by zero is not allowed."
        else:
            result = "Invalid operation."

        return render_template('results.html', cal_result=result)
@app.route('/postman_data', methods=['POST'])
def math_operation_json():
    if request.method == 'POST':
        operation = request.json['operation']  # Match 'operation' from the form
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        
        if operation == 'add':
            r = num1 + num2
            result = f'The sum of {num1} and {num2} is {r}'
        elif operation == 'subtract':
            r = num1 - num2
            result = f'The difference between {num1} and {num2} is {r}'
        elif operation == 'multiply':
            r = num1 * num2
            result = f'The product of {num1} and {num2} is {r}'
        elif operation == 'divide':
            if num2 != 0:
                r = num1 / num2
                result = f'The division of {num1} by {num2} is {r}'
            else:
                result = "Division by zero is not allowed."
        else:
            result = "Invalid operation."

        return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
