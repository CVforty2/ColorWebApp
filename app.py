from flask import Flask, render_template
from forms import ColorForm
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"


@app.route('/', methods=['get', 'post'])
def index():
    form = ColorForm()

    if form.validate_on_submit():
        # number_of_colors = form.number_of_colors.data
        color = generate_color()

        return render_template("home.html", form=form, color=color)

    return render_template("home.html", form=form)




def generate_color():
    color = "#"
    HEX_VALUES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    for i in range(6):
        random_int = random.randint(0, 15)
        color += HEX_VALUES[random_int]

    return color

if __name__ == "__main__":
    print(generate_color())
    app.run(debug=True)
