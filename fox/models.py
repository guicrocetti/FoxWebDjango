# core/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    ssn = models.PositiveBigIntegerField(null=True, blank=True)
    asaas_token = models.CharField(max_length=255, null=True, blank=True)
    phone1 = models.CharField(max_length=255, null=True, blank=True)
    phone2 = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    is_tech = models.BooleanField(default=False)
    vehicle = models.ManyToManyField('Vehicle', through='UserVehicle', related_name='user_vehicle')
    address = models.OneToOneField('Address', on_delete=models.CASCADE, related_name='user_id', null=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_blocked = models.DateTimeField(null=True, blank=True)
    
    REQUIRED_FIELDS = ["ssn", "is_tech"]

class Address(models.Model):
    cep = models.CharField(max_length=255, null=True)
    street = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=2, null=True)
    number = models.CharField(max_length=255, null=True)
    complement = models.CharField(max_length=255, null=True)

class UserVehicle(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)

class Vehicle(models.Model):
    plate = models.CharField(max_length=8, unique=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    brand = models.CharField(max_length=20, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    engine = models.CharField(max_length=8, null=True, blank=True)
    power = models.CharField(max_length=7, null=True, blank=True)
    fuel = models.CharField(max_length=20, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    fipe = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='vehicle_owned')

class Device(models.Model):
    imei = models.CharField(max_length=20, unique=True, null=False)
    brand = models.CharField(max_length=50, null=True)
    model = models.CharField(max_length=50, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    is_active = models.BooleanField(default=False)
    seller = models.CharField(max_length=128, null=True)
    comment = models.TextField(null=True)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='device')
    simcard = models.OneToOneField('Simcard', on_delete=models.CASCADE, related_name='device')

class Simcard(models.Model):
    iccid = models.CharField(max_length=20, unique=True)
    msisdn = models.CharField(max_length=13, unique=True)
    apn = models.CharField(max_length=32, null=True)
    login = models.CharField(max_length=18, null=True)
    password = models.CharField(max_length=18, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    is_active = models.BooleanField(default=False)
    comment = models.TextField(null=True)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='simcard')

class TypeOptions(models.TextChoices):
    INSTALL = "Instalação"
    REMOVE = "Retirada"
    REPLACE = "Troca"
    MAINTENANCE = "Manutenção"
    DEFAULT = "Outros"
        
class PriorityOptions(models.TextChoices):
    HIGH = "Alta"
    MEDIUM = "Normal"
    LOW = "Baixa"
    URGENT = "Urgente"
    DEFAULT = "Nenhuma"

class Task(models.Model):
    comments = models.TextField()
    type = models.CharField(max_length=50, choices=TypeOptions.choices, default=TypeOptions.DEFAULT, null=True)
    priority = models.CharField(max_length=50, choices=PriorityOptions.choices, default=PriorityOptions.DEFAULT, null=True)
    remote_block = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='created_task')
    updated_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='updated_task')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='task')
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='task')
    simcard = models.ForeignKey(Simcard, on_delete=models.CASCADE, related_name='task')
    tech = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='task')
