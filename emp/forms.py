from django import forms
from .models import *
class FeedbackForm(forms.Form):
    email=forms.EmailField(label="Enter your email",max_length=200 , required=True)
    name=forms.CharField(label="Enter your name" , max_length=100)
    feedback=forms.CharField(label="Enter Feedback", max_length=1000, required=False , widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class Formfeedback(forms.ModelForm):
    
    class Meta:
        model = Testimonial
        fields = ("name", "testimonial" , "rating" , "picture")
    def __init__(self, *args, **kwargs):
        super(Formfeedback, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
