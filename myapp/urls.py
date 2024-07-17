from django.urls import path
from myapp import views
from .views import hotel_list

urlpatterns = [
    path('',views.home,name='home'),
    path('modals/',views.modals, name='modals'),
    path('modals2/',views.modals2, name='modals2'),
    path('modals3/',views.modals3, name='modals3'),
    path('exp1',views.exp1,name='exp1'),
    path('exp2',views.exp2,name='exp2'),
    path('exp3',views.exp3,name='exp3'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('main/',views.main,name='main'),
    path('register/<int:id>',views.register,name='register'),
    path('roomRegister/',views.roomRegister,name='roomRegister'),
    path("billing/",views.billing,name='billing'),
    path('success/', views.success, name='success'),  # Add this line
    path('', hotel_list, name='hotel_list'),
    
    # other patterns...
    #re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),



]