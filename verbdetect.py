import nltk
from nltk.tokenize import word_tokenize
import re

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

def text_clean(text):
    pattern = re.compile(r'\s+')
    text = text.lower()
    Without_whitespace = re.sub(pattern, ' ', text)
    text = Without_whitespace.replace('?', ' ? ').replace(')', ') ')
    
    return text

contractions = ["t","ve","d","ll","m","re","s"]


def get_noun_and_verb(text):
    text = text_clean(text)
    noun_list = []
    verb_list = []
    tokenized_text = word_tokenize(text)
    pos_tags = nltk.pos_tag(tokenized_text)
#     print("POS Tags :  ", pos_tags)
    for val in pos_tags:
        if 'NN' in val[1] or 'NNS' in val[1] or 'NNP' in val[1] or 'NNPS' in val[1]:
            if val[0] not in contractions and val[0] not in noun_list:
                noun_list.append(val[0])
        if 'VB' in val[1] or 'VBD' in val[1] or 'VBG' in val[1] or 'VBN' in val[1] or 'VBZ' in val[1]:
            if val[0] not in verb_list:
                verb_list.append(val[0])
    return noun_list, verb_list

def generate_pos(text):
    """
    Part of Speech Conversion and Draw the Tree
    """

    tokenized_text = word_tokenize(text)
    pos_tags = nltk.pos_tag(tokenized_text)
    print("POS Tags :  ", pos_tags)
    

    # CC coordinating conjunction
    # CD cardinal digit
    # DT determiner
    # EX existential there (like: "there is" ... think of it like "there exists")
    # FW foreign word
    # IN preposition/subordinating conjunction
    # JJ adjective 'big'
    # JJR adjective, comparative 'bigger'
    # JJS adjective, superlative 'biggest'
    # LS list marker 1)
    # MD modal could, will
    # NN noun, singular 'desk'
    # NNS noun plural 'desks'
    # NNP proper noun, singular 'Harrison'
    # NNPS proper noun, plural 'Americans'
    # PDT predeterminer 'all the kids'
    # POS possessive ending parent's
    # PRP personal pronoun I, he, she
    # PRP$ possessive pronoun my, his, hers
    # RB adverb very, silently,
    # RBR adverb, comparative better
    # RBS adverb, superlative best
    # RP particle give up
    # TO infinite marker i.e. to go 'to' the store.
    # UH interjection (goodbye)
    # VB verb (ask)
    # VBD verb, past tense asked
    # VBG verb, gerund/present participle asking
    # VBN verb, past participle asked
    # VBP verb, sing. present, non-3d asking
    # VBZ verb, 3rd person sing. present asking
    # WDT wh-determiner which
    # WP wh-pronoun who, what
    # WP$ possessive wh-pronoun whose
    # WRB wh-abverb where, when
    
    return pos_tags


