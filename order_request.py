
import requests
from configuration import CREATE_ORDER_URL, GET_ORDER_BY_TRACK_URL


def post_create_order(body):
    return requests.post(CREATE_ORDER_URL, json=body)


def get_order_by_track(track):
    return requests.get(GET_ORDER_BY_TRACK_URL, params={"t": track})