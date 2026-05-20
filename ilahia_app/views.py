from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages 
from .models import Home, Academic_Program, Courses, Management_desk, Administrator_desk ,Gallery,Faculty,Notice,ArtdayGallery,Co_curricularGallery,UpComingEvents

"""
Views module for the Ilahia application.
This module contains the view functions for the Ilahia application.
"""


def index(request):
    banner=Home.objects.order_by('-id').first()
    academic=Academic_Program.objects.all()
    course=Courses.objects.all()
    notice=notice=Notice.objects.all()
    events=UpComingEvents.objects.all()
    context={
        'banner':banner,
        'academic':academic,
        'course':course,
        'notice':notice,
        'events':events,
        }
    return render(request, "index.html",context)


def aboutus(request):
    """Render the about page."""
    return render(request, "aboutus.html")


def courses(request):
    course=Courses.objects.all()
    context={
     
        'course':course,
        }
    return render(request, "courses.html",context)


def gallery(request):
    gallery=Gallery.objects.all()
    arts = ArtdayGallery.objects.all()
    co_curricular = Co_curricularGallery.objects.all()
    context={
        'gallery':gallery,
        'arts':arts,
        'co_curricular':co_curricular,
        }
    return render(request, "gallery.html",context)


def managements(request):
    management=Management_desk.objects.all()
    context={
        'management':management,
        }
    return render(request, "managements.html",context)


def contactpage(request):
    """Render the contact page."""
    return render(request, "contactpage.html")

def send_message(request):
    """Handle form submission and send email."""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Email subject and body
        subject_email = f"New Inquiry: {subject}"
        message_email = f"""
        You have received a new enquiry from {name}

        Email: {email}
        Subject: {subject}

        Message:
        {message}
        """

        try:
            # Create the email with reply-to header
            email_message = EmailMessage(
                subject=subject_email,
                body=message_email,
                from_email=settings.DEFAULT_FROM_EMAIL,  # Must be your authenticated email
                to=['ilahialaw@gmail.com'],  # Recipient
                headers={'Reply-To': email}  # User's email for reply
            )
            email_message.send(fail_silently=False)
            messages.success(request, "Your message has been sent successfully.")
        except Exception as e:
            messages.error(request, f"Failed to send message. Error: {e}")

        return redirect('contactpage')

    return render(request, "contactpage.html")

from .models import Principal_desk

def principal_desk(request):
    """Render the principal's desk page."""
    principal=Principal_desk.objects.order_by('-id').first()
    context={
        'principal':principal,
        }
    return render(request, "principal_desk.html",context)


def chairmans_desk(request):
    """Render the chairman's desk page."""
    return render(request, "chairmans_desk.html")


def admission_process(request):
    """Render the admission process page."""
    return render(request, "admission_process.html")


def fee_structure(request):
    """Render the fee structure page."""
    return render(request, "fee_structure.html")


def vicechairmans_desk(request):
    """Render the vice chairman's desk page."""
    return render(request, "vicechairmans_desk.html")


def administrator_desk(request):
    administrator=Administrator_desk.objects.all()
    context={
        'administrator':administrator,
        }
    return render(request, "administrator_desk.html",context)



def fiveyears(request,id):

    details=Courses.objects.get(id=id)
    context={
        'details':details,
        }
    
    return render(request, "fiveyears.html",context)
    

def send_llb(request): 
    """Handles the POST request for 5-year LL.B. course registration form."""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        subject_email = f"New 5-Year LL.B. Course Registration from {name}"
        message_email = f"""
        A new registration has been submitted for the 5-Year LL.B. course.

        Name: {name}
        Email: {email}
        Phone: {phone}

        Message:
        {message if message else "No message provided."}
        """

        try:
            email_msg = EmailMessage(
                subject=subject_email,
                body=message_email,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['ilahialaw@gmail.com'],
                headers={'Reply-To': email}
            )
            email_msg.send(fail_silently=False)
            messages.success(request, "Your application has been submitted successfully.")
        except Exception as e:
            messages.error(request, f"Submission failed. Error: {e}")

        return redirect('courses')

    return redirect('courses')

def threeyears(request):
    """Render the course details page."""
    return render(request, "threeyears.html")

def register_llb(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        subject_email = f"New LL.B. Course Registration from {name}"
        message_email = f"""
        A new registration has been submitted for the 3-Year LL.B. course.

        Name: {name}
        Email: {email}
        Phone: {phone}

        Message:
        {message if message else "No message provided."}
        """

        try:
            email_msg = EmailMessage(
                subject=subject_email,
                body=message_email,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['ilahialaw@gmail.com'],
                headers={'Reply-To': email}  # Let replies go directly to the applicant
            )
            email_msg.send(fail_silently=False)
            messages.success(request, "Your application has been submitted successfully.")
        except Exception as e:
            messages.error(request, f"Submission failed. Error: {e}")

        return redirect('threeyears')

    return redirect('threeyears')


def academics(request):
    """Render the academics page."""
    return render(request, "academics.html")


def programs(request):
    """Render the programs page."""
    academic=Academic_Program.objects.all()
    context={
        'academic':academic,
        }
    return render(request, "programs.html",context)


def facilities(request):
    
    return render(request, "facilities.html")


def achievements(request):
    """Render the achievements page."""
    return render(request, "achievements.html")


def moot_court_society(request):
    """Render the moot court society page."""
    return render(request, "moot_court_society.html")


def anti_ragging_cell(request):
    """Render the anti-ragging cell page."""
    return render(request, "anti_ragging_cell.html")


def women_cell(request):
    """Render the women cell page."""
    return render(request, "women_cell.html")


def complaint_cell(request):
    """Render the complaint cell page."""
    return render(request, "complaint_cell.html")


def legal_aid_clinic(request):
    """Render the legal aid clinic page."""
    return render(request, "legal_aid_clinic.html")


def statutory(request):
    """Render the legal aid clinic page."""
    return render(request, "statutory.html")

def merit(request):
    """Render the legal aid clinic page."""
    return render(request, "merit.html")

def rules(request):
    """Render the legal aid clinic page."""
    return render(request, "rules.html")

def admindesk(request):
    administrator=Administrator_desk.objects.all()
    context={
        'administrator':administrator,
        }
    return render(request, "admindesk.html",context)

def facultydesk(request):
    Faculties=Faculty.objects.all()
    context={
        'Faculty':Faculties,
        }
    return render(request, "facultydesk.html",context)

def committee(request):
    """Render the legal aid clinic page."""
    return render(request, "committee.html")

def iqac(request):
    """Render the iqac page."""
    return render(request, "iqac.html")

