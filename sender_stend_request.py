import configuration
import data
import requests

def post_new_order(creation_order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATION_ORDER,
                    json=creation_order,
                    headers=data.headers)
response = post_new_order(data.creation_order)

track_order = response.json()["track"]


def get_order_track(track_order):
    return requests.get(configuration.URL_SERVICE + configuration.GET_TRACK_ORDER,
                        params={"t": track_order})
