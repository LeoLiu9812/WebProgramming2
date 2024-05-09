from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=255,verbose_name='lost_infomation')
    updated = models.BooleanField(default=False,verbose_name='Is_Found')
    def __str__(self):
        return self.text
    class Meta:  
        verbose_name = 'Lost and Found'
        verbose_name_plural = 'Lost and Found'

