from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import UserRegisterForm
from .models import VideoThread


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')

            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})

@login_required
def video_chat(request):
    current_user = request.user
    call_logs = VideoThread.objects.filter(Q(caller_id=current_user.id) | Q(callee_id=current_user.id)).order_by('date_created')[:5]
    return render(request, 'videos/video_chat.html', {'call_logs': call_logs})