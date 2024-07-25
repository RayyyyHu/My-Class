from django.db import models
import django.utils.timezone as timezone

# Create your models here.

class Doc(models.Model):
    title = models.CharField(max_length = 250, verbose_name = '资料名称')
    photo = models.ImageField(upload_to = 'Doc/', verbose_name = '资料图片')
    file = models.FileField(upload_to = 'Service/',
                            verbose_name = '文件资料')
    publishDate = models.DateTimeField(max_length = 20,
                                       default = timezone.now,
                                       verbose_name = '发布时间')
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-publishDate']
        verbose_name = '资料共享'
        verbose_name_plural = verbose_name
