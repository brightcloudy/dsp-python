from typing import List, Dict, Union
import dspi2c
from regmap import RegisterMap, Field
import time

class ADAU1761(DSPI2C):

    rm = RegisterMap("ADAU1761", 0x4000)
    rm.addRegister(0x4000, [("CLKSRC", (3, 3)), ("INFREQ", (1, 2)), ("COREN", (0, 0))])
    rm.addRegister(0x4009,  [("MXBIAS", (5, 6)), ("ADCBIAS", (3, 4)), ("RBIAS", (1, 2))])
    rm.addRegister(0x400A, [("LINPG", (4, 6)), ("LINNG", (1, 3)), ("MX1EN", (0, 0))])
    rm.addRegister(0x400B, [("LDBOOST", (3, 4)), ("MX1AUXG", (0, 2))])
    rm.addRegister(0x400C, [("RINPG", (4, 6)), ("RINNG", (1, 3)), ("MX2EN", (0, 0))])
    rm.addRegister(0x400D, [("RDBOOST", (3, 4)), ("MX2AUXG", (0, 2))])
    rm.addRegister(0x400E, [("LDVOL", (2, 7)), ("LDMUTE", (1, 1)), ("LDEN", (0, 0))]) 
    rm.addRegister(0x400F, [("RDVOL", (2, 7)), ("RDMUTE", (1, 1)), ("RDEN", (0, 0))]) 
    rm.addRegister(0x4010, [("MPERF", (3, 3)), ("MBI", (2, 2)), ("MBIEN", (0, 0))])
    rm.addRegister(0x4011, [("PGASLEW", (6, 7)), ("ALCMAX", (3, 5)), ("ALCSEL", (0, 2))])
    rm.addRegister(0x4012, [("ALCHOLD", (4, 7)), ("ALCTARG", (0, 3))])
    rm.addRegister(0x4013, [("ALCATCK", (4, 7)), ("ALCDEC", (0, 3))])
    rm.addRegister(0x4014, [("NGTYP", (6, 7)), ("NGEN", (5, 5)), ("NGTHR", (0, 4))])
    rm.addRegister(0x4015, [("SPSRS", (6, 6)), ("LRMOD", (5, 5)), ("BPOL", (4, 4)), ("LRPOL", (3, 3)), ("CHPF", (1, 2)), ("MS", (0, 0))])
    rm.addRegister(0x4016, [("BPF", (5, 7)), ("ADTDM", (4, 4)), ("DATDM", (3, 3)), ("MSBP", (2, 2)), ("LRDEL", (0, 1))])
    rm.addRegister(0x4017, [("DAPAIR", (5, 6)), ("DAOSR", (4, 4)), ("ADOSR", (3, 3)), ("CONVSR", (0, 2))])
    rm.addRegister(0x4018, [("ADPAIR", (0, 1))])
    rm.addRegister(0x4019, [("ADCPOL", (6, 6)), ("HPF", (5, 5)), ("DMPOL", (4, 4)), ("DMSW", (3, 3)), ("INSEL", (2, 2)), ("ADCEN", (0, 1))])
    rm.addRegister(0x401A, [("LADVOL", (0, 7))])
    rm.addRegister(0x401B, [("RADVOL", (0, 7))])
    rm.addRegister(0x401C, [("MX3RM", (6, 6)), ("MX3LM", (5, 5)), ("MX3AUXG", (1, 4)), ("MX3EN", (0, 0))])
    rm.addRegister(0x401D, [("MX3G2", (4, 7)), ("MX3G1", (0, 3))])
    rm.addRegister(0x401E, [("MX4RM", (6, 6)), ("MX4LM", (5, 5)), ("MX4AUXG", (1, 4)), ("MX4EN", (0, 0))])
    rm.addRegister(0x401F, [("MX4G2", (4, 7)), ("MX4G1", (0, 3))])
    rm.addRegister(0x4020, [("MX5G4", (3, 4)), ("MX5G3", (1, 2)), ("MX5EN", (0, 0))])
    rm.addRegister(0x4021, [("MX6G4", (3, 4)), ("MX6G3", (1, 2)), ("MX6EN", (0, 0))])
    rm.addRegister(0x4022, [("MX7", (1, 2)), ("MX7EN", (0, 0))])
    rm.addRegister(0x4023, [("LHPVOL", (2, 7)), ("LHPM", (1, 1)), ("HPEN", (0, 0))])
    rm.addRegister(0x4024, [("RHPVOL", (2, 7)), ("RHPM", (1, 1)), ("HPMODE", (0, 0))])
    rm.addRegister(0x4025, [("LOUTVOL", (2, 7)), ("LOUTM", (1, 1)), ("LOMODE", (0, 0))])
    rm.addRegister(0x4026, [("ROUTVOL", (2, 7)), ("ROUTM", (1, 1)), ("ROMODE", (0, 0))])
    rm.addRegister(0x4027, [("MONOVOL", (2, 7)), ("MONOM", (1, 1)), ("MOMODE", (0, 0))])
    rm.addRegister(0x4028, [("POPMODE", (4, 4)), ("POPLESS", (3, 3)), ("ASLEW", (1, 2))])
    rm.addRegister(0x4029, [("HPBIAS", (6, 7)), ("DACBIAS", (4, 5)), ("PBIAS", (2, 3)), ("PREN", (1, 1)), ("PLEN", (0, 0))])
    rm.addRegister(0x402A, [("DACMONO", (6, 7)), ("DACPOL", (5, 5)), ("DEMPH", (2, 2)), ("DACEN", (0, 1))])
    rm.addRegister(0x402B, [("LDAVOL", (0, 7))])
    rm.addRegister(0x402C, [("RDAVOL", (0, 7))])
    rm.addRegister(0x402D, [("ADCSDP", (6, 7)), ("DACSDP", (4, 5)), ("LRCLKP", (2, 3)), ("BCLKP", (0, 1))])
    rm.addRegister(0x402F, [("CDATP", (6, 7)), ("CLCHP", (4, 5)), ("SCLP", (2, 3)), ("SDAP", (0, 1))])
    rm.addRegister(0x4030, [("SDASTR", (0, 0))])
    rm.addRegister(0x4031, [("JDSTR", (5, 5)), ("JDP", (2, 3))])
    rm.addRegister(0x4036, [("DEJIT", (0, 7))])
    rm.addRegister(0x40C6, [("GPIO0", (0, 3))])
    rm.addRegister(0x40C7, [("GPIO1", (0, 3))])
    rm.addRegister(0x40C8, [("GPIO2", (0, 3))])
    rm.addRegister(0x40C9, [("GPIO3", (0, 3))])
    rm.addRegister(0x40EB, [("DSPSR", (0, 3))])
    rm.addRegister(0x40F2, [("SINRT", (0, 3))])
    rm.addRegister(0x40F3, [("SOUTRT", (0, 3))])
    rm.addRegister(0x40F4, [("LRGP3", (3, 3)), ("BGP2", (2, 2)), ("SDOGP1", (1, 1)), ("SDIGP0", (0, 0))])
    rm.addRegister(0x40F5, [("DSPEN", (0, 0))])
    rm.addRegister(0x40F6, [("DSPRUN", (0, 0))])
    rm.addRegister(0x40F7, [("MOSLW", (4, 4)), ("ROSLW", (3, 3)), ("LOSLW", (2, 2)), ("RHPSLW", (1, 1)), ("LHPSLW", (0, 0))])
    rm.addRegister(0x40F8, [("SPSR", (0, 2))])
    rm.addRegister(0x40F9, [("SLEWPD", (6, 6)), ("ALCPD", (5, 5)), ("DECPD", (4, 4)), ("SOUTPD", (3, 3)), ("INTPD", (2, 2)), ("SINPD", (1, 1)), ("SPPD", (0, 0))])
    rm.addRegister(0x40FA, [("CLK1", (1, 1)), ("CLK0", (0, 0))])

    def __init__(self, part_addr: int = 0x3b, pllCtrlWord: int = 0x007D000C2301):
        super().__init__(part_addr)
        self.pllCtrlWord = pllCtrlWord

    def writeField(self, field: str, value: int) -> None:
        f = ADAU1761.rm.getRegField(field)
        cur_val = self.readReg(f.reg_addr)
        new_val = f.modifyInByte(cur_val, value)
        self.writeReg(f.reg_addr, new_val)

    def readField(self, field: str) -> int:
        f = ADAU1761.rm.getRegField(field)
        cur_val = self.readReg(f.reg_addr)
        return f.getFromByte(cur_val)
        
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
