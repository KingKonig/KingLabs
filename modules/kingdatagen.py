import pandas as pd


def express_gen(expression, upper_lim, lower_lim):
    df = pd.DataFrame
    for x in range(int(lower_lim), int(upper_lim)):
        y = eval(expression)
        print(f"({x}, {y})")


if __name__ == "__main__":
    express_gen(input("Input an expression: "), input("Upper limit: "), input("Lower limit: "))
