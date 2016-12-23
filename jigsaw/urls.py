from django.conf.urls import url

from . import views

urlpatterns = [
    # url('^$', views.index, name='index')
    url('^api/test$', views.api_test)
    url('^api/image/callback$', views.image_callback)
    url('^api/image/query', view.image_query)
]

