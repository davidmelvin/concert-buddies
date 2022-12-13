from utils.requests import get_data_from_url


def get_friend_activity():
    url = "https://guc-spclient.spotify.com/presence-view/v1/buddylist"

    print("getting friend activity")

    return get_data_from_url(url)
