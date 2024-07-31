from django.db import models

# Create your models here.
class UserPredictDataModel(models.Model):
    Age = models.CharField(max_length=100)
    Marital_status = models.CharField(max_length=100)
    Sleep = models.CharField(max_length=100)
    Depression = models.CharField(max_length=100)
    Smoking = models.CharField(max_length=100)
    Diabetes = models.CharField(max_length=100)
    BP = models.CharField(max_length=100)
    Hypersensitivity = models.CharField(max_length=100)
    cp = models.CharField(max_length=100)
    trestbps = models.CharField(max_length=100)
    chol = models.CharField(max_length=100)
    fbs = models.CharField(max_length=100)
    restecg = models.CharField(max_length=100)
    thalach = models.CharField(max_length=100)
    exang = models.CharField(max_length=100)
    oldpeak = models.CharField(max_length=100)
    slope = models.CharField(max_length=100)
    ca = models.CharField(max_length=100)
    thal = models.CharField(max_length=100)
    result = models.CharField(max_length=100)

    def __str__(self):
        return self.Age,self.Marital_status,self.Sleep,self.Depression,self.Smoking,self.Diabetes,self.BP,self.Hypersensitivity,self.cp,self.trestbps,self.chol,self.fbs,self.restecg,self.thalach,self.exang,self.oldpeak,self.slope,self.ca,self.thal,self.result

class DoctorFeedModel(models.Model):
    Feedback = models.TextField(max_length=100)

    def __str__(self):
        return str(self.Feedback)