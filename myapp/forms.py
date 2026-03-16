from django import forms

from myapp.models import Student

class StudentForm(forms.ModelForm):
    StuId = forms.IntegerField()
    StuName = forms.CharField(max_length=30)
    Stumarks = forms.IntegerField()
    StuEmail = forms.EmailField(label="Email Address")
    StuImg = forms.ImageField(required=False)
    class Meta:
        model = Student
        fields = '__all__'

    #validation for student ID

    def clean_StuId(self):
        stuid = self.cleaned_data.get('StuId')
        if stuid <= 0:
            raise forms.ValidationError('Stu ID must be Positive and Unique')
        return stuid
    
    #validation for student Name
    def clean_StuName(self):
        stuname = self.cleaned_data.get('StuName')
        if not stuname.replace(' ','').isalpha():
            raise forms.ValidationError('Stu Name should be letters and spaces')
        return stuname
    
    #Validation for marks
    def clean_Stumarks(self):
        stumarks = self.cleaned_data.get('Stumarks')
        if stumarks < 0 or stumarks > 100:
            raise forms.ValidationError('Marks should be between 0 and 100')
        return stumarks
    
    def clean_StuEmail(self):
        stuEmail = self.cleaned_data.get('StuEmail')
        if not stuEmail.endswith('@gmail.com'):
            raise forms.ValidationError('Only @gmail.com emails are allowed')
        return stuEmail
