import sys

from marquee.app import App


def main():
    app = App()
    app.run()

if __name__ == "__main__": #salvaguarda para obligar a acceder a la funcion main()
    sys.exit(main()) #cierre aplicacion