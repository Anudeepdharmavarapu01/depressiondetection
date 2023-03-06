from django.db import models

# Create your models here.

class All_users_model(models.Model):
    User_id = models.AutoField(primary_key = True)
    user_Profile = models.FileField(upload_to = 'images/')
    User_Email = models.EmailField(max_length = 50)
    User_Status = models.CharField(max_length = 10)
    
    class Meta:
        db_table = 'all_users'

class Upload_dataset_model(models.Model):
    User_id = models.AutoField(primary_key = True)
    Dataset = models.FileField(upload_to='images/', null=True)
    File_size = models.CharField(max_length = 100) 
    Date_Time = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'upload_dataset'