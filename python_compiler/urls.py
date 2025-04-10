from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home_view_urls'),
    path('compiler/', compiler_view, name="compiler_view_urls"),
    path('contact_us/',contact_us_view,name='contact_us_urls'),
    path('about_us/',about_us_view, name="about_us_url"),
]