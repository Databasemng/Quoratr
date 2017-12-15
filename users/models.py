from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

from users.managers import UserManager


def set_user_images_upload_path(instance, filename):
    return '/'.join([
        'users', 'user_%d' % instance.id, 'images', filename
    ])


class User(AbstractBaseUser, PermissionsMixin):
    # Base
    email = models.EmailField(
        verbose_name=_('Email'), max_length=255, unique=True
    )
    first_name = models.CharField(verbose_name=_('First Name'), max_length=50)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=50)

    # Permissions
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    is_staff = models.BooleanField(verbose_name=_('Staff'), default=False)

    # Image
    image = models.ImageField(
        verbose_name=_('Image'),
        upload_to=set_user_images_upload_path, null=True, blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name, last_name=self.last_name
        )

    def get_short_name(self):
        return '{first_name}'.format(first_name=self.first_name)

    def image_prev(self):
        if self.image:
            return '<img src="%s" style="max-height: 200px; ' \
                   'background-color:rgba(0, 0, 0, 0.1);"/>' % (
                        settings.MEDIA_URL + self.image.name
                    )
        else:
            return _('Not Found!')
    image_prev.short_description = _('Preview')
    image_prev.allow_tags = True
