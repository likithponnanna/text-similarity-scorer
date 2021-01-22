from constants import stop_word_list
import math
import string

class DocumentSimilarity:
  def __init__(self):
    self.stop_words = stop_word_list

  def preprocess_text(self, text):
    ''' Function replaces punctuations with spaces removes special 
    characters, converts the string to lowercase and returns a list 
    of words.'''
    chars = "\\`*_{}[]()>#+-.!$','"
    for c in chars:
        if c == "'": 
            text = text.replace(c, " ")
        else:
            text = text.replace(c, "")
    return text.lower().split()

  def remove_stop_words(self, word_list):
    ''' Removes stop words from the word list that is generated.'''
    return  [x for x in word_list if x not in self.stop_words]

  def dictionary_dot_product(self, sorted_word_dict_one, sorted_word_dict_second):
    ''' Compute dot product'''    
    return sum(sorted_word_dict_one[key]*sorted_word_dict_second.get(key, 0) for key in sorted_word_dict_one)

  def word_frequency (self, word_list):
    ''' Generates word frequency dictionary'''  
    count_dict = dict()
    for items in word_list: 
            count_dict[items] = word_list.count(items)     
    return count_dict 

  
  def string_tokenizer(self, text):
    ''' Generates final tokenized word frequency map'''    
    line_list = text
    word_list = self.preprocess_text(line_list) 
    stop_word_removed_list = self.remove_stop_words(word_list)
    freq_mapping = self.word_frequency(stop_word_removed_list) 
    print(len(line_list), "lines, ", ) 
    print(len(word_list), "words, ", ) 
    print(len(freq_mapping), "distinct words") 
    return freq_mapping 

  def cosine_similarity(self, sorted_word_dict_one, sorted_word_dict_second):
    '''Computes cosine similarity between two text inputs'''  
    numerator = self.dictionary_dot_product(sorted_word_dict_one, sorted_word_dict_second) 
    denominator = math.sqrt(self.dictionary_dot_product(sorted_word_dict_one,
      sorted_word_dict_one)* self.dictionary_dot_product(sorted_word_dict_second, sorted_word_dict_second)) 
    return math.acos(numerator / denominator) 

  def similarity_score(self, text_first, text_second):
    '''Function generates a similarity score between two text inputs''' 
    sorted_word_dict_one = self.string_tokenizer(text_first) 
    sorted_word_dict_second = self.string_tokenizer(text_second)
    # print(sorted_word_dict_one)
    # print(sorted_word_dict_second)
    distance = 1 - (self.cosine_similarity(sorted_word_dict_one, sorted_word_dict_second) / math.acos(0))
    print("The similarity score between the provided text snippets is: {:0.4f} ".format(distance)) 



# text_1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products " \
# "you already love. If you have any participating brands on your receipt, you'll get points " \
# "based on the cost of the products. You don't need to clip any coupons or scan individual "\
# "barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."

# text_2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you " \
# "already buy. If you have any eligible brands on your receipt, you will get " \
# "points based on the total cost of the products. You do not need to cut out " \
# "any coupons or scan individual UPCs. Just scan your receipt after you check " \
# "out and we will find the savings for you."

# text_3 = "We are always looking for opportunities for you to earn more points, which is why " \
# "we also give you a selection of Special Offers. These Special Offers are opportunities to earn " \
# "bonus points on top of the regular points you earn every time you purchase a participating brand. " \
# "No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. " \
# "We just think it is easier that way."


# docObj = DocumentSimilarity()
# docObj.similarity_score(text_1, text_2)
# docObj.similarity_score(text_1, text_3)
# docObj.similarity_score("aa qq", "qq qq")
# docObj.similarity_score("aa qq", "qq tt")