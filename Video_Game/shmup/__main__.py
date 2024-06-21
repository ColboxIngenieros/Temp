import sys
from shmup.app import run

def main(args = None):
    if args is None:
        args = sys.argv[1:]
    
    run()

if __name__ == '__main__':
    sys.exit(main())       #garantiza que la aplicacion se cierra de forma correcta