from django.shortcuts import HttpResponse,  render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views import View
from .models import Course, Video, Enrollment
from .forms import RegistrationForm, LoginForm

def home(request):
    courses = Course.objects.all()
    enrolled_courses = []
    if request.user.is_authenticated:
        enrolled_courses = Enrollment.objects.filter(user=request.user).values_list('course_id', flat=True)
    return render(request, 'courses/homepage.html', context={"courses": courses, "enrolled_courses": enrolled_courses})


def coursepage(request, slug):
    course = Course.objects.get(slug=slug)
    serial_number = request.GET.get('lecture')
    if serial_number is None:
        serial_number = 1
    video = Video.objects.get(serial_number=serial_number, course=course)
    if((request.user.is_authenticated is False) and (video.is_preview is False)):
        return redirect('login')
    return render(request, 'courses/coursepage.html', context={'course': course, 'video': video})


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'courses/signuppage.html', {'form': form})


class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request, 'courses/loginpage.html', context={'form': form})

    def post(self, request):
        form = LoginForm(request=request, data=request.POST)
        if(form.is_valid()):
            return redirect('home')
        return render(request, 'courses/loginpage.html', context={'form': form})

def signout(request):
    logout(request)
    return redirect('home')


@login_required
def confirm_enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'courses/confirm_enrollment.html', context={'course': course})

@login_required
def enroll(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)
    if created:
        message = "You have successfully enrolled in the course."
    else:
        message = "You are already enrolled in this course."
    return render(request, 'courses/enrollment_confirmation.html', context={'message': message, 'course': course})

