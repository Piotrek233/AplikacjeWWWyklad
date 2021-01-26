from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=250)
    destiny = models.CharField(max_length=250)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Rating(models.Model):
    subject = models.CharField(max_length=250)
    value = models.IntegerField()
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    def __str__(self):
        return self.subject
