from django.db import models
from django.utils import timezone

# Create your models here.

class honor(models.Model):
    HONOR_CHOICES = (
        ('学术荣誉', '学术荣誉'),
        ('艺术荣誉', '艺术荣誉'),
        ('体育荣誉', '体育荣誉'),
    )
    description = models.TextField(max_length = 500, blank = True, null = True, verbose_name = '荣誉名称')
    honorType = models.CharField(choices = HONOR_CHOICES, max_length = 50, verbose_name = '荣誉类型', default = '')
    photo = models.ImageField(upload_to = 'honor/', blank = True, verbose_name = '荣誉照片')
    publishDate = models.DateTimeField(max_length = 20, default = timezone.now, verbose_name = '发布时间')

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = '班级荣誉'
        verbose_name_plural = '班级荣誉'
        ordering = ('-publishDate',)
 