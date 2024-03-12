import youtube_dl

def download_youtube_playlist(playlist_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'ignoreerrors': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

playlist_url = "https://www.youtube.com/watch?v=h39S0PS3lTE&list=RDAdVOycZMsFk&index=4&ab_channel=NAZA"
download_youtube_playlist(playlist_url)
