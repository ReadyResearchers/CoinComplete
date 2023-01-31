import urllib.parse
import hashlib
import hmac
import base64
import requests

api_url = "https://api.binance.us"

# get binanceus signature
def get_binanceus_signature(data, secret):
    postdata = urllib.parse.urlencode(data)
    message = postdata.encode()
    byte_key = bytes(secret, 'UTF-8')
    mac = hmac.new(byte_key, message, hashlib.sha256).hexdigest()
    return mac

# Attaches auth headers and returns results of a POST request
def binanceus_request(uri_path, data, api_key, api_sec):
    headers = {}
    headers['X-MBX-APIKEY'] = api_key
    signature = get_binanceus_signature(data, api_sec)
    params={**data, "signature": signature}
    req = requests.get((api_url + uri_path), params=params, headers=headers)
    return req.text

api_key = "KRyEwNpwwFGjmZouoQrX8GbXR9C8l5QMTIyaFDS08knNl9UtJ4DEUjx6exzk79GV"
secret_key = "8qIc2Hg1i58NPcgHwlpl8FZrG9cGMv7vh5DB9UNdtNXb4FrjUdC9n3otk4t4t8rE"

uri_path = "/api/v3/openOrders"
data = {
    "symbol": "BTCUSDT",
    "timestamp": 1499827319559
}

get_open_order_result = binanceus_request(uri_path, data, api_key, secret_key)