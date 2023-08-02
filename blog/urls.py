from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard/', views.dash, name='blog-home'),
    path('dashboard/POST',views.alerts, name="alerts"),

    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/new/POST', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('media/Files/<int:pk>',PostDeleteView.as_view(),name='post-delete' ),
    path('search/',views.search,name='search' ),
    path('about/', views.about, name='blog-about'),

    path('post/confirm',views.postConfirm,name='post_confirm'),
    path('timetable/',views.timetable, name='timetable'),
    path('timetable/POST',views.timetable_download, name='timetable_download'),

    path('today/',views.today, name='today'),
 
    path('contact/',views.contact, name='contact'),
    path('contact/POST',views.message, name='mail'),
    
    path('report/',views.report, name='report'),
    path('report/POST',views.send_report, name='send_report'),
 
    path('extra/',views.extra, name='extra'),
 
    path('test/',views.test, name='test'),
    path('test/POST',views.test_case, name='test_case'),
 
    path('diet/',views.diet, name='diet'),
    path('diet/POST',views.diet_download, name='diet_download'),
 
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="blog/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="blog/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="blog/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="blog/password_reset_done.html"), 
        name="password_reset_complete"),
]
