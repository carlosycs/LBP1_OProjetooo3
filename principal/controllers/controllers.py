from flask import Blueprint, render_template

simple_page = Blueprint('teste', __name__,
    template_folder='templates')

@simple_page.route('/')
def teste():
    return render_template('index.html')
