from django.urls import path


from products.views import dynamic_lookup_view, product_list_view, product_create_view, product_delete_view


app_name = "products"
urlpatterns = [

    path('<int:my_id>/', dynamic_lookup_view, name='product-detail'),
    path('list/', product_list_view, name="product-list"),
    path('create/', product_create_view, name='product-list'),
    path('<int:my_id>/delete/', product_delete_view, 'product-delete'),

]
