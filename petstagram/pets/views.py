from django.shortcuts import render, redirect


from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from petstagram.common.forms import CommentForm
from petstagram.pets.models import Pet
from petstagram.pets.forms import PetAddForm, PetEditForm, PetDeleteForm

""" FBV:

def pet_add_page(request):
    form = PetAddForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('profile-details', pk=1)

    context = {
        "form": form,
    }

    return render(request, 'pets/pet-add-page.html', context)
"""


class PetAddPage(CreateView): # CBV version of pet_add_page view
    model = Pet
    form_class = PetAddForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})


def pet_edit_page(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)
    form = PetEditForm(request.POST or None, instance=pet)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_slug)

    context = {
        "form": form,
        "pet": pet,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def pet_delete_page(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)
    form = PetDeleteForm(instance=pet)

    if request.method == "POST":
        pet.delete()
        return redirect('profile-details', pk=1)

    context = {
        "form": form,
        "pet": pet,
    }

    return render(request, 'pets/pet-delete-page.html', context)


def pet_details_page(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()

    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form

    }

    return render(request, 'pets/pet-details-page.html', context)