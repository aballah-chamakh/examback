from django.contrib import admin
from .models import QCMQuestion,QCMPossibleAnswer,QCMUserAnswer
# Register your models here.
admin.site.register(QCMQuestion)
admin.site.register(QCMPossibleAnswer)
admin.site.register(QCMUserAnswer)
