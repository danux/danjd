from django.conf.urls import url
from django.views.decorators.cache import cache_page

from cv.views import CvTemplateView


urlpatterns = [
    url(r'^$', cache_page(60 * 15)(CvTemplateView.as_view()), name='cv'),
]
