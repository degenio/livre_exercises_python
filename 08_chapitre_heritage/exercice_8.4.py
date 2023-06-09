class Niveau(Enum):
    FRESHMAN=1
    SOPHOMORE=2
    JUNIOR=3
    SENIOR=4
    GRADUATE=5

for niveau in Niveau:
    print(niveau.name, niveau.value)