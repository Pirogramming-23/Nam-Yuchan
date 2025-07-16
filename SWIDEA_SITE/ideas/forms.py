from django import forms
from .models import Idea
from devtools.models import DevTool

class IdeaForm(forms.ModelForm):
    devtool = forms.ModelChoiceField(
        queryset=DevTool.objects.all(),
        label="예상 개발툴",
        empty_label="--------",
    )

    class Meta:
        model = Idea
        fields = ['title', 'image', 'content', 'interest', 'devtool']
        labels = {
            'title': '아이디어명',
            'image': 'Image',
            'content': '아이디어 설명',
            'interest': '아이디어의 관심도',
        }