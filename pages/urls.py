from django.urls import path 
from . import views

urlpatterns=[
    
    path('',views.index,name='index'),

    #About Dropdown Url
    path('about',views.about,name='about'),
    path('overview',views.overview,name='overview'),
    path('our-logo',views.our_logo,name='our-logo'),
    path('mission',views.mission,name='mission'),
    path('vision',views.vision,name='vision'),
    path('management',views.management,name='management'),

    #Corporate-profile Dropdown Url
    path('corporate-profile',views.corporate_profile,name='corporate-profile'),
    path('sanfran-chairman',views.sanfran_chairman,name='sanfran-chairman'),
    path('sanfran-team',views.sanfran_team,name='sanfran-team'),
    path('rewards-recognition',views.rewards_recognition,name='rewards-recognition'),
    path('milestones',views.milestones,name='milestones'),

    #Projects Dropdown Url
    path('projects',views.projects,name='projects'),
    path('completed-projects',views.completed_projects,name='completed-projects'),
    path('ongoing-projects',views.ongoing_projects,name='ongoing-projects'),
    path('upcoming-projects',views.upcoming_projects,name='upcoming-projects'),
    path('finance',views.finance,name='finance'),

    #Media Dropdown Url
    path('media',views.media,name='media'),
    path('gallery',views.gallery,name='gallery'),
    path('press-release',views.press_release,name='press-release'),
    path('news-magazines',views.news_magazines,name='news-magazines'),
    path('download-brochure',views.download_brochure,name='download-brochure'),
    path('customer-testimonials',views.customer_testimonials,name='customer-testimonials'),
    path('blog',views.blog,name='blog'),

    #Career Dropdown Url
    path('career',views.career,name='career'),
    path('current-openings',views.current_openings,name='current-openings'),
    
    #Contact-us Dropdown Url
    path('contact-us',views.contact_us,name='contact-us')
    
    
]