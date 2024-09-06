from flask import Flask
from controllers.CountdownController import CountdownController

app = Flask(__name__)

countdown_controller = CountdownController()

app.add_url_rule('/countdown', 'countdown', countdown_controller.countdown)

if __name__ == "__main__":
    app.run(debug=True)
