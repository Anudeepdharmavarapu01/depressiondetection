from django.shortcuts import render, redirect
from userapp.models import User_details, Predict_details
from django.contrib import messages
# Create your views here.



# Register
def register(req):
    if req.method == 'POST' :
        name = req.POST.get('myName')
        age = req.POST.get('myAge')
        password = req.POST.get('myPwd')
        phone = req.POST.get('myPhone')
        email = req.POST.get('myEmail')
        address = req.POST.get("address")
        image = req.FILES['image']
        try:
            user_data = User_details.objects.get(Email = email)
            messages.warning(req, 'Email was already registered, choose another email..!')
            return redirect("register")
        except:
            User_details.objects.create(Full_name = name, Image = image, Age = age, Password = password, Address = address, Email = email, Phone_Number = phone)
            messages.success(req, 'Your account was created..')
            return redirect('register')
 
    return render(req, 'user/user-register.html')

# Login Function
def login(req):
    if req.method == 'POST':
        user_email = req.POST.get('uemail')
        user_password = req.POST.get('upwd')
        try:
            user_data = User_details.objects.get(Email = user_email, Password = user_password, User_Status = 'accepted')
            req.session["User_id"] = user_data.User_id
            messages.success(req, 'You are logged in..')
            return redirect("userdashboard")
        except:
            messages.error(req, 'You are trying to loging with wrong details..')
            return redirect('login') 
           
    return render(req, 'main/main-user.html')

# User Logout
def userlogout(req):
    messages.info(req, 'You are logged out..')
    return redirect('login')

# user-dashboard Function
def userdashboard(req):
    return render(req, 'user/user-dashboard.html')

# user-profile Function
def profile(req):
    user_id = req.session["User_id"]
    user = User_details.objects.get(User_id = user_id)
    if req.method == 'POST':
        user_name = req.POST.get('userName')
        user_age = req.POST.get('userAge')
        user_phone = req.POST.get('userPhNum')
        user_email = req.POST.get('userEmail')
        user_address = req.POST.get("userAddress")
        # user_img = request.POST.get("userimg")

        user.Full_name = user_name
        user.Age = user_age
        user.Address = user_address
        user.Phone_Number = user_phone

        if len(req.FILES) != 0:
            image = req.FILES['profilepic']
            user.Image = image
            user.Full_name = user_name
            user.Age = user_age
            user.save()
        else:
            user.Full_name = user_name
            user.Age = user_age
            user.save()
        print(user_name, user_age, user_phone, user_email, user_address)
    context = {"i":user}
    return render(req, 'user/user-profile.html', context)

# predictdiabetes form Function
def predict(req):
    if req.method == 'POST':
        field_1 = req.POST.get('field1')
        field_2 = req.POST.get('field2')
        field_3 = req.POST.get('field3')
        field_4 = req.POST.get('field4')
        field_5 = req.POST.get('field5')
        field_6 = req.POST.get('field6')
        field_7 = req.POST.get('field7')
        field_8 = req.POST.get('field8')
        field_9 = req.POST.get('field9')
        field_10 = req.POST.get('field10')
        print(field_1, field_2, field_3, field_4, field_5, field_6, field_7, field_8, field_9, field_10)
        Predict_details.objects.create(Field_1 = field_1, Field_2 = field_2, Field_3 = field_3, Field_4 = field_4, Field_5 = field_5, Field_6 = field_6, Field_7 = field_7, Field_8 = field_8, Field_9 = field_9, Field_10 = field_10)
        try:
            if(field_1 != '' and field_2 != '' and field_3 != '' and field_4 != '' and field_5 != '' and field_6 != '' and field_7 != '' and field_8 != '' and field_9 != '' and field_10 != '') :
                messages.success(req, 'Your prediction was done..')
                return redirect("result")
        except:
            messages.error(req, 'You are missing some fields, please fill all the fileds..')
            return redirect('predict')
    return render(req, 'user/user-predict.html')

# Result function
def result(req):
    return render(req, 'user/user-result.html')