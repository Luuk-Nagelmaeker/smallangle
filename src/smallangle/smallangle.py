import click
import numpy as np
from numpy import pi
import pandas as pd


@click.group()
def cmd_group():
    pass


@cmd_group.command()
@click.argument('number')
def sin(number):
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.argument('number')
def tan(number):
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    cmd_group()