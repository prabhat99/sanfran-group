from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.choices import price_choices,state_choices,bedroom_choices
from realtors.models import Realtor

# Create your views here.
def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context={
        'listings':listings,
        'state_choices':state_choices,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
    }
    return render(request,'pages/index.html',context)

#About-us Dropdown Views
def about(request):
    realtors=Realtor.objects.order_by('-hire_date')
    #Get MVP
    mvp_realtors=Realtor.objects.all().filter(is_mvp=True)
    context={
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }
    return render(request,'pages/About-Us/about.html',context)

def overview(request):
    return render(request,'pages/overview/overview.html')

def our_logo(request):
    return render(request,'pages/our-logo/our-logo.html')

def mission(request):
    return render(request,'pages/mission/mission.html')

def vision(request):
    return render(request,'pages/vision/vision.html')

def management(request):
    return render(request,'pages/management/management.html')

#Corporate-profile Dropdown Views
def corporate_profile(request):
    return render(request,'pages/corporate-profile/corporate-profile.html')

def sanfran_chairman(request):
    return render(request,'pages/sanfran-chairman/sanfran-chairman.html')

def sanfran_team(request):
    return render(request,'pages/sanfran-team/sanfran-team.html')

def rewards_recognition(request):
    return render(request,'pages/rewards-recognition/rewards-recognition.html')

def milestones(request):
    return render(request,'pages/milestones/milestones.html')

#Projects Dropdown Views
def projects(request):
    return render(request,'pages/projects/projects.html')

def completed_projects(request):
    return render(request,'pages/completed-projects/completed-projects.html')

def ongoing_projects(request):
    return render(request,'pages/ongoing-projects/ongoing-projects.html')

def upcoming_projects(request):
    return render(request,'pages/upcoming-projects/upcoming-projects.html')

def finance(request):
    return render(request,'pages/finance/finance.html')

#Media Dropdown Views
def media(request):
    return render(request,'pages/media/media.html')

def gallery(request):
    return render(request,'pages/gallery/gallery.html')

def press_release(request):
    return render(request,'pages/press-release/press-release.html')

def news_magazines(request):
    return render(request,'pages/news-magazines/news-magazines.html')

def download_brochure(request):
    return render(request,'pages/download-brochure/download-brochure.html')

def customer_testimonials(request):
    return render(request,'pages/customer-testimonials/customer-testimonials.html')

def blog(request):
    return render(request,'pages/blog/blog.html')
#Career Dropdown Views
def career(request):
    return render(request,'pages/career/career.html')

def current_openings(request):
    return render(request,'pages/current-openings/current-openings.html')
#Contact-us views
def contact_us(request):
    return render(request,'pages/contact-us/contact-us.html')

