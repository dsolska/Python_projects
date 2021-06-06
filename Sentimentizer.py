def menu():
    from pyfiglet import Figlet
    from termcolor import colored
    f = Figlet(font='standard')
    print(colored(f.renderText('Welcome to Sentimentizer'), 'magenta'))

punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
choice = input("Do you want to load your .txt file or input the text manually?\nEnter 'txt' or 'input': ")
while choice.lower() != ('txt') and choice.lower() != ('input'):
    choice = input("Please enter correct input ('txt' or 'input'): ")
if choice.lower() == 'txt':
    dir = input("Enter the file name: ")
    f = open(dir+".txt", "r")
    input_text = f.read()
    for i in input_text:
        if i in punctuation:
            input_text = input_text.replace(i, "")
    input_text = input_text.lower()
    input_text = input_text.split()
else:
    input_text = input("Enter text to be analyzed: ")
    for i in input_text:
        if i in punctuation:
            input_text = input_text.replace(i, "")
    input_text = input_text.lower()
    input_text = input_text.split()

def get_json():
    import json
    with open("word_list.json") as word_list:
        data = json.load(word_list)
        positive = data["positive"]
        negative = data["negative"]
        stopwords = data["stopwords"]
    return positive, negative, stopwords


def first_text_analysis():
    positive, negative, stopwords = get_json()
    index = 0
    result = 0
    for i in range(0, len(input_text)):
        if input_text[i].lower() in positive:
            result += 1
        elif input_text[i].lower() in negative:
            result -= 1
        else:
            result += 0
        index += 1
    print("\nThe result of sentiment analysis is", result)


def plot_negative_positive():
    import matplotlib.pyplot as plt
    from collections import Counter
    positive, negative, stopwords = get_json()
    positive_list = []
    negative_list = []
    other_list = []
    index1 = 0
    for i in range(0, len(input_text)):
        if input_text[i].lower() in positive:
            positive_list.append(input_text[i])
        elif input_text[i].lower() in negative:
            negative_list.append(input_text[i])
        else:
            other_list.append(input_text[i])
        index1 += 1
    if (len(positive_list) != 0):
        x = Counter(positive_list)
        plt.subplot(131)
        plt.bar(*zip(*x.most_common(20)), width=.5, color='g')
        plt.title("Positive sentiment words")
        plt.xticks(rotation=90, fontsize = 8)
    if (len(negative_list) != 0):
        y = Counter(negative_list)
        plt.subplot(132)
        plt.bar(*zip(*y.most_common(20)), width=.5, color='r')
        plt.title("Negative sentiment words")
        plt.xticks(rotation=90, fontsize = 8)
    percentages_positive_negative = [len(positive_list), len(negative_list)]
    slice_labels = ['Positive words', 'Negative words']
    plt.subplot(133)
    plt.pie(percentages_positive_negative, labels=slice_labels, colors=('g', 'r'), autopct='%1.1f%%')
    plt.title("Percentage of positive and negative words")
    plt.savefig('Positive_negative_words')
    plt.show()


def second_text_analysis():
    import matplotlib.pyplot as plt
    from collections import Counter
    positive, negative, stopwords = get_json()
    second_analysis = input(
        "Do you want to continue the analysis and include the stopwords? (Please type 'Yes' or 'No'): ")
    if second_analysis.lower() == 'yes':
        positive_list2 = []
        negative_list2 = []
        stopword_list2 = []
        other_list2 = []
        index2 = 0
        for i in range(0, len(input_text)):
            if input_text[i].lower() in positive:
                positive_list2.append(input_text[i])
            elif input_text[i].lower() in negative:
                negative_list2.append(input_text[i])
            elif input_text[i].lower() in stopwords:
                stopword_list2.append(input_text[i])
            else:
                other_list2.append(input_text[i])
            index2 += 1
        if (len(positive_list2) !=0):
            x2 = Counter(positive_list2)
            plt.subplot(141)
            plt.bar(*zip(*x2.most_common(20)), width=.5, color='g')
            plt.title("Positive sentiment words")
            plt.xticks(rotation=90, fontsize = 8)
        if (len(negative_list2) !=0):
            y2 = Counter(negative_list2)
            plt.subplot(142)
            plt.bar(*zip(*y2.most_common(20)), width=.5, color='r')
            plt.title("Negative sentiment words")
            plt.xticks(rotation=90, fontsize = 8)
        if (len(stopword_list2) !=0):
            z2 = Counter(stopword_list2)
            plt.subplot(143)
            plt.bar(*zip(*z2.most_common(20)), width=.5, color='b')
            plt.title("Stopwords")
            plt.xticks(rotation=90, fontsize = 8)


        percentages_positive_negative2 = [len(positive_list2), len(negative_list2), len(stopword_list2)]
        slice_labels2 = ['Positive words', 'Negative words', 'Stopwords']
        plt.subplot(144)
        plt.pie(percentages_positive_negative2, labels=slice_labels2, colors=('g', 'r', 'b'), autopct='%1.1f%%')
        plt.title("Percentage of positive, negative, and stop words")
        plt.savefig('Positive_negative_stopwords')
        plt.show()


    else:
        print("If you wish so... :( ")

def third_analysis_comparative():
    global input_text2
    answer = input("Do you want to continue the analysis and add another text to compare?\nEnter 'yes' or 'no': ")
    if answer.lower() == 'yes':
        second_text = input("Do you want to load your .txt file or input the text manually?\nEnter 'txt' or 'input': ")
        while second_text.lower() != ('txt') and second_text.lower() != ('input'):
            second_text = input("Please enter correct input ('txt' or 'input'): ")
        if second_text.lower() == 'txt':
            dir = input("Enter the file name: ")
            f = open(dir + ".txt", "r")
            input_text2 = f.read()
            for i in input_text2:
                if i in punctuation:
                    input_text2 = input_text2.replace(i, "")
            input_text2 = input_text2.lower()
            input_text2 = input_text2.split()
        else:
            input_text2 = input("Enter text to be analyzed: ")
            for i in input_text2:
                if i in punctuation:
                    input_text2 = input_text2.replace(i, "")
            input_text2 = input_text2.lower()
            input_text2 = input_text2.split()
    if answer.lower() == 'no':
            print("Thank you for using Sentimentizer! Exiting...")
            exit()

    import matplotlib.pyplot as plt
    import numpy as np
    positive, negative, stopwords = get_json()
    positive_list = []
    positive_list2 = []
    negative_list = []
    negative_list2 = []
    stopword_list = []
    stopword_list2 = []
    other_list = []
    other_list2 = []
    index = 0
    index2 = 0

    for i in range(0, len(input_text)):
        if input_text[i].lower() in positive:
            positive_list.append(input_text[i])
        elif input_text[i].lower() in negative:
            negative_list.append(input_text[i])
        elif input_text[i].lower() in stopwords:
            stopword_list.append(input_text[i])
        else:
            other_list.append(input_text[i])
        index += 1

    for i in range(0, len(input_text2)):
        if input_text2[i].lower() in positive:
            positive_list2.append(input_text2[i])
        elif input_text2[i].lower() in negative:
            negative_list2.append(input_text2[i])
        elif input_text2[i].lower() in stopwords:
            stopword_list2.append(input_text2[i])
        else:
            other_list2.append(input_text2[i])
        index2 += 1

    n = 1
    index = np.arange(n)
    bar_width = 0.15
    plt.bar(index, len(positive_list), bar_width, color='lightgreen', label='The first text')
    plt.bar(index + bar_width, len(positive_list2), bar_width, color='darkcyan', label='The second text')
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    plt.ylabel('Number')
    plt.title('Positive words in both texts')
    plt.legend()
    plt.savefig('Positive_comparative')
    plt.show()

    index = np.arange(n)
    bar_width = 0.15
    plt.bar(index, len(negative_list), bar_width, color='red', label='The first text')
    plt.bar(index + bar_width, len(negative_list2), bar_width, color='darkred', label='The second text')
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    plt.ylabel('Number')
    plt.title('Negative words in both texts')
    plt.legend()
    plt.savefig('Negative_comparative')
    plt.show()

    index = np.arange(n)
    bar_width = 0.15
    plt.bar(index, len(stopword_list), bar_width, color='skyblue', label='The first text')
    plt.bar(index + bar_width, len(stopword_list2), bar_width, color='royalblue', label='The second text')
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    plt.ylabel('Number')
    plt.title('Stopwords in both texts')
    plt.legend()
    plt.savefig('Stopwords_comparative')
    plt.show()

def keywords():
    new_list = []
    positive, negative, stopwords = get_json()
    for word in input_text:
        if word not in stopwords:
            new_list.append(word)
    from collections import Counter
    Counter = Counter(new_list)
    most_frequent = Counter.most_common(5)
    print("The keywords and numbers of their occurences are:", most_frequent)

def get_results_txt():
    import sys
    sys.stdout = open("sentiment_analysis_result.txt", "w")
    return keywords(), first_text_analysis()

def main():
    menu()
    get_json()
    first_text_analysis()
    keywords()
    plot_negative_positive()
    second_text_analysis()
    third_analysis_comparative()
    get_results_txt()

main()