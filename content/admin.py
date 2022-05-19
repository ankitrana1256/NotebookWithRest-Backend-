from django.contrib import admin
from .models import Subject, Semester, Unit, Notes

# Register your models here.
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Unit)
admin.site.register(Notes)
