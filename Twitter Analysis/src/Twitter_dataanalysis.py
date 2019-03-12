
# coding: utf-8

# In[1]:

#Importing the packages
import pickle
import os


# In[5]:

#Checking the twitter path
if not os.path.exists('secret_twitter_credentials.pkl'):
    Twitter={}
    Twitter['Consumer Key'] = ''
    Twitter['Consumer Secret'] = ''
    Twitter['Access Token'] = ''
    Twitter['Access Token Secret'] = ''
    with open('secret_twitter_credentials.pkl','wb') as f:
        pickle.dump(Twitter, f)
else:
    Twitter=pickle.load(open('secret_twitter_credentials.pkl','rb'))


# Install the `twitter` package to interface with the Twitter API

# In[6]:


get_ipython().system('pip install twitter')


# In[7]:

# Importing the twitter package
import twitter

auth = twitter.oauth.OAuth(Twitter['Access Token'],
                           Twitter['Access Token Secret'],
                           Twitter['Consumer Key'],
                           Twitter['Consumer Secret'])

twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable

print(twitter_api)


# In[8]:

#Getting the world id
WORLD_WOE_ID = 1
US_WOE_ID = 23424977


# Look for the WOEID for [san-diego](http://woeid.rosselliot.co.nz/lookup/san%20diego%20%20ca)
#
# You can change it to another location.

# In[6]:

# Getting San Diego's world id
LOCAL_WOE_ID=2487889

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)
local_trends = twitter_api.trends.place(_id=LOCAL_WOE_ID)


# In[8]:


world_trends[0:1]


# In[9]:


trends=local_trends
print(type(trends))
print(list(trends[0].keys()))
print(trends[0]['trends'])


# In[10]:
#Improting the json package
import json

print((json.dumps(us_trends[:2], indent=1)))


# In[11]:

# Getting trends
trends_set = {}
trends_set['world'] = set([trend['name']
                        for trend in world_trends[0]['trends']])

trends_set['us'] = set([trend['name']
                     for trend in us_trends[0]['trends']])

trends_set['san diego'] = set([trend['name']
                     for trend in local_trends[0]['trends']])


# In[12]:


for loc in ['world','us','san diego']:
    print(('-'*10,loc))
    print((','.join(trends_set[loc])))


# In[13]:


print(( '='*10,'intersection of world and us'))
print((trends_set['world'].intersection(trends_set['us'])))

print(('='*10,'intersection of us and san-diego'))
print((trends_set['san diego'].intersection(trends_set['us'])))


# In[14]:

# Storing the hash tag
q = '#WhatIWantSantaToBringMe'

number = 100

# See https://dev.twitter.com/docs/api/1.1/get/search/tweets

# Getting the results for the hash tag
search_results = twitter_api.search.tweets(q=q, count=number)


statuses = search_results['statuses']


# In[15]:

# Printing the length and statuses
len(statuses)
print(statuses)


# In[16]:


all_text = []
filtered_statuses = []
for s in statuses:
    if not s["text"] in all_text:
        filtered_statuses.append(s)
        all_text.append(s["text"])
statuses = filtered_statuses


# In[28]:


len(statuses)


# In[30]:


[s['text'] for s in filtered_statuses]


# In[19]:


# Show one sample search result by slicing the list...
print(json.dumps(statuses[0], indent=1))


# In[22]:


# The result of the list comprehension is a list with only one element that
# can be accessed by its index and set to the variable t
t = statuses[0]
#[ status for status in statuses
#          if status['id'] == 316948241264549888 ][0]

# Explore the variable t to get familiarized with the data structure...

print(t['retweet_count'])
print(t['retweeted'])


# In[31]:


status_texts = [ status['text']
                 for status in statuses ]

screen_names = [ user_mention['screen_name']
                 for status in statuses
                     for user_mention in status['entities']['user_mentions'] ]

hashtags = [ hashtag['text']
             for status in statuses
                 for hashtag in status['entities']['hashtags'] ]

# Compute a collection of all words from all tweets
words = [ w
          for t in status_texts
              for w in t.split() ]


# In[32]:


# Explore the first 5 items for each...

print(json.dumps(status_texts[0:5], indent=1))
print(json.dumps(screen_names[0:5], indent=1))
print(json.dumps(hashtags[0:5], indent=1))
print(json.dumps(words[0:5], indent=1))


# In[33]:


from collections import Counter

for item in [words, screen_names, hashtags]:
    c = Counter(item)
    print(c.most_common()[:10]) # top 10
    print()


# In[ ]:


def prettyprint_counts(label, list_of_tuples):
    print("\n{:^20} | {:^6}".format(label, "Count"))
    print("*"*40)
    for k,v in list_of_tuples:
        print("{:20} | {:>6}".format(k,v))


# In[ ]:


for label, data in (('Word', words),
                    ('Screen Name', screen_names),
                    ('Hashtag', hashtags)):

    c = Counter(data)
    prettyprint_counts(label, c.most_common()[:10])


# In[ ]:


retweets = [
            # Store out a tuple of these three values ...
            (status['retweet_count'],
             status['retweeted_status']['user']['screen_name'],
             status['text'].replace("\n","\\"))

            # ... for each status ...
            for status in statuses

            # ... so long as the status meets this condition.
                if 'retweeted_status' in status
           ]


# In[ ]:


row_template = "{:^7} | {:^15} | {:50}"
def prettyprint_tweets(list_of_tuples):
    print()
    print(row_template.format("Count", "Screen Name", "Text"))
    print("*"*60)
    for count, screen_name, text in list_of_tuples:
        print(row_template.format(count, screen_name, text[:50]))
        if len(text) > 50:
            print(row_template.format("", "", text[50:100]))
            if len(text) > 100:
                print(row_template.format("", "", text[100:]))


# In[ ]:


# Slice off the first 5 from the sorted results and display each item in the tuple

prettyprint_tweets(sorted(retweets, reverse=True)[:10])
