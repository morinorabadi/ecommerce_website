from django.db import models


class Boss(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)

# for manage product and admin easyer
# allways first employe of every boss is self boss
class Employe(models.Model):
    boss = models.ForeignKey(Boss,on_delete=models.CASCADE)

    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)


class MoriToken(models.Model):
    time = models.DateTimeField(auto_now_add=True, editable=True)
    user = models.ForeignKey(Employe, on_delete=models.CASCADE)
    token = models.CharField(max_length=50)