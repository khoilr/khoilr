# %%
import requests
from IPython.core.display import display, HTML

paramas = {
    "label": "Lê Công Minh Khôi",
    "message": "Lê Công Minh Khôi",
    "color": "blue",
    "url": 'https://www.facebook.com/khoilr',
    'style': 'for-the-badge',
    'logo': 'facebook',
}

url = 'https://img.shields.io/static/v1'


response = requests.get(url, params=paramas)

# print link
print(response.url)
HTML(response.text)
