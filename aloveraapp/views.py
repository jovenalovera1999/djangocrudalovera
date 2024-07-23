from django.shortcuts import render, redirect
from .models import Gender

def gender_index(request):
  genders = Gender.objects.all()
  
  data = {
    'genders': genders
  }
  
  return render(request, 'gender/index.html', data)

def gender_create(request):
  return render(request, 'gender/create.html')

def gender_store(request):
  gender = request.POST.get('gender')
  Gender.objects.create(gender=gender).save()
  
  return redirect('/genders')