import re
import string
from collections import defaultdict
import json

def most_active_subreddit_in_2019(filenames_of_monthly_archives):
    import json, gzip
    count = {}
    for filename in filenames_of_monthly_archives:
        headlines = gzip.open(filename)

        for line in headlines:
            single_comment = json.loads(line)

            if single_comment['subreddit'] in count:
                count[single_comment['subreddit']] += 1
            else:
                count[single_comment['subreddit']] = 1
    result = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return result[200:2000]


def subreddits_comments(filenames_of_monthly_archives, redditName1, subredditName2):
    """
    Function to gather comments for each of the sub-reddit that we need to compare

    :param filenames_of_monthly_archives: filenames to fetch from
    :param redditName1: sub-reddit name 1 (occulus)
    :param subredditName2: sub-reddit name 2 (Vive)
    :return: 2 lists having comments for each subreddits
    """
    import json, gzip
    commentsocculus = []
    commentsVive = []

    vive = []
    for filename in filenames_of_monthly_archives:
        headlines = gzip.open(filename)

        for line in headlines:
            single_comment = json.loads(line)
            if single_comment['subreddit'] == redditName1:
                commentsocculus.append(single_comment)
            if single_comment['subreddit'] == subredditName2:
                commentsVive.append(single_comment)

    return commentsocculus, commentsVive


def createDict(filenames, subredditName1, subredditName2):
    """
    Function to create dictionaries of number of words in each of the subteddits.

    :param filenames: Names of files to gather comments from
    :param subredditName1:
    :param subredditName2:
    :return:
    """
    wordDict1 = defaultdict(int)
    wordDict2 = defaultdict(int)
    
    stop_word =["and","the","I","you","to","a","it","is","of","you","that","for","in","with","on","have","be","but","are","this","not","as","my","like","or","just","can","if","your","they","was","so","its","will","at","get","would","more","The","me","an","all","from","about","do","dont","Im","what","there","has","when","some","than","them","It","much","even","If","no","use","their","You","now","by","had","because","still","any","other","Its","then","i","how","know","way","also","make","too","which","need","we","been","could","into","well","same"]
    occulus, Vive = subreddits_comments(filenames, subredditName1, subredditName2)
    for i in occulus:


        text = i['body']
        # remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

        # remove numbers
        text = re.sub('[0-9]', '', text)

        for word in text.split():
            if word not in stop_word:
                wordDict1[word] += 1
    for i in Vive:
        text = i['body']

        # remove punctiation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # remove numbers
        text = re.sub('[0-9]', '', text)
        
        for word in text.split():
            if word not in stop_word:
                wordDict1[word] += 1

    return wordDict1, wordDict2


# gather filenames
import pathlib
filenames = []
# get filenames for the year 2018
test_data_path = pathlib.Path("/l/research/social-media-mining/reddit-sample-1-percent/comments/")
filenames += list(map(str, test_data_path.glob("RC_2018*.gz")))

# fetch files for the 6 months in 2019
raw_names = ['RC_2019-01.gz', 'RC_2019-02.gz','RC_2019-03.gz','RC_2019-04.gz','RC_2019-05.gz','RC_2019-06.gz', ]
for i  in range(len(raw_names)):
    raw_names[i] = test_data_path / raw_names[i]
filenames += raw_names


# create word dictionaries for our sub-reddits
oculusWordDict, ViveWordDict = createDict(filenames ,"oculus", 'Vive')

# sort the dictionaries in the descending order of word frequencies
occulusWordDict = {k: v for k, v in sorted(oculusWordDict.items(), key=lambda item: item[1], reverse= True)}
ViveWordDict  = {k: v for k, v in sorted(ViveWordDict.items(), key=lambda item: item[1], reverse= True)}


# just to display the key-values
i = 0
for k, v in occulusWordDict.items():
    if i > 50:
        break
    i += 1
    print(str(k) +':'+ str(v), 'occulus')

with open('occulusdict.txt', 'w') as f:
    json.dump(occulusWordDict, f)

with open('ViveWordDict.txt', 'w') as f:
    json.dump(ViveWordDict, f)

i = 0
for k, v in ViveWordDict.items():
    if i > 50:
        break
    i += 1
    print(str(k) +':'+ str(v), 'Vive')


