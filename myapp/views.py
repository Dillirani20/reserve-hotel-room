from django.shortcuts import render,redirect
from .models import Userdata,Roominfo,Bookinginfo,Billinginfo
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from .forms import HotelSearchForm


def hotel_list(request):
    

    return render(request, 'hotel_list.html', {'form': form, 'hotels': hotels})

# Create your views here.

# myapp/views.py
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from pathlib import Path
from email import encoders
from django.http import HttpResponse

def send_email(email):
     smtp_server = 'smtp.gmail.com'
     smtp_port = 587
     smtp_username = 'vivantahotelsboooking@gmail.com'  
     smtp_password = 'fdxlnoreevrrfppq' 

     from_email = smtp_username
     to_email = email  # Replace with the recipient's email address

     # Determine the path to the image file
     image_path = os.path.join(settings.BASE_DIR, 'static', 'email.png')

     subject = 'Hooray, Your Hotel Room Booking is Confirmed'
     body = '''
    <html>
        <body>
            <img src="cid:image1" alt="Booking Confirmation" style="width:600px; height:100px;"><br><br>
            <p>Hey there!,</p>
            <p>We are happy to inform you that your hotel booking is confirmed!</p>
            <p>Get ready to create some unforgettable memories.</p>
            <p>All you need to do is show us this email on the day you arrive, and you will be good to go!</p>
        </body>
    </html>
    '''
     # Create the email message
     message = MIMEMultipart()
     message['From'] = from_email
     message['To'] = to_email
     message['Subject'] = subject
     message.attach(MIMEText(body, 'html'))

    # Attach the image file
     try:
        with open(image_path, 'rb') as img_file:
            img = MIMEImage(img_file.read())
            img.add_header('Content-ID', '<image1>')
            img.add_header('Content-Disposition', 'inline', filename=os.path.basename(image_path))
            message.attach(img)
     except Exception as e:
        return HttpResponse(f'Failed to attach image: {e}', status=500)


     try:
         # Establish a connection to the SMTP server
         server = smtplib.SMTP(smtp_server, smtp_port)
         server.starttls()  # Secure the connection
         server.login(smtp_username, smtp_password)  # Log in to the SMTP server
         server.sendmail(from_email, to_email, message.as_string())  # Send the email
         server.quit()  # Close the connection
         return HttpResponse('Email sent successfully!')
     except Exception as e:
         return HttpResponse(f'Failed to send email: {e}')


def home(request):
    return render(request,'home.html')

def modals(request):
    return render(request, 'modals.html')

def modals2(request):
    return render(request, 'modals2.html')

def modals3(request):
    return render(request, 'modals3.html')

def exp1(request):
    return render(request,'exp1.html')

def exp2(request):
    return render(request,'exp2.html')

def exp3(request):
    return render(request,'exp3.html')


def signup(request,method=['GET','POST']):
    if request.method == "POST":
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')

        user=Userdata.objects.filter(email=email)

        if user.exists():
            messages.info(request,"User already exists")
        elif password1 != password2:
            messages.info(request,"Password does not match") 
        else:
            Userdata.objects.create(email=email,password=password1,fname=fname)
            return render(request,'login.html')       
            
        
    return render(request,'signup.html')


def login(request, method=['GET', 'POST']):
     if request.method == "POST":
        email=request.POST.get('email')
        password1=request.POST.get('password1')

        user=Userdata.objects.filter(email=email,password=password1)

        if user.exists():
            return redirect("/main/")
            
     return render(request,'login.html')


def main(request):
    form = HotelSearchForm(request.GET or None)
    hotels = Roominfo.objects.all()

    if form.is_valid():
        location = form.cleaned_data.get('location')
        if location:
            hotels = hotels.filter(location__icontains=location)
    return render(request,'main.html',{'form':form, 'hotels':hotels})


def register(request,id):
    room=Roominfo.objects.get(id=id)


    return render(request,'form.html',{'room':room})



def roomRegister(request):
     hotel_price = request.POST.get('hotel_price')
     if request.method == 'POST':
        room_image=request.POST.get('room_image')
        hotel_name=request.POST.get('hotel_name') 
        print(hotel_name)  
        pname=request.POST.get('pname') 
        page=request.POST.get('page') 
        pperson=request.POST.get('pperson')
        pemail=request.POST.get('pemail') 
        pcontactno=request.POST.get('pcontactno') 
        desc=request.POST.get('desc') 
        Bookinginfo.objects.create(room=room_image,hotel=hotel_name,name=pname,age=page,person=pperson,email=pemail,contactno=pcontactno,desc=desc)
        pemail=str(pemail)
        send_email(pemail)
        return render(request,'billing.html',{'hotel_price':hotel_price})
     



def billing(request):
   
    
    if request.method == "POST":
        firstName=request.POST.get('firstName') 
        hotel_price=request.POST.get('hotel_price') 
        Billinginfo.objects.filter(firstName=firstName,hotel_price=hotel_price)
        

        return redirect('/success/')
        # form = roomRegister(request.POST)
        # if form.is_valid():
        #     form.save()
            

    return render(request,'billing.html',{'hotel_price':hotel_price})


def success(request):
    return render(request, 'success.html')







