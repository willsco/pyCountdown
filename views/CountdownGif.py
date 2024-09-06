from PIL import Image, ImageDraw, ImageFont
import datetime

class CountdownGif:
    def __init__(self):
        self.width = 400
        self.height = 200
        self.font = ImageFont.truetype("arial.ttf", 24)
        self.max_duration = 30  # seconds

    def generate(self, timer):
        images = []
        for i in range(self.max_duration):
            time_left = timer.get_time_remaining()
            days_left = time_left.days
            hours_left, remainder = divmod(time_left.seconds, 3600)
            minutes_left, seconds_left = divmod(remainder, 60)
            image = Image.new("RGB", (self.width, self.height), color="white")
            draw = ImageDraw.Draw(image)
            text = (f"{days_left} days, {hours_left:02}:{minutes_left:02}:{seconds_left:02} "
                    f"left")
            text_bbox = draw.textbbox((0, 0), text, font=self.font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            text_position = ((self.width - text_width) // 2, (self.height - text_height) // 2)
            draw.text(text_position, text, fill="black", font=self.font)
            images.append(image)
            timer.target_date -= datetime.timedelta(seconds=1)

        gif_filename = "countdown.gif"
        images[0].save(gif_filename, save_all=True, append_images=images[1:], duration=1000, loop=0)

        return gif_filename
