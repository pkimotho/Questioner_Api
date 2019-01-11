import datetime

question = []


class questions():
    def __init__(self):
        self.db = question
        self.id = len(question)

    def save(self, meetup, title, name, body, votes):
        data = {
            "id": self.id + 1,
            "createdOn": datetime.datetime.utcnow(),
            "createdBy": name,
            "meetup": meetup,
            "title": title,
            "body": body,
            "votes": votes
        }
        question.append(data)
        return question

    def get_questions(self):
        return self.db
