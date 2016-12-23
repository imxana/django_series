from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=50)

class jigsaw(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    num_column = models.IntegerField()
    num_row = models.IntegerField()

class image(models.Model):
    from_jigsaw = models.ForeignKey(jigsaw)
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    pos_x = models.IntegerField()
    pos_y = models.IntegerField()



