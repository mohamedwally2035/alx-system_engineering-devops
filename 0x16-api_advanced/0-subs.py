#!/usr/bin/python3
"""
0-subs module
Queries the Reddit API and returns the number of subscribers for a subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function that returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, it returns 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'custom_user_agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0

