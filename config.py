from os import getenv

ENV = False

if ENV:
    TOKEN1 = getenv("TOKEN1")
    TOKEN2 = getenv("TOKEN2")
    TOKEN3 = getenv("TOKEN3")
    TOKEN4 = getenv("TOKEN4")
    TOKEN5 = getenv("TOKEN5")
    SUDO = list(map(int, getenv("SUDO").split(" ")))
else:
    TOKEN1 = "7005246721:AAFPGY9-BsuZR1a6noaRJyQBqrrFwZTEMyI"
    TOKEN2 = "7005246721:AAFPGY9-BsuZR1a6noaRJyQBqrrFwZTEMyI"
    TOKEN3 = ""
    TOKEN4 = ""
    TOKEN5 = ""
    SUDO = []
