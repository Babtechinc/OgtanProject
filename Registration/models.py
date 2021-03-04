from django.db import models

status = [
            ("pending", "Pending"),
            ("processing", "Processing"),
            ("Done", "done"),
            ("member", "Member"),


        ]
# Create your models here.

import os

def create_path(self, filename):
    url = "membership_form/%s/%s" % (self.NameofOrganisation, filename)
    return os.path.join(
        'membership_form',
        self.NameofOrganisation,
        filename
    )


class RegistrationMembershipFormDB(models.Model):

    Status = models.CharField(choices=status,default='pending',max_length=255)
    NameofOrganisation = models.CharField(null=True,max_length=255)
    Logo = models.ImageField( upload_to=create_path,null=True)

    Password =  models.CharField(null=True,max_length=255)
    RegNO= models.CharField(null=True,max_length=255)
    MailingAddress = models.CharField(null=True,max_length=255)
    State = models.CharField(null=True, max_length=255)
    OfficeAddress = models.CharField(null=True,max_length=255)
    CompanyPhoneNo= models.CharField(null=True,max_length=255)
    CompanyWebsite =models.CharField(null=True,max_length=255)
    DateofIncorporation = models.DateField(null=True)
    TypeofBusiness =models.CharField(null=True,max_length=255)
    TypeofOwnership =models.CharField(null=True,max_length=255)
    AnnualTurnover = models.FileField(null=True,upload_to=create_path)
    NameOfManagingDirector =models.CharField(null=True,max_length=255)
    PhoneNoOfManagingDirector =models.CharField(null=True,max_length=255)
    EmailAddressofManagingDirector =models.CharField(null=True,max_length=255)
    NameofAlternate =models.CharField(null=True,max_length=255)
    PhoneofAlternate =models.CharField(null=True,max_length=255)
    Organizationalcharts = models.FileField(null=True,upload_to=create_path)
    TotalStaffStrength =models.CharField(null=True,max_length=255)
    MissionFirm =models.TextField(null=True)
    MainActivities =models.TextField(null=True)
    TypeofTraining =models.CharField(null=True,max_length=255)
    coreAreas = models.TextField(null=True)
    InternationalAccreditation= models.FileField(null=True,upload_to=create_path)
    internationalAffiliations = models.FileField(null=True,upload_to=create_path)
    AccreditationbyRelevantBody = models.FileField(null=True,upload_to=create_path)
    CollaborativeTraining = models.TextField(null=True)
    CollaborativeTrainingFile = models.FileField(null=True,upload_to=create_path)
    RestrictionsToTraining = models.TextField(null=True)
    CertificationOfFacilitators = models.TextField(null=True)
    MethodsOfTraining =models.FileField(null=True,upload_to=create_path)
    EvaluationMethods = models.TextField(null=True)
    TrainingFacilitySize = models.TextField(null=True)
    TrainingCapacity = models.CharField(null=True,max_length=255)
    TrainingMaterials = models.TextField(null=True)
    LicensesOfTrianing = models.FileField(null=True,upload_to=create_path)
    AccommodationForTrianing =models.FileField(null=True,upload_to=create_path)
    CertifiedTrainer =models.FileField(null=True,upload_to=create_path)
    AreasOfGovernmentForTrianing = models.TextField(null=True)
    DateInputed = models.DateTimeField(blank=True)

