from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Pet
from .forms import CreateForm
from .permissions import IsOwnerOrAdmin
from .serializers import PetSerializer


def get_pets(request):
    current_user = request.user
    if current_user.is_authenticated:
        pets = Pet.objects.filter(owner=current_user)
        return render(request, 'list.html', {'pets': pets})
    else:
        pets = Pet.objects.all()
        return render(request, 'list.html', {'pets': pets})


def add_pet(request):
    current_user = request.user
    if current_user.is_authenticated:
        if request.method == 'POST':
            form = CreateForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                age = form.cleaned_data['age']
                weight = form.cleaned_data['weight']
                height = form.cleaned_data['height']
                details = form.cleaned_data['details']
                Pet.objects.create(name=name, age=age, weight=weight,
                                   height=height, details=details, owner=current_user)
                return redirect('get_pets')
        else:
            form = CreateForm()
    else:
        return redirect('login')

    return render(request, 'add_form.html', {'form': form})


class PetList(generics.ListCreateAPIView):
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Pet.objects.filter(deleted=None)
        else:
            return Pet.objects.filter(owner=user, deleted=None)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def delete(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            pet = self.get_object()
            pet.delete()
            data = model_to_dict(pet)
            serializer = self.get_serializer(data=data)
            if serializer.is_valid():
                serializer.save(deleted=True, owner=self.request.user)
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
