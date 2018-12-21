from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from surat_menyurat.models import SuratMasuk, SuratKeluar, Instansi
from surat_menyurat.forms import FormSuratMasuk, FormInstansi, FormSuratKeluar

@login_required
def home(request):
  return render(request, 'home.html')

def login_redirect(request):
  return redirect('login')

@login_required
def surat_masuk_list(request):
  return render(request, "surat/surat_masuk_list.html", {
    'data': SuratMasuk.objects.all().order_by('-id')
  })

@login_required
def surat_masuk_delete(request, id):
  surat_masuk = get_object_or_404(SuratMasuk, pk=id)
  surat_masuk.delete()
  return redirect('surat:surat_masuk_list')

@login_required
def surat_masuk_edit(r, id):
  if r.POST:
    form = FormSuratMasuk(r.POST or None)
    id = r.POST['id']
    surat_masuk = get_object_or_404(SuratMasuk, pk=id)
    if form.is_valid():
      surat_masuk.nomor = form.cleaned_data['nomor']
      surat_masuk.tgl_surat = form.cleaned_data['tgl_surat']
      surat_masuk.perihal = form.cleaned_data['perihal']
      surat_masuk.pengirim = form.cleaned_data['pengirim']
      surat_masuk.deskripsi = form.cleaned_data['deskripsi']
      surat_masuk.asal_instansi = form.cleaned_data['asal_instansi']
      surat_masuk.tgl_masuk = form.cleaned_data['tgl_masuk']

      surat_masuk.save(force_update=True)
      return redirect('surat:surat_masuk_list')
    return render(r, 'surat/surat_masuk_form_edit.html', {'form':form, 'id':id})

  surat_masuk = get_object_or_404(SuratMasuk, pk=id)
  form = FormSuratMasuk(initial={
          'nomor':surat_masuk.nomor,
          'tgl_surat':surat_masuk.tgl_surat,
          'perihal':surat_masuk.perihal,
          'pengirim':surat_masuk.pengirim,
          'deskripsi':surat_masuk.deskripsi,
          'asal_instansi':surat_masuk.asal_instansi,
          'tgl_masuk':surat_masuk.tgl_masuk,
        })
  return render(r, 'surat/surat_masuk_form_edit.html', {'form':form, 'id':surat_masuk.id})

@login_required
def surat_masuk_form(request):
  form = FormSuratMasuk(request.POST or None)
  if request.POST:
    if form.is_valid():
      form.save(commit=True)

      return redirect('surat:surat_masuk_list')

    return render(request, "surat/surat_masuk_form_new.html", {
      'form': form
    })

  return render(request, "surat/surat_masuk_form_new.html", {
    'form': form
  })

@login_required
def surat_keluar_form(request):
  form = FormSuratKeluar(request.POST or None)
  if request.POST:
    if form.is_valid():
      form.save(commit=True)

      return redirect('surat:surat_keluar_list')

    return render(request, "surat/surat_keluar_form_new.html", {
      'form': form
    })

  return render(request, "surat/surat_keluar_form_new.html", {
    'form': form
  })

@login_required
def surat_keluar_list(request):
  return render(request, "surat/surat_keluar_list.html", {
    'data': SuratKeluar.objects.all().order_by('-id')
  })

@login_required
def surat_keluar_delete(request, id):
  surat_keluar = get_object_or_404(SuraKeluar, pk=id)
  surat_keluar.delete()
  return redirect('surat:surat_keluar_list')

@login_required
def surat_keluar_edit(r, id):
  if r.POST:
    form = FormSuratKeluar(r.POST or None)
    id = r.POST['id']
    surat_keluar = get_object_or_404(SuratKeluar, pk=id)
    if form.is_valid():
      surat_keluar.nomor = form.cleaned_data['nomor']
      surat_keluar.tgl_surat = form.cleaned_data['tgl_surat']
      surat_keluar.perihal = form.cleaned_data['perihal']
      surat_keluar.pengirim = form.cleaned_data['pengirim']
      surat_keluar.deskripsi = form.cleaned_data['deskripsi']
      surat_keluar.asal_instansi = form.cleaned_data['asal_instansi']
      surat_keluar.tgl_masuk = form.cleaned_data['tgl_masuk']

      surat_keluar.save(force_update=True)
      return redirect('surat:surat_keluar_list')
    return render(r, 'surat/surat_keluar_form_edit.html', {'form':form, 'id':id})

  surat_keluar = get_object_or_404(SuratKeluar, pk=id)
  form = FormSuratMasuk(initial={
          'nomor':surat_keluar.nomor,
          'tgl_surat':surat_keluar.tgl_surat,
          'perihal':surat_keluar.perihal,
          'pengirim':surat_keluar.pengirim,
          'deskripsi':surat_keluar.deskripsi,
          'tujuan_instansi':surat_keluar.tujuan_instansi,
          'tgl_keluar':surat_keluar.tgl_keluar,
        })
  return render(r, 'surat/surat_keluar_form_edit.html', {'form':form, 'id':surat_keluar.id})

@login_required
def instansi_list(request):
  return render(request, "instansi/list.html", {
    'data': Instansi.objects.all().order_by('-id')
  })

@login_required
def instansi_delete(request, id):
  instansi = get_object_or_404(Instansi, pk=id)
  instansi.delete()
  return redirect('surat:instansi_list')

@login_required
def instansi_edit(r, id):
  if r.POST:
    form = FormInstansi(r.POST or None)
    id = r.POST['id']
    instansi = get_object_or_404(Instansi, pk=id)
    if form.is_valid():
      instansi.nama_instansi = form.cleaned_data['nama_instansi']
      instansi.kategori = form.cleaned_data['kategori']
      instansi.telepon = form.cleaned_data['telepon']
      instansi.kode_pos = form.cleaned_data['kode_pos']
      instansi.alamat = form.cleaned_data['alamat']

      instansi.save(force_update=True)
      return redirect('surat:instansi_list')
  
  instansi = get_object_or_404(Instansi, pk=id)
  form = FormInstansi(initial={
          'nama_instansi':instansi.nama_instansi,
          'kategori':instansi.kategori,
          'telepon':instansi.telepon,
          'kode_pos':instansi.kode_pos,
          'alamat':instansi.alamat,
        })
  return render(r, 'instansi/form_edit.html', {'form':form, 'id':instansi.id})

@login_required
def instansi_new(r):
  form = FormInstansi(r.POST or None)

  if r.POST:
    if form.is_valid():
      form.save(commit=True)
      return redirect('surat:instansi_list')
    
  return render(r, 'instansi/form_new.html', {'form':form})