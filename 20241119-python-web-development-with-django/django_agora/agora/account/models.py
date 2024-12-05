from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

from .managers import CustomUserManager
from .model_choices import Choices

class Account(AbstractUser):
    username = None
    first_name = None
    last_name = None
    groups = None

    email = models.EmailField(_("email"), max_length=255, unique=True)
    is_personal = models.BooleanField(
        _("personal"),
        default=True,
        help_text=_("Designates whether the user is personal with limited features."),
    )
    is_profit = models.BooleanField(
        _("profit"),
        default=False,
        help_text=_("Designates whether the user is profit with more features."),
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ["email"]
        verbose_name = _("account")
        verbose_name_plural = _("accounts")
        abstract = False

    def __str__(self):
        return f"{self.email}"

class Profile(models.Model):

    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    nickname = models.CharField(max_length=12, unique=True, blank=False)
    date_of_birth = models.DateField(_("date of birth"), null=True)
    city = models.CharField(max_length=100, blank=True) # to add options

    GENDER, PRONOUNCES, ORIENTATION, LOOKINF_FOR = Choices

    gender = MultiSelectField(choices=GENDER, max_choices=3, max_length=3)
    pronouns = MultiSelectField(choices=PRONOUNCES, max_choices=3, max_length=3)
    orientation = MultiSelectField(choices=ORIENTATION, max_choices=3, max_length=3)
    looking_for = MultiSelectField(choices=LOOKINF_FOR)

    def __str__(self):
        return f"{self.nickname} from {self.city}"

"""
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