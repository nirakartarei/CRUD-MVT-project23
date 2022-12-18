from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.
from django.db.models import Q
from app.models import *
def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)

def display_webpages(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(topic_name='Cricket')   
    LWO=Webpage.objects.exclude(topic_name='Cricket')
    LWO=Webpage.objects.all()[2:5:]
    LWO=Webpage.objects.all().order_by('name')
    LWO=Webpage.objects.filter(topic_name='Cricket').order_by('-name')
    LWO=Webpage.objects.all().order_by(Length('name'))
    LWO=Webpage.objects.all().order_by(Length('name').desc())

    
    d={'LWO':LWO}

    return render(request,'display_webpages.html',d)



def AccessRecord_display(request):
    LAO=AccessRecords.objects.all()
    d={'LAO':LAO}
    return render(request,'AccessRecord_display.html',d)

    