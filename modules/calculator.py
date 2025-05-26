from sympy import sympify


def calci():
    print("Entering calculator mode. (type \"exit\" to quit)..")
    while True:
        expr = input("calci> ")
        if expr.lower() in ("exit","quit"):
            print("exiting calculator...")
            break
        try :
            result = sympify(expr)
            print(result)
        except Exception as e:
            print("Error:", e)
