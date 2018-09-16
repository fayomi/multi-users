from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import TrainerProfile, ClientProfile, User

class TrainerSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_trainer = True
        user.save()
        trainer = TrainerProfile.objects.create(user=user)
        return user

class TrainerProfileForm(forms.ModelForm):
    class Meta:
        model = TrainerProfile
        fields = ('age','location','skills')
