from django.shortcuts import render, redirect
from .models import Gender
from django.contrib import messages

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
  messages.success(request, 'Gender successfully saved.')
  return redirect('/genders')

def gender_edit(request, gender_id):
  gender = Gender.objects.get(pk=gender_id)
  
  data = {
    'gender': gender
  }
  
  return render(request, 'gender/edit.html', data)

def gender_update(request, gender_id):
  genderObj = Gender.objects.get(pk=gender_id)
  gender = request.POST.get('gender')
  
  genderObj.gender = gender
  genderObj.save()
  
  return redirect('/genders')
  
def gender_delete(request, gender_id):
  gender = Gender.objects.get(pk=gender_id)
  
  data = {
    'gender': gender
  }
  
  return render(request, 'gender/delete.html', data)

def gender_destroy(request, gender_id):
  genderObj = Gender.objects.get(pk=gender_id)
  genderObj.delete()
  
  return redirect('/genders')