from django.urls import path
from edu.apps import EduConfig
from rest_framework.routers import DefaultRouter

from edu.views import CourseViewSet, LessonCreateAPIView, LessonRetrieveAPIView, LessonListAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

app_name = EduConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [path('create/', LessonCreateAPIView.as_view(), name='lessson-create'),
               path('list/', LessonListAPIView.as_view(), name='lesson-list'),
               path('details/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-details'),
               path('update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
               path('delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete')

               ] + router.urls
