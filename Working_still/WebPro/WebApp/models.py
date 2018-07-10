from django.db import models

# Create your models here.
class Girl(models.Model):
    g_name=models.CharField(max_length=64)
    g_image=models.ImageField()
    g_id=models.CharField(max_length=264,primary_key=True)

class Score(models.Model):
    id=models.OneToOneField(Girl,on_delete=models.CASCADE,primary_key=True)
    rating=models.FloatField()
    ranking=models.PositiveIntegerField()
    points=models.PositiveIntegerField()
