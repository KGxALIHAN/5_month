from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def root_view(request):
    return HttpResponse("Welcome to Afisha API! Visit /api/v1/ for the API.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('movie_app.urls')),
    path('', root_view),  
]
