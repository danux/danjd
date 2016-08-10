from django.conf.urls import url

from cv.views import CvTemplateView


urlpatterns = [
    url(r'^$', CvTemplateView.as_view(), name='cv'),
]
