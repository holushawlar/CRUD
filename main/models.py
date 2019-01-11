from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.
class Goal(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(default= datetime.now, blank=True)
    deadline = models.DateTimeField(default= datetime.now, blank= False)

    def get_absolute_url(self):
        return reverse("todo:goal-detail", kwargs={"pk": self.pk})
    
    