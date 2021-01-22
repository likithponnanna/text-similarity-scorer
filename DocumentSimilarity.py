from constants import stop_word_list
import math
import string


class DocumentSimilarity:
    def __init__(self):
        self.stop_words = stop_word_list

    def preprocess_text(self, text):
        """Function replaces punctuations with spaces removes special
        characters, converts the string to lowercase and returns a list
        of words."""
        chars = "\\`*_{}[]()>#+-.!$','"
        for c in chars:
            if c == "'":
                text = text.replace(c, " ")
            else:
                text = text.replace(c, "")
        return text.lower().split()

    def remove_stop_words(self, word_list):
        """ Removes stop words from the word list that is generated."""
        return [x for x in word_list if x not in self.stop_words]

    def dictionary_dot_product(self, sorted_word_dict_one, sorted_word_dict_second):
        """ Compute dot product"""
        return sum(
            sorted_word_dict_one[key] * sorted_word_dict_second.get(key, 0)
            for key in sorted_word_dict_one
        )

    def word_frequency(self, word_list):
        """ Generates word frequency dictionary"""
        count_dict = dict()
        for items in word_list:
            count_dict[items] = word_list.count(items)
        return count_dict

    def string_tokenizer(self, text):
        """ Generates final tokenized word frequency map"""
        word_list = self.preprocess_text(text)
        stop_word_removed_list = self.remove_stop_words(word_list)
        freq_mapping = self.word_frequency(stop_word_removed_list)
        return freq_mapping

    def cosine_similarity(self, sorted_word_dict_one, sorted_word_dict_second):
        """Computes cosine similarity between two text inputs"""
        numerator = self.dictionary_dot_product(
            sorted_word_dict_one, sorted_word_dict_second
        )
        denominator = math.sqrt(
            self.dictionary_dot_product(sorted_word_dict_one, sorted_word_dict_one)
            * self.dictionary_dot_product(
                sorted_word_dict_second, sorted_word_dict_second
            )
        )

        try:
            cos_sim = math.acos(numerator / denominator)
        except:
            cos_sim = math.acos(0)

        return cos_sim

    def similarity_score(self, text_first, text_second):
        """Function generates a similarity score between two text inputs"""
        sorted_word_dict_one = self.string_tokenizer(text_first)
        sorted_word_dict_second = self.string_tokenizer(text_second)
        sim_score = 1 - (
            self.cosine_similarity(sorted_word_dict_one, sorted_word_dict_second)
            / math.acos(0)
        )
        return "{:0.4f}".format(sim_score)