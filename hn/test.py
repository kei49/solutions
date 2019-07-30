import pandas as pd
hn = pd.read_csv('hn_stories.csv', names=['submission_time', 'upvotes', 'url', 'headline'])
