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
    nickname = models.CharField(max_length=12, unique=True, blank=True, null=False)
    city = models.CharField(max_length=100, default="Unknown", blank=True, null=True) # to add options
    date_of_birth = models.DateField(_("date of birth"), blank=True, null=True)

    gender = MultiSelectField(choices=Choices.GENDER, max_choices=3, blank=True, null=True)
    pronouns = MultiSelectField(choices=Choices.PRONOUNCES, max_choices=3, blank=True, null=True)
    orientation = MultiSelectField(choices=Choices.ORIENTATION, max_choices=3, blank=True, null=True)
    looking_for = MultiSelectField(choices=Choices.LOOKINF_FOR, blank=True, null=True)

    def __str__(self):
        return f"{self.nickname} from {self.city}"

    def save(self, *args, **kwargs):
        if not self.nickname:
            self.nickname = self.account.email[:12]
        super(Profile, self).save(*args, **kwargs)

class Relationship(models.Model):
    subject = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="subject", primary_key=True)
    object = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="object") # cannot be subject
    is_friend = models.BooleanField(_("friend"), default=False)
    is_following = models.BooleanField(_("following"), default=False)

    def __str__(self):
        subject_name = self.subject.nickname
        object_name = self.object.nickname
        is_friend_text = "is friend with" if self.is_friend else "is not friend with"
        is_following_text = "is following" if self.is_following else "is not following"
        return f"{subject_name} {is_friend_text} and {is_following_text} {object_name}"
