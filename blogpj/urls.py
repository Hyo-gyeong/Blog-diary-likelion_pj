from django.contrib import admin
from django.urls import path
import blog.views
import account.views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('list/', blog.views.list, name="list"),
    path('new/', blog.views.new, name="new"),
    path('blog/<int:blog_id>', blog.views.detail, name="detail"),
    path('blog/delete/<int:blog_id>', blog.views.delete, name="delete"),
    path('blog/edit/<int:blog_id>', blog.views.edit, name="edit"),

    #계정관련 url
    path('account/signin', account.views.signin, name = "signin"),
    path('account/signup', account.views.signup, name = 'signup'),
    path('account/logout', account.views.logout, name= "logout"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
