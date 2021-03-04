from django.db import models
from Registration.models import RegistrationMembershipFormDB

paymentStatus = [('full','Full'),('part','Part')]
# Create your models here.
class MembershipRegistrationPayment(models.Model):
    MembershipReg = models.ForeignKey(RegistrationMembershipFormDB,on_delete=models.CASCADE,null=True,blank=True)
    PaymentStatus = models.CharField(choices=paymentStatus,default='pending',max_length=255)
    PaymentDate = models.DateTimeField()
    PaymentDateAdded = models.DateTimeField(null=True,blank=True)
    AmountPaid = models.DecimalField(max_digits=255,decimal_places=3)