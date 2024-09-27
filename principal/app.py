
from flask import Flask, render_template
from model.model import vinhos
from controllers.controllers import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)

if __name__ == "__main__":
    app.run(debug=True)