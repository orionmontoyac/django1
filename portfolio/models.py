from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200, default='Title')
    description = models.TextField(blank=True)
    image = models.ImageField(default="", upload_to='projects')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    url = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
