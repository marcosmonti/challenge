# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from scratchers import models
from scratchers import serializers


class ScratcherViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing scratcher instances.
    """
    serializer_class = serializers.ScratcherSerializer
    queryset = models.Scratcher.objects.all()
    permission_classes = [IsAuthenticated]
