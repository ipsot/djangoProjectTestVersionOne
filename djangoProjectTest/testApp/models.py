from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


def create():
    tom = Person.objects.create(name="Tom", age=23)


def save():
    tim = Person(name="Bob", age=32)
    tim.save()


def get():
    bob = Person.objects.get(age=23)
    bob=Person.save()


def getall():
    people = Person.objects.all()


def filter():
    people = Person.objects.filter(age=32)


def in_blunk():
    people = Person.objects.in_bulk([1, 3])
    for id in people:
        print(people[id].name)
        print(people[id].age)


def filterAndUpdate():
    pip=Person.objects.filter(id=1).update(name="Bobby")


def delete():
    dot=Person.objects.get(id=2)
    dot.delete()