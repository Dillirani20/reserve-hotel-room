from django.db import models

# Create your models here.


class Userdata(models.Model):
    fname=models.CharField(max_length=20,default='Unknown',blank=False)
    lname=models.CharField(max_length=20,default='Unknown')
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)



    def __str__(self):
        return self.email
    

room_choices = (
    ('AC', 'ac'),
    ('NON-AC', 'non-ac'),
)   
class Roominfo(models.Model):
    room_image=models.ImageField(upload_to="hotels/")  
    hotel_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    room_spec = models.CharField(max_length=600)
    hotel_price = models.IntegerField(default=1800)
    room = models.CharField(max_length=8, choices=room_choices,default='AC')


    def __str__(self):
        return self.hotel_name    
    


class Bookinginfo(models.Model):
    room = models.ImageField(upload_to='hotels/', default=None)
    hotel=models.CharField(max_length=100)
    #hotel = models.ForeignKey(hotel, on_delete=models.CASCADE) 
    name=models.CharField(max_length=100)
    age = models.IntegerField()
    person = models.IntegerField()
    email= models.CharField(max_length=100)
    contactno=models.IntegerField(max_length=15)
    desc=models.TextField(null=True,blank=True) 

    def __str__(self):
        return self.name    



class Billinginfo(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    userName=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.IntegerField()
    hotel_price=models.IntegerField()
    payment_choices=[
        ('UPI', 'upi'),
        ('NET BANKING', 'net banking'),
        ('DEBIT CARD', 'debit card'),
        ('CREDIT CARD', 'credit card'),
    ]
    pay=models.CharField(max_length=20,choices=payment_choices,unique=True)

    def __str__(self):
        return self.firstName
