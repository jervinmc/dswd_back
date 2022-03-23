from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Donate(models.Model):
    firstname=models.CharField(_('donate'),max_length=255,blank=True,null=True)
    lastname=models.CharField(_('package'),max_length=255,blank=True,null=True)
    middlename=models.CharField(_('descriptions'),max_length=255,blank=True,null=True)
    status=models.CharField(_('status'),max_length=255,blank=True,null=True)
    image = models.ImageField(
        _('image'), upload_to=nameFile, default="uploads/Donate.png")

    class Meta:
        ordering = ["-id"]
