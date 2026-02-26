from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Category, Course, Module, Lecture
from .serializers import CategorySerializer, CourseSerializer, ModuleSerializer, LectureSerializer
from accounts_app.permissions import IsAdmin, IsInstructor
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated()]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    filterset_fields = ['category', 'level', 'price']
    ordering_fields = ['price', 'created_at']
    search_fields = ['title']

    def get_permissions(self):
        if self.action in ['create']:
            return [IsAuthenticated(), IsInstructor()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [IsAuthenticated]