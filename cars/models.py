from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Car(models.Model):
    
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    desc = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.type

class Post(models.Model):
    
    any_comment = models.CharField(max_length=255)

    def __str__(self) :
        return self.any_comment