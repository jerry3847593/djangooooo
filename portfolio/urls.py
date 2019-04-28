from django.contrib import admin
from django.urls import path, include
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('home/', portfolio.views.home, name='home'),
    path('post/<int:portfolio_id>', portfolio.views.detail, name="detail"),
    path('post/new', portfolio.views.portfolio_new, name="new"),
    path('post/<int:portfolio_id>/edit', portfolio.views.post_edit, name="edit"),
    path('post/<int:portfolio_id>/delete', portfolio.views.post_delete, name="delete"),
]
