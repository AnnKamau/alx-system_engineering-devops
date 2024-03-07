#!/usr/bin/python3
'''
Module contains function number_of_subscribers
'''

import requests
def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Lizzie"}

      try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if "data" in data and "subscribers" in data["data"]:
            return data["data"]["subscribers"]
        else:
            return 0
    except requests.RequestException:
        return 0

    if __name__ == "__main__":
    subreddit_name = input("Enter the subreddit name: ")
    subscribers_count = number_of_subscribers(subreddit_name)
    print(f"Number of subscribers in r/{subreddit_name}: {subscribers_count}")
