import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Person, Car


class PersonType(DjangoObjectType):
	class Meta:
		model = Person


class CarType(DjangoObjectType):
	class Meta:
		model = Car


class HomeQuery(ObjectType):
	persons = graphene.List(PersonType)
	cars = graphene.List(CarType)
	person = graphene.Field(PersonType, name=graphene.String())
	car = graphene.Field(CarType, id=graphene.Int())

	def resolve_persons(parent, info, **kwargs):
		return Person.objects.all()

	def resolve_cars(parent, info, **kwargs):
		return Car.objects.all()

	def resolve_person(parent, info, **kwargs):
		name = kwargs.get('name')
		if name is not None:
			return Person.objects.get(name=name)
		return None

	def resolve_car(parent, info, **kwargs):
		id = kwargs.get('id')
		if id is not None:
			return Car.objects.get(id=id)
		return None


class PersonInput(graphene.InputObjectType):
	name = graphene.String()
	age = graphene.Int()


class CreatePerson(graphene.Mutation):
	class Arguments:
		input = PersonInput(required=True)

	person = graphene.Field(PersonType)
	ok = graphene.Boolean(default_value=False)

	@staticmethod
	def mutate(parent, info, input=None):
		person_instance = Person.objects.create(name=input.name, age=input.age)
		ok = True
		return CreatePerson(person=person_instance, ok=ok)


class Mutate(graphene.ObjectType):
	create_person = CreatePerson.Field()
