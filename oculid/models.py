from django.db import models
import base64
import os

class tester(models.Model):
    test_id = models.IntegerField(unique=True,blank=False)
    time = models.DateTimeField(auto_now_add=True)
    phone_manufacturer = models.CharField(max_length=200)
    phone_model = models.CharField(max_length=200)
    screen_height = models.IntegerField()
    screen_width = models.IntegerField()

    def __str__(self):
        return '%s' % self.test_id


class picx(models.Model):
    height = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField()
    pic_num = models.IntegerField(unique=True)
    tester =models.ForeignKey(tester,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',blank=True)
    base64_image=models.TextField(blank=True)


    def __str__(self):
        return '%s' % self.image


    def save(self, *args,**kwargs):

        path = self.image.path
        new_path = path.replace("\\", "/")


        with open(new_path, "rb") as image_file:
            self.base64_image = base64.b64encode(image_file.read())

        super(picx,self).save(*args,**kwargs)


class video(models.Model):
    duration = models.TextField(blank=True)
    time = models.DateTimeField(auto_now_add=True)
    tester =models.ForeignKey(tester,on_delete=models.CASCADE)




