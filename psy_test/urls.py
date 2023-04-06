"""psy_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testing import views
from django.conf import settings
from django.conf.urls.static import static
from testing.views import EditResult, EditTest, DeleteTest, DeleteQuestion
from numerology.views import destiny_number, soul_number, pithagor_matrix

urlpatterns = [
    # general URLs

    path("admin/", admin.site.urls),
    path("register/", views.register, name='register'),
    path("login/", views.auth, name='login'),
    path("home/", views.index, name='home'),
    path("logout/", views.log_out, name='log_out'),

    # testing_app urls

    path("tests_list/", views.tests_list, name='tests-list'),
    path("<int:test_id>/test_info/", views.test_info, name='test_info'),
    path("edit_question/<int:test_id>/<int:question_id>/", views.edit_question, name='edit_question'),
    path('create_test/', views.create_test, name='create_psytest'),
    path('create_questions/<int:test_id>/', views.create_questions, name='create_questions'),
    path('create_results/<int:test_id>/', views.create_test_results, name='create_results'),
    path('edit_test/<pk>/', EditTest.as_view(), name='edit_test'),
    path('edit_result/<pk>/', EditResult.as_view(), name='edit_result'),
    path('delete_test/<pk>/', DeleteTest.as_view(), name='delete_test'),
    path('delete_question/<pk>', DeleteQuestion.as_view(), name='delete_question'),
    path('take_test/<int:test_id>/', views.take_test, name='take_test'),
    path('tests/results/<int:result_id>/', views.get_results, name='get_results'),
    path('home/your_results', views.your_results, name='your_results'),
    path('home/your_results_details/<int:result_id>', views.your_results_details, name='your_results_details'),

    # numerology_app urls
    path('numerology/destiny_number', destiny_number, name='destiny_number'),
    path('numerology/soul_number', soul_number, name='soul_number'),
    path('numerology/pithagor_matrix', pithagor_matrix, name='pithagor_matrix'),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
