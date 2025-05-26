from pint import UnitRegistry


def convert(quantity , From , To):
    ureg = UnitRegistry()
    qt = quantity * getattr(ureg,From)
    qtTo = qt.to( getattr(ureg,To))
    return qtTo

def get_converting():
    print("Entering converter mode. (type \"exit\" to quit)..")
    while True:
        expr = input("convi> ")
        exprList = expr.split()
        if expr.lower() in ("exit","quit"):
            print("exiting converter...")
            break
        try :
            result = convert(int(exprList[0]),exprList[1],exprList[3],)
            print(result)
        except Exception as e:
            print("Error:", e)
