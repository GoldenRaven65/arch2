MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-',
    '?': '..--..'}


def message_to_morse(message):
    translated_words = []
    for word in message.upper().split(" "):
        translated_characters = []
        for character in word:
            if character in MORSE_CODE_DICT:
                translated_characters.append(MORSE_CODE_DICT[character])
            else:
                print(f"Can't convert char [{character}]")
        translated_words.append(" ".join(translated_characters))
    return "    ".join(translated_words)


def morse_to_message(morse):
    morse_code_dict = {code: character for character, code in MORSE_CODE_DICT.items()}
    words = []
    for word in morse.split("    "):
        characters = []
        for code in word.split():
            if code in morse_code_dict:
                characters.append(morse_code_dict[code])
            else:
                print(f"Can't convert char [{code}]")
        words.append("".join(characters))
    return " ".join(words)


def translate_text(text):
    stripped_text = text.strip()
    if stripped_text and set(stripped_text) <= set(".- "):
        return morse_to_message(stripped_text)
    return message_to_morse(text)


def main():
    message = input()
    print(translate_text(message))


if __name__ == "__main__":
    main()