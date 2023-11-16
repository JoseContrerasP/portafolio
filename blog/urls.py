from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
	path('', views.render_post, name='posts'),
	path('<int:post_id>', views.get_post, name='post')
]