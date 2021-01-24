import graphene
import home.schema


class Query(home.schema.HomeQuery, graphene.ObjectType):
	pass


class Mutation(home.schema.Mutate, graphene.ObjectType):
	pass


schema = graphene.Schema(query=Query, mutation=Mutation)
