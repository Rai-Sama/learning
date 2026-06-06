import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _(np):
    a = np.array([1, 2, 3])

    b = np.array([[10], [20], [30]])

    #b = np.array([[10, 20, 30]])
    return a, b


@app.cell
def _(b):
    print(b.shape)
    return


@app.cell
def _(a, b, np):
    print(np.shape(a+b))
    return


@app.cell
def _(a):
    a1 = a.reshape(-1, 1)
    return (a1,)


@app.cell
def _(a1):
    a1
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
