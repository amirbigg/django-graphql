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

	def resolve_persons(parent, info, **kwargs):
		return Person.objects.all()

	def resolve_cars(parent, info, **kwargs):
		return Car.objects.all()
