from smbus2 import SMBus, i2c_msg
from typing import List
import time

class ADAU1761:
    def __init__(self, part_addr: int = 0x3b, pllCtrlWord: int = 0x007D000C2301):
        self.part_addr = part_addr
        self.pllCtrlWord = pllCtrlWord

    def highByte(input_word: int, byte_num: int = 1):
        return (input_word & (0xFF << (byte_num * 8))) >> (byte_num * 8)

    def lowByte(input_word: int):
        return ADAU1761.highByte(input_word, 0)

    def splitAddr(input_addr: int):
        return [ADAU1761.highByte(input_addr), ADAU1761.lowByte(input_addr)]

    def wordToList(input_word: int, num_bytes: int = 2):
        byteList = []
        for i in reversed(range(num_bytes)):
            byteList.append(ADAU1761.highByte(input_word, i))
        return byteList

    def printReg(addr: int, values: List[int]):
        for i, x in enumerate(values):
            print("Register 0x{0:04X}: {1:08b}\t0x{1:02X}".format(addr + i, x, x))

    def displayReg(self, reg_addr: int, length: int = 1):
        values = self.readReg(reg_addr, length)
        ADAU1761.printReg(reg_addr, values)

    def readReg(self, reg_addr: int, num_bytes: int = 1):
        with SMBus(1) as bus:
            msg_wr = i2c_msg.write(self.part_addr, ADAU1761.splitAddr(reg_addr))
            msg_rd = i2c_msg.read(self.part_addr, num_bytes)
            bus.i2c_rdwr(msg_wr, msg_rd)
            return list(msg_rd)

    def writeReg(self, reg_addr: int, data: List[int]):
        with SMBus(1) as bus:
            write_content = ADAU1761.splitAddr(reg_addr)
            write_content.extend(data)
            msg_wr = i2c_msg.write(0x3b, write_content)
            bus.i2c_rdwr(msg_wr)

    def initClkSrc(self, src_pll: bool = True, direct_freq: int = 0x3, core_en: bool = False):
        clkCtrl = (src_pll << 3) | (direct_freq << 1) | (core_en)
        self.writeReg(0x4000, [clkCtrl])

    def enableCoreClk(self):
        r0 = self.readReg(0x4000)[0]
        self.writeReg(0x4000, [r0 | 0x01])

    def disableCoreClk(self):
        r0 = self.readReg(0x4000)[0]
        self.writeReg(0x4000, [r0 & ~(0x01)])

    def checkPLLLocked(self):
        r1 = self.readReg(0x4002, 6)
        return (r1[5] & 0x02)

    def writePLLCtrl(self):
        r1 = ADAU1761.wordToList(self.pllCtrlWord, 6)
        self.writeReg(0x4002, r1)

    def updatePLLCtrl(self, newPllWord: int):
        self.pllCtrlWord = newPllWord
        self.writePllCtrl()

def main():
    dsp = ADAU1761(0x3b)
    dsp.displayReg(0x4000)
    print("PLL Locked: {}".format(dsp.checkPLLLocked()))
    dsp.enableCoreClk()
    dsp.displayReg(0x4000)
    dsp.displayReg(0x402D)


#reg_addr = 0x4002
#query_regs(reg_addr, 6)
#
#pll_settings = [0x00, 0x7D, 0x00, 0x0C, 0x23, 0x01]
#write_reg(reg_addr, pll_settings)
#
#time.sleep(0.5)
#query_regs(reg_addr, 6)

#write = i2c_msg.write(0x3b, [(reg_addr & 0xFF00) >> 8, (reg_addr & 0x00FF)])
#read = i2c_msg.read(0x3b, 6)
#with SMBus(1) as bus:
#        bus.i2c_rdwr(write, read)
#        for i,x in enumerate(list(read)):
#            print("Value {0:04X}: 0x{1:02X} {1:08b}".format(reg_addr + i, x, x))

if __name__ == "__main__":
    main()
