import datetime

question = []


class questions():
    def __init__(self):
        self.db = meetup
        self.id = len(question)

    def save(self, location, topic, name, happeningOn):
        data = {
            "id": self.id + 1,
            "createdOn": datetime.datetime.utcnow(),
            "createdBy": name,
            "location": location,
            "topic": topic,
            "happeningOn": happeningOn
        }
        meetup.append(data)
        return meetup

    def get_meetUps(self):
        return self.db
