from django.contrib import admin
from .models import *


admin.site.register(Major)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(StudentApplication)
admin.site.register(Administrator)