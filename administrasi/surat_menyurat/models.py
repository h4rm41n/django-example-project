from django.db import models
from django.utils.translation import ugettext_lazy as _

class Instansi(models.Model):
  KATEGORI_INSTANSI = (
    ('swasta', 'Swasta'),
    ('pemerintah', 'Pemerintah'),
  )

  nama_instansi = models.CharField(max_length=255, blank=False, null=False)
  kategori      = models.CharField(max_length=255, choices=KATEGORI_INSTANSI)
  telepon       = models.CharField(max_length=255, blank=True, null=True)
  kode_pos      = models.CharField(max_length=255, blank=True, null=True)
  alamat        = models.TextField(blank=True, null=True)
  created       = models.DateTimeField(auto_now=False, auto_now_add=True)
  updated       = models.DateTimeField(auto_now=True, auto_now_add=False)

  def __str__(self):
    return self.nama_instansi

class Surat(models.Model):
  nomor         = models.CharField(max_length=255, blank=False, null=False)
  tgl_surat     = models.CharField(
                  _("Tanggal surat"),
                  help_text=_('Tanggal di dalam isi surat'),
                  max_length=255, blank=False, null=False)
  perihal       = models.CharField(max_length=255, blank=False, null=False)
  pengirim      = models.CharField(
                  help_text=_('Orang atau jasa yang mengantar surat'),
                  max_length=255, blank=True, null=True)
  deskripsi     = models.TextField(blank=True, null=True)

class SuratMasuk(Surat):
  asal_instansi = models.ForeignKey(
                  Instansi,
                  help_text=_('Jika asal instansi tidak ada, silahkan ke menu instansi'),
                  on_delete=models.CASCADE)
  tgl_masuk     = models.CharField(
                  _("Tanggal masuk"),
                  help_text=_('Tanggal masuk surat ke kantor'),
                  max_length=255, blank=False, null=False)
  created       = models.DateTimeField(auto_now=False, auto_now_add=True)
  updated       = models.DateTimeField(auto_now=True, auto_now_add=False)

  def __str__(self):
    return self.nomor

class SuratKeluar(Surat):
  tujuan_instansi   = models.ForeignKey(
                      Instansi,
                      help_text=_('Jika tujuan instansi tidak ada, silahkan ke menu instansi'),
                      on_delete=models.CASCADE)
  tgl_keluar        = models.CharField(
                      _("Tanggal keluar"),
                      help_text=_('Tanggal keluar surat dari kantor'),
                      max_length=255, blank=False, null=False)
  created           = models.DateTimeField(auto_now=False, auto_now_add=True)
  updated           = models.DateTimeField(auto_now=True, auto_now_add=False)

  def __str__(self):
    return self.nomor
