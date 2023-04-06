from django.contrib import admin
from testing import models
from django import template


admin.site.register(models.TestCategory)
admin.site.register(models.Question)
admin.site.register(models.PsyTest)
admin.site.register(models.TestResult)
admin.site.register(models.PersonalResult)
admin.site.register(models.Option)

