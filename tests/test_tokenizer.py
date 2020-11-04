from src.tokenizer import tokenize


def test_tokinzer():
    assert ["これ", "は", "テスト", "の", "テキスト", "です", "。", "ファミリーマート"] == tokenize(
        "これはテストのテキストです。ファミリーマート"
    )
