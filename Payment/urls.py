from django.urls import path,include
from . import views
urlpatterns = [
    path('membership-form/API', views.registration_form_payment, name='registration_form_paymentAPI'),
    path('membership-form', views.MembershipRegistrationPayment_Form, name='registration_form_payment'),
]