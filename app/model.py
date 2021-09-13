"""
Labs DS Machine Learning Engineer Role
- Machine Learning Interface
"""
import os
from datetime import datetime

import joblib
import pytz
from sklearn.model_selection import train_test_split

from app.data import Data
from sklearn.ensemble import RandomForestClassifier


class Model:
    path = "app/model.job"

    def __init__(self):
        data = Data()
        self.total = data.count()
        df = data.df().set_index("idx")
        target = df["target"]
        features = df.drop(columns=["target"])
        x_train, x_test, y_train, y_test = train_test_split(
            features,
            target,
            test_size=0.20,
            random_state=42,
        )
        self.model = RandomForestClassifier(
            n_jobs=-1,
            random_state=42,
        )
        lambda_time = pytz.timezone('US/Pacific')
        start_time = datetime.now(lambda_time)
        self.model.fit(x_train, y_train)
        stop_time = datetime.now(lambda_time)
        self.duration = f"{(stop_time - start_time).total_seconds():.2f} sec"
        self.time_stamp = stop_time.strftime('%Y-%m-%d %H:%M:%S')
        self.score = f"{100 * self.model.score(x_test, y_test):.2f}%"
        joblib.dump(self, self.path)

    def __call__(self, *features):
        prediction, *_ = self.model.predict([features])
        probability, *_ = self.model.predict_proba([features])
        return prediction, f"{100 * max(probability):.2f}%"

    @property
    def info(self):
        return {
            "Model": repr(self.model),
            "Time Stamp": self.time_stamp,
            "Validation Score": self.score,
            "Time to Train": self.duration,
            "Total Rows": self.total,
        }

    @classmethod
    def load(cls):
        if os.path.exists(cls.path):
            return joblib.load(cls.path)
        else:
            return cls()

    def __str__(self):
        return "\n  ".join(f"{k}: {v}" for k, v in self.info.items())


if __name__ == '__main__':
    # print(Model())
    print(Model.load())
