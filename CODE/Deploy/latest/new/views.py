from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from . import forms
from . import models
import numpy as np
import joblib

model = joblib.load('E:/Diwakar/Project/Machine learning/ITPML15/Deploy/latest/new/Lr.pkl')

# Create your views here.
def home_view(request):
    if request.method == "POST":
        username = request.POST['username']
        #print(username)
        password = request.POST['password']
        #print(password)
        name = request.POST['user']
        if name == "user":
            user = authenticate(request, username=username, password=password)
            #print(user)
            if user is not None:
                login(request, user)
                return render(request, 'new/index.html')
            else:
                msg = 'Invalid Credentials'
                form = AuthenticationForm(request.POST)
                return render(request, 'new/user_login.html', {'form': form, 'msg': msg})
        else:
            user = authenticate(request, username=username, password=password)
            #print(user)
            if user is not None:
                login(request, user)
                model = models.UserPredictDataModel.objects.latest('id')
                form = forms.DoctorFeedForm(request.POST)
                #print(model)
                return render(request, 'new/last.html', {'model':model,'form':form})
            else:
                msg = 'Invalid Credentials'
                form = AuthenticationForm(request.POST)
                return render(request, 'new/user_login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
    return render(request, 'new/user_login.html', {'form': form})


def doctor_login(request):
    form = AuthenticationForm()
    return render(request, 'new/login.html', {'form': form})

def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #print('saving')
            form.save()
            return render(request, 'new/user_signup.html', {'msg':"Successfully registered",'form':form})
    else:
        form = UserCreationForm()
    return render(request, 'new/user_signup.html',{'form':form})

def doctor_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #print('saving')
            form.save()
            return render(request, 'new/user_signup.html', {'msg':"Successfully registered",'form':form})
    else:
        form = UserCreationForm()
    return render(request, 'new/signup.html',{'form':form})




def predict_view(request):
    if request.method == 'POST':
        print('IF')
        fieldss = ['Age', 'Marital_status', 'Sleep', 'Depression', 'Smoking', 
        'Diabetes', 'BP', 'Hypersensitivity', 'cp', 'trestbps', 'chol', 'fbs',
         'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        form = forms.UserPredictDataForm(request.POST)
        features = []
        for i in fieldss:
            info = request.POST[i]
            features.append(info)
        final_features = [np.array(features)]
        #print(final_features)
        prediction = model.predict(final_features)
        #print(prediction)
        output = prediction[0]
        print(features)
        print(output)
        if output == 1:
            output = 'You Are Safe'
            return render(request, 'new/index.html', {'prediction_text':output,'form':form})
        else:
            output = 'Please Consult your Cardiologist as you are prone to Myocardial infaraction'
            if form.is_valid():
                print('saving')
                form.save()
            ob = models.UserPredictDataModel.objects.latest('id')
            ob.result = output
            ob.save()
            return render(request, 'new/index.html', {'prediction_text':output,'form':form})
    else:
        print('ELSE')
        form = forms.UserPredictDataForm(request.POST)
    return render(request, 'new/index.html', {'form':form})



def doctor_patient_details_view_all(request):
    model = models.UserPredictDataModel.objects.all()
    #print(model)
    return render(request, 'new/all.html', {'model':model})



def doctor_patient_details_view_last(request):
    if request.method == "POST":
        form = forms.DoctorFeedForm(request.POST)
        #print('form',form)
        if form.is_valid():
            form.save()
            model = models.UserPredictDataModel.objects.latest('id')
            #print(model)
            return render(request, 'new/last.html', {'model':model,'msg':'Feedback sent'})
        else:
            model = models.UserPredictDataModel.objects.latest('id')
            return render(request, 'new/last.html', {'model':model,'msg':'Feedback Error'})
    else:
        form = forms.DoctorFeedForm()
        model = models.UserPredictDataModel.objects.latest('id')
    return render(request, 'new/last.html', {'model':model,'form':form})
        


def feedback(request):
    model = models.DoctorFeedModel.objects.latest('id')
    return render(request, 'new/feedback.html', {'model':model})

def apredict(request):
    return render(request, 'new/index.html')

def logout_view(request):
    logout(request)
    return redirect('home_view')

