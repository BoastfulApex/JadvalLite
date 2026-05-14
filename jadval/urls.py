from django.urls import path
from . import views

urlpatterns = [
    # Mobile (asosiy sahifa)
    path('', views.mobile_home, name='mobile_home'),

    # Kiosk (katta ekran)
    path('kiosk/', views.kiosk_home, name='kiosk_home'),

    # Display (dark theme, landscape)
    path('display/', views.display, name='display'),

    # Admin panel
    path('admin-panel/login/', views.admin_login, name='admin_login'),
    path('admin-panel/logout/', views.admin_logout, name='admin_logout'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-panel/guruh/yangi/', views.guruh_create, name='guruh_create'),
    path('admin-panel/guruh/<int:pk>/tahrir/', views.guruh_edit, name='guruh_edit'),
    path('admin-panel/guruh/<int:pk>/ochir/', views.guruh_delete, name='guruh_delete'),
    path('admin-panel/guruh/<int:pk>/excel/', views.guruh_excel_upload, name='guruh_excel_upload'),
    path('admin-panel/bulk-upload/', views.bulk_upload, name='bulk_upload'),
    path('admin-panel/clear-all/', views.clear_all, name='clear_all'),
]
