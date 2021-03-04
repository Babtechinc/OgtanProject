from django.urls import path,include
from . import views
urlpatterns = [
    path('AddMember', views.AddMember, name='AddMember'),
    path('AddMember/<str:regID>', views.AddMemberID, name='AddMemberId'),
    path('log_in/', views.LogIN, name='log_in'),
   # path('Profile/All', views.all, name='log_in'),
    # path('membership-form', views.MembershipRegistrationPayment_Form, name='registration_form_payment'),
]