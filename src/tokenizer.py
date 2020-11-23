import MeCab

mecab = MeCab.Tagger("-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
mecab.parse("")  # バグ対処


def tokenize(text):
    result = mecab.parse(str(text)).strip().split(" ")
    return result
