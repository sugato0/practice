from rest_framework import serializers

# class User(models.Model):
#     id = models.AutoField(primary_key=True,auto_created=True)
#     FIO = models.CharField(max_length=200)
#     email = models.EmailField(unique=True)
#     email_verified = models.BooleanField(default=-1)
#     password = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=15)
#     birthday = models.DateField()
#     college = models.CharField(max_length=100)
#     profession = models.CharField(max_length=200)

# class Command(models.Model):
#     command_name = models.CharField(max_length=100)
#     type_of_game = models.CharField(max_length=100)
#     nick_name = models.CharField(max_length=50)
#     score = models.CharField(max_length=100)
#     steam = models.CharField(max_length=200)
#     discord = models.CharField(max_length=200)
#     users = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    FIO = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    email_verified = serializers.BooleanField(default=-1)
    password = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=15)
    birthday = serializers.CharField(max_length=15)
    college = serializers.CharField(max_length=100)
    profession = serializers.CharField(max_length=200)



class CommandSerialiser(serializers.Serializer):
    
    

    command_name = serializers.CharField(max_length=100)
    type_of_game = serializers.CharField(max_length=100)
    nick_name = serializers.CharField(max_length=50)
    score = serializers.CharField(max_length=100)
    steam = serializers.CharField(max_length=200)
    discord = serializers.CharField(max_length=200)
    users = UserSerializer()






    
