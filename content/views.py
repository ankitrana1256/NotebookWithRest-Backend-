from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from account.renderer import UserRenderer
from content.serializer import SubjectSerializer, SemesterSerializer, UnitSerializer, NotesSerializer
from rest_framework.response import Response
from .models import Subject, Semester, Unit, Notes


class SubjectView(APIView):
    subjects = Subject.objects.all()
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = SubjectSerializer(self.subjects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SemesterView(APIView):
    semester = Semester.objects.all()
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = SemesterSerializer(self.semester, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UnitView(APIView):
    units = Unit.objects.all()
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UnitSerializer(self.units, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NotesView(APIView):
    notes = Notes.objects.all()
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = NotesSerializer(self.notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)