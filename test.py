import requests

import json
from flask import Flask, jsonify
res = requests.get("https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?offset=&host_mid=37507923&timezone_offset=-60&platform=web&features=itemOpusStyle,listOnlyfans",headers={'User-Agent':'Mozilla/5.0'},
                   cookies={'SESSDATA':'aa8486f3%2C1717499470%2Ca96b0%2Ac1CjDsinf5F4ETKi7izwuZquWLXJexReMNpBSQJ_uxqJHkbV3Eg5P_VWo9r18EQ_hYkYsSVk9lUzh5NkVpU2pFMGZDYzRGLWhTTC1lb0dwQ19TYVhMZkxsVFA2T19HSWtJdng0bFZYR3NqQng0UF9WX3NETjc3d295R0ZzVE1SYndGNHUwbGVlZDF3IIEC'})
item = res.json()
print(item)