from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import News,Category
from django.views.generic import TemplateView,View,ListView

from .forms import ContactForm



# Create your views here.

def page404View(request):
    context={}
    return render(request,'news/404.html',context)


def news_list(request):
    # news=News.objects.filter(status=News.Status.Published)
    news=News.published.all()
    context={
        'news':news
    }
    return render(request,'news/news_list.html',context)

# def news_detail(request,id):
    # news=get_object_or_404(News,id=id,status=News.Status.Published)
def news_detail(request,news):
    news=get_object_or_404(News,slug=news,status=News.Status.Published)
    context={
        'news':news
    }
    return render(request,'news/news_detail.html',context)

# def homepageView(request):
#     categories=Category.objects.all()
#     news_list=News.published.all().order_by('-publish_time')[:10]
#     local_one=News.published.all().filter(category__title="Mahalliy").order_by('-publish_time')[:1]
#     local_news=News.published.all().filter(category__title="Mahalliy").order_by('-publish_time')[1:5]
#     context={
#         'news_list':news_list,
#         'categories':categories,
#         'local_news':local_news,
#         'local_one':local_one,
#     }
#     return render(request,'news/index.html',context)



class HomePageView(ListView):
    model = News
    context_object_name = 'news'
    template_name='news/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] =Category.objects.all()
        context["news_list"]=News.published.all().order_by('-publish_time')[:10]
        context['mahalliy_news']=News.published.all().filter(category__title="Mahalliy").order_by('-publish_time')[:5]
        context['xorij_news']=News.published.all().filter(category__title="Xorij").order_by('-publish_time')[:5]
        context['texnologiya_news']=News.published.all().filter(category__title="Texnologiya").order_by('-publish_time')[:5]
        context['sport_news']=News.published.all().filter(category__title="Sport").order_by('-publish_time')[:5]
        return context
    


def contactpageView(request):
    print(request.POST)
    form = ContactForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save()
        return HttpResponse("Biz bilan bog'langaniz uchun tashakkur!")
    context={
        "form":form
    }
    return render(request,'news/contact.html',context)


class ContactPageView(View):
    template_name='news/contact.html'

    def get(self,request,*args, **kwargs):
        form=ContactForm()
        context={
            "form":form
        }
        return render(request,"news/contact.html",context)
    
    def post(self,request,*args, **kwargs):
        form=ContactForm(request.POST)
        if request.method=="POST" and form.is_valid():
            form.save()

        context={
            'form':form
        }
        return render(request,"news/contact.html",context)
    

class LocalNewsView(ListView):
    model=News
    template_name='news/mahalliy.html'
    context_object_name='mahalliy_yangiliklar'

    def get_queryset(self):
        news=self.model.published.all().filter(category__title="Mahalliy").order_by('-publish_time')
        return news

class ForeignNewsView(ListView):
    model=News
    template_name='news/xorij.html'
    context_object_name='xorij_yangiliklar'

    def get_queryset(self):
        news=self.model.published.all().filter(category__title="Xorij").order_by('-publish_time')
        return news

class TechnologyNewsView(ListView):
    model=News
    template_name='news/texnologiya.html'
    context_object_name='texnologiya_yangiliklar'

    def get_queryset(self):
        news=self.model.published.all().filter(category__title="Texnologiya").order_by('-publish_time')
        return news

class SportNewsView(ListView):
    model=News
    template_name='news/sport.html'
    context_object_name='sport_yangiliklar'

    def get_queryset(self):
        news=self.model.published.all().filter(category__title="Sport").order_by('-publish_time')
        return news