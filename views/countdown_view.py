from PIL import Image, ImageDraw, ImageFont
import datetime


def generate_countdown_gif(target_date):
    images = []
    width, height = 400, 200
    font = ImageFont.truetype("arial.ttf", 32)

    max_duration = 60  # seconds

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
