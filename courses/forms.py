from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
        ]
    def clean_title(self):
        title = self.cleaned_data.get('title')
        bad_words = ['%$#@!', '!@#$']
        for i in bad_words:
            if i in title:
                raise forms.ValidationError("You cannot put bad polish words")
        return title
