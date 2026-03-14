from django import forms

from myapp.models import Student

class StudentForm(forms.ModelForm):
    StuId = forms.IntegerField()
    StuName = forms.CharField(max_length=30)
    Stumarks = forms.IntegerField()
    StuImg = forms.ImageField(required=False)
    class Meta:
        model = Student
        fields = '__all__'