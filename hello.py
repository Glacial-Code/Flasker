from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret key'
class NamerForm(FlaskForm):
    name = StringField('Whats ur name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')

#def index():
#   return "<h1>Hello World</h1>"

def index():
    first_name = 'Glacial'
    stuff = 'this is <strong>Bold</strong> Text'
    favorite_pizza = ['pepperoni', 'chesse', 'pepper']
    return render_template('index.html', first_name=first_name, stuff=stuff, favorite_pizza=favorite_pizza)

# localhost:5000/user/john
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)


# custom Error pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

# internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500


@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        
    return render_template("name.html",
                           name = name,
                           form = form)
