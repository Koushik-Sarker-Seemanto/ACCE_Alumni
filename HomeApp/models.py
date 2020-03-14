from django.db import models

# Create your models here.
from datetime import datetime

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from PIL import Image as PILImage, Image
from io import StringIO,BytesIO
import sys


class Notice(models.Model):
    title = models.CharField(max_length=100, default='', blank=True)
    description = models.CharField(max_length=500, default='', blank=True)
    notice_pic = models.ImageField(default='', blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    def save(self):
        # Opening the uploaded image
        if self.notice_pic:
            im = Image.open(self.notice_pic)

            output = BytesIO()

            # Resize/modify the image
            im = im.resize((640, 640))

            # after modifications, save it to the output
            im.save(output, format='JPEG', quality=60)
            output.seek(0)

            # change the imagefield value to be the newley modifed image value
            self.notice_pic = InMemoryUploadedFile(
                output, 'ImageField', "%s.jpg" % self.notice_pic.name.split('.')[0],
                'image/jpeg', sys.getsizeof(output), None)

        super(Notice, self).save()


class Carousel(models.Model):
    title = models.CharField(max_length=100, default='', blank=True)
    description = models.CharField(max_length=500, default='', blank=True)
    carousel_pic = models.ImageField(default='',blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now)

    def save(self):
        # Opening the uploaded image
        if self.carousel_pic:
            im = Image.open(self.carousel_pic)

            output = BytesIO()

            # Resize/modify the image
            im = im.resize((640, 640))

            # after modifications, save it to the output
            im.save(output, format='JPEG', quality=60)
            output.seek(0)

            # change the imagefield value to be the newley modifed image value
            self.carousel_pic = InMemoryUploadedFile(
                output, 'ImageField', "%s.jpg" % self.carousel_pic.name.split('.')[0],
                'image/jpeg', sys.getsizeof(output), None)

        super(Carousel, self).save()
