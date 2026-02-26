from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    path('api/courses/', include('courses_app.urls')),
    path('api/enroll/', include('enrollments_app.urls')),
    path('api/reviews/', include('reviews_app.urls')),
    path('api/dashboard/', include('dashboard_app.urls')),
]