from assembler import assemble
from schematic import make_schematic

def main():
    program = 'idk'
    
    as_filename = f'mcomputer/{program}.as'
    mc_filename = f'mcomputer/{program}.mc'
    schem_filename = f'mcomputer/{program}program.schem'

    assemble(as_filename, mc_filename)
    make_schematic(mc_filename, schem_filename)

if __name__ == '__main__':
    main()