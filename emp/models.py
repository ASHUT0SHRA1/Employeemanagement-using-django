from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=100  )
    emp_id=models.CharField(max_length=200)
    phone=models.IntegerField(max_length=10)
    address=models.CharField(max_length=150)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=10)

    def __str_(self):
        return self.name  
    
class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    testimonial=models.TextField()
    picture=models.ImageField(upload_to="testimonial/")
    rating=models.IntegerField(max_length=1 )

