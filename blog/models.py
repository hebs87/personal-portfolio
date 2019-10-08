from django.db import models


# Create your models here.
class Blog(models.Model):
    '''
    Allows user to add a blog post
    '''
    title = models.CharField(
        max_length=100,
        blank=False)
    pub_date = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True)
    body = models.TextField(
        max_length=2000,
        blank=False)
    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True)

    def __str__(self):
        return self.title
