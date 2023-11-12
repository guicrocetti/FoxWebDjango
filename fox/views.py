from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, mixins
from .models import UserProfile, Address, UserVehicle, Vehicle, Device, Simcard, Task
from .serializers import (
    AddressSerializer,
    UserVehicleSerializer,
    VehicleSerializer,
    DeviceSerializer,
    SimcardSerializer,
    UserProfileSerializer,
    TaskSerializer,
    CustomJWTSerializer,
)
from rest_framework.permissions import IsAuthenticated
from .permissions import CustomCreateUserPermission


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


class AddressListCreateView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class UserVehicleListCreateView(generics.ListCreateAPIView):
    queryset = UserVehicle.objects.all()
    serializer_class = UserVehicleSerializer


class UserVehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserVehicle.objects.all()
    serializer_class = UserVehicleSerializer


class VehicleListCreateView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class SimcardListCreateView(generics.ListCreateAPIView):
    queryset = Simcard.objects.all()
    serializer_class = SimcardSerializer


class SimcardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Simcard.objects.all()
    serializer_class = SimcardSerializer


class UserProfileCreateView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, CustomCreateUserPermission]


class UserProfileListView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
