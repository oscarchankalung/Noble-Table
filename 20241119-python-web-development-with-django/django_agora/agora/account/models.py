from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class Account(AbstractUser):
    username = None
    first_name = None
    last_name = None
    groups = None
    email = models.EmailField(_("email address"), max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_personal = models.BooleanField(default=True)
    is_organization = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("account")
        verbose_name_plural = _("accounts")
        abstract = False

    def __str__(self):
        return f"{self.email}"

"""
class Profile(models.Model):
    class Gender(models.TextChoices):
        FEMALE = "F", _("Female")
        MALE = "M", _("Male")
        NON_BINARY = "NB", _("Non Binary")
    
    class Pronouns(models.TextChoices):
        FEMALE = "F", _("She/Her")
        MALE = "M", _("He/Him")
        NON_BINARY = "NB", _("They/Them")

    class Orientation(models.TextChoices):
        HETEROSEXUAL = "HETER", _("Hetersexual")
        HOMOSEXUAL = "HOMO", _("Homosexual")
        BISEXUAL = "BI", _("Bisexual")
    
    class LookingFor(models.TextChoices):
        LONG_TERM = "LONG", _("Long-Term Relationship")
        SHORT_TERM = "SHORT", _("Short-Term Relationship")
        FRIEND = "FRIEND", _("Friendship")

    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    nickname = models.CharField(max_length=12, unique=True, blank=False)
    date_of_birth = models.DateField(_("date of birth"), null=True)
    city = models.CharField(max_length=100, blank=True) # to add options
    gender = models.CharField(max_length=4, choices=Gender, blank=True)
    pronouns = models.CharField(max_length=4, choices=Pronouns, blank=True)
    orientation = models.CharField(max_length=10, choices=Orientation, blank=True)
    looking_for = models.CharField(_("looking for"), max_length=10, choices=LookingFor, blank=True)

    def __str__(self):
        return f"{self.nickname} from {self.city}"

class Relationship():
    subject = models.ForeignKey(Profile, on_delete=models.CASCADE, primary_key=True)
    object = models.OneToOneField(Profile, on_delete=models.CASCADE) # cannot be subject
    is_friend = models.BooleanField(_("is friend"), default=False)
    is_following = models.BooleanField(_(" is following"), default=False)

    def __str__(self):
        subject_name = self.subject.get("nickname")
        object_name = self.object.get("nickname")
        is_friend_text = "is friend with" if self.is_friend else "is not friend with"
        is_following_text = "is following" if self.is_following else "is not following"
        return f"{subject_name} {is_friend_text} and {is_following_text} {object_name}"
"""