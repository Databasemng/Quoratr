from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField()
    # author = models.ForeignKey(verbose_name='User', to='users.User',
    #     related_name='questions')
    # topic_name = models.ForeignKey(verbose_name='Topic', to='topics.Topic',
    #     related_name='questions')
