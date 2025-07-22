from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from .models import Post, Comment 
from django.db.models import Q

def index(request):
    posts = Post.objects.all().order_by('-created_at')


    context = {
        'posts': posts,
    }
    return render(request, 'pirosta/index.html', context)

def post_create(request):
    if request.method == 'POST':
        author_username = request.POST.get('author_username')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        if author_username and content and image:
            Post.objects.create(
                author_username=author_username,
                content=content,
                image=image,
                likes_count=0
            )
            return redirect('pirosta:index')
        else:
            return render(request, 'pirosta/post_create.html', {'error_message': '빈칸을 채워주세요.'})
    return render(request, 'pirosta/post_create.html')


@require_POST
def like_toggle(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    post.likes_count += 1
    post.save()

    liked = True 
    message = "좋아요 수 증가"

    return JsonResponse({
        'liked': liked, 
        'likes_count': post.total_likes,
        'message': message
    })


@require_POST
def comment_create(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    author_username = "piro_man"
    comment_text = request.POST.get('comment_text')

    if comment_text:
        comment = Comment.objects.create(
            post=post,
            author_username=author_username,
            text=comment_text
        )
        return JsonResponse({
            'success': True,
            'comment_id': comment.id,
            'author_username': comment.author_username,
            'text': comment.text,
            'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M'),
            'comments_count': post.total_comments
        })
    return JsonResponse({'success': False, 'message': '댓글 내용을 입력해주세요.'})

@require_POST
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post = comment.post
    comment.delete()

    return JsonResponse({
        'success': True,
        'comment_id': comment_id,
        'comments_count': post.total_comments
    })

@require_GET
def search_posts(request):
    query = request.GET.get('q', '')
    if query:
        posts = Post.objects.filter(
            Q(author_username__icontains=query) | Q(content__icontains=query)
        ).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')

    results = []
    for post in posts:
        results.append({
            'id': post.id,
            'author_username': post.author_username,
            'content': post.content,
            'image_url': post.image.url,
            'likes_count': post.total_likes,
            'comments_count': post.total_comments
        })
    return JsonResponse({'posts': results})