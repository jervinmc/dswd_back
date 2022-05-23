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


class Intervention(models.Model):
    name=models.CharField(_('name'),max_length=255,blank=True,null=True)
    case_id=models.CharField(_('case_id'),max_length=255,blank=True,null=True)
    # image = models.ImageField(
    #     _('image'), upload_to=nameFile, default="uploads/Intervention.png")

    class Meta:
        ordering = ["-id"]
