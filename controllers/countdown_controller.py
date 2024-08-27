from flask import send_file
from models.countdown_model import get_time_remaining
from views.countdown_view import generate_countdown_gif


def countdown():
    target_date = get_time_remaining("2024-12-31 23:59:59")

    gif_filename = generate_countdown_gif(target_date)

    return send_file(gif_filename, mimetype='image/gif')
