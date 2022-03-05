# %%
import requests
from IPython.core.display import display, HTML

url = 'https://github-readme-stats.vercel.app/api'
params = {
    'show_icons':True,
    'username': 'khoilr',
    'title_color': 'F9C859',
    'text_color': '10B1FE',
    'icon_color': 'f9598a',
    'bg_color': '282c34',
    'hide_border': False,
    'cache_seconds': 1800
}

response = requests.get(url, params=params)

# print link
print(response.url)
HTML(response.text)
