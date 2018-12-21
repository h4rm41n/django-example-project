from django.urls import path, include
from . import views

app_name ='surat_menyurat'

urlpatterns = [
  path('instansi/', views.instansi_list, name='instansi_list'),
  path('instansiform/', views.instansi_new, name='instansi_form'),
  path('instansidelete/<int:id>', views.instansi_delete, name='instansi_delete'),
  path('instansiedit/<int:id>', views.instansi_edit, name='instansi_edit'),
  
  path('suratmasuk/', views.surat_masuk_list, name='surat_masuk_list'),
  path('suratmasukform/', views.surat_masuk_form, name='surat_masuk_form'),
  path('suratmasukdelete/<int:id>', views.surat_masuk_delete, name='surat_masuk_delete'),
  path('suratmasukedit/<int:id>', views.surat_masuk_edit, name='surat_masuk_edit'),

  path('suratkeluar/', views.surat_keluar_list, name='surat_keluar_list'),
  path('suratkeluarform/', views.surat_keluar_form, name='surat_keluar_form'),
  path('suratkeluardelete/<int:id>', views.surat_keluar_delete, name='surat_keluar_delete'),
  path('suratkeluaredit/<int:id>', views.surat_keluar_edit, name='surat_keluar_edit'),
]
