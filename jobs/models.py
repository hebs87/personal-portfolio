from django.db import models


# Create your models here.
class Job(models.Model):
    '''
    Stores information about user's projects/jobs
    that they worked on
    '''
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary
