from rest_framework import serializers
from .models import Exam,Question,UserExam
from QCM.serializers import QCMQuestionSerializer

class QuestionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='content_object.name')
    question_type  = serializers.SerializerMethodField()
    class Meta :
        model = Question
        fields = ('id','order','name','duration','type','question_type')
    def get_question_type(self,question_obj):
        qcm_question_obj = question_obj.content_object
        serializer = QCMQuestionSerializer(qcm_question_obj,many=False)
        return serializer.data

class ExamSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    class Meta :
        model = Exam
        fields = ('id','course_id','name','duration','total_score','questions',)
    def get_questions(self,exam_obj):
        qs = exam_obj.question_set.all()
        serializer = QuestionSerializer(qs,many=True)
        return serializer.data

class UserExamSerializer(serializers.ModelSerializer):
    exam = serializers.SerializerMethodField(read_only=True)
    course_id = serializers.IntegerField(write_only=True)
    class Meta :
        model = UserExam
        fields = ('id','user_id','course_id','exam','finished')
    def create(self,validated_data):
        print(validated_data)
        course_id = validated_data.get('course_id')
        exam_obj = Exam.objects.get(course_id=course_id)
        del validated_data['course_id']
        userexam_obj = UserExam.objects.create(exam=exam_obj,**validated_data)
        return userexam_obj
    def get_exam(self,userexam_obj):
        serializer = ExamSerializer(userexam_obj.exam,many=False)
        return serializer.data
