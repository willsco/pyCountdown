from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont
import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


def generate_countdown_gif(target_date):
    images = []
    width, height = 400, 200
    font = ImageFont.truetype("arial.ttf", 24)
    max_duration = 60  # in seconds

    for i in range(max_duration):
        current_date = datetime.datetime.now()
        time_left = target_date - current_date

        if time_left.total_seconds() <= 0:
            break

        days_left = time_left.days
        hours_left, remainder = divmod(time_left.seconds, 3600)
        minutes_left, seconds_left = divmod(remainder, 60)
        image = Image.new("RGB", (width, height), color="white")
        draw = ImageDraw.Draw(image)
        text = (f"{days_left} days, {hours_left:02}:{minutes_left:02}:{seconds_left:02} "
                f"left")
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_position = ((width - text_width) // 2, (height - text_height) // 2)
        draw.text(text_position, text, fill="black", font=font)
        images.append(image)
        target_date -= datetime.timedelta(seconds=1)
    gif_filename = "countdown.gif"
    images[0].save(gif_filename, save_all=True, append_images=images[1:], duration=1000, loop=0)

    return gif_filename


@app.route('/countdown')
def countdown():
    target_date = datetime.datetime(2024, 12, 31, 23, 59, 59)
    gif_filename = generate_countdown_gif(target_date)
    return send_file(gif_filename, mimetype='image/gif')


if __name__ == '__main__':
    app.run()
