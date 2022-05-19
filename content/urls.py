from django.urls import path
from .views import SubjectView, SemesterView, UnitView, NotesView

urlpatterns = [
    path("subject", SubjectView.as_view(), name="subject"),
    path("semester", SemesterView.as_view(), name="semester"),
    path("unit", UnitView.as_view(), name="unit"),
    path("notes", NotesView.as_view(), name="notes")
]
