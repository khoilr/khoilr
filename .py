# %%
import requests
from IPython.core.display import display, HTML

url = 'https://capsule-render.vercel.app/api?'
params = {
    'type': 'soft',
    'color': 'timeGradient',
    'text': 'Lê Công Minh Khôi',
    'animation': 'fadeIn',
}

response = requests.get(url, params=params)

# print link
print(response.url)
HTML(response.text)
