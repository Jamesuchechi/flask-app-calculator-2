from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods= ['GET', 'POST'])
def calculator():
    
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        operator =request.form['operator']
        num2 = float(request.form['num2'])

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2
        
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by Zero"

        return render_template('calculator.html', result=result)
    return render_template('calculator.html')

if __name__=="__main__":
    app.run(debug=True)

