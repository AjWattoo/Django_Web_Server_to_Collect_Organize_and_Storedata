
from django.contrib import admin
from .models import tester, picx, video

class tester_notes(admin.ModelAdmin):
    list_display = ('test_id', 'phone_manufacturer', 'phone_model','screen_height','screen_width')
    search_fields = ('test_id',)
    list_filter = ('test_id','phone_manufacturer','phone_model')


admin.site.register(tester, tester_notes)


class picx_notes(admin.ModelAdmin):
    list_display = ('pic_num','tester',)
    list_filter = ('tester__test_id',)


admin.site.register(picx, picx_notes)


class video_notes(admin.ModelAdmin):
    list_display = ('tester','duration',)
    list_filter = ('tester__test_id',)


admin.site.register(video, video_notes)
