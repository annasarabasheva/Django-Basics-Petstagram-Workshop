from django.urls import path, include

from petstagram.pets import views

urlpatterns = [
    path('add/', views.PetAddPage.as_view(), name='add-pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.PetDetailsPage.as_view(), name='pet-details'),
        path('edit/', views.pet_edit_page, name='edit-pet'),
        path('delete/', views.pet_delete_page, name='delete-pet'),
    ]))
]