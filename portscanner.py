from typing import NoReturn, Final
from socket import socket, AF_INET, SOCK_STREAM


def main_f() -> NoReturn:
    """
        Core function.
    """
    # Lista contendo portas alvo.
    PORTAS_ALVO: Final = list(range(80, 1023))

    sock_obj = None

    print("\n")
    host: Final = input("Host para varrer: ")
    print("ALUNO: RM92029 - PABLO")
    print("\n")

    if '://' in host:
        print(f"O host {host} não deve especificar nenhum protocolo.")
        exit(1)

    try:
        sock_obj = socket(AF_INET, SOCK_STREAM)
    except OSError as err:
        print(f"Não foi possível criar o socket, erro: {err}")
        exit(1)

    for test_porta in PORTAS_ALVO:
        # Se o método connect_ex retornar 0, a porta está aberta, caso contrário fechada.
        ret = sock_obj.connect_ex((host, test_porta))

        msg = "Aberta" if ret == 0 else "Fechada"
        print(f"$[{host} ~ {test_porta}] \t\t Status: {msg}")


if __name__ == '__main__':
    main_f()
