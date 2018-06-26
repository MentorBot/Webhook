from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import ASCIIUsernameValidator

class MentorDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, unique=True)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=100)
    linkdin = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image')
    short_bio = models.TextField()
    mentor_status = models.BooleanField(default=False)
    mentorship_field = models.CharField(max_length=100)
    mentorship_details = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    mentoraccount = models.ForeignKey('MentorLogin.username', related_name='menotrdetails', on_delete=models.CASCADE, null=False)

    class Meta:
        ordering=('date_created',)

    def __str__(self):
        return self.name, self.phone_nummber, self.email, self.linkdin, self.github, self.facebook, self.twitter, self.mentorship_field, self.mentorship_detials, self.date_created, self.date_modified


class MentorLogin(models.Model):
    username_validator = ASCIIUsernameValidator()
    email = models.EmailField(_('email address'), blank=True)
    username = models.CharField( _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    password = models.CharField(max_length=250, null=True)
    last_login = models.CharField(max_length=250, null=True)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return '{} ( {} )'.format(self.email, self.username)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
