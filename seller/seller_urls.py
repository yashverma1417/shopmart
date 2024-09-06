from django.urls import path
from seller import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.dashboard),
    path('categories/', views.add_category),
    path('categories/delete/<category_id>', views.delete_category),  
    path('categories/add-product/<category_id>', views.add_product),
    
    path('products/', views.view_products),
    path('products/delete/<product_id>', views.delete_product),
    path('products/update/<product_id>', views.update_product),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
