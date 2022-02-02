from django.core.management.base import BaseCommand
from oculid.models import tester,picx,video
import json,base64

class Command(BaseCommand):
    help = 'Import Tester'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('C:/Users/mufal/Downloads/oculid_backend_challenge/oculid_backend_challenge/data/tester.json',
                  encoding='utf-8') as data_file:
            json_data = json.loads(data_file.read())
            models = tester(test_id=json_data['test_id'],
                            time=json_data['time'],
                            phone_manufacturer=json_data['phone_manufacturer'],
                            phone_model=json_data['phone_model'],
                            screen_height=json_data['screen_height'],
                            screen_width=json_data['screen_width']
                            )
            models.save()

        with open('C:/Users/mufal/Downloads/oculid_backend_challenge/oculid_backend_challenge/data/pics.json',
                  encoding='utf-8') as data_pic_file:
            json_pic_data = json.loads(data_pic_file.read())

            for i in range(len(json_pic_data)):
                with open(json_pic_data[i]['image_path'], "rb") as image_file:
                    image_encode =base64.b64encode(image_file.read())

                models_picx = picx(height=json_pic_data[i]["height"],
                                   time=json_pic_data[i]['time'],
                                   width=json_pic_data[i]['width'],
                                   pic_num=json_pic_data[i]['pic_num'],
                                   tester=tester.objects.get(pk='1'),
                                   image=json_pic_data[i]['image_path'],
                                   base64_image=image_encode,
                                   )
                models_picx.save()

        with open('C:/Users/mufal/Downloads/oculid_backend_challenge/oculid_backend_challenge/data/video.json',
                  encoding='utf-8') as data_vid_file:
            json_vid_data = json.loads(data_vid_file.read())
            models_vid=video(duration=json_vid_data['duration'],
                          time=json_vid_data['time'],
                          tester=tester.objects.get(pk='1')
                          )
            models_vid.save()





