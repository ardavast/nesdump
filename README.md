# Nesdump
A utility for dumping NES cartridges which controls an Arduino board through a serial protocol.

## Examples
Dump PRGROM of cartridge with mapper 7 and 128 KiB PRGROM to dump_prgrom.bin:
```
nesdump -s /dev/ttyACM0 -m 7 -p 128 -fp dump_prgrom.bin
```

Dump CHRROM of cartridge with mapper 7 and 128 KiB CHRROM to dump_chrrom.bin:
```
nesdump -s /dev/ttyACM0 -m 7 -c 128 -fc dump_chrrom.bin
```

Dump PRGROM of cartridge with mapper 7, 128 KiB PRGROM, and 0 KiB CHRROM to dump_prgrom.bin and dump.bin:
```
nesdump -s /dev/ttyACM0 -m 7 -p 128 -c 0 -fc dump_prgrom.bin -f dump.bin
```

Dump PRGROM of cartridge with mapper 7, 128 KiB PRGROM, and 0 KiB CHRROM to dump.bin:
```
nesdump -s /dev/ttyACM0 -m 7 -p 128 -c 0 -f dump.bin
```
