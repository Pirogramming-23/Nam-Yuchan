from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse 
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Idea, IdeaStar
from .forms import IdeaForm


def idea_list(request):
    sort_by = request.GET.get('sort', 'created_date')
    
    if sort_by == 'starred':
        ideas = Idea.objects.annotate(star_count=Count('ideastar')).order_by('-star_count')
    elif sort_by == 'title':
        ideas = Idea.objects.order_by('title')
    elif sort_by == 'interest':
        ideas = Idea.objects.order_by('-interest')
    else: #기본적으로 최신순
        ideas = Idea.objects.order_by('-created_date')

    paginator = Paginator(ideas, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'sort_by': sort_by,
    }
    return render(request, 'ideas/idea_list.html', context)



def idea_upload(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect('idea_detail', pk=idea.pk) 
    else:
        form = IdeaForm()
    
    return render(request, 'ideas/idea_upload.html', {'form': form})


def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    
    is_starred = False
    try:
        if IdeaStar.objects.filter(idea=idea).exists():
            is_starred = True
    except IdeaStar.DoesNotExist:
        pass

    context = {
        'idea': idea,
        'is_starred': is_starred,
    }
    return render(request, 'ideas/idea_detail.html', context)


def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            idea = form.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
        
    context = {
        'form': form,
        'idea': idea,
    }
    return render(request, 'ideas/idea_update.html', context)


def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        idea.delete()
        return redirect('idea_list')
    return redirect('idea_detail', pk=idea.pk)


#관심도 조절 AJAX
def update_interest(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        idea_pk = request.POST.get('pk')
        action = request.POST.get('action')
        idea = get_object_or_404(Idea, pk=idea_pk)
        
        if action == 'increment':
            idea.interest += 1
        elif action == 'decrement':
            idea.interest -= 1
        idea.save()
        
        return JsonResponse({'interest': idea.interest})
    return JsonResponse({'error': 'Invalid request'}, status=400)


#찜하기 AJAX
def star_idea(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        idea_pk = request.POST.get('pk')
        idea = get_object_or_404(Idea, pk=idea_pk)
        
        try:
            star = IdeaStar.objects.get(idea=idea)
            star.delete()
            starred = False
        except IdeaStar.DoesNotExist:
            IdeaStar.objects.create(idea=idea) 
            starred = True
            
        return JsonResponse({'starred': starred, 'star_count': idea.ideastar_set.count()})
    return JsonResponse({'error': 'Invalid request'}, status=400)