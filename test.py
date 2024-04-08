import requests

import json
from flask import Flask, jsonify
res = requests.get("https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?offset=&host_mid=37507923&timezone_offset=-60&platform=web&features=itemOpusStyle,listOnlyfans",headers={'User-Agent':'Mozilla/5.0'})
item = res.json()
print(item)