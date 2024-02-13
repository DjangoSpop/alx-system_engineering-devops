import requests

def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        articles = data["data"]["children"]
        for article in articles:
            hot_list.append(article["data"]["title"])
        
        if data["data"]["after"] is not None:
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return None