from django.urls import path
from django.conf.urls.static import static
from . import views
from upSkillWithUs.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('course/<str:slug>', views.coursepage, name="coursepage"),
    path('confirm-enrollment/<str:slug>', views.confirm_enrollment, name='confirm_enrollment'),
    path('enroll/<str:slug>', views.enroll, name="enroll"),
]+static(MEDIA_URL, document_root=MEDIA_ROOT)

