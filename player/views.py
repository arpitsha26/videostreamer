import os 
from django.shortcuts import render
from django.urls import reverse
from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404
from player.models import Movie


def serve_hls_playlist(request, Movie_id):
    try:
        Movie = get_object_or_404(Movie, pk=Movie_id)
        hls_playlist_path = Movie.hls

        with open(hls_playlist_path, 'r') as m3u8_file:
            m3u8_content = m3u8_file.read()

        base_url = request.build_absolute_uri('/') 
        serve_hls_segment_url = base_url +"serve_hls_segment/" +str(Movie_id)
        m3u8_content = m3u8_content.replace('{{ dynamic_path }}', serve_hls_segment_url)


        return HttpResponse(m3u8_content, content_type='application/vnd.apple.mpegurl')
    except (Movie.DoesNotExist, FileNotFoundError):
        return HttpResponse("Video or HLS playlist not found", status=404)


def serve_hls_segment(request, movie_id, segment_name):
    try:
        Movie = get_object_or_404(Movie, pk=movie_id)
        hls_directory = os.path.join(os.path.dirname(Movie.video.path), 'hls_output')
        segment_path = os.path.join(hls_directory, segment_name)

       
        return FileResponse(open(segment_path, 'rb'))
    except (Movie.DoesNotExist, FileNotFoundError):
        return HttpResponse("Video or HLS segment not found", status=404)


def hls_video_player(request, movie_id):
    Movie = Movie.objects.filter(slug=movie_id).first()
    hls_playlist_url = reverse('serve_hls_playlist', args=[Movie.id])
    
    

    context = {
        'hls_url': hls_playlist_url,
        'video': Movie,
    }

    return render(request, 'video_player.html', context)



def all_videos(request):
    Movies = Movie.objects.filter(status='Completed')

    context = {
        'Movies': Movies,
    }

    return render(request, 'all_videos.html', context)