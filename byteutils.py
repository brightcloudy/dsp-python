from typing import List

def highByte(input_word: int, byte_num: int = 1) -> int:
    return (input_word & (0xFF << (byte_num * 8))) >> (byte_num * 8)

def lowByte(input_word: int) -> int:
    return highByte(input_word, 0)

def wordToBytes(input_word: int, num_bytes: int = 2) -> List[int]:
    byteList = []
    for i in reversed(range(num_bytes)):
        byteList.append(highByte(input_word, i))
    return byteList
