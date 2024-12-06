from datetime import datetime

class ScoreManager:
    def __init__(self):
        self.start_time = datetime.now()
        self.stop_time = None  # This will hold the time when the game ends
        self.kills = 0

    def get_time_survived(self):
        if self.stop_time:
            return int((self.stop_time - self.start_time).total_seconds())
        return int((datetime.now() - self.start_time).total_seconds())

    def end_game(self):
        """Record the stop time when the game ends."""
        self.stop_time = datetime.now()

    def save_score(self):
        """Save the score and time survived to a file."""
        with open("etc/scores.txt", "a") as f:
            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"Score: {self.kills}, Time: {self.get_time_survived()}s, Date: {date_time}\n")
