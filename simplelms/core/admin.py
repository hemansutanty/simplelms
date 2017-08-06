# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from simplelms.core.models import User,Category,Publisher,Author,Book
# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)