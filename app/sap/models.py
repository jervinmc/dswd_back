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


class SAP(models.Model):
    firstname=models.CharField(_('firstname'),max_length=255,blank=True,null=True)
    lastname=models.CharField(_('lastname'),max_length=255,blank=True,null=True)
    gender=models.CharField(_('gender'),max_length=255,blank=True,null=True)
    address=models.CharField(_('address'),max_length=255,blank=True,null=True)
    occupation=models.CharField(_('occupation'),max_length=255,blank=True,null=True)
    monthly_salary=models.CharField(_('monthly_salary'),max_length=255,blank=True,null=True)
    type_of_id=models.CharField(_('type_of_id'),max_length=255,blank=True,null=True)
    id_number=models.CharField(_('id_number'),max_length=255,blank=True,null=True)
    cellphone=models.CharField(_('cellphone'),max_length=255,blank=True,null=True)
    workplace=models.CharField(_('workplace'),max_length=255,blank=True,null=True)
    sector=models.CharField(_('sector'),max_length=255,blank=True,null=True)
    barangay=models.CharField(_('barangay'),max_length=255,blank=True,null=True)
    status=models.CharField(_('status'),max_length=255,blank=True,null=True)
    health_condition=models.CharField(_('health_condition'),max_length=255,blank=True,null=True)
    family_member=models.CharField(_('family_member'),max_length=500,blank=True,null=True)
    user_id=models.CharField(_('user_id'),max_length=500,blank=True,null=True)
    date_start=models.DateField(_('date_start'),blank=True,null=True)
    mop=models.CharField(_('mop'),max_length=255,blank=True,null=True)
    # =models.CharField(_('lastname'),max_length=255,blank=True,null=True)
    image = models.ImageField(
        _('image'), upload_to=nameFile, default="uploads/SAP.png")