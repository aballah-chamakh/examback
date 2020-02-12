from rest_framework import serializers
from .models import QCMQuestion,QCMPossibleAnswer,QCMUserAnswer

class QCMPossibleAnswerSerializer(serializers.ModelSerializer):
    qcm_question_id = serializers.IntegerField(source='qcm_question.id')
    class Meta :
        model = QCMPossibleAnswer
        fields = ('id','qcm_question_id','score','name')

class QCMQuestionSerializer(serializers.ModelSerializer):
    possible_answers = serializers.SerializerMethodField()
    class Meta :
        model =QCMQuestion
        fields = ('id','name','possible_answers')
    def get_possible_answers(self,qcm_question_obj):
        qs = qcm_question_obj.qcmpossibleanswer_set.all()
        serializer = QCMPossibleAnswerSerializer(qs,many=True)
        return serializer.data


class QCMUserAnswerSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta :
        model = QCMUserAnswer
        fields = ('id','answer','expiration_date')

    def get_answers(self,qcm_user_question_obj):
        qs = qcm_user_question_obj.answer.all()
        ser = QCMPossibleAnswerSerializer(qs,many=True)
        return ser.data
