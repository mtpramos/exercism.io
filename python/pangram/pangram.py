def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return not (set(alphabet) - set(sentence.lower()))
