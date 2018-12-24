def get_neg(sentence):
    counter = 0
    for word in sentence.split():
        if strip_punctuation(word) in negative_words:
            counter += 1
    return counter

def get_pos(sentence):
    counter = 0
    for word in sentence.split():
        if strip_punctuation(word) in positive_words:
            counter += 1
    return counter

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    for char in punctuation_chars:
        if char in word:
            word = word.replace(char, "")
    return word


# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

with open("project_twitter_data.csv", 'r') as tweet_f:
    header = True
    f = open("resulting_data.csv", 'w')
    h = "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n"
    f.write(h)
    for lin in tweet_f:
        if header == False:
            tweet_data = lin.split(",")
            pos = get_pos(tweet_data[0])
            neg = get_neg(tweet_data[0])
            s = "{0}, {1}, {2}, {3}, {4}\n".format(tweet_data[1], tweet_data[2].strip(), pos, neg, pos - neg)
            f.write(s)
        else:
            header = False
