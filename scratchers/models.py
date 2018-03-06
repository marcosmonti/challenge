# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Scratcher(models.Model):
    """Simple Scratcher model"""

    EXTRA_SMALL = 'XS'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    EXTRA_LARGE = 'XL'

    SIZES = (
        (EXTRA_SMALL, 'Extra Small'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (EXTRA_LARGE, 'Extra Large'),
    )

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    size = models.CharField(max_length=2, choices=SIZES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
