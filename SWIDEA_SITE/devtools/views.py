from django.shortcuts import render, get_object_or_404, redirect
from .models import DevTool
from .forms import DevToolForm
from ideas.models import Idea 


def devtool_list(request):
    devtools = DevTool.objects.all().order_by('name')
    context = {
        'devtools': devtools,
    }
    return render(request, 'devtools/devtool_list.html', context)


def devtool_upload(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            devtool = form.save()
            return redirect('devtool_detail', pk=devtool.pk) # 기능15 등록 후 디테일 페이지로 이동
    else:
        form = DevToolForm()
        
    return render(request, 'devtools/devtool_upload.html', {'form': form})




def devtool_detail(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    #12
    related_ideas = Idea.objects.filter(devtool=devtool)

    context = {
        'devtool': devtool,
        'related_ideas': related_ideas,
    }
    return render(request, 'devtools/devtool_detail.html', context)




def devtool_update(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    
    if request.method == 'POST':
        form = DevToolForm(request.POST, instance=devtool)
        if form.is_valid():
            devtool = form.save()
            return redirect('devtool_detail', pk=devtool.pk)
    else:
        form = DevToolForm(instance=devtool)
        
    context = {
        'form': form,
        'devtool': devtool,
    }
    return render(request, 'devtools/devtool_update.html', context)


def devtool_delete(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    if request.method == 'POST':
        devtool.delete()
        return redirect('devtool_list')
    return redirect('devtool_detail', pk=devtool.pk)