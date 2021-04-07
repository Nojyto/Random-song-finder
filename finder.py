import requests, random, webbrowser
from bs4 import BeautifulSoup

def hasSongBeenUsed(url):
    for songs in open("listenedSongs.txt", "r"):
            if url + "\n" == songs:
                return True
    return False

if __name__ == "__main__":
    page = requests.get('https://old.reddit.com/r/listentothis/rising/', headers={'User-Agent': 'Mozilla/5.0'})
    posts = BeautifulSoup(page.text, 'html.parser').findAll("div", {"data-domain":"youtube.com"})

    urls = []
    for url in posts:
        if(hasSongBeenUsed(url["data-url"]) == False):
            urls.append(url["data-url"])
    
    try:
        songToPlay = random.choice(urls)

        usedSongs = open("listenedSongs.txt", "a")
        usedSongs.write(songToPlay + "\n")
        usedSongs.close()

        webbrowser.open(songToPlay)
    except:
        print("Out of songs.")
    
