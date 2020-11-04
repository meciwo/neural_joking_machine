import pickle


def test_vocab():
    with open("data/vocab.pkl", "rb") as f:
        vocab = pickle.load(f)
        print(type(vocab))
    pass
