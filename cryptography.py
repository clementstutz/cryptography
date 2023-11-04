import random

CRYPTED_UNKNOWN_SYMBOL = chr(63)+chr(63)
DECRYPTED_UNKNOWN_SYMBOL = chr(63)

crypted_symbols = {
    ' ': [chr(79)+chr(56), chr(34)+chr(90)],
    '!': [chr(71)+chr(38), chr(114)+chr(59)],
    '"': [chr(113)+chr(60), chr(101)+chr(124)],
    '#': [chr(55)+chr(82), chr(42)+chr(45)],
    '$': [chr(51)+chr(77), chr(56)+chr(85)],
    '%': [chr(42)+chr(120), chr(114)+chr(91)],
    '&': [chr(34)+chr(108), chr(61)+chr(80)],
    "'": [chr(50)+chr(83), chr(63)+chr(105)],
    '(': [chr(76)+chr(50), chr(51)+chr(72)],
    ')': [chr(60)+chr(93), chr(101)+chr(54)],
    '*': [chr(87)+chr(66), chr(67)+chr(70)],
    '+': [chr(44)+chr(63), chr(68)+chr(103)],
    ',': [chr(54)+chr(107), chr(100)+chr(61)],
    '-': [chr(101)+chr(71), chr(52)+chr(46)],
    '.': [chr(89)+chr(92), chr(61)+chr(112)],
    '/': [chr(49)+chr(60), chr(80)+chr(68)],
    '0': [chr(44)+chr(40), chr(126)+chr(123)],
    '1': [chr(57)+chr(64), chr(76)+chr(122)],
    '2': [chr(75)+chr(51), chr(109)+chr(63)],
    '3': [chr(75)+chr(79), chr(113)+chr(68)],
    '4': [chr(107)+chr(78), chr(123)+chr(55)],
    '5': [chr(37)+chr(126), chr(98)+chr(120)],
    '6': [chr(98)+chr(46), chr(97)+chr(110)],
    '7': [chr(35)+chr(110), chr(40)+chr(68)],
    '8': [chr(116)+chr(101), chr(45)+chr(97)],
    '9': [chr(126)+chr(53), chr(97)+chr(40)],
    ':': [chr(62)+chr(65), chr(40)+chr(94)],
    ';': [chr(116)+chr(125), chr(32)+chr(63)],
    '<': [chr(111)+chr(108), chr(74)+chr(117)],
    '=': [chr(102)+chr(54), chr(85)+chr(53)],
    '>': [chr(121)+chr(110), chr(56)+chr(76)],
    '?': [chr(56)+chr(95), chr(90)+chr(52)],
    '@': [chr(125)+chr(40), chr(113)+chr(51)],
    'A': [chr(126)+chr(63), chr(72)+chr(69)],
    'B': [chr(40)+chr(89), chr(50)+chr(90)],
    'C': [chr(123)+chr(99), chr(85)+chr(88)],
    'D': [chr(114)+chr(104), chr(83)+chr(34)],
    'E': [chr(73)+chr(112), chr(121)+chr(94)],
    'F': [chr(35)+chr(126), chr(65)+chr(74)],
    'G': [chr(89)+chr(117), chr(113)+chr(67)],
    'H': [chr(110)+chr(92), chr(110)+chr(34)],
    'I': [chr(50)+chr(62), chr(64)+chr(64)],
    'J': [chr(75)+chr(73), chr(111)+chr(79)],
    'K': [chr(56)+chr(121), chr(68)+chr(122)],
    'L': [chr(73)+chr(52), chr(60)+chr(67)],
    'M': [chr(59)+chr(110), chr(125)+chr(99)],
    'N': [chr(115)+chr(89), chr(109)+chr(97)],
    'O': [chr(112)+chr(66), chr(70)+chr(100)],
    'P': [chr(74)+chr(97), chr(59)+chr(102)],
    'Q': [chr(105)+chr(108), chr(121)+chr(76)],
    'R': [chr(46)+chr(93), chr(89)+chr(50)],
    'S': [chr(91)+chr(123), chr(108)+chr(116)],
    'T': [chr(49)+chr(75), chr(121)+chr(112)],
    'U': [chr(126)+chr(124), chr(105)+chr(74)],
    'V': [chr(86)+chr(113), chr(103)+chr(101)],
    'W': [chr(40)+chr(72), chr(97)+chr(55)],
    'X': [chr(57)+chr(47), chr(34)+chr(47)],
    'Y': [chr(36)+chr(54), chr(68)+chr(90)],
    'Z': [chr(41)+chr(77), chr(56)+chr(91)],
    '[': [chr(68)+chr(123), chr(74)+chr(61)],
   '\\': [chr(83)+chr(102), chr(114)+chr(82)],
    ']': [chr(62)+chr(85), chr(102)+chr(102)],
    '^': [chr(56)+chr(57), chr(77)+chr(65)],
    '_': [chr(105)+chr(56), chr(52)+chr(65)],
    '`': [chr(63)+chr(69), chr(95)+chr(84)],
    'a': [chr(103)+chr(40), chr(45)+chr(83)],
    'b': [chr(97)+chr(113), chr(98)+chr(114)],
    'c': [chr(87)+chr(117), chr(70)+chr(89)],
    'd': [chr(50)+chr(35), chr(34)+chr(86)],
    'e': [chr(114)+chr(60), chr(70)+chr(99)],
    'f': [chr(83)+chr(76), chr(84)+chr(57)],
    'g': [chr(61)+chr(100), chr(52)+chr(38)],
    'h': [chr(88)+chr(68), chr(71)+chr(43)],
    'i': [chr(57)+chr(106), chr(80)+chr(58)],
    'j': [chr(76)+chr(116), chr(125)+chr(35)],
    'k': [chr(93)+chr(54), chr(80)+chr(106)],
    'l': [chr(88)+chr(66), chr(75)+chr(106)],
    'm': [chr(44)+chr(124), chr(117)+chr(62)],
    'n': [chr(90)+chr(64), chr(89)+chr(55)],
    'o': [chr(85)+chr(35), chr(83)+chr(68)],
    'p': [chr(91)+chr(65), chr(48)+chr(83)],
    'q': [chr(82)+chr(125), chr(116)+chr(70)],
    'r': [chr(93)+chr(41), chr(43)+chr(60)],
    's': [chr(122)+chr(42), chr(91)+chr(37)],
    't': [chr(34)+chr(94), chr(64)+chr(109)],
    'u': [chr(75)+chr(44), chr(35)+chr(117)],
    'v': [chr(57)+chr(104), chr(83)+chr(104)],
    'w': [chr(39)+chr(76), chr(105)+chr(47)],
    'x': [chr(77)+chr(87), chr(33)+chr(96)],
    'y': [chr(89)+chr(118), chr(101)+chr(51)],
    'z': [chr(126)+chr(51), chr(99)+chr(64)],
    '{': [chr(117)+chr(119), chr(36)+chr(63)],
    '|': [chr(47)+chr(59), chr(67)+chr(86)],
    '}': [chr(96)+chr(48), chr(104)+chr(126)],
    '~': [chr(114)+chr(75), chr(32)+chr(55)],
    }

decrypted_symbols = {
    chr(79)+chr(56): ' ',
    chr(34)+chr(90): ' ',
    chr(71)+chr(38): '!',
    chr(114)+chr(59): '!',
    chr(113)+chr(60): '"',
    chr(101)+chr(124): '"',
    chr(55)+chr(82): '#',
    chr(42)+chr(45): '#',
    chr(51)+chr(77): '$',
    chr(56)+chr(85): '$',
    chr(42)+chr(120): '%',
    chr(114)+chr(91): '%',
    chr(34)+chr(108): '&',
    chr(61)+chr(80): '&',
    chr(50)+chr(83): "'",
    chr(63)+chr(105): "'",
    chr(76)+chr(50): '(',
    chr(51)+chr(72): '(',
    chr(60)+chr(93): ')',
    chr(101)+chr(54): ')',
    chr(87)+chr(66): '*',
    chr(67)+chr(70): '*',
    chr(44)+chr(63): '+',
    chr(68)+chr(103): '+',
    chr(54)+chr(107): ',',
    chr(100)+chr(61): ',',
    chr(101)+chr(71): '-',
    chr(52)+chr(46): '-',
    chr(89)+chr(92): '.',
    chr(61)+chr(112): '.',
    chr(49)+chr(60): '/',
    chr(80)+chr(68): '/',
    chr(44)+chr(40): '0',
    chr(126)+chr(123): '0',
    chr(57)+chr(64): '1',
    chr(76)+chr(122): '1',
    chr(75)+chr(51): '2',
    chr(109)+chr(63): '2',
    chr(75)+chr(79): '3',
    chr(113)+chr(68): '3',
    chr(107)+chr(78): '4',
    chr(123)+chr(55): '4',
    chr(37)+chr(126): '5',
    chr(98)+chr(120): '5',
    chr(98)+chr(46): '6',
    chr(97)+chr(110): '6',
    chr(35)+chr(110): '7',
    chr(40)+chr(68): '7',
    chr(116)+chr(101): '8',
    chr(45)+chr(97): '8',
    chr(126)+chr(53): '9',
    chr(97)+chr(40): '9',
    chr(62)+chr(65): ':',
    chr(40)+chr(94): ':',
    chr(116)+chr(125): ';',
    chr(32)+chr(63): ';',
    chr(111)+chr(108): '<',
    chr(74)+chr(117): '<',
    chr(102)+chr(54): '=',
    chr(85)+chr(53): '=',
    chr(121)+chr(110): '>',
    chr(56)+chr(76): '>',
    chr(56)+chr(95): '?',
    chr(90)+chr(52): '?',
    chr(125)+chr(40): '@',
    chr(113)+chr(51): '@',
    chr(126)+chr(63): 'A',
    chr(72)+chr(69): 'A',
    chr(40)+chr(89): 'B',
    chr(50)+chr(90): 'B',
    chr(123)+chr(99): 'C',
    chr(85)+chr(88): 'C',
    chr(114)+chr(104): 'D',
    chr(83)+chr(34): 'D',
    chr(73)+chr(112): 'E',
    chr(121)+chr(94): 'E',
    chr(35)+chr(126): 'F',
    chr(65)+chr(74): 'F',
    chr(89)+chr(117): 'G',
    chr(113)+chr(67): 'G',
    chr(110)+chr(92): 'H',
    chr(110)+chr(34): 'H',
    chr(50)+chr(62): 'I',
    chr(64)+chr(64): 'I',
    chr(75)+chr(73): 'J',
    chr(111)+chr(79): 'J',
    chr(56)+chr(121): 'K',
    chr(68)+chr(122): 'K',
    chr(73)+chr(52): 'L',
    chr(60)+chr(67): 'L',
    chr(59)+chr(110): 'M',
    chr(125)+chr(99): 'M',
    chr(115)+chr(89): 'N',
    chr(109)+chr(97): 'N',
    chr(112)+chr(66): 'O',
    chr(70)+chr(100): 'O',
    chr(74)+chr(97): 'P',
    chr(59)+chr(102): 'P',
    chr(105)+chr(108): 'Q',
    chr(121)+chr(76): 'Q',
    chr(46)+chr(93): 'R',
    chr(89)+chr(50): 'R',
    chr(91)+chr(123): 'S',
    chr(108)+chr(116): 'S',
    chr(49)+chr(75): 'T',
    chr(121)+chr(112): 'T',
    chr(126)+chr(124): 'U',
    chr(105)+chr(74): 'U',
    chr(86)+chr(113): 'V',
    chr(103)+chr(101): 'V',
    chr(40)+chr(72): 'W',
    chr(97)+chr(55): 'W',
    chr(57)+chr(47): 'X',
    chr(34)+chr(47): 'X',
    chr(36)+chr(54): 'Y',
    chr(68)+chr(90): 'Y',
    chr(41)+chr(77): 'Z',
    chr(56)+chr(91): 'Z',
    chr(68)+chr(123): '[',
    chr(74)+chr(61): '[',
    chr(83)+chr(102): '\\',
    chr(114)+chr(82): '\\',
    chr(62)+chr(85): ']',
    chr(102)+chr(102): ']',
    chr(56)+chr(57): '^',
    chr(77)+chr(65): '^',
    chr(105)+chr(56): '_',
    chr(52)+chr(65): '_',
    chr(63)+chr(69): '`',
    chr(95)+chr(84): '`',
    chr(103)+chr(40): 'a',
    chr(45)+chr(83): 'a',
    chr(97)+chr(113): 'b',
    chr(98)+chr(114): 'b',
    chr(87)+chr(117): 'c',
    chr(70)+chr(89): 'c',
    chr(50)+chr(35): 'd',
    chr(34)+chr(86): 'd',
    chr(114)+chr(60): 'e',
    chr(70)+chr(99): 'e',
    chr(83)+chr(76): 'f',
    chr(84)+chr(57): 'f',
    chr(61)+chr(100): 'g',
    chr(52)+chr(38): 'g',
    chr(88)+chr(68): 'h',
    chr(71)+chr(43): 'h',
    chr(57)+chr(106): 'i',
    chr(80)+chr(58): 'i',
    chr(76)+chr(116): 'j',
    chr(125)+chr(35): 'j',
    chr(93)+chr(54): 'k',
    chr(80)+chr(106): 'k',
    chr(88)+chr(66): 'l',
    chr(75)+chr(106): 'l',
    chr(44)+chr(124): 'm',
    chr(117)+chr(62): 'm',
    chr(90)+chr(64): 'n',
    chr(89)+chr(55): 'n',
    chr(85)+chr(35): 'o',
    chr(83)+chr(68): 'o',
    chr(91)+chr(65): 'p',
    chr(48)+chr(83): 'p',
    chr(82)+chr(125): 'q',
    chr(116)+chr(70): 'q',
    chr(93)+chr(41): 'r',
    chr(43)+chr(60): 'r',
    chr(122)+chr(42): 's',
    chr(91)+chr(37): 's',
    chr(34)+chr(94): 't',
    chr(64)+chr(109): 't',
    chr(75)+chr(44): 'u',
    chr(35)+chr(117): 'u',
    chr(57)+chr(104): 'v',
    chr(83)+chr(104): 'v',
    chr(39)+chr(76): 'w',
    chr(105)+chr(47): 'w',
    chr(77)+chr(87): 'x',
    chr(33)+chr(96): 'x',
    chr(89)+chr(118): 'y',
    chr(101)+chr(51): 'y',
    chr(126)+chr(51): 'z',
    chr(99)+chr(64): 'z',
    chr(117)+chr(119): '{',
    chr(36)+chr(63): '{',
    chr(47)+chr(59): '|',
    chr(67)+chr(86): '|',
    chr(96)+chr(48): '}',
    chr(104)+chr(126): '}',
    chr(114)+chr(75): '~',
    chr(32)+chr(55): '~',
    }

def crypting(message: str) -> str:
    """Encrypt a message.

    Args:
        message (str): the message to encrypt

    Returns:
        str: crypted message
    """
    crypted_message = ""
    for char in message:
        if char in crypted_symbols:
            new_char = crypted_symbols[char][random.randint(0, 1)]
            crypted_message += new_char
        else:
            crypted_message += CRYPTED_UNKNOWN_SYMBOL
    return crypted_message

def decrypting(crypted_message: str) -> str:
    """Decrypt a message that was encrypted with the crypting method of this script.

    Args:
        crypted_message (str): the message to decrypt

    Returns:
        str: decrypted message
    """
    message = ""
    for i in range(0, len(crypted_message), 2):
        if crypted_message[i]+crypted_message[i+1] in decrypted_symbols:
            message += decrypted_symbols[crypted_message[i]+crypted_message[i+1]]
        else:
            message += DECRYPTED_UNKNOWN_SYMBOL
    return message


if __name__ == "__main__":
    
    print("Enter the message you want to encrypt :")
    message = input()
    
    crypted_message = crypting(message)
    print(crypted_message)

    decrypted_message = decrypting(crypted_message)
    print(decrypted_message)
