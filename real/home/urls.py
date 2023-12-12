from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
   
    path('', views.login, name='login'),
    path('adm/', views.adm, name='adm'),
    #type and cost Search
    path('search/', views.search, name='search'),
    #name Search
    path('ser/<int:id>', views.search_auto, name='ser'),
    path('search2/', views.search2, name='search2'),
    #property_view
    path('pro_view/', views.property_view, name='pro_view'),
    #user view
    path('user_pro/', views.user_view, name='user_pro'),
    path('logout/', views.user_view, name='logout'),
    ]



urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)