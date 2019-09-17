from typing import List, Dict, Union
from byteutils import highByte, lowByte, wordToBytes
from smbus2 import SMBus, i2c_msg

def formatReg(reg_addr: int, value: Union[int, List[int]]) -> List[str]:
    lines = ["Register Num\tBinary\tHex"]
    if isinstance(value, int):
        value = [value]
    for n, x in enumerate(value):
        lines.append("Register 0x{0:04X}:\t{1:08b}\t0x{1:02X}".format(reg_addr + n, x))
    return lines

class DSPI2C:
    def __init__(self, i2c_addr: int, i2c_bus: int = 1):
        self.i2c_addr = i2c_addr
        self.bus = SMBus(i2c_bus)

    def readReg(self, reg_addr: int, num_bytes: int = 1) -> Union[int, List[int]]:
        msg_wr = i2c_msg.write(self.i2c_addr, wordToBytes(reg_addr))
        msg_rd = i2c_msg.read(self.i2c_addr, num_bytes)
        self.bus.i2c_rdwr(msg_wr, msg_rd)
        rd_list = list(msg_rd)
        return rd_lest[0] if len(rd_list) == 1 else rd_list

    def writeReg(self, reg_addr: int, data: Union[int, List[int]]) -> None:
        if isinstance(data, int):
            data = [data]
        wr_content = wordToBytes(reg_addr)
        wr_content.extend(data)
        msg_wr = i2c_msg.write(self.i2c_addr, wr_content)
        self.bus.i2c_rdwr(msg_wr)

    def showReg(self, reg_addr: int, length: int = 1) -> None:
        reg_values = self.readReg(reg_addr, length)
        for line in formatReg(reg_addr, reg_values):
            print(line)
