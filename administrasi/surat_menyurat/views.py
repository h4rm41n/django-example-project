from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, View, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from surat_menyurat.models import SuratMasuk, SuratKeluar, Instansi
from surat_menyurat.forms import FormSuratMasuk, FormInstansi, FormSuratKeluar

@login_required
def home(request):
  return render(request, 'home.html')

def login_redirect(request):
  return redirect('login')

class InstansiUpdateView(LoginRequiredMixin, UpdateView):
  model = Instansi
  form_class = FormInstansi
  template_name = 'instansi/form_edit.html'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return redirect("surat:instansi_list")

  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super(InstansiUpdateView, self).dispatch(request, *args, **kwargs)

class InstansiListView(LoginRequiredMixin, ListView):
  queryset = Instansi.objects.all()
  template_name='instansi/instansi_list.html'

class InstansiCreateView(LoginRequiredMixin, CreateView):
  form_class = FormInstansi
  template_name = 'instansi/form_new.html'
  success_url = reverse_lazy('surat:instansi_list')

class InstansiDeleteView(LoginRequiredMixin, View):
  def get(self, r, id):
    instansi = get_object_or_404(Instansi, id=id)
    instansi.delete()
    return redirect('surat:instansi_list')

class SMUpdateView(LoginRequiredMixin, UpdateView):
  form_class = FormSuratMasuk
  template_name = 'surat/sm_edit.html'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return redirect("surat:sm_list")

  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super(SMUpdateView, self).dispatch(request, *args, **kwargs)

class SMListView(LoginRequiredMixin, ListView):
  queryset = SuratMasuk.objects.all()
  template_name='surat/sm_list.html'

class SMCreateView(LoginRequiredMixin, CreateView):
  form_class = FormSuratMasuk
  template_name = 'surat/sm_new.html'
  success_url = reverse_lazy('surat:sm_list')

class SMDeleteView(LoginRequiredMixin, View):
  def get(self, r, id):
    sm = get_object_or_404(SuratMasuk, id=id)
    sm.delete()
    return redirect('surat:sm_list')

class SKUpdateView(LoginRequiredMixin, UpdateView):
  form_class = FormSuratKeluar
  template_name = 'surat/sk_edit.html'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return redirect("surat:sk_list")

  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super(SKUpdateView, self).dispatch(request, *args, **kwargs)

class SKListView(LoginRequiredMixin, ListView):
  queryset = SuratKeluar.objects.all()
  template_name='surat/sk_list.html'

class SKCreateView(LoginRequiredMixin, CreateView):
  form_class = FormSuratKeluar
  template_name = 'surat/sk_new.html'
  success_url = reverse_lazy('surat:sk_list')

class SKDeleteView(LoginRequiredMixin, View):
  def get(self, r, id):
    sk = get_object_or_404(SuratKeluar, id=id)
    sk.delete()
    return redirect('surat:sk_list')