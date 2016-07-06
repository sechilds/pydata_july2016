import sys
import os

def python_path():
    return '\n'.join(sys.path)

def system_path():
    return '\n'.join(os.environ['PATH'].split(':'))

def main():
    print('This is my Python path:\n\n')
    print(python_path())
    print('\n\nThis is my system path:\n\n')
    print(system_path())

if __name__=='__main__':
    main()
