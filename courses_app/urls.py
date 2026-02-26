from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CourseViewSet, ModuleViewSet, LectureViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('courses', CourseViewSet)
router.register('modules', ModuleViewSet)
router.register('lectures', LectureViewSet)

urlpatterns = router.urls