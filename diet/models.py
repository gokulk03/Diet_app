from django.db import models 

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Diet(models.Model):
    diet = models.CharField(max_length=100)
    def __str__(self):
        return self.diet


class Day(models.Model):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    Day_type_choices = [(MONDAY,'Monday'),(TUESDAY,'Tuesday'),(WEDNESDAY,'Wednesday'),(THURSDAY,'Thursday'),(FRIDAY,'Friday'),(SATURDAY,'Saturday'),(SUNDAY,'Sunday')]
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    day = models.IntegerField(choices=Day_type_choices)
    diet = models.ForeignKey(Diet,on_delete=models.CASCADE)   

    def __str__(self):
        return f"{self.name},{self.day},{self.diet}"
    



    



