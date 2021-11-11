from django.contrib import admin
from django.urls import path, include
from pages.views import (about_view,
                         contact_view,
                         home_view,
                         )



urlpatterns = [
    path('', home_view, name='home'),
    path('courses/', include("courses.urls")),
    path('products/', include("products.urls")),
    path('blog/', include("Blog.urls")),
    path('about/<int:id>/', about_view),
    path('contact/', contact_view),
    path('admin/', admin.site.urls),
]
