from django.db import models
from customuser.models import CustomUser

class TestCategory(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1024)

    def __str__(self):
        return self.title

class PsyTest(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1024)
    author = models.CharField(max_length=128)
    added_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    addition_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(PsyTest, on_delete=models.CASCADE)
    description = models.TextField(max_length=256)
    
    def __str__(self):
        return self.description

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    description = models.CharField(max_length=128)
    points = models.IntegerField(default=0)
    
    def __str__(self):
        return self.description
    
    
class TestResult(models.Model):
    test = models.ForeignKey(PsyTest, on_delete=models.CASCADE)
    condition_max = models.PositiveIntegerField()
    condition_min = models.PositiveIntegerField()
    description = models.TextField(max_length=2048)
    
    def __str__(self):
        return self.description

class PersonalResult(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    test = models.ForeignKey(PsyTest, on_delete=models.CASCADE)
    result = models.ForeignKey(TestResult, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
    answers =models.TextField(max_length=4096)

    def __str__(self):
        return f"{self.user} - {self.test}"
