from django.db import models

# Create your models here.
# class GitUser(models.Model):
#     username = models.CharField(max_length=100)
#     # repositories = models.ManyToManyField('Repository')

#     def __str__(self):
#         return self.name

class Repository(models.Model):
   
    title = models.CharField(max_length=255 ,null = True,blank = True)
    ownername = models.CharField(max_length=255)
    description = models.CharField(max_length=255 , null = True , blank=True)
    created = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=255 , default=None )

    def __str__(self):
        return self.title