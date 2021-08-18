from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PostIt
from .forms import PostItForm
from users.forms import UserUpdateInfoForm, UserImageExtensionForm
from django.contrib import messages
from django.core.paginator import Paginator


@login_required()
def home_page(request):
    if request.method == 'POST':
        form = PostItForm(request.POST)
        form.instance.posted_by = request.user

        if form.is_valid():
            form.save()
            return redirect('post-home')
    else:
        form = PostItForm()

    number_of_posts = PostIt.objects.filter(posted_by=request.user.id)

    post_it_list = PostIt.objects.order_by('-posted_date')
    paginator = Paginator(post_it_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'post_its': page_obj,
        'number_of_personal_posts': len(number_of_posts),
        'form': form
    }

    return render(request, 'post/home.html', context)


@login_required()
def single_post_it(request, post_it_id, update=None):
    data = PostIt.objects.get(id=post_it_id)

    update_screen = True if update == 'update' else False

    if request.method == 'POST':
        form = PostItForm(request.POST)
        if form.is_valid():
            data.post_title = form.instance.post_title
            data.post_body = form.instance.post_body
            data.save()
            return redirect('post-home')
    else:
        form_data = {'post_title': data.post_title, 'post_body': data.post_body}
        form = PostItForm(initial=form_data)

    context = {
        'post_it': PostIt.objects.get(id=post_it_id),
        'update': update_screen,
        'form': form
    }

    return render(request, 'post/single-postit.html', context)


@login_required()
def delete_post_it(request, post_it_id):
    PostIt.objects.filter(id=post_it_id).delete()
    return redirect('post-home')


@login_required()
def account_page(request):
    if request.method == 'POST':
        user_update_info_form = UserUpdateInfoForm(request.POST, instance=request.user)

        if hasattr(request.user, 'userimageextension'):
            user_image_extension_form = UserImageExtensionForm(request.POST, request.FILES,
                                                               instance=request.user.userimageextension)
        else:
            user_image_extension_form = UserImageExtensionForm(request.POST, request.FILES)

            user_image_extension_form.instance.user = request.user

        if user_update_info_form.is_valid() and user_image_extension_form.is_valid():
            user_update_info_form.save()
            user_image_extension_form.save()
            messages.success(request, 'Account Updated')
            return redirect('post-account')
    else:
        user_update_info_form = UserUpdateInfoForm(instance=request.user)
        if hasattr(request.user, 'userimageextension'):
            user_image_extension_form = UserImageExtensionForm(instance=request.user.userimageextension)
        else:
            user_image_extension_form = UserImageExtensionForm()

    context = {
        'user_update_info_form': user_update_info_form,
        'user_image_extension_form': user_image_extension_form
    }

    return render(request, 'post/account.html', context)


def about_page(request):
    return render(request, 'post/about.html')
