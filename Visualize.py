import matplotlib.pyplot as plt
import json

def visualize(fileName, subredditName):
    wordDict = {}

    with open(fileName, 'r') as f:
        wordDict = json.load(f)

    plt.figure(figsize=(50, 10))
    plt.bar(list(wordDict.keys())[:30], list(wordDict.values())[:30] )  # `density=False` would make counts
    plt.title("Word List for subreddit : {}".format(subredditName))
    plt.ylabel('Count')

    plt.savefig(subredditName+'.png')
    plt.xlabel('words')
    plt.show()
visualize('occulusdict.txt', 'occulus')
visualize('ViveWordDict.txt', 'Vive')
# print(ViveWordDict)

# plt.figure(figsize=(50, 10))
# # x = np.random.normal(size=len(occulusWordDict))
# plt.bar(list(ViveWordDict.keys())[:50], list(ViveWordDict.values())[:50] )  # `density=False` would make counts
#
# plt.ylabel('Count')
# plt.xlabel('words')
# # plt.xticks(np.arange(0, 50), list(occulusWordDict.keys())[:50])
# plt.show()
