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


class Cases(models.Model):
    remarks=models.CharField(_('price'),max_length=255,blank=True,null=True)
    firstname=models.CharField(_('firstname'),max_length=255,blank=True,null=True)
    lastname=models.CharField(_('lastname'),max_length=255,blank=True,null=True)
    middlename=models.CharField(_('middlename'),max_length=255,blank=True,null=True)
    category=models.CharField(_('category'),max_length=255,blank=True,null=True)
    status=models.CharField(_('status'),max_length=255,blank=True,null=True)
    contact_number=models.CharField(_('contact_number'),max_length=255,blank=True,null=True)
    # =models.CharField(_('lastname'),max_length=255,blank=True,null=True)
    image = models.ImageField(
        _('image'), upload_to=nameFile, default="uploads/Cases.png")
    
    birthplace=models.CharField(_('birthplace'),max_length=255,blank=True,null=True)
    date_start=models.DateField(_('date_start'),blank=True,null=True)
    age=models.CharField(_('age'),max_length=255,blank=True,null=True)
    sex=models.CharField(_('sex'),max_length=255,blank=True,null=True)
    religion=models.CharField(_('religion'),max_length=255,blank=True,null=True)
    number_of_siblings=models.CharField(_('number_of_siblings'),max_length=255,blank=True,null=True)
    address=models.CharField(_('address'),max_length=255,blank=True,null=True)
    attainment=models.CharField(_('attainment'),max_length=255,blank=True,null=True)
    attended=models.CharField(_('attended'),max_length=255,blank=True,null=True)
    fathername=models.CharField(_('fathername'),max_length=255,blank=True,null=True)
    birthplace_father=models.CharField(_('birthplace_father'),max_length=255,blank=True,null=True)
    occupation=models.CharField(_('occupation'),max_length=255,blank=True,null=True)
    mothername=models.CharField(_('mothername'),max_length=255,blank=True,null=True)
    birthplace_mother=models.CharField(_('birthplace_mother'),max_length=255,blank=True,null=True)
    occupation_mother=models.CharField(_('occupation_mother'),max_length=255,blank=True,null=True)
    parentsaddress=models.CharField(_('parentsaddress'),max_length=255,blank=True,null=True)
    case_category=models.CharField(_('case_category'),max_length=255,blank=True,null=True)
    perpetrator_name=models.CharField(_('perpetrator_name'),max_length=255,blank=True,null=True)
    perpetrator_nickname=models.CharField(_('perpetrator_nickname'),max_length=255,blank=True,null=True)
    perpetrator_age=models.CharField(_('perpetrator_age'),max_length=255,blank=True,null=True)
    perpetrator_sex=models.CharField(_('perpetrator_sex'),max_length=255,blank=True,null=True)
    perpetrator_relation=models.CharField(_('perpetrator_relation'),max_length=255,blank=True,null=True)
    perpetrator_occupation=models.CharField(_('perpetrator_occupation'),max_length=255,blank=True,null=True)
    perpetrator_address=models.CharField(_('perpetrator_address'),max_length=255,blank=True,null=True)
    perpetrator_status=models.CharField(_('perpetrator_status'),max_length=255,blank=True,null=True)
    source_of_referral=models.CharField(_('source_of_referral'),max_length=255,blank=True,null=True)
    social_worker=models.CharField(_('social_worker'),max_length=255,blank=True,null=True)
    intervention=models.CharField(_('intervention'),max_length=255,blank=True,null=True)
    referral=models.CharField(_('referral'),max_length=255,blank=True,null=True)

    class Meta:
        ordering = ["-id"]