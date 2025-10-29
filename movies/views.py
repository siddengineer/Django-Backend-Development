# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse
# from .models import Movie
# from django.db import connection

# def lazy_demo(request):
#     # Step 1: Searching movies like Netflix (No query yet)
#     movies = Movie.objects.filter(genre="Sci-Fi")
#     print("Step 1: No query executed yet!")
#     print("Total Queries:", len(connection.queries))

#     # Step 2: Add another filter (Still no query)
#     movies = movies.filter(rating__gte=8.0)
#     print("Step 2: Still no query executed!")
#     print("Total Queries:", len(connection.queries))

#     # Step 3: Access data — query executes here
#     print("\nAccessing movie titles now (Query executes!)\n")
#     movie_titles = [m.title for m in movies]
#     print("Total Queries After Evaluation:", len(connection.queries))

#     return HttpResponse(f"Movies Found: {movie_titles}")
from django.http import HttpResponse
from .models import Movie
from django.db import connection

def lazy_demo(request):
   
    genre = request.GET.get('genre', 'Sci-Fi')
    min_rating = float(request.GET.get('rating', 0))

    print(f"\n🔍 Searching for movies with genre='{genre}' and rating>={min_rating}")

    #  queryset (no query yet)
    movies = Movie.objects.filter(genre=genre)
    print("Step 1: No query executed yet!")
    print("Total Queries:", len(connection.queries))

    #  Add another 
    movies = movies.filter(rating__gte=min_rating)
    print("Step 2: Still no query executed!")
    print("Total Queries:", len(connection.queries))

    # Access data 
    print("\n🎥 Accessing movie titles now (Query executes!)\n")
    movie_titles = [m.title for m in movies]
    print("Total Queries After Evaluation:", len(connection.queries))

    return HttpResponse(f"Movies Found ({genre}, rating ≥ {min_rating}): {movie_titles}")
