from django.db import models

# Create your models here.
class uploads(models.Model):
    image = models.ImageField(upload_to="images")
    Description = models.CharField(max_length=100)

    def __str__(self):
        return self.Description
    
class uploadfile(models.Model):
    file = models.FileField(upload_to="file")
    Description = models.CharField(max_length=100)

    def __str__(self):
        return self.Description