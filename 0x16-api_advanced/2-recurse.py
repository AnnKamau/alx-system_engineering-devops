#!/usr/bin/python3
"""Contains the recurse function"""
import requests

def fetch_hot_posts(subreddit, hot_list=[], after="", count=0):
    """Fetches titles of all hot posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "Custom User Agent"}

    params = {"after": after, "count": count, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for 4XX or 5XX status codes
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

    try:
        data = response.json()["data"]
        after = data.get("after")
        count += data.get("dist")
        for child in data.get("children"):
            hot_list.append(child["data"]["title"])

        if after is not None:
            return fetch_hot_posts(subreddit, hot_list, after, count)
        return hot_list
    except Exception as e:
        print("Error processing response:", e)
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
