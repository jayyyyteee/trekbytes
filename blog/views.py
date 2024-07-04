from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post, GeoLocation
from django.views import View
from django.http import JsonResponse
import json

# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]

    def get_queryset(self):
        return Post.objects.order_by('-date')[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.get_queryset()
        context['geolocations'] = GeoLocation.objects.all()
        return context



class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name="all_posts"
    



class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["post_tags"]=self.object.tags.all()
        return context

class AboutMeView(TemplateView):
    template_name = "blog/about-me.html"


class TrackLocationView(View):
    template_name = "blog/trackme.html"

    def post(self, request, *args, **kwargs):
        try:

            data = json.loads(request.body.decode('utf-8'))

            latitude = data.get('latitude')
            longitude = data.get('longitude')

            latitude = float(latitude)
            longitude = float(longitude)

            # Save latitude and longitude to model
            geolocation = GeoLocation.objects.create(latitude=latitude, longitude=longitude)

            return JsonResponse({'status': 'success'})

        except (ValueError, TypeError) as e:
            print('Error:', str(e))  # Debugging statement
            return JsonResponse({'status': 'error', 'message': 'Latitude and longitude must be numeric.'}, status=400)
        except json.JSONDecodeError as e:
            print('JSON Decode Error:', str(e))  # Debugging statement
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)
        except Exception as e:
            print('Unexpected Error:', str(e))  # Debugging statement
            return JsonResponse({'status': 'error', 'message': 'An unexpected error occurred'}, status=500)
    
    def get(self, request, *args, **kwargs):
        geolocations = GeoLocation.objects.all()
        return render(request, self.template_name)