import pandas as pd

def load_data():
    hn = pd.read_csv('hn_stories.csv', names=['submission_time', 'upvotes', 'url', 'headline'])
    print(hn.head())
    return hn
