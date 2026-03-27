def count_vowels_consonants():
    """The function counts the number of vowels and consonants in a sentence"""
    vowels = set('аеёиоуыэюяАЕЁИОУЫЭЮЯ')
    consonants = set('бвгджзйклмнпрстфхцчшщъьБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ')

    sentence = input()
    
    vowels_count = 0
    consonants_count = 0
    
    for ch in sentence:
        if ch in vowels:
            vowels_count += 1
        elif ch in consonants:
            consonants_count += 1
    
    print(f"Гласных: {vowels_count}")
    print(f"Согласных: {consonants_count}")

count_vowels_consonants()
