from django.db import models


    


# Create your models here.
# Create your models here.

# ФИО: gsdfghsdfghfdsgx
# Телефон: gsdfgsdgdfg
# Дата рождения: sfdgdsfgdfgfsdhdf
# Учебное учреждение: dfgdsfgsdfgdf
# Специальность: sdfgsdfgdfg
# Эл. почта: dsfgdsfgdfsgdf


# команда

# Название команды
# Дисциплина
# Учебное заведение
# ФИО
# Телефон
# Дата рождения
# Никнейм
# Рейтинг
# Steam
# Discord
# Специальность


class User(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    FIO = models.CharField(max_length=200)
    emails = models.EmailField()
    email_verified = models.BooleanField(default=-1)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    birthday = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    profession = models.CharField(max_length=200)


class Command(models.Model):
    command_name = models.CharField(max_length=100)
    type_of_game = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=50)
    score = models.CharField(max_length=100)
    steam = models.CharField(max_length=200)
    discord = models.CharField(max_length=200)
    users = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)

