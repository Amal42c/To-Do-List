from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal", "normal"
    elif 25 <= bmi < 29.9:
        return "Overweight", "overweight"
    else:
        return "Obese", "obese"

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None
    css_class = None

    if request.method == 'POST':
        try:
            height = float(request.form['height'])
            weight = float(request.form['weight'])
            bmi = calculate_bmi(weight, height)
            category, css_class = get_bmi_category(bmi)
        except (ValueError, ZeroDivisionError):
            bmi = None
            category = "Invalid input."
            css_class = "error"

    return render_template('index.html', bmi=bmi, category=category, css_class=css_class)

if __name__ == '__main__':
    app.run(debug=True)