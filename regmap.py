from typing import List, Dict, Union, Optional, Generic, NamedTuple, Tuple
from byteutils import highByte, lowByte, wordToBytes
from collections import namedtuple

def filled_bits(value: int = 0) -> Dict[int, int]:
    bits = {}
    for i in range(8):
        bits[i] = 1 if (value & (1 << i)) else 0
    return bits

class Field(namedtuple('Field', ['name', 'bits', 'reg_addr'])):

    def positionBits(self) -> List[int]:
        return list(range(self.bits[0], self.bits[1]+1))

    def positionMask(self, inv: bool = False) -> int:
        mask = 0
        for posn in self.positionBits():
            mask = mask | (1 << posn)
        return mask if not inv else ~(mask)

    def getFromByte(self, byte_val: int) -> int:
       return (byte_val & self.positionMask()) >> self.bits[0]

    def modifyInByte(self, byte_val: int, field_val: int) -> int:
        byte_val = byte_val & self.positionMask(True)
        byte_val = byte_val | (field_val << self.bits[0])
        return byte_val


#class Register:
#    def __init__(self, address: int, fields: List[NamedTuple], name: str = "undefined", initial_value: int = 0):
#        self.address = address
#        self.fields = fields
#        self.fields.sort(key = lambda x: x[1])
#        self.name = name 
#        self.value = initial_value

class RegisterMap:
    def __init__(self, name: str = "Undefined", start_addr: int = 0x00):
        self.name = name
        self.start_addr = start_addr
        self.regmap = {}

    def addField(self, new_field: Field, value: int = 0) -> None:
        self.regmap[new_field.name] = (new_field.bits, new_field.reg_addr)

    def addRegister(self, reg_addr: int, fields: List[Tuple[str, Tuple[int, int]]]) -> None:
        for f in fields:
            self.regmap[f[0]] = (f[1], reg_addr)

    def listAllFields(self) -> List[Field]:
        return [Field(k, v[0], v[1]) for (k,v) in self.regmap.items()]

    def listRegFields(self, reg_addr: int) -> List[Field]:
        return [Field(k, v[0], reg_addr) for (k,v) in self.regmap.items() if v[1] == reg_addr]

    def getRegField(self, reg_name: str) -> Field:
        return Field(reg_name, self.regmap[reg_name][0], self.regmap[reg_name][1])


