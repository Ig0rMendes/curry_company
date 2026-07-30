import plotly.express as px

def bar_chart(df, x, y):
    return px.bar(df, x=x, y=y)


def pie_chart(df, values, names):
    return px.pie(df, values=values, names=names)


def scatter_chart(df, x, y, size, color):
    return px.scatter(df, x=x, y=y, size=size, color=color)


def line_chart(df, x, y):
    return px.line(df, x=x, y=y)