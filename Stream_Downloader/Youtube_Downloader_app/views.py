from django.shortcuts import render,HttpResponse
from pathlib import Path
from django.http import FileResponse
from pytube import YouTube

# Create your views here.
def youtubeQueryFetcher(request):
    file_to_download = YouTube("https://www.youtube.com/watch?v=txXXRMfp12w")
    response = FileResponse(file_to_download,content_type = "application/force-download")
    response['Content-Disposition'] = 'inline ; filename = "file.md"'
    return response
