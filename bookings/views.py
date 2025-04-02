from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, BookingForm
from .models import ClassSchedule, Booking, UserProfile
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q

def home(request):
    query = request.GET.get('q')
    if query:
        classes = ClassSchedule.objects.filter(
            Q(title__icontains=query) | Q(trainer__icontains=query)
        )
    else:
        classes = ClassSchedule.objects.all()
    return render(request, 'bookings/home.html', {'classes': classes, 'query': query})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create profile
            UserProfile.objects.create(
                user=user,
                phone=form.cleaned_data.get('phone'),
                bio=form.cleaned_data.get('bio')
            )

             # Send welcome email
            send_mail(
                '🎉 Welcome to Fitness Class Booking!',
                f"Hi {user.username},\n\n"
                f"Thank you for signing up for our fitness class booking platform.\n"
                f"You can now log in, view available classes, and book your favorite sessions.\n\n"
                f"Let's get fit together! 💪",
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False
            )
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'home'

@login_required
def book_class(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            selected_class = form.cleaned_data['class_schedule']
            existing_bookings = Booking.objects.filter(class_schedule=selected_class).count()

            if existing_bookings >= selected_class.capacity:
                form.add_error(None, 'This class is already fully booked.')
            else:
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()

                # Send confirmation email
                send_mail(
                    '🎟️ Fitness Class Booking Confirmation',
                    f"Hi {request.user.username},\n\n"
                    f"You have successfully booked the class '{selected_class.title}'.\n",
                    settings.DEFAULT_FROM_EMAIL,
                    [request.user.email],
                    fail_silently=False
                )

                return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'bookings/book_class.html', {'form': form})

@login_required
def booking_success(request):
    return render(request, 'bookings/booking_success.html')
