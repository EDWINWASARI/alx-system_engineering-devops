#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit.
    If the subreddit is invalid, return 0.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'my_user_agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
