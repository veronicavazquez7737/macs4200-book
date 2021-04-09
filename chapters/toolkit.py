def textClean( text ):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = text.upper()
    cleaned = ''
    for char in text:
        if char in LETTERS:
            cleaned += char          
    return cleaned

def textBlock( text ):
    text = textClean( text )
    blocked = ''
    for i in range(0, len(text), 5):
        blocked += text[i:i+5] + ' '
    return blocked[:-1]

def caesarDecipher(text, key):
    plaintext = textClean(text)
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ''
   
    for char in plaintext:
        ciphertext += LETTERS[  (LETTERS.find(char) + key) % 26 ]
    
    return textBlock(ciphertext) 
  
def caesarDecipher(text, key):
    ciphertext = textClean(text)
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = ''
   
    for char in ciphertext:
        plaintext += LETTERS[  (LETTERS.find(char) - key) % 26 ]
    
    return plaintext.lower()  
  
def affineDecipher(text, akey, mkey):
    ciphertext = textClean(text)
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = ''
    minverse = -1
    
    for testinverse in range(0,26):
        if (testinverse * mkey) % 26 == 1:
            minverse = testinverse
    
    for char in ciphertext:
        plaintext += LETTERS[ minverse * (LETTERS.find(char) - akey) % 26 ]
    
    return plaintext.lower()  

def affineEncipher(text, akey, mkey):
    plaintext = textClean(text)
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ''
    
    for char in plaintext:
        ciphertext += LETTERS[ (mkey * LETTERS.find(char) + akey) % 26 ]
    
    return textBlock(ciphertext)

def trithemiusEncipher( text, start, direction, step):
    plaintext = textClean( text )
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ''
    keystream = ''

    counter = start
    while len(keystream) != len(plaintext):
        keystream += LETTERS[counter]
        counter = ( counter + (direction * step) ) % 26
    
    for i in range(0, len(plaintext)):
        keyValue = LETTERS.find(keystream[i]) 
        plaintextValue = LETTERS.find(plaintext[i])
        ciphertext += LETTERS[ (plaintextValue + keyValue) % 26 ]
    
    return textBlock(ciphertext)
  
def vigenereEncipher(text, keyword):
    ciphertext = ''
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = textClean(text)
    keyword = textClean(keyword)

    for i in range(0, len(text)):
        plainnum = LETTERS.find( text[i] )
        keynum = LETTERS.find( keyword[i % len(keyword)] )
        ciphertext += LETTERS[ ( plainnum + keynum) % 26 ]

    return textBlock(ciphertext)
  
def vigenereDecipher(text, keyword):
    plaintext = ''
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = textClean(text)
    keyword = textClean(keyword)

    for i in range(0, len(text)):
        ciphernum = LETTERS.find( text[i] )
        keynum = LETTERS.find( keyword[i % len(keyword)] )
        plaintext += LETTERS[ ( ciphernum - keynum) % 26 ]

    return plaintext.lower()

def autokeyEncipher(text, keyword):
    ciphertext = ''
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = textClean(text)
    keystream = textClean(keyword) + text

    for i in range(0, len(text)):
        plainnum = LETTERS.find( text[i] )
        keynum = LETTERS.find( keystream[i] )
        ciphertext += LETTERS[ ( plainnum + keynum) % 26 ]

    return textBlock(ciphertext)
  
def letterFrequency(text):
    text = textClean(text)
    frequencyList = []
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for char in LETTERS:
        frequencyList.append( 100 * text.count(char) / len(text))
    
    return frequencyList

def letterCount(text):
    text = textClean( text )
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    myList = []
    
    for char in LETTERS:
        myList.append(text.count(char))
        
    return myList

def chiSquaredScore(text):
    text = textClean(text)
    standardDist = [0.08167, 0.01492, 0.02728, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
    theCount = letterCount(text)
    expectedCount = []
    chiScore = 0

    for num in standardDist:
        expectedCount.append(num * len(text))

    for i in range(0,26):
        chiScore += ((theCount[i] - expectedCount[i])**2)/expectedCount[i]

    return chiScore

def textSplitter(text, keylength):
    text = textClean(text)
    listOfText = ['']*keylength
    
    for group in range(0, keylength):
        for index in range(group, len(text), keylength):
            listOfText[group] += text[index]
            
    return listOfText

def IC(text):
    text = textClean(text)
    letterCountList = letterCount(text)
    totalNum = sum(letterCountList)
    
    total = 0
    for element in letterCountList:
      prob = (element/totalNum)*((element-1)/(totalNum-1))
      total += prob
        
    return total

def XOR( binary1, binary2):
    binary1 = binary1.replace(' ','')
    binary2 = binary2.replace(' ','')
    result = format(int(binary1, 2) ^ int(binary2, 2), 'b')
    return result.zfill(max(len(binary1), len(binary2) ))
  
def charToBinary(char):
    if len(char)>1:
        char = char[0]
    if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return '{:06b}'.format( ord(char) - 65 )
    elif char in 'abcdefghijklmnopqrstuvwxyz':
        return '{:06b}'.format( ord(char) - 71 )
    elif char in '0123456789':
        return '{:06b}'.format( ord(char) + 4 )
    elif char == '+':
        return '{:06b}'.format( 62 )
    elif char == '/':
        return '{:06b}'.format( 63 )
    else:
        return ''

def textToBinary(text):
    text = text.replace(' ','')
    binary = ''
    for char in text:
        binary += charToBinary(char)
    
    return binary
        
def binaryToChar(binary):
    binary = binary.replace(' ','')
    if len(binary) < 6:
        binary = binary.zfill(6)
    if len(binary) > 6:
        return ''
    num = int(binary,2)
    if (num >= 0) and (num <= 25):
        return chr(num + 65)
    elif (num >= 26) and (num <= 51):
        return chr(num + 71)
    elif (num >= 52) and (num <= 61):
        return chr(num - 4)
    elif num == 62:
        return '+'
    elif num == 63:
        return '/'
    else:
        return ''

def binaryToText(binary):
    text = ''
    for i in range(0, len(binary), 6):
        text += binaryToChar(binary[i:i+6])
    
    return text

def lfsrStream(register, taps, length):
    stream = ''
    while len(stream) != length:
        stream += register[-1]
        position = abs( taps[0] - len(register))
        newbit = register[ position ]
        for i in range(1, len(taps) ):
            position = abs(taps[i] - len(register))
            newbit = XOR( newbit, register[position] )
        register = newbit + register[:-1]    
    return stream
  
def kidRSAkeys( a, b, ap, bp ):
    M = a * b - 1
    e = ap * M + a
    d = bp * M + b
    n = ( e*d - 1) // M
    return (e, d, n)