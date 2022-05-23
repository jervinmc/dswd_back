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


class PS(models.Model):
    firstname=models.CharField(_('PS'),max_length=255,blank=True,null=True)
    lastname=models.CharField(_('package'),max_length=255,blank=True,null=True)
    middlename=models.CharField(_('descriptions'),max_length=255,blank=True,null=True)
    status=models.CharField(_('status'),max_length=255,blank=True,null=True)
    remarks=models.CharField(_('remarks'),max_length=255,blank=True,null=True)
    date_start=models.DateField(_('date_start'),blank=True,null=True)
    user_id=models.CharField(_('user_id'),max_length=255,blank=True,null=True)
    mop=models.CharField(_('mop'),max_length=255,blank=True,null=True)
    image = models.ImageField(
        _('image'), upload_to=nameFile, default="uploads/PS.png")
    image1 = models.ImageField(
        _('image1'), upload_to=nameFile, default="uploads/PS.png")
    image2 = models.ImageField(
        _('image2'), upload_to=nameFile, default="uploads/PS.png")

    class Meta:
        ordering = ["-id"]
