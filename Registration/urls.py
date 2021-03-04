from django.urls import path,include

from Registration import views
urlpatterns = [
    path('', views.registration_form, name='registration_form'),

    path('check', views.registration_check, name='registration_check'),
    path('list', views.registration_form_list, name='registration_form_list'),
    path('list/<str:regID>', views.registration_form_list_single, name='registration-form-list-single'),
    path('list/<str:regID>/update', views.registration_update_status, name='registration_update_status')

]