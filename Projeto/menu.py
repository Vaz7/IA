import sys
from time import sleep

import keyboard
from os import system, name

import ProjetoIA, grafo


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def menu1():
    print('╔══════════════════════════════════════════════════════════════════════════════╗')
    print('║                                                                              ║')
    print('║ ██████╗░██████╗░░█████╗░░░░░░██╗███████╗████████╗░█████╗░░░░░░░░░██╗░█████╗░ ║')
    print('║ ██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝╚══██╔══╝██╔══██╗░░░░░░░░██║██╔══██╗ ║')
    print('║ ██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░░░░██║░░░██║░░██║░░░░░░░░██║███████║ ║')
    print('║ ██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░░░░██║░░░██║░░██║░░░░░░░░██║██╔══██║ ║')
    print('║ ██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗░░░██║░░░╚█████╔╝░░░░░░░░██║██║░░██║ ║')
    print('║ ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░░░╚═╝░░░░╚════╝░░░░░░░░░╚═╝╚═╝░░╚═╝ ║')
    print('║                     █▀█ █▀▀█ █▀█ █▀█ ░░ █▀█ █▀▀█ █▀█ █▀▀█                    ║')
    print('║                     ░▄▀ █▄▀█ ░▄▀ ░▄▀ ▀▀ ░▄▀ █▄▀█ ░▄▀ ░░▀▄                    ║')
    print('║                     █▄▄ █▄▄█ █▄▄ █▄▄ ░░ █▄▄ █▄▄█ █▄▄ █▄▄█                    ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                █▀ █ █▄░█ █▀▀ █░░ █▀▀   █▀█ █░░ ▄▀█ █▄█ █▀▀ █▀█               ║')
    print('║             ▶  ▄█ █ █░▀█ █▄█ █▄▄ ██▄   █▀▀ █▄▄ █▀█ ░█░ ██▄ █▀▄               ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                  █▀▄▀█ █░█ █░░ ▀█▀ █ █▀█ █░░ ▄▀█ █▄█ █▀▀ █▀█                 ║')
    print('║                  █░▀░█ █▄█ █▄▄ ░█░ █ █▀▀ █▄▄ █▀█ ░█░ ██▄ █▀▄                 ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('╚══════════════════════════════════════════════════════════════════════════════╝')


def menu2():
    print('╔══════════════════════════════════════════════════════════════════════════════╗')
    print('║                                                                              ║')
    print('║ ██████╗░██████╗░░█████╗░░░░░░██╗███████╗████████╗░█████╗░░░░░░░░░██╗░█████╗░ ║')
    print('║ ██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝╚══██╔══╝██╔══██╗░░░░░░░░██║██╔══██╗ ║')
    print('║ ██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░░░░██║░░░██║░░██║░░░░░░░░██║███████║ ║')
    print('║ ██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░░░░██║░░░██║░░██║░░░░░░░░██║██╔══██║ ║')
    print('║ ██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗░░░██║░░░╚█████╔╝░░░░░░░░██║██║░░██║ ║')
    print('║ ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░░░╚═╝░░░░╚════╝░░░░░░░░░╚═╝╚═╝░░╚═╝ ║')
    print('║                     █▀█ █▀▀█ █▀█ █▀█ ░░ █▀█ █▀▀█ █▀█ █▀▀█                    ║')
    print('║                     ░▄▀ █▄▀█ ░▄▀ ░▄▀ ▀▀ ░▄▀ █▄▀█ ░▄▀ ░░▀▄                    ║')
    print('║                     █▄▄ █▄▄█ █▄▄ █▄▄ ░░ █▄▄ █▄▄█ █▄▄ █▄▄█                    ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                █▀ █ █▄░█ █▀▀ █░░ █▀▀   █▀█ █░░ ▄▀█ █▄█ █▀▀ █▀█               ║')
    print('║                ▄█ █ █░▀█ █▄█ █▄▄ ██▄   █▀▀ █▄▄ █▀█ ░█░ ██▄ █▀▄               ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                  █▀▄▀█ █░█ █░░ ▀█▀ █ █▀█ █░░ ▄▀█ █▄█ █▀▀ █▀█                 ║')
    print('║               ▶  █░▀░█ █▄█ █▄▄ ░█░ █ █▀▀ █▄▄ █▀█ ░█░ ██▄ █▀▄                 ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('╚══════════════════════════════════════════════════════════════════════════════╝')


def menuPesquisa1():
    print('╔══════════════════════════════════════════════════════════════════════════════╗')
    print('║                                                                              ║')
    print('║       ██████╗░███████╗░██████╗░██████╗░██╗░░░██╗██╗░██████╗░█████╗░██╗       ║')
    print('║       ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║░░░██║██║██╔════╝██╔══██╗╚═╝       ║')
    print('║       ██████╔╝█████╗░░╚█████╗░██║██╗██║██║░░░██║██║╚█████╗░███████║░░░       ║')
    print('║       ██╔═══╝░██╔══╝░░░╚═══██╗╚██████╔╝██║░░░██║██║░╚═══██╗██╔══██║░░░       ║')
    print('║       ██║░░░░░███████╗██████╔╝░╚═██╔═╝░╚██████╔╝██║██████╔╝██║░░██║██╗       ║')
    print('║       ╚═╝░░░░░╚══════╝╚═════╝░░░░╚═╝░░░░╚═════╝░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝       ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║              █▄░█ ▄▀█ █▀█   █ █▄░█ █▀▀ █▀█ █▀█ █▀▄▀█ ▄▀█ █▀▄ ▄▀█             ║')
    print('║           ▶  █░▀█ █▀█ █▄█   █ █░▀█ █▀░ █▄█ █▀▄ █░▀░█ █▀█ █▄▀ █▀█             ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                     █ █▄░█ █▀▀ █▀█ █▀█ █▀▄▀█ ▄▀█ █▀▄ ▄▀█                     ║')
    print('║                     █ █░▀█ █▀░ █▄█ █▀▄ █░▀░█ █▀█ █▄▀ █▀█                     ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('╚══════════════════════════════════════════════════════════════════════════════╝')


def menuPesquisa2():
    print('╔══════════════════════════════════════════════════════════════════════════════╗')
    print('║                                                                              ║')
    print('║       ██████╗░███████╗░██████╗░██████╗░██╗░░░██╗██╗░██████╗░█████╗░██╗       ║')
    print('║       ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║░░░██║██║██╔════╝██╔══██╗╚═╝       ║')
    print('║       ██████╔╝█████╗░░╚█████╗░██║██╗██║██║░░░██║██║╚█████╗░███████║░░░       ║')
    print('║       ██╔═══╝░██╔══╝░░░╚═══██╗╚██████╔╝██║░░░██║██║░╚═══██╗██╔══██║░░░       ║')
    print('║       ██║░░░░░███████╗██████╔╝░╚═██╔═╝░╚██████╔╝██║██████╔╝██║░░██║██╗       ║')
    print('║       ╚═╝░░░░░╚══════╝╚═════╝░░░░╚═╝░░░░╚═════╝░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝       ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║              █▄░█ ▄▀█ █▀█   █ █▄░█ █▀▀ █▀█ █▀█ █▀▄▀█ ▄▀█ █▀▄ ▄▀█             ║')
    print('║              █░▀█ █▀█ █▄█   █ █░▀█ █▀░ █▄█ █▀▄ █░▀░█ █▀█ █▄▀ █▀█             ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                     █ █▄░█ █▀▀ █▀█ █▀█ █▀▄▀█ ▄▀█ █▀▄ ▄▀█                     ║')
    print('║                  ▶  █ █░▀█ █▀░ █▄█ █▀▄ █░▀░█ █▀█ █▄▀ █▀█                     ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('╚══════════════════════════════════════════════════════════════════════════════╝')


def menuProcuraNInformada1():
    print('╔══════════════════════════════════════════════════════════════════════════════╗')
    print('║                                                                              ║')
    print('║  ░█████╗░██╗░░░░░░██████╗░░█████╗░██████╗░██╗████████╗███╗░░░███╗░█████╗░██╗ ║')
    print('║  ██╔══██╗██║░░░░░██╔════╝░██╔══██╗██╔══██╗██║╚══██╔══╝████╗░████║██╔══██╗╚═╝ ║')
    print('║  ███████║██║░░░░░██║░░██╗░██║░░██║██████╔╝██║░░░██║░░░██╔████╔██║██║░░██║░░░ ║')
    print('║  ██╔══██║██║░░░░░██║░░╚██╗██║░░██║██╔══██╗██║░░░██║░░░██║╚██╔╝██║██║░░██║░░░ ║')
    print('║  ██║░░██║███████╗╚██████╔╝╚█████╔╝██║░░██║██║░░░██║░░░██║░╚═╝░██║╚█████╔╝██╗ ║')
    print('║  ╚═╝░░╚═╝╚══════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝░╚════╝░╚═╝ ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                █▄▄ █▀█ █▀▀ ▄▀█ █▀▄ ▀█▀ █░█ ▄▄ █▀▀ █ █▀█ █▀ ▀█▀               ║')
    print('║             ▶  █▄█ █▀▄ ██▄ █▀█ █▄▀ ░█░ █▀█ ░░ █▀░ █ █▀▄ ▄█ ░█░               ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                    █▀▄ █▀▀ █▀█ ▀█▀ █░█ ▄▄ █▀▀ █ █▀█ █▀ ▀█▀                   ║')
    print('║                    █▄▀ ██▄ █▀▀ ░█░ █▀█ ░░ █▀░ █ █▀▄ ▄█ ░█░                   ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('╚══════════════════════════════════════════════════════════════════════════════╝')


def menuProcuraNInformada2():
    print('╔══════════════════════════════════════════════════════════════════════════════╗')
    print('║                                                                              ║')
    print('║  ░█████╗░██╗░░░░░░██████╗░░█████╗░██████╗░██╗████████╗███╗░░░███╗░█████╗░██╗ ║')
    print('║  ██╔══██╗██║░░░░░██╔════╝░██╔══██╗██╔══██╗██║╚══██╔══╝████╗░████║██╔══██╗╚═╝ ║')
    print('║  ███████║██║░░░░░██║░░██╗░██║░░██║██████╔╝██║░░░██║░░░██╔████╔██║██║░░██║░░░ ║')
    print('║  ██╔══██║██║░░░░░██║░░╚██╗██║░░██║██╔══██╗██║░░░██║░░░██║╚██╔╝██║██║░░██║░░░ ║')
    print('║  ██║░░██║███████╗╚██████╔╝╚█████╔╝██║░░██║██║░░░██║░░░██║░╚═╝░██║╚█████╔╝██╗ ║')
    print('║  ╚═╝░░╚═╝╚══════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝░╚════╝░╚═╝ ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                █▄▄ █▀█ █▀▀ ▄▀█ █▀▄ ▀█▀ █░█ ▄▄ █▀▀ █ █▀█ █▀ ▀█▀               ║')
    print('║                █▄█ █▀▄ ██▄ █▀█ █▄▀ ░█░ █▀█ ░░ █▀░ █ █▀▄ ▄█ ░█░               ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                    █▀▄ █▀▀ █▀█ ▀█▀ █░█ ▄▄ █▀▀ █ █▀█ █▀ ▀█▀                   ║')
    print('║                 ▶  █▄▀ ██▄ █▀▀ ░█░ █▀█ ░░ █▀░ █ █▀▄ ▄█ ░█░                   ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('╚══════════════════════════════════════════════════════════════════════════════╝')


def menuProcuraInformada1():
    print('╔══════════════════════════════════════════════════════════════════════════════╗')
    print('║                                                                              ║')
    print('║  ░█████╗░██╗░░░░░░██████╗░░█████╗░██████╗░██╗████████╗███╗░░░███╗░█████╗░██╗ ║')
    print('║  ██╔══██╗██║░░░░░██╔════╝░██╔══██╗██╔══██╗██║╚══██╔══╝████╗░████║██╔══██╗╚═╝ ║')
    print('║  ███████║██║░░░░░██║░░██╗░██║░░██║██████╔╝██║░░░██║░░░██╔████╔██║██║░░██║░░░ ║')
    print('║  ██╔══██║██║░░░░░██║░░╚██╗██║░░██║██╔══██╗██║░░░██║░░░██║╚██╔╝██║██║░░██║░░░ ║')
    print('║  ██║░░██║███████╗╚██████╔╝╚█████╔╝██║░░██║██║░░░██║░░░██║░╚═╝░██║╚█████╔╝██╗ ║')
    print('║  ╚═╝░░╚═╝╚══════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝░╚════╝░╚═╝ ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                            ▄▀█ ▄▄ █▀ ▀█▀ ▄▀█ █▀█                             ║')
    print('║                         ▶  █▀█ ░░ ▄█ ░█░ █▀█ █▀▄                             ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                           █▀▀ █▀█ █▀▀ █▀▀ █▀▄ █▄█                            ║')
    print('║                           █▄█ █▀▄ ██▄ ██▄ █▄▀ ░█░                            ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('╚══════════════════════════════════════════════════════════════════════════════╝')


def menuProcuraInformada2():
    print('╔══════════════════════════════════════════════════════════════════════════════╗')
    print('║                                                                              ║')
    print('║  ░█████╗░██╗░░░░░░██████╗░░█████╗░██████╗░██╗████████╗███╗░░░███╗░█████╗░██╗ ║')
    print('║  ██╔══██╗██║░░░░░██╔════╝░██╔══██╗██╔══██╗██║╚══██╔══╝████╗░████║██╔══██╗╚═╝ ║')
    print('║  ███████║██║░░░░░██║░░██╗░██║░░██║██████╔╝██║░░░██║░░░██╔████╔██║██║░░██║░░░ ║')
    print('║  ██╔══██║██║░░░░░██║░░╚██╗██║░░██║██╔══██╗██║░░░██║░░░██║╚██╔╝██║██║░░██║░░░ ║')
    print('║  ██║░░██║███████╗╚██████╔╝╚█████╔╝██║░░██║██║░░░██║░░░██║░╚═╝░██║╚█████╔╝██╗ ║')
    print('║  ╚═╝░░╚═╝╚══════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝░╚════╝░╚═╝ ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                            ▄▀█ ▄▄ █▀ ▀█▀ ▄▀█ █▀█                             ║')
    print('║                            █▀█ ░░ ▄█ ░█░ █▀█ █▀▄                             ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                           █▀▀ █▀█ █▀▀ █▀▀ █▀▄ █▄█                            ║')
    print('║                        ▶  █▄█ █▀▄ ██▄ ██▄ █▄▀ ░█░                            ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('╚══════════════════════════════════════════════════════════════════════════════╝')


# def menuNumeroJogadores():
#     print('╔══════════════════════════════════════════════════════════════════════════════╗')
#     print('║                                                                              ║')
#     print('║              ██╗░░░██╗███████╗░█████╗░████████╗░█████╗░██████╗░              ║')
#     print('║              ██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗              ║')
#     print('║              ╚██╗░██╔╝█████╗░░██║░░╚═╝░░░██║░░░██║░░██║██████╔╝              ║')
#     print('║              ░╚████╔╝░██╔══╝░░██║░░██╗░░░██║░░░██║░░██║██╔══██╗              ║')
#     print('║              ░░╚██╔╝░░███████╗╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║              ║')
#     print('║              ░░░╚═╝░░░╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝              ║')
#     print('║                       ██████╗░░█████╗░░█████╗░███████╗                       ║')
#     print('║                       ██╔══██╗██╔══██╗██╔══██╗██╔════╝                       ║')
#     print('║                       ██████╔╝███████║██║░░╚═╝█████╗░░                       ║')
#     print('║                       ██╔══██╗██╔══██║██║░░██╗██╔══╝░░                       ║')
#     print('║                       ██║░░██║██║░░██║╚█████╔╝███████╗                       ║')
#     print('║                       ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚══════╝                       ║')
#     print('║                                                                              ║')
#     print('║                                                                              ║')
#     print('║                    ░░█ █▀█ █▀▀ ▄▀█ █▀▄ █▀█ █▀█ █▀▀ █▀ ▀                      ║')
#     print('║                    █▄█ █▄█ █▄█ █▀█ █▄▀ █▄█ █▀▄ ██▄ ▄█ ▄                      ║')
#     print('║                                                                              ║')
#     print('║                                                                              ║')
#     print('║                                ══ ══ ══ ══                                   ║')
#     print('║                                                                              ║')
#     print('╚══════════════════════════════════════════════════════════════════════════════╝')


def menuMapas1():
    print('╔══════════════════════════════════════════════════════════════════════════════╗')
    print('║                                                                              ║')
    print('║              ██╗░░░██╗███████╗░█████╗░████████╗░█████╗░██████╗░              ║')
    print('║              ██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗              ║')
    print('║              ╚██╗░██╔╝█████╗░░██║░░╚═╝░░░██║░░░██║░░██║██████╔╝              ║')
    print('║              ░╚████╔╝░██╔══╝░░██║░░██╗░░░██║░░░██║░░██║██╔══██╗              ║')
    print('║              ░░╚██╔╝░░███████╗╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║              ║')
    print('║              ░░░╚═╝░░░╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝              ║')
    print('║                       ██████╗░░█████╗░░█████╗░███████╗                       ║')
    print('║                       ██╔══██╗██╔══██╗██╔══██╗██╔════╝                       ║')
    print('║                       ██████╔╝███████║██║░░╚═╝█████╗░░                       ║')
    print('║                       ██╔══██╗██╔══██║██║░░██╗██╔══╝░░                       ║')
    print('║                       ██║░░██║██║░░██║╚█████╔╝███████╗                       ║')
    print('║                       ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚══════╝                       ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                             █▀▄▀█ ▄▀█ █▀█ ▄▀█ ▄█                             ║')
    print('║                          ▶  █░▀░█ █▀█ █▀▀ █▀█ ░█                             ║')
    print('║                                                                              ║')
    print('║                             █▀▄▀█ ▄▀█ █▀█ ▄▀█ ▀█                             ║')
    print('║                             █░▀░█ █▀█ █▀▀ █▀█ █▄                             ║')
    print('║                                                                              ║')
    print('╚══════════════════════════════════════════════════════════════════════════════╝')


def menuMapas2():
    print('╔══════════════════════════════════════════════════════════════════════════════╗')
    print('║                                                                              ║')
    print('║              ██╗░░░██╗███████╗░█████╗░████████╗░█████╗░██████╗░              ║')
    print('║              ██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗              ║')
    print('║              ╚██╗░██╔╝█████╗░░██║░░╚═╝░░░██║░░░██║░░██║██████╔╝              ║')
    print('║              ░╚████╔╝░██╔══╝░░██║░░██╗░░░██║░░░██║░░██║██╔══██╗              ║')
    print('║              ░░╚██╔╝░░███████╗╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║              ║')
    print('║              ░░░╚═╝░░░╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝              ║')
    print('║                       ██████╗░░█████╗░░█████╗░███████╗                       ║')
    print('║                       ██╔══██╗██╔══██╗██╔══██╗██╔════╝                       ║')
    print('║                       ██████╔╝███████║██║░░╚═╝█████╗░░                       ║')
    print('║                       ██╔══██╗██╔══██║██║░░██╗██╔══╝░░                       ║')
    print('║                       ██║░░██║██║░░██║╚█████╔╝███████╗                       ║')
    print('║                       ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚══════╝                       ║')
    print('║                                                                              ║')
    print('║                                                                              ║')
    print('║                             █▀▄▀█ ▄▀█ █▀█ ▄▀█ ▄█                             ║')
    print('║                             █░▀░█ █▀█ █▀▀ █▀█ ░█                             ║')
    print('║                                                                              ║')
    print('║                             █▀▄▀█ ▄▀█ █▀█ ▄▀█ ▀█                             ║')
    print('║                          ▶  █░▀░█ █▀█ █▀▀ █▀█ █▄                             ║')
    print('║                                                                              ║')
    print('╚══════════════════════════════════════════════════════════════════════════════╝')


opt = 1
menu1()
escolhas = []

while True:
    key = keyboard.read_key()

    if key == keyboard.KEY_UP:
        if opt == 2:
            sleep(0.15)
            clear()
            menu1()
            opt = 1
        elif opt == 4:
            sleep(0.15)
            clear()
            menuPesquisa1()
            opt = 3
        elif opt == 6:
            sleep(0.15)
            clear()
            menuProcuraNInformada1()
            opt = 5
        elif opt == 8:
            sleep(0.15)
            clear()
            menuProcuraInformada1()
            opt = 7
        elif opt == 11:
            sleep(0.15)
            clear()
            menuMapas1()
            opt = 10
    if key == keyboard.KEY_DOWN:
        if opt == 1:
            sleep(0.15)
            clear()
            menu2()
            opt = 2
        elif opt == 3:
            sleep(0.15)
            clear()
            menuPesquisa2()
            opt = 4
        elif opt == 5:
            sleep(0.15)
            clear()
            menuProcuraNInformada2()
            opt = 6
        elif opt == 7:
            sleep(0.15)
            clear()
            menuProcuraInformada2()
            opt = 8
        elif opt == 10:
            sleep(0.15)
            clear()
            menuMapas2()
            opt = 11
    if key == "enter":
        if opt == 1:
            escolhas.append(opt)
            sleep(0.15)
            clear()
            menuPesquisa1()
            opt = 3
        elif opt == 2:
            escolhas.append(opt)
            sleep(0.15)
            clear()
            menuPesquisa1()
            opt = 3
        elif opt == 3:
            escolhas.append(opt)
            sleep(0.15)
            clear()
            menuProcuraNInformada1()
            opt = 5
        elif opt == 4:
            escolhas.append(opt)
            sleep(0.15)
            clear()
            menuProcuraInformada1()
            opt = 7
        elif opt == 5:
            escolhas.append(opt)
            sleep(0.15)
            clear()
            menuMapas1()
            opt = 10
        elif opt == 6:
            escolhas.append(opt)
            sleep(0.15)
            clear()
            menuMapas1()
            opt = 10
        elif opt == 7:
            escolhas.append(opt)
            sleep(0.15)
            clear()
            menuMapas1()
            opt = 10
        elif opt == 8:
            escolhas.append(opt)
            sleep(0.15)
            clear()
            menuMapas1()
            opt = 10
        elif opt == 10:
            # se opt == 10, selecionamos o mapa1
            sleep(0.15)
            clear()
            ProjetoIA.parseMapa("mapa.txt")
            if escolhas.__contains__(1):
                # modo de jogo singleplayer
                if escolhas.__contains__(5):
                    ProjetoIA.setUpGraphNotInformed()
                    print(grafo.Graph.procura_BFS(ProjetoIA.getGrafo(), ProjetoIA.getStart(), ProjetoIA.getEnd()))
                    ProjetoIA.desenhaMapa(grafo.Graph.procura_BFS(ProjetoIA.getGrafo(), ProjetoIA.getStart(), ProjetoIA.getEnd()), "mapa.txt")
                    break
                elif escolhas.__contains__(6):
                    ProjetoIA.setUpGraphNotInformed()
                    print(grafo.Graph.procura_DFS(ProjetoIA.getGrafo(), ProjetoIA.getStart(), ProjetoIA.getEnd(), path=[], visited=set()))
                    ProjetoIA.desenhaMapa(grafo.Graph.procura_DFS(ProjetoIA.getGrafo(), ProjetoIA.getStart(), ProjetoIA.getEnd(), path=[], visited=set()), "mapa.txt")
                    break
                elif escolhas.__contains__(7):
                    ProjetoIA.setUpGraphInformed()
                    ProjetoIA.setUpHeuristica()
                    #print(grafo.Graph.procura_aStar(ProjetoIA.getGrafo(), ProjetoIA.getStart(), ProjetoIA.getEnd(), ProjetoIA.getWall()))
                    path, cost = ProjetoIA.getGrafo().procura_aStar(ProjetoIA.getStart(), ProjetoIA.getEnd(), ProjetoIA.getWall(), (0, 0))
                    current = 0
                    pathFinal = []
                    while current + 1 < len(path):
                        res, cost = ProjetoIA.getGrafo().a_star(path[current], [path[current + 1]], ProjetoIA.getWall())
                        if res[0] in pathFinal:
                            if len(res) > 1 and res[0] == res[1]:
                                res.pop(0)
                            res.pop(0)
                        pathFinal = pathFinal + res  # list(set(res) - set(pathFinal))
                        current += 1
                    print((pathFinal, ProjetoIA.getGrafo().calcula_custo(pathFinal)))
                    ProjetoIA.desenhaMapa((path,cost), "mapa.txt")
                    break
                elif escolhas.__contains__(8):
                    ProjetoIA.setUpGraphInformed()
                    ProjetoIA.setUpHeuristica()
                    #print(grafo.Graph.greedy(ProjetoIA.getGrafo(), ProjetoIA.getStart(), ProjetoIA.getEnd(), ProjetoIA.getWall()))
                    path, cost = ProjetoIA.getGrafo().greedy(ProjetoIA.getStart(), ProjetoIA.getEnd(), ProjetoIA.getWall(), (0, 0))
                    current = 0
                    pathFinal = []
                    while current + 1 < len(path):
                        res, cost = ProjetoIA.getGrafo().a_star(path[current], [path[current + 1]], ProjetoIA.getWall())
                        if res[0] in pathFinal:
                            if len(res) > 1 and res[0] == res[1]:
                                res.pop(0)
                            res.pop(0)
                        pathFinal = pathFinal + res  # list(set(res) - set(pathFinal))
                        current += 1
                    print((pathFinal, ProjetoIA.getGrafo().calcula_custo(pathFinal)))
                    ProjetoIA.desenhaMapa((path,cost), "mapa.txt")
                    break
            elif escolhas.__contains__(2):
                # modo de jogo multiplayer
                #jogadores =  input('Insere número de jogadores: ')
                jogadores = 3
                if escolhas.__contains__(5):
                    ProjetoIA.setUpGraphNotInformed()
                    ProjetoIA.multiplayerBFS(jogadores, "mapa.txt")
                    break
                elif escolhas.__contains__(6):
                    ProjetoIA.setUpGraphNotInformed()
                    break
                elif escolhas.__contains__(7):
                    ProjetoIA.setUpGraphInformed()
                    ProjetoIA.setUpHeuristica()
                    ProjetoIA.multiplayerASTAR(2, "mapa.txt")
                    break
                elif escolhas.__contains__(8):
                    ProjetoIA.setUpGraphInformed()
                    ProjetoIA.setUpHeuristica()
                    break
        elif opt == 11:
            # se opt == 11, selecionamos o mapa2
            sleep(0.15)
            clear()
            ProjetoIA.parseMapa("gigaMap.txt")
            if escolhas.__contains__(1):
                # modo de jogo singleplayer
                if escolhas.__contains__(5):
                    ProjetoIA.setUpGraphNotInformed()
                    print(grafo.Graph.procura_BFS(ProjetoIA.getGrafo(), ProjetoIA.getStart(), ProjetoIA.getEnd()))
                    ProjetoIA.desenhaMapa(grafo.Graph.procura_BFS(ProjetoIA.getGrafo(), ProjetoIA.getStart(), ProjetoIA.getEnd()), "gigaMap.txt")
                    break
                elif escolhas.__contains__(6):
                    ProjetoIA.setUpGraphNotInformed()
                    print(grafo.Graph.procura_DFS(ProjetoIA.getGrafo(), ProjetoIA.getStart(), ProjetoIA.getEnd(), path=[], visited=set()))
                    ProjetoIA.desenhaMapa(grafo.Graph.procura_DFS(ProjetoIA.getGrafo(), ProjetoIA.getStart(), ProjetoIA.getEnd(), path=[], visited=set()), "gigaMap.txt")
                    break
                elif escolhas.__contains__(7):
                    ProjetoIA.setUpGraphInformed()
                    ProjetoIA.setUpHeuristica()
                    # print(grafo.Graph.procura_aStar(g, start, end, wall))
                    path, cost = ProjetoIA.getGrafo().procura_aStar(ProjetoIA.getStart(), ProjetoIA.getEnd(), ProjetoIA.getWall(), (0, 0))
                    current = 0
                    pathFinal = []
                    while current + 1 < len(path):
                        res, cost = ProjetoIA.getGrafo().a_star(path[current], [path[current + 1]], ProjetoIA.getWall())
                        if res[0] in pathFinal:
                            if len(res) > 1 and res[0] == res[1]:
                                res.pop(0)
                            res.pop(0)
                        pathFinal = pathFinal + res  # list(set(res) - set(pathFinal))
                        current += 1
                    print((pathFinal, ProjetoIA.getGrafo().calcula_custo(pathFinal)))
                    ProjetoIA.desenhaMapa((path, cost), "gigaMap.txt")
                    break
                elif escolhas.__contains__(8):
                    ProjetoIA.setUpGraphInformed()
                    ProjetoIA.setUpHeuristica()
                    # print(grafo.Graph.greedy(g, start, end, wall))
                    path, cost = ProjetoIA.getGrafo().greedy(ProjetoIA.getStart(), ProjetoIA.getEnd(), ProjetoIA.getWall(), (0, 0))
                    current = 0
                    pathFinal = []
                    while current + 1 < len(path):
                        res, cost = ProjetoIA.getGrafo().a_star(path[current], [path[current + 1]], ProjetoIA.getWall())
                        if res[0] in pathFinal:
                            if len(res) > 1 and res[0] == res[1]:
                                res.pop(0)
                            res.pop(0)
                        pathFinal = pathFinal + res  # list(set(res) - set(pathFinal))
                        current += 1
                    print((pathFinal, ProjetoIA.getGrafo().calcula_custo(pathFinal)))
                    ProjetoIA.desenhaMapa((path, cost), "gigaMap.txt")
                    break
            elif escolhas.__contains__(2):
                # modo de jogo multiplayer
                #jogadores = input('Insere número de jogadores: ')
                jogadores = 3
                if escolhas.__contains__(5):
                    ProjetoIA.setUpGraphNotInformed()
                    ProjetoIA.multiplayerBFS(jogadores, "gigaMap.txt")
                    break
                elif escolhas.__contains__(6):
                    ProjetoIA.setUpGraphNotInformed()
                    ProjetoIA.multiplayerDFS(jogadores, "gigaMap.txt")
                    break
                elif escolhas.__contains__(7):
                    ProjetoIA.setUpGraphInformed()
                    ProjetoIA.setUpHeuristica()
                    ProjetoIA.multiplayerASTAR(1, "gigaMap.txt")
                    break
                elif escolhas.__contains__(8):
                    ProjetoIA.setUpGraphInformed()
                    ProjetoIA.setUpHeuristica()
                    break

    # opt1 -> opcao singleplayer
    # opt2 -> opcao multiplayer
    # opt3 -> opcao nao informada
    # opt4 -> opcao informada
    # opt5 -> opcao BFS
    # opt6 -> opcao DFS
    # opt7 -> opcao A-star
    # opt8 -> opcao Greedy
    # opt9 -> opcao jogadores
    # opt10 -> opcao mapa1
    # opt11 -> opcao mapa2

    # if keyboard.read_key() == "esc":
    #     if opt == 1:
    #         sleep(0.05)
    #         clear()
    #         print('Exiting!')
    #         break
    #     elif opt == 2:
    #         sleep(0.05)
    #         clear()
    #         print('Exiting!')
    #         break
    #     elif opt == 3:
    #         sleep(0.05)
    #         clear()
    #         menu1()
    #         opt = 1
    #     elif opt == 4:
    #         sleep(0.05)
    #         clear()
    #         menu1()
    #         opt = 1
    #     elif opt == 5:
    #         sleep(0.05)
    #         clear()
    #         menuPesquisa1()
    #         opt = 3
    #     elif opt == 6:
    #         sleep(0.05)
    #         clear()
    #         menuPesquisa1()
    #         opt = 3
    #     elif opt == 7:
    #         sleep(0.05)
    #         clear()
    #         menuPesquisa1()
    #         opt = 3
    #     elif opt == 8:
    #         sleep(0.05)
    #         clear()
    #         menuPesquisa1()
    #         opt = 3
    #     elif opt == 9:
    #         sleep(0.05)
    #         clear()
    #         menu1()
    #         opt = 1
    #     elif opt == 10:
    #         sleep(0.05)
    #         clear()
    #         menuPesquisa1()
    #         opt = 3
    #     elif opt == 11:
    #         sleep(0.05)
    #         clear()
    #         menuPesquisa1()
    #         opt = 3