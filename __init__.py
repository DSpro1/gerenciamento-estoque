from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///estoque.db'
db = SQLAlchemy(app)


@app.route('/')
def menu():
    return render_template('menu.html')


if __name__ == '__main__':
    app.run(debug=True)

