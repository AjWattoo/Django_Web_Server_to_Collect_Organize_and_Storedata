from django import forms
from .models import tester,picx,video

class Testerform(forms.ModelForm):
    class Meta:
        model = tester
        fields = ['test_id', 'phone_manufacturer','phone_model','screen_height','screen_width']

class Picform(forms.ModelForm):
    class Meta:
        model = picx
        fields = ['height', 'width','pic_num','image','tester']

class Videoform(forms.ModelForm):
    class Meta:
        model = video
        fields = ['duration','tester']
