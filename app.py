from flask import Flask
from controllers.countdown_controller import countdown

app = Flask(__name__)

app.add_url_rule('/countdown', 'countdown', countdown)

if __name__ == "__main__":
    app.run(debug=True)
