from django.shortcuts import render
from rest_framework import viewsets,status,generics,permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Exam,Question,UserExam
from QCM.models import QCMQuestion,QCMUserAnswer
from .serializers import ExamSerializer,UserExamSerializer
from django.shortcuts import get_object_or_404
import datetime
from time import sleep

class ExamViewset(viewsets.ModelViewSet):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    @action(methods=['PUT'],detail=True)
    def add_question(self,request,pk):
        exam_obj = self.get_object()
        question = self.request.data.get('question')
        order = self.request.data.get('order')
        duration_seconds = self.request.data.get('duration_seconds')
        it = datetime.timedelta(seconds=duration_seconds)
        qcm_question_obj = QCMQuestion.objects.create(name=questions)
        question_obj = Question.objects.create(exam=exam_obj,
                                               order = order,
                                               duration = it,
                                               type = qcm_question_obj)
        serializer = QuestionSerializer(question_obj,many=False)
        return Response({'response':serializer.data},status=status.HTTP_200_OK)

    @action(methods=['PUT'],detail=True)
    def add_possible_question(self,request,pk):
        exam_obj = self.get_object()
        qcm_question_id = self.request.data.get('question_id')
        qcm_question_obj = QCMQuestion.objects.get(id=qcm_question_id)
        possible_answer_score = self.request.data.get('score')
        possible_answer_name = self.request.data.get('name')
        qcm_possible_answer_obj = QCMPossibleAnswer.objects.create(qcm_question=qcm_question_obj,
                                                                 score = possible_answer_score,
                                                                 name=possible_answer_name)
        serializer = QCMPossibleAnswerSerializer(qcm_possible_answer_obj,many=False)
        return Response({'response':serializer.data},status=status.HTTP_200_OK)

class UserExamViewset(viewsets.ModelViewSet):
    serializer_class = UserExamSerializer
    queryset = UserExam.objects.all()

    @action(methods=['PUT'],detail=True)
    def answer(self,request,pk):
        userexam_obj = self.get_object()
        question_id = self.request.data.get('question_id')
        possible_answer_ids= self.request.data.get('possible_answer_ids')
        question_obj = Question.objects.get(id=question_id)  #userexam_obj.question_set.all().filter(id=question_id)

        qcmuseranswer_obj = QCMUserAnswer.objects.get(user_exam=userexam_obj,qcm_question=question_obj.content_object)
        qcmpossibleanswer_qs = question_obj.content_object.qcmpossibleanswer_set.all()
        for pa in qcmpossibleanswer_qs :
            if pa.id in possible_answer_ids :
                qcmuseranswer_obj.add(pa)
        qcmuseranswer_obj.save()
        user_answer_qs = QCMUserAnswer.objects.all().filter(user_exam=userexam_obj)
        print(user_answer_qs)
        total_score = 0
        for user_answer in user_answer_qs :
            for answer in user_answer.answer.all() :
                total_score += answer.score
        print('score : ',str(total_score))
        # calculating the score
        return Response({'response':'done'},status=status.HTTP_200_OK)


    @action(methods=['PUT'],detail=True)
    def answer_and_pre_answer(self,request,pk):
        userexam_obj = self.get_object()
        question_id = self.request.data.get('question_id')
        possible_answer_ids= self.request.data.get('possible_answer_ids')
        question_obj = Question.objects.get(id=question_id)
        #print(question_obj.order)
        qcmuseranswer_obj = QCMUserAnswer.objects.get(user_exam=userexam_obj,qcm_question=question_obj.content_object) #question_obj.qcmquestion.qcmuseranswer_set.filter(exam=userexam_obj.exam,qcm_question=question_obj.qcmquestion)
        qcmpossibleanswer_qs = question_obj.content_object.qcmpossibleanswer_set.all()
        #print(qcmpossibleanswer_qs)
        for pa in qcmpossibleanswer_qs :
            if pa.id in possible_answer_ids :
                qcmuseranswer_obj.add(pa)
        qcmuseranswer_obj.save()
        # calculating the score
        print(userexam_obj.exam.name)
        print(userexam_obj.exam.question_set.all())
        next_question = userexam_obj.exam.question_set.all().get(order=question_obj.order+1) #Question.objects.get(order=question_obj.order+1)
        print(next_question)

        qcmuseranswer_obj = QCMUserAnswer.objects.create(user_exam=userexam_obj,qcm_question=next_question.content_object)
        return Response({'response':'done'},status=status.HTTP_200_OK)

    @action(methods=['PUT'],detail=True)
    def pre_answer(self,request,pk):
        userexam_obj = self.get_object()
        question_obj = userexam_obj.exam.question_set.all().get(order=0)
        # print(question_obj.content_object.qcmuseranswer)
        qcmuseranswer_obj = QCMUserAnswer.objects.create(user_exam=userexam_obj,qcm_question=question_obj.content_object)
        return Response({'response':'done'},status=status.HTTP_200_OK)
