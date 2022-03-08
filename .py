# %%
from IPython.display import HTML
import requests

url = 'https://capsule-render.vercel.app/api?'
params = {
    'type': 'waving',
    'color': 'timeGradient',
    'section': 'footer',
    "height": 90,
    'width': 200,
    'text': '😘 Thank you for visiting my GitHub profile!',
    'fontSize': 16,
    'fontAlign': 19,
    'fontAlignY': 90,
}

response = requests.get(url, params=params)

print(response.url)
HTML(response.text)
