from django.shortcuts import render
from .forms import Testerform,Picform,Videoform

def home(request):
    if request.method == 'POST':
        filled_form = Testerform(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = ' Your name is %s  and this is your %s mobile for QA!' % (filled_form.cleaned_data['test_id'], filled_form.cleaned_data['phone_model'])
        else:
             note = 'this test_id is already register'
        new_form = Testerform()
        return render(request, 'home.html', {'Registrationform':new_form, 'note':note})
    else:
        form = Testerform()
        return render(request, 'home.html', {'Registrationform':form})


def picx(request):
    if request.method == 'POST':
        filled_form = Picform(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = ' Your test image number is  %s !' % (filled_form.cleaned_data['pic_num'])
        else:
             note = 'this test image number is already taken'
        new_form = Picform()
        return render(request, 'picx.html', {'picx_Registrationform':new_form, 'note':note})
    else:
        form = Picform()
        return render(request, 'picx.html', {'picx_Registrationform':form})

def video(request):
    if request.method == 'POST':
        filled_form = Videoform(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = ' Your video duration is  %s !' % (filled_form.cleaned_data['duration'])
        new_form = Videoform()
        return render(request, 'video.html', {'video_Registrationform':new_form, 'note':note})
    else:
        form = Videoform()
        return render(request, 'video.html', {'video_Registrationform':form})








