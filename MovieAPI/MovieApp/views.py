from django.http import HttpRequest, JsonResponse
from .models import Movie, Genre

# Create your views here.
def all_add_movies(request: HttpRequest):
    if request.method == "GET":
        result = Movie.objects.all()
        movies = []
        for row in result:
            movies.append({
                "movie": {
                    "id": row.m_id,
                    "title": row.m_title,
                    "box_office": row.m_box_office,
                }
            })
        return JsonResponse({
            "movies": movies
        })
    elif request.method == "POST":
        movie = Movie(
            m_title = request.POST.get("title"),
            m_box_office = request.POST.get("box_office"),
        )
        movie.save()
        for gid in request.POST.get("genre").split():
            genre = Genre.objects.get(g_id = gid)
            movie.genre.add(genre)
        return JsonResponse({
            "msg": "Movie added successfully.",
        })
    else:
        return JsonResponse({
            "msg": "This method is not allowed on this route."
        })

def get_movie(request: HttpRequest, mid):
    try:
        movie = Movie.objects.get(m_id = mid)
        return JsonResponse({
            "movie": {
                "id": movie.m_id,
                "title": movie.m_title,
                "box_office": movie.m_box_office,
            }
        })
    except Movie.DoesNotExist:
        return JsonResponse({
            "msg": "Movie with this id is not found."
        })
    

def update_movie(request: HttpRequest, mid):
    try:
        if request.method == "POST":
            movie = Movie.objects.get(m_id = mid)
            movie.m_title = request.POST.get("title")
            movie.m_box_office = request.POST.get("box_office")
            movie.genre.clear()
            for gid in request.POST.get("genre").split():
                genre = Genre.objects.get(g_id = gid)
                movie.genre.add(genre)
            movie.save()
            return JsonResponse({
                "msg": "Movie updated successfully."
            })
        else:
            return JsonResponse({
                "msg": "This http method ism't supported for this route."
            })
    except Movie.DoesNotExist:
        return JsonResponse({
            "msg": "Movie with this id is not found."
        })


def delete_movie(request: HttpRequest, mid):
    try:
        if request.method == "POST":
            movie = Movie.objects.get(m_id = mid)
            movie.delete()
            return JsonResponse({
                "msg": "Movie deleted successfully."
            })
        else:
            return JsonResponse({
                "msg": "This http method ism't supported for this route."
            })
    except Movie.DoesNotExist:
        return JsonResponse({
            "msg": "Movie with this id is not found."
        })