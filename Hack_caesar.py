# Caesar Cypher Hacker

message = input('Enter a cypher message: ').upper()
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Loop through every possible key
for key in range(len(LETTERS)):

    translated = ''

    # Run the encryption/decryption code on each symbol in the message
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # Get the number of the symbol
            num = num - key

            # Handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)

            # Add number's symbol at the end of translated
            translated = translated + LETTERS[num]

        else:
            # Just add the symbol without encrypting/decrypting
            translated = translated + symbol

    print('Key #%s: %s' % (key, translated))
