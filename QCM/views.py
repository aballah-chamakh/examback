from django.shortcuts import render
from rest_framework import viewsets,status,generics,permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import QCMUserAnswer,QCMPossibleAnswer
from .serializers import QCMUserAnswerSerializer
from django.shortcuts import get_object_or_404
from .serializers import QCMQuestionSerializer
import datetime

class QCMUserAnswerViewset(viewsets.ModelViewSet):
    serializer_class = QCMUserAnswerSerializer
    queryset = QCMUserAnswer.objects.all()

    @action(methods=['PUT'],detail=True)
    def answer_question(self,request,pk):
        qcmuseranswer_obj = self.get_object()
        server_res_time = datetime.timedelta(seconds=5)
        is_question_timing_valid = qcmuseranswer_obj.expiration_date + server_res_time >= datetime.datetime.now()
        possible_answer_id       = self.request.data.get('possible_answer_id')
        qcmpossibleanswer_obj    = QCMPossibleAnswer.objects.get(id=possible_answer_id)
        if is_question_timing_valid :
            qcmuseranswer_obj.answer = qcmpossibleanswer_obj
            qcmuseranswer_obj.save()
            QCMUserAnswer.objects.create()
            return Response({'valid_timing':True,'response':serializer.data},status=status.HTTP_200_OK)
        qcmpossibleanswer_obj.invalid_timing = True
        qcmpossibleanswer_obj.save()
        return Response({'valid_timing':False},status=status.HTTP_200_OK)
