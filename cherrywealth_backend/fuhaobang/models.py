import os
from django.conf import settings
from django.db import models


def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'images')

class Person(models.Model):
    name = models.CharField('姓名', max_length=200)
    #gender = models.CharField(max_length=200)
    birthday = models.DateField('生日')
    wealth = models.CharField('身价', max_length=200)
    brief_intro = models.TextField('简介')
    portrait = models.ImageField('头像', upload_to='fuhaobang/static/fuhaobang/images/portrait/', default='images/portrait/default.png')
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )
    gender = models.CharField('性别', max_length=1, choices=GENDER_CHOICES)
    country = models.CharField('国家', max_length=200, default='')
    rank = models.IntegerField('当前排名', default=-1)
    #photo = models.FilePathField(path=images_path)
    #print(images_path())
    def __str__(self):
        return self.name

class Event(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField('标题', max_length=200)
    display_time = models.CharField('前端显示时间', default='1900', max_length=200)
    time = models.DateField('时间', default='1900-01-01', blank=True)
    location = models.CharField('地点', default=' ', max_length=200)
    brief_intro = models.TextField('简介')
    attachment_type = models.CharField('附件类型', max_length=5, choices=(('Empty', '无'), ('Image','图片'), ('Video', '视频')))
    image = models.ImageField('图片', upload_to='fuhaobang/static/fuhaobang/images/event/', default='images/event/default.png')
    video = models.FileField('视频', upload_to='fuhaobang/static/fuhaobang/videos/event/', default='images/video/default.mp4')
    def __str__(self):
        return self.title


class Link(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField('标题', max_length=200)
    brief_intro = models.TextField('简介')
    link_type = models.CharField('附件类型', max_length=5, choices=(('News', '新闻'), ('Book','书籍'), ('Other', '其他')))
    image = models.ImageField('图片', upload_to='fuhaobang/static/fuhaobang/images/link/', default='images/link/default.png')
    link = models.CharField('链接', max_length=300)
    def __str__(self):
        return self.title
