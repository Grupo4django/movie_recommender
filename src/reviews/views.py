from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Review
from movies.models import Movie
from .forms import ReviewForm

def review_list(request, movie_id):
    """List all reviews for a specific movie"""
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.reviews.filter(is_approved=True)
    return render(request, 'reviews/review_list.html', {'movie': movie, 'reviews': reviews})

def review_home(request):
    """Home page for reviews, showing all movies with reviews."""
    movies_with_reviews = Movie.objects.filter(reviews__is_approved=True).distinct()
    return render(request, 'reviews/review_home.html', {'movies': movies_with_reviews})

@login_required
def create_review(request, movie_id):
    """Create a new review for a movie"""
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('review_list', movie_id=movie.id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/create_review.html', {'form': form, 'movie': movie})
