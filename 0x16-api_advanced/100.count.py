import requests

def count_words(subreddit, word_list, after=None, count={}):
    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit, after)
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        
        for post in posts:
            title = post['data']['title'].lower()
            
            for word in word_list:
                word = word.lower()
                
                if word in title:
                    if word in count:
                        count[word] += 1
                    else:
                        count[word] = 1
        
        after = data['data']['after']
        
        if after is not None:
            count_words(subreddit, word_list, after, count)
        else:
            sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
            
            for word, count in sorted_count:
                print("{}: {}".format(word, count))
    else:
        print("Invalid subreddit or no posts match.")