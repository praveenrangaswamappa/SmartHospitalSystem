from django.contrib import admin

from apps.disease.models import Disease, Category

admin.site.register(Disease)
admin.site.register(Category)
