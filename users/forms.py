from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']



class FeedbackForm(forms.Form):
    feedback = forms.CharField(widget=forms.Textarea)
    name = forms.CharField()
    subject = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()