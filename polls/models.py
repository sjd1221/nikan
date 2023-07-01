from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
import os


class PathAndRename:
    """
    fields to use for naming, order is important
    """

    def __init__(self, path, fields_to_use=('pk',)):
        self.path = path
        self.fields_to_use = fields_to_use

    def wrapper(self, instance, filename):
        ext = '.'.join(filename.split('.')[1:])

        if self.is_any_unique_exist(instance):
            filename = '{}.{}'.format(self.get_filename_by_fields(instance), ext)
        elif self.is_any_unique_together_exist(instance):
            filename = '{}.{}'.format(self.get_filename_by_fields(instance), ext)
        else:
            filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)

    def is_any_unique_exist(self, instance):
        if 'pk' in self.fields_to_use:
            return True
        return any([instance._meta.get_field(field).unique for field in self.fields_to_use if hasattr(instance, field)])

    def is_any_unique_together_exist(self, instance):
        if hasattr(instance._meta, 'unique_together'):
            if isinstance(instance._meta.unique_together, (list, tuple)):
                for uniques in instance._meta.unique_together:
                    # if any one of the unique together set is exists in the fields to use
                    if all(map(lambda field: field in self.fields_to_use, uniques)):
                        return True
            else:
                if all(map(lambda field: field in self.fields_to_use, instance._meta.unique_together)):
                    return True
        return False

    def get_filename_by_fields(self, instance):
        return '_'.join([str(getattr(instance, field)) for field in self.fields_to_use])



Hospital_Choices = (
    ('نیکان غرب', 'نیکان غرب'),
    ('نیکان اقدسیه', 'نیکان اقدسیه'),
    ('نیکان شرق', 'نیکان شرق'),
)

class Doctor(models.Model):
    Prof_Choices = (
        ('ارتوپدی', 'ارتوپدی'),
        ('اورولوژی', 'اورولوژی'),
        ('اطفال', 'اطفال'),
        ('پزشک عمومی', 'پزشک عمومی'),
        ('جراح عمومی', 'جراح عمومی'),
        ('جراحی مغز و اعصاب', 'جراحی مغز و اعصاب'),
        ('داخلی', 'داخلی'),
        ('نورولوژی', 'نورولوژی'),
        ('زنان و زایمان', 'زنان و زایمان'),
        ('قلب و عروق', 'قلب و عروق'),
        ('گوش و حلق و بینی', 'گوش و حلق و بینی'),
    )
    Prof2_Choices = (
        ('پزشک عمومی', 'پزشک عمومی'),
        ('جراحی استخوان', 'جراحی استخوان'),
        ('اکوکاردیوگرافی', 'اکوکاردیوگرافی'),
        ('اینترونشنال کاردیوگرافی', 'اینترونشنال کاردیوگرافی'),
        ('برست', 'برست'),
        ('جراحی درون بین', 'جراحی درون بین'),
        ('جراحی درون بین لاپارسکوپی', 'جراحی درون بین لاپارسکوپی'),
        ('جراحی سرطان', 'جراحی سرطان'),
        ('رینولوژی', 'رینولوژی'),
    )
    IdDoctor = models.BigIntegerField(unique=True)
    Name = models.CharField(max_length= 300)
    Mobile = models.BigIntegerField()
    Home = models.BigIntegerField(null = True, blank= True)
    Desc = models.TextField(null = True, blank= True)
    ClinicNum = models.BigIntegerField(null = True, blank= True)
    ClinicAdd = models.TextField(null = True, blank= True)
    ClinicShift = models.TextField(null = True, blank= True)
    Prof = models.CharField(max_length= 300, choices= Prof_Choices)
    Prof2 = models.CharField(max_length=300, choices= Prof2_Choices)
    # IDIMG = models.CharField(max_length=300, default='D')
    IMG = models.ImageField(upload_to= PathAndRename('media/doctor', ['IdDoctor']).wrapper, null= True, blank= True)
    Hospital = models.CharField(max_length= 300, choices= Hospital_Choices)
    is_active = models.BooleanField(default=True)
    HospitalExtra = models.CharField(max_length= 300, blank= True)
    Username = models.CharField(max_length= 300, null = True, blank= True)
    Password = models.CharField(max_length= 300, null = True, blank= True)

    # class Meta:
    #     db_table = 'Doctor_view_table'



class Personnel(models.Model):
    Section_Choices = (
        ('سپند', 'سپند'),
        ('سپهر', 'سپهر'),
        ('ستایش', 'ستایش'),
        ('سپید', 'سپید'),
    )
    Post_Choices = (
        ('پرستار', 'پرستار'),
        ('کاخدار', 'کاخدار'),
        ('منشی', 'منشی'),
        ('کمک بهیار', 'کمک بهیار'),
        ('کارشناس', 'کارشناس'),
    )
    IdPersonnel = models.BigIntegerField(unique=True)
    Name = models.CharField(max_length= 300)
    Mobile = models.BigIntegerField()
    Home = models.BigIntegerField(null = True, blank= True)
    Section = models.CharField(max_length= 300, choices= Section_Choices)
    Post = models.CharField(max_length= 300,choices= Post_Choices)
    Hospital = models.CharField(max_length=300, choices= Hospital_Choices)
    # IDIMG = models.CharField(max_length=300, default='P')
    IMG = models.ImageField(upload_to=PathAndRename('media/personnel', ['IdPersonnel']).wrapper, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    HospitalExtra = models.CharField(max_length=300, blank=True)
    Username = models.CharField(max_length=300, null = True, blank= True)
    Password = models.CharField(max_length=300, null = True, blank= True)
    # class Meta:
    #     db_table = 'Personnel_view_table'


class Person(models.Model):
    IdPerson = models.BigIntegerField(unique=True)
    Name = models.CharField(max_length= 300)
    Mobile = models.BigIntegerField()
    Home = models.BigIntegerField(null = True, blank= True)
    About = models.TextField(null = True, blank= True)
    Hospital = models.CharField(max_length=300, choices= Hospital_Choices)
    # IDIMG = models.CharField(max_length=300, default='A')
    IMG = models.ImageField(upload_to=PathAndRename('media/ashkhas', ['IdPerson']).wrapper, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    HospitalExtra = models.CharField(max_length=300, blank=True)
    Username = models.CharField(max_length=300, null = True, blank= True)
    Password = models.CharField(max_length=300, null = True, blank= True)
    # class Meta:
    #     db_table = 'Person_view_table'


class HospitalName(models.Model):
    Name = models.CharField(max_length= 300)