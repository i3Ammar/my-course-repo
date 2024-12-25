from django import forms
from .models import Lesson


class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'course', 'content', 'video']  # Include 'video' in uploadable fields