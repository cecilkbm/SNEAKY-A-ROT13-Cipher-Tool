def print_banner():
    banner = r"""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║          ███████╗███╗   ██╗███████╗ █████╗ ██╗  ██╗██╗   ██╗         ║
║          ██╔════╝████╗  ██║██╔════╝██╔══██╗██║ ██╔╝╚██╗ ██╔╝         ║
║          ███████╗██╔██╗ ██║█████╗  ███████║█████╔╝  ╚████╔╝          ║
║          ╚════██║██║╚██╗██║██╔══╝  ██╔══██║██╔═██╗   ╚██╔╝           ║
║          ███████║██║ ╚████║███████╗██║  ██║██║  ██╗   ██║            ║
║          ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝            ║
║                                                                      ║
║             "Caesar's cipher for modern-day secrets"                 ║
║        "What happens in ROT13, stays in ROT13... sort of"            ║
║                                                                      ║
║         Because sometimes your group chat needs plausible            ║
║              deniability and Victorian-era encryption                ║
║                                                                      ║
║              What your lover reads: "V ybir lbh"                     ║
║              What everyone else sees: Gibberish                      ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""
    print(banner)

def check_easter_eggs(message, translated):
    """Check for easter eggs and return a cheeky message if found"""
    msg_lower = message.lower().strip()
    
    # love messages
    if msg_lower == "v ybir lbh" or msg_lower == "i love you":
        return "💕 Aww, a secret love note! How romantic (and easily crackable)!"
    
    # secret society references
    if "frperg fbpvrgl" in msg_lower or "secret society" in msg_lower:
        return "🎭 Ah yes, the ancient order of the easily-decoded messages!"
    
    # frat references
    if "seng" in msg_lower or "frat" in msg_lower:
        return "🍺 Greek life using Greek... er, Roman ciphers. Close enough!"
    
    # ROT13 itself
    if "ebg13" in msg_lower or "rot13" in msg_lower:
        return "🤯 You're encrypting the name of the encryption! Meta!"
    
    # caesar references
    if "pnrfne" in msg_lower or "caesar" in msg_lower:
        return "👑 Et tu, Brute? Caesar would be proud... or confused!"
    
    # self-aware messages
    if "guvf vf abg frpher" in msg_lower or "this is not secure" in msg_lower:
        return "😅 Hey now, at least you're honest about it!"
    
    # password references
    if "cnffjbeq" in msg_lower or "password" in msg_lower:
        return "🔐 Pro tip: Don't actually use this for your passwords!"
    
    # help/confused messages
    if msg_lower in ["uryc", "help", "jung", "what"]:
        return "🤔 Just type any message and watch the magic happen! (It's not actually magic)"
    
    return None

if __name__ == "__main__":
    print_banner()

# setting up the constants:
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

print("ROT13 Cipher, by Nostripeszebra with inspiration from Al Sweigart's work")
print()

while True:           # main program loop
    print('Enter a message to encrypt/decrypt (or QUIT):')
    message = input('> ')

    if message.upper() == 'QUIT':
        break        # break out of the programs main loop

    # rotate the letters in message by 13 characters
    translated = ''
    for character in message:
        if character.isupper():
            # concatenate uppercase trasnslated character.
            transCharIndex = (UPPER_LETTERS.find(character) + 13) % 26
            translated += UPPER_LETTERS[transCharIndex]
        elif character.islower():
            # concatenate lowercase translated character.
            transCharIndex = (LOWER_LETTERS.find(character) + 13) % 26
            translated += LOWER_LETTERS[transCharIndex]
        else:
            # concatenate the character untranslated.
            translated += character

    # display the translation:
    print('The translated message is:')
    print(translated)

    # check for easter eggs
    easter_egg = check_easter_eggs(message, translated)
    if easter_egg:
        print(easter_egg)    

    print()
