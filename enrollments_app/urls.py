from rest_framework.routers import DefaultRouter
from .views import EnrollmentViewSet, LectureProgressViewSet

router = DefaultRouter()
router.register('', EnrollmentViewSet)
router.register('progress', LectureProgressViewSet)

urlpatterns = router.urls