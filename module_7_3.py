import string
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        unwanted_symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            words_list = []
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for symbol in unwanted_symbols:
                        line = line.replace(symbol, "")
                    words_list.extend(line.split())
                    all_words[file_name] = words_list

        return all_words

    def find(self, word):
        word = word.lower()
        results_find = {}
        for file_name, words in self.get_all_words().items():
            if word in words:
               results_find[file_name] = words.index(word) + 1
            else:
                results_find[file_name] = None
        return results_find

    def count(self, word):
        word = word.lower()
        results_conts = {}
        for file_name, words in self.get_all_words().items():
            results_conts[file_name] = words.count(word)

        return results_conts



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

