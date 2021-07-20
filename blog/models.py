from django.db import models

class Blog(models.Model):
    title = models.CharField('title',max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='author'
    )
    content = models.TextField('text')

    def __str__(self):
        return self.title
    def author_name(self):
        return '%s' % self.author.first_name
    author_name.short_description='author_name'

# Create your models here.
