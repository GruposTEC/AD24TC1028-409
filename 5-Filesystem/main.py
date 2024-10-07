import sys
from pathlib import Path

def main():
    print(sys.argv)
    print(sys.argv[1])
    print(sys.argv[2])

    print(Path.cwd())
    print(Path.cwd().parent)

    raiz = Path.cwd().parent
    folder = Path("4-Funciones")
    ruta_small = raiz / folder / sys.argv[1]

    print(ruta_small)

    f = open(ruta_small,"r")
    for linea in f:
        linea = linea.strip()
        linea = linea.split(",")
        print(linea)

    f.close()

if __name__ == "__main__":
    main()