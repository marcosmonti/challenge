# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from scratchers import models


# Register your models here.
class ScratcherAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'price', )


admin.site.register(models.Scratcher, ScratcherAdmin)
