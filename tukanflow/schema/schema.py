import graphene
from graphene_django import DjangoObjectType

# from .models import Feature


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

# class QuestionType(DjangoObjectType):
#     class Meta:
#         model = Question
#         fields = ("id", "question_text")

# class Query(graphene.ObjectType):
#     features = graphene.Field(Feature, id=graphene.ID())
#     question_by_id = graphene.Field(QuestionType, id=graphene.String())

#     def resolve_features(root, info, **kwargs):
#         # Querying a list
#         return Feature.objects.all()

#     def resolve_question_by_id(root, info, id):
#         # Querying a single question
#         return Question.objects.get(pk=id)

schema = graphene.Schema(query=Query)

# <--> Graphene (GraphQL Server for Python) <--> Django Models <--> MongoDB
