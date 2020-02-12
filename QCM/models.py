from django.db import models
import datetime
from Exam.models import UserExam
# Create your models here.

class QCMQuestion(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class QCMPossibleAnswer(models.Model):
    qcm_question = models.ForeignKey(QCMQuestion,on_delete=models.CASCADE)
    score    = models.IntegerField(default=0) # +5 -2
    name     = models.TextField()
    def __str__(self):
        return 'question : {q}  possible_answer : {pa}  score : {s}'.format(q=self.qcm_question.name,
                                                                          pa=self.name,
                                                                          s = self.score,
                                                                          )
class QCMUserAnswer(models.Model):
    # qcm_question = models.OneToOneField(QCMQuestion)
    user_exam = models.ForeignKey(UserExam,on_delete=models.CASCADE,blank=True,null=True)
    qcm_question = models.ForeignKey(QCMQuestion,on_delete=models.CASCADE,blank=True,null=True)
    answer = models.ManyToManyField(QCMPossibleAnswer)
    expiration_date = models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return 'question : {q}  user_answer : {user_answer}  score : {score}'.format(q=self.qcm_question.name,
                                                                                   user_answer=self.answer.name,
                                                                                score=self.calc_score())
    def calc_score(self):
        total = 0
        for a in self.answer.all() :
            total += a.score
        return total
