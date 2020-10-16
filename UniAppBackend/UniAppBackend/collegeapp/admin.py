from django.contrib import admin
from .models import College, Major, Subject, Student, StudentApplication, Administrator


admin.site.register(College)
admin.site.register(Major)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(StudentApplication)
admin.site.register(Administrator)