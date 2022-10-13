from django.urls import path
from django.views.generic import RedirectView


from hero.views import HulkView, IronManView, BlackWidowView, SpiderManView, IndexView, PhotoListView, PhotoDetailView

urlpatterns = [
    path('', RedirectView.as_view(url='photo/')),
    path('photo/', PhotoListView.as_view()),
    path('photo/<str:name>', PhotoDetailView.as_view()),
    
]