from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from accounts_app.models import User
from courses_app.models import Course
from enrollments_app.models import Enrollment


class DashboardStatsView(APIView):

    def get(self, request):

        users_count = cache.get("admin:users:count")
        if not users_count:
            users_count = User.objects.count()
            cache.set("admin:users:count", users_count, timeout=600)

        courses_count = cache.get("admin:courses:count")
        if not courses_count:
            courses_count = Course.objects.count()
            cache.set("admin:courses:count", courses_count, timeout=600)

        enrollments_count = cache.get("admin:enrollments:count")
        if not enrollments_count:
            enrollments_count = Enrollment.objects.count()
            cache.set("admin:enrollments:count", enrollments_count, timeout=600)

        return Response({
            "total_users": users_count,
            "total_courses": courses_count,
            "total_enrollments": enrollments_count
        })