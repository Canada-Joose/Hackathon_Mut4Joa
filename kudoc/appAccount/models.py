from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User


# Create your models here.
class User(AbstractUser):
    #unique=True 유일한 값으로 변경해주기
    #null=True빈값 입력가능하도록 하기
    nickname = models.CharField(max_length=15, unique=True, null=True) 
    def __str__(self):
        return self.email
#이렇게 하면 호출했을 때, 이메일로 호출하도록 만듬.
#allauth는 기본 유저 정보를 입력하고, 다음 닉네임같은 값들을 넣어준다.