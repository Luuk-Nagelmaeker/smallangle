import click
import numpy as np
from numpy import pi
import pandas as pd


@click.group()
def cmd_group():
    pass


@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,)
def sin(n):
    """calculate the sin of N numbers

    the N numbers are equidistant between 0 and 2 pi

    default = 10
    """
    x = np.linspace(0, 2 * pi, int(n))
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "-n",
    default=10,)
def tan(n):
    """calculate the tan of N numbers

    the N numbers are equidistant between 0 and 2 pi

    default = 10
    """
    x = np.linspace(0, 2 * pi, int(n))
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    cmd_group()