from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

class special(models.Model):
    img=models.ImageField(upload_to='picture')
    date=models.DateField()
    caption=models.CharField(max_length=100)
    description=models.TextField()




