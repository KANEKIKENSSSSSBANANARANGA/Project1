from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name = 'home.html'), name = 'home'),

    path('users/', include('users.urls')),
    path('repairs/', include('repairs.urls'), name="repairs"),
]
