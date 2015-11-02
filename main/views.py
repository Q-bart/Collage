from django.shortcuts import render, redirect
from main.forms import Collage
from Collage.settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
import tweepy, time, sys
from PIL import Image
import requests
from io import BytesIO
import urllib

def collage(request):
    context = {
        'form': Collage()
    }
    if request.POST:
        form = Collage(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)

            folowers = tweepy.Cursor(api.followers, screen_name=cd['user']).items(cd['width']*cd['height'])
            width = cd['width']
            height = cd['height']
            collage = Image.new('RGBA', (width*48, height*48), color='white')

            x = 0
            y = 0
            for i, folower in enumerate(folowers):
                url = folower.profile_image_url
                file = BytesIO(urllib.request.urlopen(url).read())
                avatar = Image.open(file)
                collage.paste(avatar, box=(x*48,y*48))

                if (i+1) % width==0:
                    x = 0
                    y += 1
                else:
                    x += 1

            collage.save(r'static/ready_collage/collage.png')

            return redirect('/collage/')
    else:
        return render(request, 'send_data.html', context)

def ready_collage(request):
    return render(request, 'collage.html')
