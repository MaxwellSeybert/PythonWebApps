from django.urls import path
from hero.views import HulkView, IronManView, BlackWidowView, SpiderManView, IndexView

urlpatterns = [
    path('hulk',        HulkView.as_view()),
    path('ironman',        IronManView.as_view()),
    path('blackwidow',        BlackWidowView.as_view()),
    path('spiderman',    SpiderManView.as_view()),
    path('',            IndexView.as_view()),
    
]