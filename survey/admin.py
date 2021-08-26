from django.contrib import admin
from .models import Survey, Question,Choice

# Register your models here.


admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Choice)