import json
import os
from datetime import datetime

class QuizTracker:
    def __init__(self):
        self.data_file = "quiz_progress.json"
        self.load_progress()

    def load_progress(self):
        if os.path.exists(self.data_file):
            with open(self.data_file) as f:
                self.progress = json.load(f)
        else:
            self.progress = {"scores": {}, "weak_topics": {}}

    def save_progress(self):
        with open(self.data_file, "w") as f:
            json.dump(self.progress, f, indent=2)

    def record_score(self, topic, score, total):
        percentage = round((score / total) * 100, 1)
        self.progress["scores"][topic] = {
            "score": score,
            "total": total,
            "percentage": percentage,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        if percentage < 65:
            self.progress["weak_topics"][topic] = self.progress["weak_topics"].get(topic, 0) + 1
        self.save_progress()
        return percentage