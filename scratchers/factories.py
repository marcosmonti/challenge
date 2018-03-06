# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from factory import DjangoModelFactory, fuzzy

from scratchers.models import Scratcher


class ScratcherFactory(DjangoModelFactory):
    class Meta:
        model = Scratcher
        django_get_or_create = ('name',)

    name = fuzzy.FuzzyText()
    description = fuzzy.FuzzyText()
    size = fuzzy.FuzzyChoice(dict(Scratcher.SIZES).keys())
    price = fuzzy.FuzzyDecimal(10, 50)


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    first_name = fuzzy.FuzzyText()
    last_name = fuzzy.FuzzyText()
