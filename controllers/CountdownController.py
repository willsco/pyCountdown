from flask import send_file
from models.CountdownTimer import CountdownTimer
from views.CountdownGif import CountdownGif

class CountdownController:
    def __init__(self):
        self.target_date_str = "2024-12-31 23:59:59"
    
    def countdown(self):
        timer = CountdownTimer(self.target_date_str)
        gif_generator = CountdownGif()
        gif_filename = gif_generator.generate(timer)
        return send_file(gif_filename, mimetype='image/gif')
