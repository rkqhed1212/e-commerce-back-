from django.contrib.auth.models import AbstractUser
from django.db import models
from core import models as core_models



class Address_list(core_models.TimeStampedModel):

    address = models.CharField(max_length=10, null = True, blank= True)
    pcc = models.CharField(max_length=10, null = True, blank= True)
    user = models.ForeignKey("User", related_name = "Address_list", on_delete = models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)



class User(AbstractUser): 

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_CHOICSES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female")
    )
    
    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "KOREAN")
    )

    SNS_NAVER = "naver"
    SNS_KAKAO = "kakao"
    SNS_GOOGLE = "google"
    

    SNS_CHOICES = (
        (SNS_NAVER, "naver"),
        (SNS_KAKAO, "kakao"),
        (SNS_GOOGLE, "google")
    )


    number = models.CharField(max_length=20, null = True)
    point = models.CharField(max_length=3, null = True, blank = True )
    address = models.ForeignKey("Address_list", related_name = "User", max_length=20, on_delete = models.CASCADE ,null = True, blank= True)
    nick_name = models.CharField(max_length=20, null = True,)
    gender = models.CharField(choices = GENDER_CHOICSES, max_length=10, null = True, blank = True)
    sns_type = models.CharField(choices = SNS_CHOICES, max_length=10, null = True, blank= True)
    birthday = models.DateField(null = True, blank= True)
    language = models.CharField(choices = LANGUAGE_CHOICES, max_length = 10, null = True,  blank = True)
    superhost = models.BooleanField(default = False)
