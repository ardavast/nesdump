from sys import stderr

class BaseMapper:
    WRITE_PRG_BYTE = b'\x01'
    READ_PRG_BYTES = b'\x02'
    WRITE_CHR_BYTE = b'\x03'
    READ_CHR_BYTES = b'\x04'

    def writePrgByte(self, addr, val):
        self.ser.write(self.WRITE_PRG_BYTE)
        self.ser.write(addr.to_bytes(2, 'big'))
        self.ser.write(val.to_bytes(1, 'big'))

    def readPrgBytes(self, startAddr, endAddr):
        self.ser.write(self.READ_PRG_BYTES)
        self.ser.write(startAddr.to_bytes(2, 'big'))
        self.ser.write(endAddr.to_bytes(2, 'big'))
        return self.ser.read(endAddr - startAddr + 1)

    def __init__(self, prgSize, chrSize):
        if prgSize in self.validPrgSizes:
            self.prgSize = prgSize
        else:
            print(f'Invalid prgSize: {prgSize}', file=stderr)
            print(f'Valid prgSizes: {self.validPrgSizes}', file=stderr)
            raise SystemExit(1)

        if chrSize in self.validChrSizes:
            self.chrSize = chrSize
        else:
            print(f'Invalid chrSize: {chrSize}', file=stderr)
            print(f'Valid chrSizes: {self.validChrSizes}', file=stderr)
            raise SystemExit(1)
