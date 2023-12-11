import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_http_methods
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from api.models import Category, NewsArticle, Comment
from api.forms import CustomUserCreationForm

def main_spa(request):
    categories = Category.objects.all()
    articles = NewsArticle.objects.all()
    return render(request, 'api/spa/index.html', {'categories': categories, 'articles': articles})

def SignUpView(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful")
            return redirect('login')
    return render(request, 'api/spa/signup.html', {'form': form})

def LogInView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Email or Password is incorrect')
            return redirect('login')
    return render(request, 'api/spa/login.html', {})

def LogoutView(request):
    logout(request)
    messages.success(request, "You were logged out.")
    return redirect('login')

@require_http_methods(["GET"])
def get_articles(request):
    data = NewsArticle.objects.all()
    article_list = [{'id': d.pk, 'title': d.title, 'content': d.content, 'category': d.category.name, 'created_at': d.created_at} for d in data]
    return JsonResponse({'articles': article_list})

@require_http_methods(["POST"])
@csrf_exempt
def post_article(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if not data:
            return JsonResponse({'error': 'Empty request body'}, status=400)

        category_name = data.get('category')
        category, created = Category.objects.get_or_create(name=category_name)
        article = NewsArticle(title=data.get('title'), content=data.get('content'), category=category)
        article.save()
        return JsonResponse({'message': 'Article created successfully'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@require_http_methods(["DELETE"])
@csrf_exempt
def delete_article(request, article_id):
    if request.method == 'DELETE':
        article = get_object_or_404(NewsArticle, pk=article_id)
        article.delete()
        return JsonResponse({'message': 'Article deleted successfully'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@require_http_methods(["PUT"])
@csrf_exempt
def update_article(request, article_id):
    try:
        article = get_object_or_404(NewsArticle, pk=article_id)
        data = json.loads(request.body)
        if not data:
            return JsonResponse({'error': 'Empty request body'}, status=400)

        category_name = data.get('category')
        category, created = Category.objects.get_or_create(name=category_name)
        article.title = data.get('title', article.title)
        article.content = data.get('content', article.content)
        article.category = category
        article.save()
        return JsonResponse({'message': 'Article updated successfully'})
    except NewsArticle.DoesNotExist:
        return JsonResponse({'error': 'Article not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Error updating article: {str(e)}'}, status=500)

@require_http_methods(["GET"])
def get_comments(request, article_id):
    if request.method == 'GET':
        article = get_object_or_404(NewsArticle, pk=article_id)
        comments = article.comments.all()
        comment_list = [{'id': c.pk, 'user': c.user.email, 'content': c.content, 'parent_comment': c.parent_comment_id, 'created_at': c.created_at} for c in comments]
        return JsonResponse({'comments': comment_list})

@require_http_methods(["POST"])
@csrf_exempt
def post_comment(request, article_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        if not data:
            return JsonResponse({'error': 'Empty request body'}, status=400)

        article = get_object_or_404(NewsArticle, pk=article_id)
        user = request.user  # Assuming the user is authenticated
        content = data.get('content')
        parent_comment_id = data.get('parent_comment_id')
        parent_comment = None
        if parent_comment_id:
            parent_comment = get_object_or_404(Comment, pk=parent_comment_id)
        comment = Comment(user=user, article=article, content=content, parent_comment=parent_comment)
        comment.save()
        return JsonResponse({'message': 'Comment created successfully'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@require_http_methods(["PUT"])
@csrf_exempt
def update_comment(request, comment_id):
    try:
        comment = get_object_or_404(Comment, pk=comment_id)
        data = json.loads(request.body)
        if not data:
            return JsonResponse({'error': 'Empty request body'}, status=400)

        comment.content = data.get('content', comment.content)
        comment.save()
        return JsonResponse({'message': 'Comment updated successfully'})
    except Comment.DoesNotExist:
        return JsonResponse({'error': 'Comment not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Error updating comment: {str(e)}'}, status=500)

@require_http_methods(["DELETE"])
@csrf_exempt
def delete_comment(request, comment_id):
    if request.method == 'DELETE':
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.delete()
        return JsonResponse({'message': 'Comment deleted successfully'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)
