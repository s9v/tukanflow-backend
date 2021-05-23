import graphene
from graphene_mongo import MongoengineObjectType
from tukanflow.models.feature import Feature as FeatureModel
import mongoengine

mongoengine.connect('tukanflow', host='127.0.0.1', port=27017)

class Feature(MongoengineObjectType):
    class Meta:
        model = FeatureModel

class Query(graphene.ObjectType):
    features = graphene.Field(Feature, id=graphene.ID())

    def resolve_features(root, info, **kwargs):
        f = FeatureModel()
        # f.id = '0'
        # f.title = 'Title'
        # f.stages = []
        # f.save()

        print(root.objects)
        print(root.objects)
        print(root.objects)
        return root.objects()

schema = graphene.Schema(query=Query)

# <--> Graphene (GraphQL Server for Python) <--> Django Models <--> MongoDB
