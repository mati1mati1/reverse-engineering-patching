def validate(data):
    if len(data) < 2:
        return False
     
    arg_0 = data[0]
    var_0 = data[1]
    var_a = 0x12
    for i in range(min(arg_0,len(data)-2)):
        var_a ^= data[i+2]
    return var_a == var_0

def check_message(path: str) -> bool:
    """
    Return True if `msgcheck` would return 0 for the file at the specified path,
    return False otherwise.
    :param path: The file path.
    :return: True or False.
    """
    with open(path, 'rb') as reader:
        # Read data from the file, do whatever magic you need
        data = reader.read(0x400)
        
        if not data:
            return False
           
        return validate(data)



def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msg-file>'.format(argv[0]))
        return -1
    path = argv[1]
    if check_message(path):
        print('valid message')
        return 0
    else:
        print('invalid message')
        return 1


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
