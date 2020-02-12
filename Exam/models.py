from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import datetime

# Create your models here.
class Exam(models.Model):
    course_id = models.IntegerField(default=0)
    name  = models.CharField(max_length=1000)
    duration = models.DurationField()
    total_score = models.IntegerField()
    # finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Question(models.Model):
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    duration = models.DurationField()
    type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('type', 'object_id')
    def __str__(self):
        if self.content_object :
            return self.content_object.name
        return 'empty question'

class UserExam(models.Model):
    user_id = models.IntegerField(default=0)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    finished = models.BooleanField(default=False)
    def __str__(self):
        return 'id : {id} user_id : {user_id} exam_name : {exam_name} finished : {finished} '.format(
                                                                                         id = self.id ,
                                                                                          user_id=self.user_id,
                                                                                          exam_name=self.exam.name,
                                                                                          finished=self.finished)
