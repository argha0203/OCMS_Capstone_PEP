from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Enrollment, LectureProgress
from .serializers import EnrollmentSerializer, LectureProgressSerializer
from accounts_app.permissions import IsStudent


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), IsStudent()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


class LectureProgressViewSet(viewsets.ModelViewSet):
    queryset = LectureProgress.objects.all()
    serializer_class = LectureProgressSerializer
    permission_classes = [IsAuthenticated]