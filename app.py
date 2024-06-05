from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    invested_amount = request.form.get('invested_amount')
    returned_amount = request.form.get('returned_amount')

    if not invested_amount or not returned_amount:
        error_message = "Please provide both invested amount and returned amount."
        return render_template('index.html', error=error_message)

    try:
        invested_amount = float(invested_amount)
        returned_amount = float(returned_amount)
    except ValueError:
        error_message = "Invalid input. Please provide numerical values."
        return render_template('index.html', error=error_message)

    # Calculate Percentage Gain and ROI
    percentage_gain = ((returned_amount - invested_amount) / invested_amount) * 100
    roi = (returned_amount - invested_amount) / invested_amount

    return render_template('result.html', invested_amount=invested_amount, returned_amount=returned_amount,
                           percentage_gain=percentage_gain, roi=roi)

if __name__ == '__main__':
    app.run(debug=True)
