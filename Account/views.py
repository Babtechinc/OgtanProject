
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
#importing Models
from .models import MembershipDB
from django.contrib.auth.models import User
from Registration.models import RegistrationMembershipFormDB as Membership_form,status
from Payment.models import MembershipRegistrationPayment
from ogtanProject import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.models import User
import random
# importing the requests library
import requests
#Import Date
from django.contrib.auth import authenticate
from Payment.views import AmountReg
import datetime
dateNow =datetime.datetime.today()

from django.contrib import messages
# Create your views here.
import ast
def dashboard(request):
    return render(request,'Dashboard.html',context={})

def LogIN(request):
    if request.POST:
        usernameIN = request.POST['username']
        passwordIn = request.POST['password']
        user = authenticate(username=usernameIN, password=passwordIn)
        if user is not None:
            return redirect('home')
        # A backend authenticated the credentials
        else:
            messages.error(request, "Check Detail Again")
        # No backend authenticated the credentials
    return render(request,'Log-In.html',context={})

def All_Member(request):

    return render(request,'membershipDB.html',context={})

def AddMember(request):
    SumbittedForm = Membership_form.objects.all()
    if request.POST:
        print(request.POST)

        MN = request.POST.getlist('MN')
        password_length = 5
        possible_characters = "abcdefghijklmnopqrstuvwxyz1234567890"
        random_character_list = [random.choice(possible_characters) for i in range(password_length)]
        random_password = "".join(random_character_list)
        password = "OGTAN" + random_password
        #create new member without id
        #check it exist

        if not MembershipDB.objects.filter(UserName=str(MN[0])+str(MN[1])):
            NameofOrganisation = request.POST['NameofOrganisation']
            uploadPath = 'media/membership/' + NameofOrganisation + '/'
            uploadPathModel = 'membership/' + NameofOrganisation + '/'
            MailingAddress = None
            if request.POST['MailingAddress']:
                MailingAddress = request.POST['MailingAddress']
            OfficeAddress = None
            if request.POST['OfficeAddress']:
                OfficeAddress = request.POST['OfficeAddress']
            CompanyPhoneNo = None
            if request.POST['CompanyPhoneNo']:
                CompanyPhoneNo = request.POST['CompanyPhoneNo']
            CompanyWebsite = None
            if request.POST['CompanyWebsite']:
                CompanyWebsite = request.POST['CompanyWebsite']
            DateofAccepted = None
            if request.POST['DateofAccepted']:
                DateofAccepted = request.POST['DateofAccepted']
            State = None
            if request.POST['State']:
                State = request.POST['State']
            logo = None
            if request.FILES['Logo']:
                logo = request.FILES['Logo']
                fs = FileSystemStorage(location=uploadPath)
                filename = fs.save(logo.name, logo)
                logo = uploadPathModel + logo.name  # saves the file to `media` folde
            coreAreas = None
            if request.POST.getlist('coreAreas'):
                coreAreas = str(request.POST.getlist('coreAreas'))
            user = User.objects.create_user(username=str(MN[0]) + str(MN[1]), email=MailingAddress,
                                            password=password)
            MembershipDB.objects.create(UserName=str(MN[0]) + str(MN[1]), Email=MailingAddress,
                                        Password=password,User=user,Logo=logo,TrainingSpecialization=coreAreas,State=State,
                                        Phone=CompanyPhoneNo,Address=OfficeAddress,JoinedDate=DateofAccepted,DateInputed=dateNow
                                        ,MembershipNumber=str(MN[0])+'/'+str(MN[1]))
        else:
            messages.error(request, "Member Number Exist ")
    return render(request,'AddMember-form.html',context={"SumbittedForm":SumbittedForm})

def AddMemberID(request,regID):
    member =False
    SumbittedForm = Membership_form.objects.all()
    Membership_form.objects.filter(id=regID).update(Status='member')
    #check if regID is int
    if Membership_form.objects.filter(id=regID):
        member =Membership_form.objects.get(id=regID)

    if request.POST:
        print(request.POST)
        print('LRMLVK DBN')
        if Membership_form.objects.filter(id=regID):
            member = Membership_form.objects.get(id=regID)
            MN=request.POST.getlist('MN')
            DateMembership=request.POST['DateMembership']
            #create password
            password_length = 5
            possible_characters = "abcdefghijklmnopqrstuvwxyz1234567890"
            random_character_list = [random.choice(possible_characters) for i in range(password_length)]
            random_password = "".join(random_character_list)
            password = "OGTAN" + random_password
            #create the user to django user model
            if not MembershipDB.objects.filter(UserName=str(MN[0])+str(MN[1]),MembershipNumber=str(MN[0])+'/'+str(MN[1])):
                user = User.objects.create_user(username=str(MN[0])+str(MN[1]),email=member.MailingAddress,password=password)
                MembershipDB.objects.create(UserName=str(MN[0])+str(MN[1]),Email=member.MailingAddress,Password=password,
                                            User=user,Logo=member.Logo,TrainingSpecialization=member.coreAreas ,
                                            State=member.State,CompanyName=member.NameofOrganisation,Phone=member.CompanyPhoneNo,
                                            Address=member.OfficeAddress,Website=member.CompanyWebsite,RegistrationMembershipFormID=member
                                            ,JoinedDate =DateMembership,MembershipNumber=str(MN[0])+'/'+str(MN[1]),
                                            DateInputed=dateNow,
                                            )
            else:
                messages.error(request, "Member Number Exist ")

            # NewMember = MembershipDB
            # print(MN)




    return render(request,'AddMember.html',context={"SumbittedForm":SumbittedForm,'member':member})