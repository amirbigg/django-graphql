import graphene
import graphql_jwt
from graphene_django.types import DjangoObjectType, ObjectType
from django.contrib.auth.models import User
from graphql_jwt.decorators import login_required


class UserType(DjangoObjectType):
	class Meta:
		model = User


class AccountsQuery(ObjectType):
	user = graphene.Field(UserType, id=graphene.ID())

	@login_required
	def resolve_user(parent, info, **kwargs):
		id = kwargs.get('id')
		if id is not None:
			return User.objects.get(id=id)
		return None


class UserInput(graphene.InputObjectType):
	username = graphene.String()
	email = graphene.String()
	password = graphene.String()


class CreateUser(graphene.Mutation):
	class Arguments:
		input = UserInput(required=True)

	ok = graphene.Boolean(default_value=False)
	user = graphene.Field(UserType)

	@staticmethod
	def mutate(parent, info, input=None):
		user_instance = User.objects.create_user(input.username, input.email, input.password)
		ok = True
		return CreateUser(user=user_instance, ok=ok)


class Mutation(graphene.ObjectType):
	create_user = CreateUser.Field()
	token_auth = graphql_jwt.ObtainJSONWebToken.Field()
	verify_token = graphql_jwt.Verify.Field()
	refresh_token = graphql_jwt.Refresh.Field()

# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InJvb3QiLCJleHAiOjE2MTMxMjcxMjcsIm9yaWdJYXQiOjE2MTMxMjY4Mjd9.BrySPzW7aYmUmWlK9G0U5y6NpNLZZ0iqjLCe6vicOrI