# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from simplelms.core.enums import UserGender
from django.db.models import CharField,PositiveSmallIntegerField,TextField,ForeignKey,ManyToManyField,Model
# Create your models here.
class User(AbstractUser):
	phone_no = CharField(max_length=20)
	gender = PositiveSmallIntegerField(default=UserGender.UNKNOWN, choices=UserGender.CHOICES)

	class Meta(AbstractUser.Meta):
		abstract = False

class Category(Model):
	name = CharField(max_length=30)

class Publisher(Model):
	name = CharField(max_length=256)

class Author(Model):
	name = CharField(max_length=256)

class Book(Model):
	title = CharField(max_length=256)
	desc = TextField()
	publisher = ForeignKey(Publisher,related_name="books")
	author = ForeignKey(Author,related_name="books")
	categories = ManyToManyField(Category,related_name="books")