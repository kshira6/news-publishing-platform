from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from .models import Article
from .forms import ArticleForm

def published_articles(request):
    articles = Article.objects.filter(publish_date__isnull=False).order_by('-publish_date')
    return render(request, 'newsapp/published_articles.html', {'articles': articles})

def is_admin(user):
    return user.is_staff  # or customize

@login_required
@user_passes_test(is_admin)
def admin_article_list(request):
    articles = Article.objects.all().order_by('-publish_date')
    return render(request, 'newsapp/admin_article_list.html', {'articles': articles})

@login_required
@user_passes_test(is_admin)
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_article_list')
    else:
        form = ArticleForm()
    return render(request, 'newsapp/article_form.html', {'form': form, 'create': True})

@login_required
@user_passes_test(is_admin)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('admin_article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'newsapp/article_form.html', {'form': form, 'create': False})

@login_required
@user_passes_test(is_admin)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('admin_article_list')
    return render(request, 'newsapp/article_confirm_delete.html', {'article': article})