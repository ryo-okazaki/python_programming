l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_word(words, func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     return word.capitalize()

# def sample_func(word):
#     return word.lower()

sample_func = lambda word: word.capitalize()
sample_func2 = lambda word: word.lower()

change_word(l, sample_func)
change_word(l, sample_func2)
# 関数オブジェクト

# ラムダ
# 関数を引数にする場合、ラムダ式を使う