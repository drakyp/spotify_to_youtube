from bs4 import BeautifulSoup
from requests_html import HTMLSession
from pathlib import Path
import yt_dlp 
import pandas 
import os 


# this will scrape and get the video id
def ScrapeVidId(query):
    print(f"Getting the video id for : {query}")

    #this is the basic url to search on youtube 
    BASIC="https://www.youtube.com/results?search_query="

    #to this url we add the query which is the name of the song 
    URL = (BASIC + query )

    #to search in a url we replace the ' ' with '+' 
    URL.replace(" ", "+")
    #page = requests.get(URL)

    #this will create a session so we can do some http request and htlmsession can handle javascript
    session = HTMLSession()

    # we try to send a get request with the http we just created for the url we just created
    response = session.get(URL)

    #Renders the JavaScript on the page to load dynamic content.
    response.html.render(sleep=1)

    #Passes the rendered HTML content to BeautifulSoup, which allows for easy HTML parsing and data extraction.
    soup = BeautifulSoup(response.html.html, "html.parser")

    # this is to find the first 'a' in the get request we gave and that have the "video-title" tag so we have the video title 
    results = soup.find('a', id= "video-title")
    if results:

        #the purpose of this is to construct the youtube url with the href that look something like this href="/watch?v=UDVtMYqUAyw&pp=ygUYSW50ZXJzdGVsbGFy"
        vid_url = "https://www.youtube.com" + results['href'].split('&')[0]
        return vid_url
    else:
        print("Prout")
        return None



def DownloadVideosFromTitles(list_of_songs):
    ids = []
    #traverse all the song 
    for item in enumerate(list_of_songs):
        # call scrape video to get the url of youtube
        vid_id = ScrapeVidId(item)
        if vid_id:
            #we add the urk if it is not empty
            ids += [vid_id]
    print("Downloading songs")
    DownloadsVideoFromIds(ids)



def DownloadsVideoFromIds(list_of_videos):
    #Creates a string SAVE_PATH that represents the directory path where the downloaded songs will be saved.
    SAVE_PATH = str(os.path.join(Path.home(), "Downloads/Music/songs"))
    #try to create the folder where we want to save the songs
    try:
        os.mkdir(SAVE_PATH)
    except:
        print("Downloads folder exists")
    # configure the download options for the yt_dlp using a dictionnary ydl_opts
    ydl_opts = {
        'format' : 'bestaudio/best',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192',
        }],
        'outtmpl' : SAVE_PATH + '/%(title)s.%(ext)s',
        'default_search' : 'ytsearch',
    }
    #creating a youtube_dl object then download it 
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(list_of_videos)
    
def __main__():
    #read the csv files names "songs.csv"
	data = pandas.read_csv('songs.csv')
    #extract the column name of the files and transform it to a list
	data = data['name'].tolist()
    #print the number of songs we found 
	print("Found ", len(data), " songs!")
    #calling the function to start download them
	DownloadVideosFromTitles(data[2:])
__main__()