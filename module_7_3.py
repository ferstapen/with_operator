class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                sign = file.read().lower()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    sign = sign.replace(i, '')
                sign = sign.split()
            all_words[name] = sign
        return all_words

    def find(self, word):
        all_word = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                all_word[name] = words.index(word.lower()) + 1
        return all_word
    
    def count(self, word):
        all_word = {}
        for name, words in self.get_all_words().items():
            all_word[name] = words.count(word.lower())
        return all_word

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
