import json
import pandas as pd
import matplotlib.pyplot as plt
import re


def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

def main():
    tweets_data_path = 'twitter_data.txt'

    tweets_data = []
    tweets_file = open(tweets_data_path, "r")
    # print("tweets_file",tweets_file)
    for line in tweets_file:
        line = line.replace("data", "")
        # print("line", line)
        try:
            tweet = json.loads(line)
            # print("tweet", tweet)
            tweets_data.append(tweet)
        except:
            continue
    # print("len(tweets_data)", len(tweets_data))
    # print("tweets_data",tweets_data)


    tweets = pd.DataFrame()
    # print(type(tweets))
    tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
    tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
    tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

    tweets['python'] = list(map(lambda tweet: word_in_text('python', tweet['text']), tweets_data))
    # print("tweets['python']",tweets['python'])

    tweets['javascript'] = list(map(lambda tweet: word_in_text('javascript', tweet['text']), tweets_data))
    # print("tweets['python']",tweets['python'])

    tweets['ruby'] = list(map(lambda tweet: word_in_text('ruby', tweet['text']), tweets_data))
    tweets['programming'] = list(map(lambda tweet: word_in_text('programming', tweet['text']), tweets_data))
    tweets['tutorial'] = list(map(lambda tweet: word_in_text('tutorial', tweet['text']), tweets_data))

    tweets['programming'] = list(map(lambda tweet: word_in_text('programming', tweet['text']), tweets_data))
    tweets['tutorial'] = list(map(lambda tweet: word_in_text('tutorial', tweet['text']), tweets_data))

    tweets['relevant'] = list(
        map(lambda tweet: word_in_text('programming', tweet['text']), tweets_data) or word_in_text('tutorial', tweet))

    tweets['link'] = list(map(lambda tweet: extract_link(str(tweet)), tweets_data))

    tweets_relevant = tweets[tweets['relevant'] == True]
    tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']

    tweets_by_country = tweets['country'].value_counts()
    # print("tweets_by_country",tweets_by_country)

    # print("tweets[tweets['relevant'] == True] ==", tweets[tweets['relevant'] == True])
    # print("tweets[tweets['relevant'] == True]['python'].value_counts()[True] ==",tweets[tweets['relevant'] == True]['python'].value_counts()[True])



    # print("python", tweets_relevant_with_link[tweets_relevant_with_link['python']== True])
    # ['python'].value_counts()[True]
    # print("javascript",tweets_relevant_with_link[tweets_relevant_with_link['javascript'] == True]['javascript'].value_counts()[True])
    # print("ruby", tweets_relevant_with_link[tweets_relevant_with_link['ruby'] == True]['ruby'].value_counts()[True])

    # print("tweets['relevant'] == True",tweets[tweets['relevant'] == True]['python'].value_counts()[True])
    # print("['python'].value_counts()[True]",tweets['python'].value_counts()[True])


    prg_langs = ['python', 'javascript', 'ruby']

    tweets_by_prg_lang = [
        tweets[tweets['relevant'] == True]['python'].value_counts()[True],
        tweets[tweets['relevant'] == True]['javascript'].value_counts()[True],
        tweets[tweets['relevant'] == True]['ruby'].value_counts()[True]
    ]
    # print("tweets_by_prg_lang", tweets_by_prg_lang)
    x_pos = list(range(len(prg_langs)))
    width = 0.8
    fig, ax = plt.subplots()
    plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')
    ax.set_ylabel('Number of tweets', fontsize=15)
    ax.set_title('Ranking: python vs. javascript vs. ruby (Relevant data)', fontsize=10, fontweight='bold')
    ax.set_xticks([p + 0.4 * width for p in x_pos])
    ax.set_xticklabels(prg_langs)
    plt.grid()

    # tweets_by_prg_lang = [tweets['python'].value_counts()[True], tweets['javascript'].value_counts()[True],
    #                       tweets['ruby'].value_counts()[True]]
    #
    # x_pos = list(range(len(prg_langs)))
    # width = 0.5
    # fig, ax = plt.subplots()
    # plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')
    #
    # # Setting axis labels and ticks
    # ax.set_ylabel('Number of tweets', fontsize=15)
    # ax.set_title('Ranking: python vs. javascript vs. ruby (Raw data)', fontsize=10, fontweight='bold')
    # ax.set_xticks([p + 0.4 * width for p in x_pos])
    # ax.set_xticklabels(prg_langs)
    # plt.grid()

    # fig, ax = plt.subplots()
    # ax.tick_params(axis='x', labelsize=15)
    # ax.tick_params(axis='y', labelsize=10)
    # ax.set_xlabel('Countries', fontsize=15)
    # ax.set_ylabel('Number of tweets' , fontsize=15)
    # ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
    # tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')


    plt.show()

if __name__=='__main__':
	main()