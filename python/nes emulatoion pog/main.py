with open(r"python\nes emulatoion pog\Super Mario Bros. (World).nes", "rb") as f:
    data = f.read()

header = data[:16]

assert header[:4] == b"NES\x1a"

prg_rom_size = header[4] * 16384
chr_rom_size = header[5] * 8192

class Cartridge:
    def __init__(self) -> None:
        self.prg_rom = data[]
    
    def read(self, address):
        return self.prg_rom[address - 0x8000]

class PPU:
    def __init__(self) -> None:
        pass

class Bus:
    def __init__(self):
        self.ram = bytearray(0x800)
        self.ppu = PPU()
        self.cartridge = Cartridge()

    def read(self, address):
        if address < 0x2000:
            return self.ram[address % 0x800]

        elif 0x2000 <= address <= 0x3FFF:
            return self.ppu.read(address)

        elif address >= 0x4020:
            return self.cartridge.read(address)

        return 0
    
class CPU:
    def __init__(self) -> None:
        self.a = 0
        self.x = 0
        self.y = 0
        self.pc = 0
        self.sp = 0xFD
        self.status = 0x24