from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token
from .models import UserProfile, Address, UserVehicle, Vehicle, Device, Simcard, Task
from django.contrib.auth.models import Group


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: UserProfile) -> Token:
        token = super().get_token(user)

        token["asaas"] = user.asaas_token
        token["is_super"] = user.is_superuser
        token["is_tech"] = user.is_tech
        token["is_staff"] = user.is_staff
        token["is_active"] = user.is_active
        token["username"] = user.username

        return token


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class UserVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVehicle
        fields = "__all__"


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class SimcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simcard
        fields = "__all__"


class CreateOrGetSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            value, created = self.get_queryset().get_or_create(**{self.slug_field: data})
            return value
        except (TypeError, ValueError):
            self.fail('invalid')

class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    groups = CreateOrGetSlugRelatedField(many=True, slug_field='name', queryset=Group.objects.all())
    class Meta:
        model = UserProfile
        exclude = ['last_login', 'date_joined', 'date_updated', 'date_blocked']


    def create(self, validated_data):
       group_names = validated_data.pop('groups')
       user = UserProfile.objects.create_user(**validated_data)
       for group_name in group_names:
           group, created = Group.objects.get_or_create(name=group_name)
           user.groups.add(group)
       return user
   
    def update(self, instance, validated_data):
        group_names = validated_data.pop('groups', [])
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_tech = validated_data.get('is_tech', instance.is_tech)
        instance.save()

        # Remove all groups
        instance.groups.clear()
        # Add new groups
        for group_name in group_names:
            group, created = Group.objects.get_or_create(name=group_name)
            instance.groups.add(group)

        return instance

    def delete(self, instance):
        instance.is_active = False
        instance.save()

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
