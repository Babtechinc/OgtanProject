from django.db import models
from Registration.models import RegistrationMembershipFormDB
from django.contrib.auth.models import User
# Create your models here.
import os
def create_path(self, filename):
    url = "membership/%s/%s" % (self.NameofOrganisation, filename)
    return os.path.join(
        'membership_form',
        self.NameofOrganisation,
        filename
    )



class MembershipDB(models.Model):
    UserName = models.CharField(null=True, max_length=255)
    Email = models.CharField(null=True, max_length=255)
    Password =  models.CharField(null=True,max_length=255)
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Logo = models.ImageField(null=True,upload_to=create_path)
    TrainingSpecialization= models.TextField(null=True)
    State =  models.CharField(null=True,max_length=255)
    CompanyName = models.CharField(null=True,max_length=255)
    Phone = models.CharField(null=True,max_length=255)
    Address = models.CharField(null=True,max_length=255)
    Website = models.CharField(null=True,max_length=255)
    MembershipNumber = models.CharField(null=True,max_length=255)
    JoinedDate = models.DateTimeField(blank=True, null=True)
    MembershipStartDate = models.DateTimeField(blank=True,null=True)
    MembershipEndDate = models.DateTimeField(blank=True,null=True)
    RegistrationMembershipFormID = models.ForeignKey(RegistrationMembershipFormDB,on_delete=models.CASCADE,blank=True,null=True)
    DateInputed = models.DateTimeField(blank=True)