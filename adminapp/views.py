from django.shortcuts import render, redirect
from adminapp.models import  All_users_model, Upload_dataset_model
from userapp.models import User_details
from django.contrib import messages
import os
import socket

# Admin logout
def adminlogout(req):
    messages.info(req, 'You are logged out..!')
    return redirect('admin')

#Admin Dashboard index.html
def admindashboard(req):
    all_users_count =  User_details.objects.all().count()
    pending_users_count = User_details.objects.filter(User_Status = 'Pending').count()
    rejected_users_count = User_details.objects.filter(User_Status = 'removed').count()
    accepted_users_count = User_details.objects.filter(User_Status = 'accepted').count()
    datasets_count = Upload_dataset_model.objects.all().count()
    return render(req, 'admin/admin-dashboard.html',{'a' : pending_users_count, 'b' : all_users_count, 'c' : rejected_users_count, 'd' : accepted_users_count, 'e' : datasets_count})

# Admin pending users
def pendingusers(req):
    pending = User_details.objects.filter(User_Status = 'Pending')
    return render(req, 'admin/admin-pending-users.html', {'pending' : pending})

# Acept users
def accept_user(req, id):
    status_update = User_details.objects.get(User_id = id)
    status_update.User_Status = 'accepted'
    status_update.save()
    messages.info(req, 'User was accepted..!')
    return redirect('pendingusers')

# Remove user
def remove_user(req,id):
    status_update2 = User_details.objects.get(User_id = id)
    status_update2.User_Status = 'removed'
    status_update2.save()
    messages.warning(req, 'User was Removed..!')
    return redirect('pendingusers')

# Admin all users
def allusers(req):
    all_users = User_details.objects.all()
    return render(req, 'admin/admin-all-users.html', {"allu" : all_users})

# change status
# def change_status(req, id):
#     status_update = User_details.objects.get(User_id = id)
#     if (status_update.User_Status == 'accepted'):
#         status_update.User_Status = 'rejected'
#     else:
#         status_update.User_Status = 'accepted'

#     status_update.save()
#     return redirect('allusers')

#Deleet user
def delete_user(req,id):
    user_delete = User_details.objects.get(User_id = id).delete()
    messages.warning(req, 'User was Deleted..!')
    return redirect('allusers')

# Admin upload dataset
def uploaddataset(req):
    if req.method == 'POST':
        file = req.FILES['data_file']
        # print(file)
        file_size = str((file.size)/1024) +' kb'
        # print(file_size)
        Upload_dataset_model.objects.create(File_size = file_size, Dataset = file)
        messages.success(req, 'Your dataset was uploaded..')
    return render(req, 'admin/admin-upload-dataset.html')

# Admin view dataset
def viewdataset(req):
    dataset = Upload_dataset_model.objects.all()
    return render(req, 'admin/admin-view-dataset.html', {'data' : dataset})

# Admin delete dataset
def delete_dataset(req, id):
    dataset = Upload_dataset_model.objects.get(User_id = id).delete()
    messages.warning(req, 'Dataset was deleted..!')
    return redirect('viewdataset')

# Admin ANM Alogorithm
def anmalgm(req):
    return render(req, 'admin/admin-anm-algorithm.html')

# Admin XGBOOST Algorithm
def xgbalgm(req):
    return render(req, 'admin/admin-xgboost-algorithm.html')

# Admin ADA Boost Algorithm
def adabalgm(req):
    return render(req, 'admin/admin-adaboost-algorithm.html')

# Admin KNN Algorithm
def knnalgm(req):
    return render(req, 'admin/admin-knn-algorithm.html')

# Admin SXM Algorithm
def sxmalgm(req):
    return render(req, 'admin/admin-sxm-algorithm.html')

# Admin Decission tree Algorithm
def dtalgm(req):
    return render(req, 'admin/admin-decission-algorithm.html')

# Admin Comparison graph
def cgraph(req):
    return render(req, 'admin/admin-graph-analysis.html')



