from basemapper import BaseMapper

class Mapper(BaseMapper):
    def __init__(self, prgSize, chrSize):
        self.validPrgrom = (128, 256)
        self.validChrrom = (0,)
        super().__init__(prgSize, chrSize)

    def readPrgrom(self):
        bankSel = 0x8000
        startAddr = 0x8000
        endAddr = 0xffff

        print(f'Reading {self.prgSize} KiB PRGROM from the cartridge')
        bufPrg = b''
        for bank in range(self.prgSize // 32):
            print(f'  Switching to bank {bank}')
            self.writePrgByte(bankSel, bank)
            print(f'  Reading 0x{startAddr:04x}-0x{endAddr:04x} ({endAddr - startAddr + 1} bytes)')
            bufPrg += self.readPrgBytes(startAddr, endAddr)

        return bufPrg
