from django.db import models

# Create your models here.

class Imageai(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default="")
    image_ai = models.ImageField(upload_to="mediaai", blank=True, null = True)

    def __str__(self):
        return self.title



    class Meta:
        verbose_name = "Imageia"
        verbose_name_plural = "Obrazy AI"