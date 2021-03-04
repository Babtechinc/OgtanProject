from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
#importing Models
from .models import RegistrationMembershipFormDB as Membership_form,status
from Payment.models import MembershipRegistrationPayment
from ogtanProject import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import random
# importing the requests library
import requests
#Import Date
from Payment.views import AmountReg
import datetime
dateNow =datetime.datetime.today()

from django.contrib import messages
# Create your views here.
import ast


def registration_form_list(request):
    listSumitted = Membership_form.objects.all()

    return render(request,'membership-form-sumbitted.html',context={'listSumitted':listSumitted})

def registration_form_list_single(request,regID):
    coreArea = False
    CertificationOfFacilitators = False
    EvaluationMethods = False

    if Membership_form.objects.filter(id=regID):
        Sumitted = Membership_form.objects.get(id=regID)
        # Converting string to list
        coreArea = ast.literal_eval(Sumitted.coreAreas)
        CertificationOfFacilitators = ast.literal_eval(Sumitted.CertificationOfFacilitators)
        EvaluationMethods = ast.literal_eval(Sumitted.EvaluationMethods)
        AmountPaid = 0.00
        for foo in MembershipRegistrationPayment.objects.filter(MembershipReg=Sumitted):
            AmountPaid = float(foo.AmountPaid) + float(AmountPaid)

    else:
        messages.error(request, "Can't find the Company Name")
        return redirect('registration_form_list')
    return render(request,'membership-form-sumbitted-single.html',context={ 'Sumitted':Sumitted,
                                                                            "status":status ,
                                                                            "coreArea":coreArea,
                                                                            "AmountPaid":AmountPaid,
                                                                            "AmountReg":AmountReg,
                                                                            'CertificationOfFacilitators':CertificationOfFacilitators,
                                                                            'EvaluationMethods':EvaluationMethods})
def registration_update_status(request,regID):
    if request.method == 'POST':
        statusUpdate = request.POST['statusUpdate']
        if Membership_form.objects.filter(id=regID):
            Sumitted = Membership_form.objects.filter(id=regID).update(Status=statusUpdate)

    return HttpResponse("hell world")

def registration_check(request):
    if request.method == 'POST':
        regID = request.POST['regID']
        password = request.POST['password']
        if Membership_form.objects.filter(RegNO=regID):
            if Membership_form.objects.filter(RegNO=regID, Password=password):
                Sumitted=Membership_form.objects.get(RegNO=regID, Password=password)
                password_length = 5
                possible_characters = "abcdefghijklmnopqrstuvwxyz1234567890"
                random_character_list = [random.choice(possible_characters) for i in range(password_length)]
                random_password = "".join(random_character_list)
                password = "OGTAN" + random_password
                return render(request, 'membership-form-checked-Status.html', context={'Sumitted': Sumitted,'dateNow':str(password),'AmountReg':AmountReg })
            else:
                messages.error(request, 'Check detail again')
        else:
            messages.error(request, 'No Company of ('+regID+') doesn\'t Exist')

    return render(request,'membership-form-check-Status.html',context={})



def registration_form(request):
    regNo=False
    try:
        if request.POST:
            print(request.POST)
            NameofOrganisation  = request.POST['NameofOrganisation']
            uploadPath = 'media/membership_form/' + NameofOrganisation + '/'
            uploadPathModel = 'membership_form/' + NameofOrganisation + '/'
            MailingAddress = None
            if request.POST['MailingAddress']:
                MailingAddress= request.POST['MailingAddress']
            OfficeAddress=None
            if request.POST['OfficeAddress']:
                OfficeAddress= request.POST['OfficeAddress']
            CompanyPhoneNo=  None
            if request.POST['CompanyPhoneNo']:
                CompanyPhoneNo = request.POST['CompanyPhoneNo']
            CompanyWebsite = None
            if request.POST['CompanyWebsite']:
                CompanyWebsite = request.POST['CompanyWebsite']
            DateofIncorporation = None
            if request.POST['DateofIncorporation']:
                DateofIncorporation = request.POST['DateofIncorporation']
            TypeofBusiness = None
            if request.POST['TypeofBusiness']:
                TypeofBusiness = request.POST['TypeofBusiness']
            TypeofOwnership = None
            if request.POST['TypeofOwnership']:
                TypeofOwnership = request.POST['TypeofOwnership']
            AnnualTurnover = None
            if request.FILES['AnnualTurnover']:
                AnnualTurnover = request.FILES['AnnualTurnover']
                fs = FileSystemStorage(location=uploadPath)
                filename = fs.save(AnnualTurnover.name, AnnualTurnover)
                AnnualTurnover  =uploadPathModel + AnnualTurnover.name # saves the file to `media` folde
            NameOfManagingDirector = None
            if request.POST['NameOfManagingDirector']:
                NameOfManagingDirector = request.POST['NameOfManagingDirector']
            PhoneNoOfManagingDirector =None
            if request.POST['PhoneNoOfManagingDirector']:
                PhoneNoOfManagingDirector =request.POST['PhoneNoOfManagingDirector']
            EmailAddressofManagingDirector= None
            if request.POST['EmailAddressofManagingDirector']:
                EmailAddressofManagingDirector= request.POST['EmailAddressofManagingDirector']
            NameofAlternate = None
            if request.POST['NameofAlternate']:
                NameofAlternate = request.POST['NameofAlternate']
            PhoneofAlternate = None
            if request.POST['PhoneofAlternate']:
                PhoneofAlternate = request.POST['PhoneofAlternate']
            Organizationalcharts = None
            if request.FILES['Organizationalcharts']:
                Organizationalcharts  = request.FILES['Organizationalcharts']
                fs = FileSystemStorage(location=uploadPath)
                filename = fs.save(Organizationalcharts.name, Organizationalcharts)
                Organizationalcharts =uploadPathModel+Organizationalcharts.name # saves the file to `media` folde
            TotalStaffStrength = None
            if request.POST['TotalStaffStrength']:
                TotalStaffStrength = request.POST['TotalStaffStrength']
            MissionFirm = None
            if request.POST['MissionFirm']:
                MissionFirm = request.POST['MissionFirm']
            MainActivities = None
            if request.POST['MainActivities']:
                MainActivities = request.POST['MainActivities']
            TypeofTraining =None
            if request.POST['TypeofTraining'] :
                TypeofTraining = request.POST['TypeofTraining']
            coreAreas = None
            if request.POST.getlist('coreAreas'):
                coreAreas = str(request.POST.getlist('coreAreas'))
            InternationalAccreditation = None
            if request.FILES['InternationalAccreditation']:
                InternationalAccreditation =  request.FILES['InternationalAccreditation']
                fs = FileSystemStorage(location=uploadPath)
                filename = fs.save(InternationalAccreditation.name, InternationalAccreditation)
                InternationalAccreditation = uploadPathModel+InternationalAccreditation.name
            internationalAffiliations =None
            if request.FILES['internationalAffiliations']:
                internationalAffiliations = request.FILES['internationalAffiliations']
                fs = FileSystemStorage(location=uploadPath)
                filename = fs.save(internationalAffiliations.name, internationalAffiliations)
                internationalAffiliations = uploadPathModel+internationalAffiliations.name
            AccreditationbyRelevantBody = None
            if request.FILES['AccreditationbyRelevantBody']:
                AccreditationbyRelevantBody = request.FILES['AccreditationbyRelevantBody']
                fs = FileSystemStorage(location=uploadPath)
                filename = fs.save(AccreditationbyRelevantBody.name, AccreditationbyRelevantBody)
                AccreditationbyRelevantBody=  uploadPathModel + AccreditationbyRelevantBody.name
            CollaborativeTrainingFile = None
            if request.FILES['CollaborativeTrainingFile']:
                CollaborativeTrainingFile = request.FILES['CollaborativeTrainingFile']
                fs = FileSystemStorage(location=uploadPath)
                filename = fs.save(CollaborativeTrainingFile.name, CollaborativeTrainingFile)
                CollaborativeTrainingFile = uploadPathModel+ CollaborativeTrainingFile.name
            CollaborativeTraining = None
            if request.POST['CollaborativeTraining']:
                CollaborativeTraining = request.POST['CollaborativeTraining']
            RestrictionsToTraining = None
            if request.POST['CollaborativeTraining']:
                RestrictionsToTraining = request.POST['CollaborativeTraining']
            CertificationOfFacilitators = None
            if request.POST.getlist('CertificationOfFacilitators'):
                CertificationOfFacilitators = str(request.POST.getlist('CertificationOfFacilitators'))
            MethodsOfTraining = None
            if request.FILES['MethodsOfTraining']:
                MethodsOfTraining = request.FILES['MethodsOfTraining']
                fs = FileSystemStorage(location=uploadPath)
                filename = fs.save(MethodsOfTraining.name, MethodsOfTraining)
                MethodsOfTraining =uploadPathModel+MethodsOfTraining.name
            EvaluationMethods =  None
            if request.POST.getlist('EvaluationMethods'):
                EvaluationMethods =  str(request.POST.getlist('EvaluationMethods'))
            TrainingFacilitySize =None
            if request.POST['TrainingFacilitySize']:
                TrainingFacilitySize = request.POST['TrainingFacilitySize']
            TrainingCapacity = None
            if request.POST['TrainingCapacity']:
                TrainingCapacity = request.POST['TrainingCapacity']
            TrainingMaterials = None
            if request.POST['TrainingMaterials']:
                TrainingMaterials = request.POST['TrainingMaterials']
            LicensesOfTrianing = None
            if request.FILES['LicensesOfTrianing']:
                LicensesOfTrianing = request.FILES['LicensesOfTrianing']
                fs = FileSystemStorage(location=uploadPath)
                filename = fs.save(LicensesOfTrianing.name, LicensesOfTrianing)
                LicensesOfTrianing = uploadPathModel+LicensesOfTrianing.name
            AccommodationForTrianing = None
            if request.FILES['AccommodationForTrianing']:
                AccommodationForTrianing = request.FILES['AccommodationForTrianing']
                fs = FileSystemStorage(location=uploadPath)
                filename = fs.save(AccommodationForTrianing.name, AccommodationForTrianing)
                AccommodationForTrianing =uploadPathModel+AccommodationForTrianing.name
            CertifiedTrainer =None
            if request.FILES['CertifiedTrainer']:
                CertifiedTrainer = request.FILES['CertifiedTrainer']
                fs = FileSystemStorage(location=uploadPath)
                filename = fs.save(CertifiedTrainer.name, CertifiedTrainer)
                CertifiedTrainer = uploadPathModel + CertifiedTrainer.name

            AreasOfGovernmentForTrianing = None
            if request.POST['AreasOfGovernmentForTrianing']:
                AreasOfGovernmentForTrianing = request.POST['AreasOfGovernmentForTrianing']

            password_length = 5
            possible_characters = "abcdefghijklmnopqrstuvwxyz1234567890"
            random_character_list = [random.choice(possible_characters) for i in range(password_length)]
            random_password = "".join(random_character_list)
            password = "OGTAN" + random_password
            if Membership_form.objects.last():
                regNo = Membership_form.objects.last()
                regNo = "OGTAN" + str(regNo.id + 1)


            Membership_form.objects.create(NameofOrganisation=NameofOrganisation,
                                                RegNO=regNo,
                                                    Password=password,
                                                  MailingAddress=MailingAddress,
                                                  CompanyWebsite=CompanyWebsite,
                                                  OfficeAddress=OfficeAddress,
                                                  CompanyPhoneNo=CompanyPhoneNo,
                                                  DateofIncorporation=DateofIncorporation,
                                                  TypeofBusiness=TypeofBusiness,
                                                  TypeofOwnership=TypeofOwnership,
                                                  AnnualTurnover= AnnualTurnover,
                                                  NameOfManagingDirector=NameOfManagingDirector,
                                                  PhoneNoOfManagingDirector=PhoneNoOfManagingDirector,
                                                  EmailAddressofManagingDirector=EmailAddressofManagingDirector,
                                                  NameofAlternate=NameofAlternate,
                                                  PhoneofAlternate=PhoneofAlternate,
                                                  Organizationalcharts=Organizationalcharts,
                                                  TotalStaffStrength=TotalStaffStrength,
                                                  MissionFirm=MissionFirm,
                                                  MainActivities=MainActivities,
                                                  TypeofTraining=TypeofTraining,
                                                  coreAreas=coreAreas,
                                                  InternationalAccreditation=InternationalAccreditation,
                                                  internationalAffiliations=internationalAffiliations,
                                                  AccreditationbyRelevantBody=AccreditationbyRelevantBody,
                                                  CollaborativeTraining=CollaborativeTraining,
                                                  CollaborativeTrainingFile=CollaborativeTrainingFile,
                                                  RestrictionsToTraining=RestrictionsToTraining,
                                                  CertificationOfFacilitators = CertificationOfFacilitators,
                                                  MethodsOfTraining=MethodsOfTraining,
                                                  EvaluationMethods=EvaluationMethods,
                                                  TrainingFacilitySize=TrainingFacilitySize,
                                                  TrainingCapacity=TrainingCapacity,
                                                  TrainingMaterials=TrainingMaterials,
                                                  LicensesOfTrianing= LicensesOfTrianing,
                                                  AccommodationForTrianing=AccommodationForTrianing,
                                                  CertifiedTrainer = CertifiedTrainer,
                                                  AreasOfGovernmentForTrianing=AreasOfGovernmentForTrianing,
                                                  Status='pending',
                                                  DateInputed=dateNow )
            MailReg(request,regNo,password,MailingAddress)

    except KeyError:
        ...

    return render(request,'membership-form.html',context={})
def MailReg (request,regno,password,email):
    if Membership_form.objects.filter(RegNO=regno,MailingAddress=email,Password=password):
        member = Membership_form.objects.get(RegNO=regno,MailingAddress=email,Password=password)
        subject = 'Your Company '+member.NameofOrganisation+'was register at OGTAN'
        html_message = render_to_string('RegMail.html', {"member":member})
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['adegbola.babs-ogunleye@stu.cu.edu.ng']
        message = EmailMessage(subject, html_message, email_from, recipient_list)
        message.content_subtype = 'html'  # this is required because there is no plain text email message
        message.send()
        messages.success(request, 'Email Sent')



