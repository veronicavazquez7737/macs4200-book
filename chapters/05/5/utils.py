def text_clean( text ):
    # input: string: `text`
    # output: string
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = text.upper()
    cleaned = ''
    for char in text:
        if char in LETTERS:
            cleaned += char
            
    return cleaned

def caesar(text, key):
    # inputs: string: text, int: key
    # output: string: ciphertext
    plaintext = textClean(text)
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ''
    
    for char in plaintext:
        ciphertext += LETTERS[ (LETTERS.find(char) + key) % 26 ]
    
    return ciphertext