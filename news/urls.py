from django.urls import path
from .views import (news_list,news_detail,
                    # homepageView,
                    ContactPageView,page404View,HomePageView,
                    LocalNewsView,ForeignNewsView,
                    TechnologyNewsView,SportNewsView)


urlpatterns = [
    path('',HomePageView.as_view(),name='home-page'),
    path('news/',news_list,name='news-list'),
    # path('news/<int:id>/',news_detail,name='news-detail'),
    path('news/<slug:news>/',news_detail,name='news-detail'),
    path('contact/',ContactPageView.as_view(),name='contact-page'),
    path('page404/',page404View,name='page404'),
    path('mahalliy/',LocalNewsView.as_view(),name='mahalliy-page'),
    path('xorij/',ForeignNewsView.as_view(),name='xorij-page'),
    path('texnologiya/',TechnologyNewsView.as_view(),name='texnologiya-page'),
    path('sport/',SportNewsView.as_view(),name='sport-page'),
]
