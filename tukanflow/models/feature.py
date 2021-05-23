# from djongo import models
from django.db.models.fields import IntegerField
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import IntField, StringField, ListField, EmbeddedDocumentField

class Goal(EmbeddedDocument):
    id = StringField(unique=True)
    text = StringField()
    status = StringField()
    authorId = StringField(unique=True)

class User(EmbeddedDocument):
    id = StringField(unique=True)
    email = StringField()
    name = StringField()

class Approval(EmbeddedDocument):
    status = StringField()
    user = EmbeddedDocumentField(User)

class Stage(EmbeddedDocument):
    id = StringField(unique=True)
    progress = IntField()
    text = StringField()
    summary = StringField()
    prevStageId = StringField()
    approvals = ListField(EmbeddedDocumentField(Approval))
    goals = ListField(EmbeddedDocumentField(Goal))
    thumbnail = StringField()

class Feature(Document):
    meta = {'collection': 'features'}
    id = StringField(unique=True)
    title = StringField()
    stages = ListField(EmbeddedDocumentField(Stage))
