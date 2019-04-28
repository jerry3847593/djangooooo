from django.db import models
from django.utils import timezone

# Create your models here.

class Portfolio(models.Model):
    name = models.TextField()
    age  = models.IntegerField()
    major = models.TextField()
    grade = models.IntegerField()
    hometown = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

