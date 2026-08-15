from django.utils import timezone
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def login_view(request):

    if request.user.is_authenticated:
        return redirect('/home/')

    error_type = None

    if request.method == 'POST':

        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        when_we_met = request.POST.get('when_we_met', '').strip()

        # Temporary dummy details
        correct_username = 'Thakur_sahab'
        correct_password = 'Gjb_yarr_dadaji'
        correct_date = '11/05/2025'

        if username != correct_username:

            error_type = 'username'

        elif password != correct_password:

            error_type = 'password'

        elif when_we_met != correct_date:

            error_type = 'date'

        else:

            # Create dummy Django user automatically if it doesn't exist
            user, created = User.objects.get_or_create(
                username=correct_username
            )

            # Set password
            user.set_password(correct_password)
            user.save()

            # Login the user
            login(request, user)

            return redirect('/home/')

    return render(
        request,
        'registration/login.html',
        {
            'error_type': error_type
        }
    )


# Countdown unlock date/time
COUNTDOWN_END = datetime(2026, 8, 15, 15, 0, 0, tzinfo=timezone.get_current_timezone())
@login_required
def home(request):
    return render(
        request,
        'surprise/home.html',
        {
            'countdown_end': COUNTDOWN_END.isoformat()
        }
    )


@login_required
def beginning(request):

    # Don't allow access before countdown finishes
    if timezone.now() < COUNTDOWN_END:
        return redirect('/home/')

    return render(request, 'surprise/beginning.html')


@login_required
def memories(request):
    return render(request, 'surprise/memories.html')


@login_required
def letter(request):
    return render(request, 'surprise/letter.html')


@login_required
def cake(request):
    return render(request, 'surprise/cake.html')


@login_required
def final(request):
    return render(request, 'surprise/final.html')


def logout_view(request):
    logout(request)
    return redirect('/')