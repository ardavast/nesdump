#!/usr/bin/env python3

import argparse
import time
import sys
from importlib import import_module

import serial

def parseCmdline():
    example = '''Examples:
Dump PRGROM of cartridge with mapper 7 and 128 KiB PRGROM to dump_prgrom.bin:
nesdump -s /dev/ttyACM0 -m 7 -p 128 -fp dump_prgrom.bin

Dump CHRROM of cartridge with mapper 7 and 128 KiB CHRROM to dump_chrrom.bin:
nesdump -s /dev/ttyACM0 -m 7 -c 128 -fc dump_chrrom.bin

Dump PRGROM of cartridge with mapper 7, 128 KiB PRGROM, and 0 KiB CHRROM to dump_prgrom.bin and dump.bin:
nesdump -s /dev/ttyACM0 -m 7 -p 128 -c 0 -fc dump_prgrom.bin -f dump.bin

Dump PRGROM of cartridge with mapper 7, 128 KiB PRGROM, and 0 KiB CHRROM to dump.bin:
nesdump -s /dev/ttyACM0 -m 7 -p 128 -c 0 -f dump.bin
'''

    parser = argparse.ArgumentParser(epilog=example,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-s',  '--serial',  dest='serialDev', required=True)
    parser.add_argument('-m',  '--mapper',  dest='mapper', required=True)
    parser.add_argument('-p',  '--prgsize', dest='prgSize', type=int)
    parser.add_argument('-c',  '--chrsize', dest='chrSize', type=int)
    parser.add_argument('-fp', '--prgfile', dest='prgFile')
    parser.add_argument('-fc', '--chrfile', dest='chrFile')
    parser.add_argument('-f',  '--file',    dest='file')

    args = parser.parse_args()

    if not (args.prgSize or args.chrSize):
        print('At least one of -p/--prgsize or -c/--chrsize must be used')

    if args.prgSize and not (args.prgFile or args.file):
        print('-p/--prgsize must be used with -fp/--prgfile and/or -f/--file')

    if args.chrSize and not (args.chrFile or args.file):
        print('-c/--chrsize must be used with -fc/--chrfile and/or -f/--file')

    return args

def main():
    args = parseCmdline()

    print(f'Starting {sys.argv[0]} with settings:')
    print(f'  Mapper: {args.mapper}')
    print(f'  PRGROM size: {args.prgSize} KiB')
    print(f'  CHRROM size: {args.chrSize} KiB')

    mapperClass = getattr(import_module(f'mapper{args.mapper}'), 'Mapper')
    mapper = mapperClass(args.prgSize, args.chrSize)

    print(f'Connecting to serial device {args.serialDev}... ', end='')
    mapper.ser = serial.Serial(args.serialDev)
    print(f'connected to {args.serialDev}')

    print('Waiting 1s for the Arduino to reset')
    time.sleep(1)

    bufPrg = mapper.readPrgrom()
    if args.prgFile:
        print(f'Writing {args.prgSize} KiB PRGROM to {args.prgFile}')
        with open(args.prgFile, 'wb') as f:
            f.write(bufPrg)

    if args.file:
        print(f'Writing {args.prgSize} KiB PRGROM to {args.file}')
        with open(args.file, 'wb') as f:
            f.write(bufPrg)

if __name__ == "__main__":
    main()
