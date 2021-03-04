from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
#importing Models
from .models import paymentStatus, RegistrationMembershipFormDB as Membership_form,paymentStatus,MembershipRegistrationPayment
from Registration.models import status
# importing the requests library
import requests
import decimal
#Amount to of Register
AmountReg = 20000
# Create your views here.
#Import Date
import datetime
dateNow =datetime.datetime.today()



def registration_form_payment(request):
    print(request.POST)
    if request.method == 'POST':
        print('hello')
        ref = request.POST['ref']
        URL = 'https://api.paystack.co/transaction/verify/'+ref
        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'reference': 'REFOGTAN18'}
        headers = {'Authorization': 'Bearer sk_test_5ed66684f189ccc4c2883f408be90b947a5e9e0c'}
        # sending get request and saving the response as response object
        r = requests.get(url=URL, headers=headers)
        data = r.json()
        print(data)
        RegNo = request.POST['RegNo']
        #check the status and Amount
        if data['status'] == True:
            print(AmountReg*100)
            if Membership_form.objects.filter(id=RegNo):
                Sumitted = Membership_form.objects.get(id=RegNo)
                print(data['data' ]['amount'])
                if float(data['data' ]['amount']) == float(AmountReg*100):
                    print('INNN')
                    membershipRegPayment=MembershipRegistrationPayment.objects.create(MembershipReg=Sumitted,AmountPaid=data['data' ]['amount']/100,
                                                        PaymentDate= dateNow,PaymentDateAdded=dateNow,PaymentStatus=paymentStatus[0]
                                                        )
                    print('hello')
                    membershipReg=Membership_form.objects.filter(id=RegNo).update(Status='processing')
                else:
                    print('ffvedwvd')
                    membershipRegPayment=MembershipRegistrationPayment.objects.create(MembershipRegNo=Sumitted, AmountPaid=data['data']['amount']/100,
                                                           PaymentDate=dateNow, PaymentStatus=paymentStatus[1]
                                                          )

    return HttpResponse("hello world")



def MembershipRegistrationPayment_Form(request):
    SumbittedForm = Membership_form.objects.all()
    if request.POST:
        Company = request.POST['Company']
        Amount = request.POST['Amount']
        DatePaid = request.POST['DatePaid']
        Status = request.POST['Status']
        if Membership_form.objects.filter(id=Company):
            Company = Membership_form.objects.get(id=Company)
            Amount = float(Amount)
            CompanyTotal = 0
            for foo in MembershipRegistrationPayment.objects.filter(MembershipReg=Company):
               CompanyTotal = float(foo.AmountPaid) +float(CompanyTotal)
            AmountTotal= Amount+CompanyTotal
            print(AmountTotal)
            if AmountTotal == AmountReg:
                MembershipRegistrationPayment.objects.create(MembershipReg=Company,AmountPaid=Amount,PaymentDateAdded=dateNow,
                                                         PaymentStatus='full',PaymentDate=DatePaid)
                membershipReg = Membership_form.objects.filter(id=Company.id).update(Status='processing')
            elif AmountTotal<AmountReg:
                MembershipRegistrationPayment.objects.create(MembershipReg=Company, AmountPaid=Amount,PaymentDateAdded=dateNow,
                                                             PaymentStatus='part', PaymentDate=DatePaid)
            else:
                messages.error(request, "The Amount You Inputted is too high for a Registration fee . Try Again!")



    return render(request,'MembershipRegistrationPayment_Form.html',context={"SumbittedForm":SumbittedForm,'paymentStatus':paymentStatus})
