"""
Zestaw zadan 2
zadania od 2.10 do 2.19
testy znajduja sie w bloku main
"""
def count_words(line):
    """
    Zwraca liczbe wyrazow w stringu, gdzie wyraz
    to ciag czarnych znakow oddzielony od reszty wyrazow bialymi.
    """
    words = line.split()
    return len(words)

def underscore_word(word):
    """
    Zwraca string, w ktorym znaki stringu word sa rozdzielone znakiem podkreslenia.
    """
    return "_".join(word)

def first_last(line):
    """
    Zwraca dwa stringi:
    - string utworzony z pierwszych znakow wyrazow ze stringu line
    - string utworzony z ostatnich znakow wyrazow ze stringu line
    """
    words = line.split()
    first = "".join(wd[0] for wd in words)
    last = "".join(wd[-1] for wd in words)
    return first, last

def all_words_length(line):
    """
    Zwraca laczna dlugosc wyrazow ze stringu line.
    """
    words = line.split()
    return sum(len(wd) for wd in words)

def longest_word(line):
    """
    Zwraca najdluzszy wyraz oraz dlugosc najdluzszego wyrazu w stringu line.
    """
    words = line.split()
    longest = max(words, key=len)
    return longest, len(longest)

def join_numbers(L):
    """
    Zwraca string bedacy ciagiem cyfr kolejnych liczb z listy L.
    """
    return "".join(str(i) for i in L)

def replace_gvr(line):
    """
    Zamienia kazdy ciag znakow "GvR" znajdujacy sie w tekscie w stringu line
    na "Guido van Rossum".
    """
    return line.replace("GvR", "Guido van Rossum")

def sort_words(line):
    """
    Zwraca dwie roznie posortowane listy wyrazow ze stringu line:
    - alfabetycznie
    - pod wzgledem dlugosci
    """
    words = line.split()
    return sorted(words), sorted(words, key=len)

def count_zero(n):
    """
    Zwraca liczbe cyfr zero w duzej liczbie calkowitej n.
    """
    return str(n).count("0")

def numbers_format(L):
    """
     Zwraca string zbudowany z trzycyfrowych blokow reprezentujacych liczby z
     listy L. Liczby jedno- i dwucyfrowe maja blok dopelniony zerami.

    """
    return "".join(str(i).zfill(3) for i in L)

if __name__ == "__main__":
    # testy
    # 2.10
    assert count_words('''Hello \n world''') == 2

    # 2.11
    assert underscore_word("Kot") == "K_o_t"

    # 2.12
    assert first_last("Ala ma psa") == ("Amp", "aaa")

    # 2.13
    assert all_words_length("Hello world") == 10

    # 2.14
    assert longest_word("ktory wyraz jest najdluzszy") == ("najdluzszy", 10)

    # 2.15
    assert join_numbers([11, 76, 89, 1]) == ("1176891")

    # 2.16
    assert replace_gvr("GvR to tworca Pythona") == "Guido van Rossum to tworca Pythona"

    # 2.17
    assert sort_words("kot oraz chomik") == (["chomik", "kot", "oraz"], ["kot", "oraz", "chomik"])

    # 2.18
    assert count_zero(1003400670030) == 7

    # 2.19
    assert numbers_format([1, 6, 8, 98, 101]) == "001006008098101"

    print("All tests passed successfully")



