from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from .views import UserExamViewset,ExamViewset

router = routers.DefaultRouter()
router.register('user-exam', UserExamViewset)
router.register('exam', ExamViewset)

urlpatterns = [
    path('', include(router.urls)),
]
