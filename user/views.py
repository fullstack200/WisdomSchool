from re import template
from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Testimonials
from owner.models import Pictures, Toppers, Announcements

# Create your views here.

def homepageView(request):
    testimonials = Testimonials.objects.all()
    announcements = Announcements.objects.all()
    noOfTestimonials = len(testimonials) - 1
    template = get_template("homePage.html") 
    context = {
        'firstReview':testimonials[0],
        'allReviews':testimonials[1:],
        # For Numeric iteration in django template. 
        'count1':range(1),
        'count':range(noOfTestimonials),
        'announcements':announcements
    }
    return HttpResponse(template.render(context,request))


class Curriculum(TemplateView):
    template_name = 'curriculum.html'

class LifeAtWisdom(TemplateView):
    template_name = 'lifeatwisdom.html'

class ContactView(CreateView):
    template_name = "contact.html"
    model = Testimonials
    fields = '__all__'
    success_url = 'contact'
    

def toppersView(request):
    toppers = Toppers.objects.all()
    template = get_template("toppers.html") 
    context = {
        'toppers':toppers,
    }
    return HttpResponse(template.render(context,request))
    
class GalleryView(TemplateView):
    template_name = "events.html"
     
def classroomsView(request):
    mydata = Pictures.objects.filter(pictureType="Classroom")
    template = loader.get_template('classrooms.html')
    context = {
        'classrooms':mydata,
    }
    return HttpResponse(template.render(context,request))

def sportsView(request):
    mydata = Pictures.objects.filter(pictureType="Sports")
    template = loader.get_template('sports.html')
    context = {
        'sports':mydata,
    }
    return HttpResponse(template.render(context,request))

def exhibitionView(request):
    mydata = Pictures.objects.filter(pictureType="Exhibition")
    template = loader.get_template('exhibition.html')
    context = {
        'exhibition':mydata,
    }
    return HttpResponse(template.render(context,request))

def competitionsView(request):
    mydata = Pictures.objects.filter(pictureType="Competitions")
    template = loader.get_template('competitions.html')
    context = {
        'competitions':mydata,
    }
    return HttpResponse(template.render(context,request))

def graduationView(request):
    mydata = Pictures.objects.filter(pictureType="Graduation")
    template = loader.get_template('graduation.html')
    context = {
        'graduation':mydata,
    }
    return HttpResponse(template.render(context,request))

def schoolTripView(request):
    mydata = Pictures.objects.filter(pictureType="School Trip")
    template = loader.get_template('schooltrip.html')
    context = {
        'schoolTrip':mydata,
    }
    return HttpResponse(template.render(context,request))

def peView(request):
    mydata = Pictures.objects.filter(pictureType="PE")
    template = loader.get_template('pe.html')
    context = {
        'pe':mydata,
    }
    return HttpResponse(template.render(context,request))
