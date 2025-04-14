from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()


class Animal(models.Model):
    name=models.CharField(max_length=100)
    species=models.CharField(max_length=50)
    breed=models.CharField(max_length=50,blank=True)
    age=models.PositiveIntegerField(null=True,blank=True)
    photo=models.ImageField(upload_to='animals/',null=True,blank=True)

    def __str__(self):
        return f"{self.name} ({self.species})"
    
class RescueReport(models.Model):
    animal=models.ForeignKey(Animal,on_delete=models.CASCADE,related_name='reports')
    reporter=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=50, choices=[
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
])

    location=models.CharField( max_length=255)
    notes=models.TextField(blank=True)
    reported_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{ self.animal.name }-{self.get_status_display()}"




    

    