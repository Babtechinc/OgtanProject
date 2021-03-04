# Generated by Django 3.1.7 on 2021-03-04 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipRegistrationPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PaymentStatus', models.CharField(choices=[('full', 'Full'), ('part', 'Part')], default='pending', max_length=255)),
                ('PaymentDate', models.DateTimeField()),
                ('PaymentDateAdded', models.DateTimeField(blank=True, null=True)),
                ('AmountPaid', models.DecimalField(decimal_places=3, max_digits=255)),
                ('MembershipReg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration.registrationmembershipformdb')),
            ],
        ),
    ]
