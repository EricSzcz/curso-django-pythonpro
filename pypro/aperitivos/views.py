from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video aperitivo: Motivação', 'vimeo_id': 396196904}
    return render(request, 'aperitivos/video.html', context={'video': video})
