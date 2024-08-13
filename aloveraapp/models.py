from django.db import models

class Gender(models.Model):
  class Meta:
    db_table = 'tbl_genders'
    
  def __str__(self):
    return self.gender
  
  gender_id = models.BigAutoField(primary_key=True)
  gender = models.CharField(blank=False, max_length=55)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)
  
class User(models.Model):
  class Meta:
    db_table = 'tbl_users'
    
  user_id = models.BigAutoField(primary_key=True)
  first_name = models.CharField(blank=False, max_length=55)
  middle_name = models.CharField(blank=True, max_length=55)
  last_name = models.CharField(blank=False, max_length=55)
  age = models.IntegerField(blank=False)
  gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
  birthdate = models.DateField(blank=False)
  username = models.CharField(blank=False, max_length=55)
  password = models.CharField(blank=False, max_length=255)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)
  