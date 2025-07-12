from django.shortcuts import render, get_object_or_404, redirect
from .models import MovieReview
from .forms import MovieReviewForm


def review_list(request):
    reviews = MovieReview.objects.all() # 모든 리뷰 가져오기
    return render(request, 'reviews/reviews_list.html', {'reviews': reviews})


def review_detail(request, pk):
    review = get_object_or_404(MovieReview, pk=pk)
    # 분단위 -> 시간+분단위로 계산하
    hours = review.running_time_minutes // 60
    minutes = review.running_time_minutes % 60
    running_time_display = f"{hours}시간 {minutes}분" if hours > 0 else f"{minutes}분"

    return render(request, 'reviews/reviews_detail.html', {
        'review': review,
        'running_time_display': running_time_display
    })

#새 리뷰 작성 폼
def review_create(request):
    if request.method == 'POST':
        form = MovieReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews:review_list') # 저장 후 리뷰 리스트로 이동
    else:
        form = MovieReviewForm() # 빈 폼
    return render(request, 'reviews/reviews_create.html', {'form': form})


def review_update(request, pk):
    review = get_object_or_404(MovieReview, pk=pk)
    if request.method == 'POST':
        form = MovieReviewForm(request.POST, instance=review) # 기존에 저장해 둔 정보들로 form 채움
        if form.is_valid():
            form.save()
            return redirect('reviews:review_detail', pk=review.pk) #수정 후 해당 리뷰 디테일로 이동
    else:
        form = MovieReviewForm(instance=review) # 기존 데이터를 폼에 채움
    return render(request, 'reviews/reviews_update.html', {'form': form, 'review': review})


def review_delete(request, pk):
    review = get_object_or_404(MovieReview, pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('reviews:review_list') # 삭제 후 리뷰 리스트로 이동
    return render(request, 'reviews/reviews_confirm_delete.html', {'review': review})