from rest_framework import serializers
from lms.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        read_only_fields = ("owner",)


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.IntegerField(source="lessons.count", read_only=True)
    lessons = LessonSerializer(source="lessons", many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            "pk",
            "name",
            "preview",
            "description",
            "lessons_count",
            "lessons",
            "owner",
        ]
        read_only_fields = ("owner",)