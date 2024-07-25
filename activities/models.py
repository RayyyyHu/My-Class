from django.db import models
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone

# Create your models here.

class MyActivity(models.Model):
    title = models.CharField(max_length = 50, verbose_name = '活动标题')
    photo = models.ImageField(upload_to = 'activities/', blank = True, verbose_name = '活动首页照片')
    abstract = models.TextField(max_length = 120, verbose_name = '简介')
    description = UEditorField(u'内容',
                               default = '',
                               width = 1000,
                               height = 300,
                               imagePath = 'news/images',
                               filePath = 'news/files')
    publishDate = models.DateTimeField(max_length = 20,
                                       default = timezone.now,
                                       verbose_name = '发布时间')
    views = models.PositiveIntegerField('浏览量', default = 0)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-publishDate']
        verbose_name = '新闻'
        verbose_name_plural = verbose_name
