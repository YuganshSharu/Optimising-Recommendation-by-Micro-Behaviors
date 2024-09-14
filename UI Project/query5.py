import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import googleapiclient.discovery
import requests

def youtube_api(VIDEO_NAME, CHANNEL_NAME):
  API_KEY = "AIzaSyCWjzINaaHcowX9szNEgxM8tjdQVbC2q1E"
  MAX_RESULTS = 1
  API_VERSION = "v3"
  SERVICE_NAME = "youtube"
  service = build(SERVICE_NAME, API_VERSION, developerKey=API_KEY)
  query = f"{VIDEO_NAME} channel:{CHANNEL_NAME}"
  request = service.search().list(
    part="id,snippet",
    type="video",
    q=query,
    maxResults=MAX_RESULTS,
    fields="items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
  )
  response = request.execute()
  result = response.get("items", [])[0]
  return result['id']['videoId']

def youtube_id(video_id):
  API_KEY = 'AIzaSyCWjzINaaHcowX9szNEgxM8tjdQVbC2q1E'
  service = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

  results = service.videos().list(
    part='statistics',
    id=video_id
  ).execute()
  view_count = results['items'][0]['statistics']['viewCount']
  like_count = results['items'][0]['statistics']['likeCount']
  return [view_count, like_count]
def final_yt_api(VIDEO_NAME, CHANNEL_NAME):
  id = youtube_api(VIDEO_NAME, CHANNEL_NAME)
  stats = youtube_id(id)
  return stats

def spotify_api(TRACK_NAME, ARTIST_NAME):
  CLIENT_ID = "f140204fb8fd473eb63b889a4b8beda7"
  CLIENT_SECRET = "126bc623696742fa876ba52d599566bd"


  MAX_RESULTS = 1

  auth_response = requests.post("https://accounts.spotify.com/api/token",
    data={
      "grant_type": "client_credentials"
    },
    auth=(CLIENT_ID, CLIENT_SECRET)
  )

  if auth_response.status_code == 200:
    auth_data = auth_response.json()
    
    access_token = auth_data['access_token']
    
    headers = {
      "Authorization": f"Bearer {access_token}"
    }
    
    query = f"{TRACK_NAME} artist:{ARTIST_NAME}"
    
    url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit={MAX_RESULTS}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
      data = response.json()
      
      result = data['tracks']['items'][0]
      return data['tracks']['items'][0]['popularity']
    else:
      # Print an error message
      print(f"Error: {response.status_code}")
  else:
    # Print an error message
    print(f"Error: {auth_response.status_code}")

def last_api(track_name, artist_name):
	API_KEY = 'fe408cff5b6bf55f0da8b7440477d149'

	response = requests.get(
	  'http://ws.audioscrobbler.com/2.0/',
	  params={
	    'method': 'track.getInfo',
	    'api_key': API_KEY,
	    'track': track_name,
	    'artist': artist_name,
	    'format': 'json'
	  }
	)

	data = response.json()
	play_count = data['track']['playcount']
	user_count = data['track']['listeners']

	# print(f'Play count: {play_count}')
	# print(f'User count: {user_count}')
	return [play_count, user_count]


def query_5(uid,cat):
        # kajsbcdkbasc
	return [uid,cat]

# print(query_5("Guzarish", "Javed Ali", "T-series"))
