import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download('averaged_perceptron_tagger')

"""Part of Speech Conversion and Draw the Tree"""
# text = "hye how are you"
# tokenized_text = word_tokenize(text)
# pos_tags = nltk.pos_tag(tokenized_text)
# print("POS Tags :  ", pos_tags)

# print (tokenized_text)
def noun_and_verb_detection (text):
    
    noun_list = []
    verb_list = []
    # text = "I play football every wednesday"
    tokenized_text = word_tokenize(text)
    pos_tags = nltk.pos_tag(tokenized_text)
    # print("POS Tags :  ", pos_tags)
    for val in pos_tags:
        if 'NN' in val[1]:
            noun_list.append(val[0])
        if 'VB' in val[1]:
            verb_list.append(val[0])
        # return noun_list

    print (noun_list) 

    print (verb_list)
    return verb_list, noun_list