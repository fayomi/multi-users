# NEXT STEPS:
#use function for register view
# CREATE THE SAME SIGN UP PAGE FOR CLIENT PROFILES
# FIGURE OUT HOW TO ADD AND VALIDATE THE PROFILE FORMS IN THE REGISTRATION
# FOCUS ON DECORATORS TO CONTROL ACCESS
# THEN DETAIL AND LIST VIEWS


from django.shortcuts import render
from django.views.generic import (View,
TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from .forms import TrainerSignUpForm, TrainerProfileForm
from .models import User, TrainerProfile
# Create your views here.
class IndexView(TemplateView):
    template_name = 'testing/index.html'


def trainerRegister(request):
    if request.method == 'POST':
        form = TrainerSignUpForm(request.POST)
        profile_form = TrainerProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('testing:index')
    else:
        form = TrainerSignUpForm()
        profile_form = TrainerProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request,'registration/signup_form.html', context)

class TrainerListView(ListView):
    context_object_name = 'trainers'
    model = TrainerProfile

# class TrainerSignUpView(CreateView):
#     model = User
#     form_class = TrainerSignUpForm
#     template_name = 'registration/signup_form.html'
#
#     def get_context_data(self,**kwargs):
#         kwargs['user_type'] = 'trainer'
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self,form):
#         user=form.save()
#         login(self.request, user)
#         return redirect('testing:index')
