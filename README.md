# Concert Buddies

## How to run this code

Using a Python `venv` called `localenv`. `pip` modules are indicated ins the `requirements.txt` file in the root directory.

1. First, activate the local virtual env:

```
source localenv/bin/activate
```

1. Install the pip modules:

```
python3 -m pip install -r requirements.txt
```

1. Run the Flask app

```
flask --app app --debug run
```

1. Open the app in the browser at http://127.0.0.1:5000

1. Paste in your Spotify User ID

## To-Do List

- get shared artists
- get all playlists I follow
- get all playlists my friends follow
- get shared playlists
- track when a friend listens to an artist I follow or a playlist I follow

## Pages

- Home Page
  - header
  - what is your spotify username?
  - what is your spotify cookie? (Can I just use my cookie for everything? Probably...)
- Artists You follow
  - for each artist, list all friends that follow that artist
  - display counts
- Friends You Follow
  - for each friend, list all artists they follow (prboably too big...)
  - display counts

## Data Models

May want to use a graph database.

- artists
  - uri - string
  - name - string
  - is_following? (maybe)
- accounts
  - uri
  - name
- playlists
- song events
  - uri
  - name
  - album (prob piskip this)
  - artist
  - playlist
  - timestamp
- follow data
  - follower account id
  - followed account id

# Resources

1. https://realpython.com/flask-by-example-part-1-project-setup/
