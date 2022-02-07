from django.contrib.auth.models import Group, User
from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class AnimalType(models.Model):
    name = models.CharField(max_length=256, blank=True, verbose_name=_('İsim'))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('Türler')
        verbose_name_plural = _('Tür Liste')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class Animal(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name=_('Hayvan Sahibi'))
    name = models.CharField(max_length=100,blank=True,verbose_name=_("İsim"))
    type = models.ForeignKey(AnimalType,related_name="animal_type",null=True, blank=True, on_delete=models.CASCADE,verbose_name=_('Tür'))
    age = models.IntegerField(default=0,blank=True,verbose_name=_("Yaş"))
    description = RichTextUploadingField(blank=True, verbose_name=_('Açıklama'))
    genus = models.CharField(max_length=100,blank=True, verbose_name=_("Cins"))

    class Meta:
        verbose_name = _('Hayvanlar')
        verbose_name_plural = _('Hayvan Listesi')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


