from infosec.core import assemble
import os

def patch_program_data(program: bytes) -> bytes:
    """
    Implement this function to return the patched program. This program should
    execute lines starting with #!, and print all other lines as-is.
    
    WARNING! THIS FUNCTION MUST WORK EVEN IF THE SOURCE PROGRAM IS PLACED IN A DIFFERENT PATH!
    Use the provided path to the source program, and avoid hard-coding the path in
    the exercise directory!

    Use the `assemble` module to translate assembly to bytes. For help, in the
    command line run:

        ipython3 -c 'from infosec.core import assemble; help(assemble)'

    :param data: The bytes of the source program.
    :return: The bytes of the patched program.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    patch1_path = os.path.join(script_dir, "patch1.asm")
    patch2_path = os.path.join(script_dir, "patch2.asm")
    
    patch1_binary = assemble.assemble_file(patch1_path)
    patch2_binary = assemble.assemble_file(patch2_path)
    pro_array = bytearray(program)
    
    for i in range(len(patch1_binary)):
        pro_array[0x633+i] = patch1_binary[i]
        
    
    for i in range(len(patch2_binary)):
        pro_array[0x5CD+i] = patch2_binary[i]
        
    return bytes(pro_array)
        
def patch_program(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    patched = patch_program_data(data)
    with open(path + '.patched', 'wb') as writer:
        writer.write(patched)


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <readfile-program>'.format(argv[0]))
        return -1
    path = argv[1]
    patch_program(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
