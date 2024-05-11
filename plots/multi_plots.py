import seaborn as sns
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import plotly.express as px

def scatterplot(df, col_1, col_2):
    if os.path.exists("./static/img/plot_imgs/scatterplot.jpeg"):
        os.remove("./static/img/plot_imgs/scatterplot.jpeg")
        fig = px.scatter(df, x=col_1, y=col_2)
        fig.write_image("./static/img/plot_imgs/scatterplot.jpeg")
    else:
        fig = px.scatter(df, x=col_1, y=col_2)
        fig.write_image("./static/img/plot_imgs/scatterplot.jpeg")



def lineplot(df, col_1, col_2):
    if os.path.exists("./static/img/plot_imgs/lineplot.jpeg"):
        os.remove("./static/img/plot_imgs/lineplot.jpeg")
        fig = px.line(df, x=col_1, y=col_2)
        fig.write_image("./static/img/plot_imgs/lineplot.jpeg")
    else:
        fig = px.line(df, x=col_1, y=col_2)
        fig.write_image("./static/img/plot_imgs/lineplot.jpeg")


def boxplot(df, col_1):
    if os.path.exists("./static/img/plot_imgs/boxplot.jpeg"):
        os.remove("./static/img/plot_imgs/boxplot.jpeg")
        fig = px.box(df, x=col_1)
        fig.write_image("./static/img/plot_imgs/boxplot.jpeg")
    else:
        fig = px.box(df, x=col_1)
        fig.write_image("./static/img/plot_imgs/boxplot.jpeg")

    # return "./static/img/plot_imgs/boxplot.jpeg"


def histplot(df, col_1):
    if os.path.exists("./static/img/plot_imgs/histogram.jpeg"):
        os.remove("./static/img/plot_imgs/histogram.jpeg")
        print("d")
        fig = px.histogram(df, x=col_1)
        fig.write_image("./static/img/plot_imgs/histogram.jpeg")
    else:
        fig = px.histogram(df, x=col_1)
        fig.write_image("./static/img/plot_imgs/histogram.jpeg")
    
    # return "./static/img/plot_imgs/histogram.jpeg"


# import plotly.express as px
# df = px.data.tips()
# fig = px.histogram(df, x="total_bill")
# fig.show()