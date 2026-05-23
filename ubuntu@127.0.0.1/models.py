from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.PROTECT)
    def __str__(self):
        return self.title



class Entry(models.Model):
    Book=models.ForeignKey(Book,on_delete=models.PROTECT)

    Summary=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Entries'

    def __str__(self):
       if len(self.Summary)>50:
           return self.Summary[:50]+"..."
       else:
           return self.Summary