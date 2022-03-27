from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.views.generic import ListView

from Posts.models import PostModel


class home(ListView):
    model = PostModel
    template_name = 'home_page.html'
    context_object_name = 'posts'
    paginate_by = 20


@login_required
def profile(request):
    return render(request, 'NewsApp1/uprof.html')


def about_us(request):
    return render(request, 'NewsApp1/about_us.html')
