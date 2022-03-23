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


class Beneficiaries(models.Model):
    location=models.CharField(_('location'),max_length=255,blank=True,null=True)
    firstname=models.CharField(_('firstname'),max_length=255,blank=True,null=True)
    lastname=models.CharField(_('lastname'),max_length=255,blank=True,null=True)
    middlename=models.CharField(_('middlename'),max_length=255,blank=True,null=True)
    occupation=models.CharField(_('occupation'),max_length=255,blank=True,null=True)
    status=models.CharField(_('status'),max_length=255,blank=True,null=True)
    user_id=models.CharField(_('user_id'),max_length=255,blank=True,null=True)
    # image = models.ImageField(
    #     _('image'), upload_to=nameFile, default="uploads/Beneficiaries.png")

    class Meta:
        ordering = ["-id"]
