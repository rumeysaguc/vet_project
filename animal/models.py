from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class AnimalType(models):
    name = models.CharField(max_length=256, blank=True, verbose_name=_('İsim'))

    class Meta:
        verbose_name = _('Türler')
        verbose_name_plural = _('Tür Liste')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class Animal(models.Model):
    name = models.CharField(max_length=100,blank=True,verbose_name=_("İsim"))
    type = models.ForeignKey(AnimalType,related_name="animal_type",null=True, blank=True, on_delete=models.CASCADE,verbose_name=_('Tür'))
    age = models.IntegerField(default=1,blank=True,verbose_name=_("Yaş"))
    description = RichTextUploadingField(blank=True, verbose_name=_('Açıklama'))

    class Meta:
        verbose_name = _('Hayvanlar')
        verbose_name_plural = _('Hayvan Listesi')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


