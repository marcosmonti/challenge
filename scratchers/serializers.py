# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from scratchers import models


class ScratcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Scratcher
        fields = ('id', 'name', 'description', 'size', 'price')

