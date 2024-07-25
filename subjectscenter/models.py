from django.db import models
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone

# Create your models here.

class MySubject(models.Model):
    SUBJECTS_CHOICES = (
        ('语文', '语文'),
        ('数学', '数学'),
        ('英语', '英语'),
        ('物理', '物理'),
        ('化学', '化学'),
        ('生物', '生物'),
        ('地理', '地理'),
        ('历史', '历史'),
        ('政治', '政治'),
    )
    title = models.CharField(max_length = 50, verbose_name = '标题')
    abstract = models.TextField(max_length = 100, verbose_name = '简介')
    photo = models.ImageField(upload_to = 'subjectscenter/images', blank = True)
    description = UEditorField(u'内容',
                               default = '',
                               width = 1000,
                               height = 300,
                               imagePath = 'subjectscenter/images',
                               filePath = 'subjectscenter/files')
    subjectType = models.CharField(choices = SUBJECTS_CHOICES,
                                   max_length = 50,
                                   verbose_name = '学科')
    publishDate = models.DateTimeField(max_length = 20,
                                       default = timezone.now,
                                       verbose_name = '发布时间')
    views = models.PositiveIntegerField('浏览量', default = 0)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-publishDate',]
        verbose_name = '学科新闻'
        verbose_name_plural = verbose_name
