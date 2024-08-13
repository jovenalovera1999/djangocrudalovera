from django.shortcuts import render, redirect
from .models import Gender, User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

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

def user_index(request):
  users = User.objects.select_related('gender').all()
  
  data = {
    'users': users
  }
  
  return render(request, 'user/index.html', data)

def user_create(request):
  genders = Gender.objects.all()
  
  data = {
    'genders': genders
  }
  
  return render(request, 'user/create.html', data)

def user_store(request):
  firstName = request.POST.get('first_name');
  middleName = request.POST.get('middle_name');
  lastName = request.POST.get('last_name');
  age = request.POST.get('age');
  genderId = request.POST.get('gender');
  birthDate = request.POST.get('birthdate');
  username = request.POST.get('username');
  password = request.POST.get('password');
  
  User.objects.create(
    first_name=firstName,
    middle_name=middleName,
    last_name=lastName,
    age=age,
    gender_id=genderId,
    birthdate=birthDate,
    username=username,
    password=make_password(password)
  ).save()
  
  messages.success(request, 'User successfully saved.')
  
  return redirect('/users')

def user_edit(request, user_id):
  user = User.objects.select_related('gender').get(pk=user_id)
  genders = Gender.objects.all()
  
  data = {
    'user': user,
    'genders': genders
  }
  
  return render(request, 'user/edit.html', data)

def user_update(request, user_id):
  user = User.objects.get(pk=user_id)
  
  firstName = request.POST.get('first_name');
  middleName = request.POST.get('middle_name');
  lastName = request.POST.get('last_name');
  age = request.POST.get('age');
  genderId = request.POST.get('gender');
  birthDate = request.POST.get('birthdate');
  username = request.POST.get('username');
  
  user.first_name = firstName
  user.middle_name = middleName
  user.last_name = lastName
  user.age = age
  user.gender_id = genderId
  user.birthdate = birthDate
  user.username = username
  user.save()
  
  messages.success(request, 'User successfully updated.')
  
  return redirect('/users')

def user_delete(request, user_id):
  user = User.objects.select_related('gender').get(pk=user_id)
  
  data = {
    'user': user
  }
  
  return render(request, 'user/delete.html', data)

def user_destroy(request, user_id):
  user = User.objects.get(pk=user_id)
  user.delete()
  
  messages.success(request, 'User successfully deleted.')
  return redirect('/users')