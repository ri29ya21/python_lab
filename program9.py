
# Program 9: Text Anagram and Pattern Matcher Tool

from collections import Counter

def clean_text(text):
    """Remove spaces and convert text to lowercase."""
    return ''.join(
        filter(str.isalnum, text.lower())
    )


def are_anagrams(word1, word2):
    """Check anagrams using sorted characters."""
    text1 = clean_text(word1)
    text2 = clean_text(word2)

    return sorted(text1) == sorted(text2)


def character_count(text):
    """Count character frequencies."""
    return Counter(clean_text(text))


def main():
    print("----- Text Anagram and Pattern Matcher Tool -----")

    word1 = input("Enter the first word or phrase: ")
    word2 = input("Enter the second word or phrase: ")

    if are_anagrams(word1, word2):
        print("\nResult: The given texts are anagrams.")
    else:
        print("\nResult: The given texts are not anagrams.")

    print("\nCharacter counts:")
    print("First text:", dict(character_count(word1)))
    print("Second text:", dict(character_count(word2)))

    # Group multiple words by their anagram pattern
    n = int(input("\nHow many words do you want to group? "))
    groups = {}

    for i in range(n):
        word = input(f"Enter word {i + 1}: ")
        key = tuple(sorted(clean_text(word)))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    print("\nAnagram Groups:")
    for key, words in groups.items():
        print(words)


if __name__ == "__main__":
    main()