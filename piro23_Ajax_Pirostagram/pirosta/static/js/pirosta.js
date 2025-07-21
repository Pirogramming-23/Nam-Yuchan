document.addEventListener('DOMContentLoaded', function() {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    //좋아요
    document.querySelectorAll('.like-button').forEach(button => {
        button.addEventListener('click', function() {
            const postId = this.dataset.postId;
            const url = `/post/${postId}/like/`;
            const likeButton = this;
            const likesCountSpan = likeButton.querySelector('.likes-count');

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
            })
            .then(response => response.json())
            .then(data => {
                likeButton.classList.add('liked'); 
                likesCountSpan.textContent = data.likes_count;
                console.log(data.message);
            })
            .catch(error => console.error('Error incrementing like:', error)); 
        });
    });

    //댓글 작성 기능
    document.querySelectorAll('.comment-form').forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();

            const postId = this.dataset.postId;
            const commentTextInput = this.querySelector('input[name="comment_text"]');
            const commentText = commentTextInput.value;
            const url = `/post/${postId}/comment/create/`;
            const commentList = this.closest('.comments-section').querySelector('.comment-list');
            const commentsInfoSpan = this.closest('.post-card').querySelector('.comments-info');

            if (!commentText.trim()) {
                alert('댓글 내용을 입력해주세요.');
                return;
            }

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrftoken,
                },
                body: `comment_text=${encodeURIComponent(commentText)}`
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const newCommentLi = document.createElement('li');
                    newCommentLi.dataset.commentId = data.comment_id;
                    newCommentLi.innerHTML = `
                        <strong>${data.author_username}</strong>: ${data.text}
                        <span class="comment-date">${data.created_at}</span>
                        <button class="delete-comment-button" data-comment-id="${data.comment_id}">❌</button>
                    `;
                    commentList.appendChild(newCommentLi);
                    commentTextInput.value = '';

                    newCommentLi.querySelector('.delete-comment-button').addEventListener('click', handleDeleteComment);
                } else {
                    alert('댓글 작성 실패: ' + data.message);
                }
            })
            .catch(error => console.error('Error creating comment:', error));
        });
    });

    //댓글 삭제
    document.addEventListener('click', function(event) {
        if (event.target.classList.contains('delete-comment-button')) {
            handleDeleteComment(event);
        }
    });

    //댓글 삭제 함수
    function handleDeleteComment(event) {
        const deleteButton = event.target;
        const commentId = deleteButton.dataset.commentId;
        const commentLi = deleteButton.closest('li');
        const commentsInfoSpan = deleteButton.closest('.post-card').querySelector('.comments-info');

        if (confirm('이 댓글을 삭제하시겠습니까?')) {
            const url = `/comment/${commentId}/delete/`;

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    commentLi.remove();
                    console.log('댓글 삭제 성공');
                } else {
                    alert('댓글 삭제 실패: ' + data.message);
                }
            })
            .catch(error => console.error('Error deleting comment:', error));
        }
    }

    //검색 에이젝스
    const searchInput = document.getElementById('search-input');
    const searchResultsDiv = document.getElementById('search-results');

    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = this.value;
            const url = `/search/?q=${encodeURIComponent(query)}`;

            fetch(url, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            })
            .then(response => response.json())
            .then(data => {
                searchResultsDiv.innerHTML = '';
                if (data.posts && data.posts.length > 0) {
                    data.posts.forEach(post => {
                        const postDiv = document.createElement('div');
                        postDiv.classList.add('search-result-item');
                        postDiv.innerHTML = `
                            <img src="${post.image_url}" alt="${post.content}" width="50">
                            <div>
                                <strong>${post.author_username}</strong><br>
                                <p>${post.content.substring(0, 50)}...</p>
                                <span>❤️ ${post.likes_count} 💬 ${post.comments_count}</span>
                            </div>
                        `;
                        searchResultsDiv.appendChild(postDiv);
                    });
                } else {
                    searchResultsDiv.innerHTML = '<p>검색 결과가 없습니다.</p>';
                }
            })
            .catch(error => console.error('Error searching posts:', error));
        });
    }
});