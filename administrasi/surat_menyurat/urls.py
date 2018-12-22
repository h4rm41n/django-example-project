from django.urls import path, include
from . import views

app_name ='surat_menyurat'

urlpatterns = [
  path('instansi-list/', views.InstansiListView.as_view(), name='instansi_list'),
  path('instansi-form/', views.InstansiCreateView.as_view(), name='instansi_form'),
  path('instansi-delete/<int:id>', views.InstansiDeleteView.as_view(), name='instansi_delete'),
  path('instansi-edit/<int:pk>', views.InstansiUpdateView.as_view(), name='instansi_edit'),

  path('suratmasuk-list/', views.SMListView.as_view(), name='sm_list'),
  path('suratmasuk-form/', views.SMCreateView.as_view(), name='sm_form'),
  path('suratmasuk-delete/<int:id>', views.SMDeleteView.as_view(), name='sm_delete'),
  path('suratmasuk-edit/<int:id>', views.SMUpdateView.as_view(), name='sm_edit'),

  path('suratkeluar-list/', views.SKListView.as_view(), name='sk_list'),
  path('suratkeluar-form/', views.SKCreateView.as_view(), name='sk_form'),
  path('suratkeluar-delete/<int:id>', views.SKDeleteView.as_view(), name='sk_delete'),
  path('suratkeluaredit/<int:id>', views.SKUpdateView.as_view(), name='sk_edit'),
]
