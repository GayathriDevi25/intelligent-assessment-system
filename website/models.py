from mongoengine import Document, StringField, IntField, DateTimeField
from mongoengine import Document, StringField, ListField, EmbeddedDocument, EmbeddedDocumentField
from datetime import datetime
class User(Document):
    email = StringField(max_length=150,unique=True)
    password = StringField(max_length=150)
    first_name = StringField(max_length=150)
    role = StringField(max_length=50, default='student')

    meta = {'collection': 'users'}


class Login(Document):
    email=StringField(max_length=150,unique=True)
    password_count=IntField(required=True)
    meta = {'collection': 'login'}



class TopicResult(EmbeddedDocument):
    topic = StringField(required=True)
    correct_answers = IntField(required=True)
    number_of_questions = IntField(required=True)

class TestResult(EmbeddedDocument):
    subject = StringField(required=True)
    test_number = IntField(required=True)
    correct = IntField(required=True)
    total_questions = IntField(required=True)
    total_easy_questions = IntField(required=True)
    total_medium_questions = IntField(required=True)
    total_hard_questions = IntField(required=True)
    correct_easy_questions = IntField(required=True)
    correct_medium_questions = IntField(required=True)
    correct_hard_questions = IntField(required=True)
    date = StringField(required=True)
    time = StringField(required=True)
    easy_topics = ListField(EmbeddedDocumentField(TopicResult))
    medium_topics = ListField(EmbeddedDocumentField(TopicResult))
    hard_topics = ListField(EmbeddedDocumentField(TopicResult))

class TestResultData(Document):
    email = StringField(max_length=150, unique=True)
    test_results = ListField(EmbeddedDocumentField(TestResult))

    meta = {'collection': 'test_results'}


class Topic(EmbeddedDocument):
    topic = StringField()
    easy = ListField(StringField())
    medium = ListField(StringField())
    hard = ListField(StringField())

class Subject(EmbeddedDocument):
    subject = StringField()
    topics = ListField(EmbeddedDocumentField(Topic))

class CorrectQuestion(Document):
    email = StringField(required=True, unique=True)
    subjects = ListField(EmbeddedDocumentField(Subject))