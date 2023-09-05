class Word(object):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Word!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

w = Word('text')
w2 = Word('########')
print(w + w2) # text########

print(w) # Word!!!!
# オブジェクトの特殊メソッド

print(len(w)) # 4

print(w == w2) # False

"""
__init__ : 初期化

__str__ : 文字列を返す

__len__ : len()で呼ばれる

__add__ : +演算子で呼ばれる

__eq__ : ==演算子で呼ばれる

"""