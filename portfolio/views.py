from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Portfolio
from .forms import PortfolioForm


# Create your views here.

def home(request):
    portfolio = Portfolio.objects
    return render (request, 'portfolio/home.html', {'portfolios':portfolios})

def detail(request, portfolio_id):
    portfolio_detail = get_object_or_404(Portfolio, pk = portfolio_id)
    return render(request, 'portfolio/detail.html', {'portfolio': portfolio_detail})

def portfolio_new(request):
    if request.method== "POST":
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.published_date = timezone.datetime.now()
            portfolio.save()
            return redirect('detail', portfolio_id=portfolio.pk)
    else:
        form = PortfolioForm()
        return render(request, 'portfolio/new.html', {'form':form})

def post_edit(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    if request.method=="POST":
        form=PortfolioForm(request.POST, isinstance=portfolio)
        if form.is_valid():
            portfolio=form.save(commit=False)
            portfolio.published_date=timezone.datetime.now()
            portfolio.save()
            return redirect('detail', portfolio_id=portfolio.pk)
    else:
        form=PortfolioForm(isinstance=portfolio)
        return render(request, 'portfolio/edit.html', {'form':form})

def post_delete(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    portfolio.delete()
    return redirect('home')