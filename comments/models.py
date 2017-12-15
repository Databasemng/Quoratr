from django.db import models
from django.utils import timezone
# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        verbose_name='User', to='users.User', related_name='comments')
   # topic_name = models.ForeignKey(verbose_name='Topic', to='topics.Topic',
   #     related_name='questions')
    which_question = models.ForeignKey(
        verbose_name='Question', to='questions.Question', related_name='comments')
    vote = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'comments'
    def __str__(self):
        return '{text} - {created_date}'.format(
            text=self.text,
            created_date=self.created_date,
        )
