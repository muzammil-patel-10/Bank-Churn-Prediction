# LIME SECTION
import sklearn
import sklearn.datasets
import sklearn.ensemble
import lime
import lime.lime_tabular
import pandas as pd
import joblib
from pathlib import Path
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
import plotly.express as px



# load model
filename = 'models/nate_random_forest.sav'
rf_grid = joblib.load(filename)   

# read the train file 
X_train_path = 'Resources/X_train.csv'
X_train = pd.read_csv(X_train_path)
X_train = X_train.drop('Unnamed: 0', axis=1)
# print(X_train)


def prob_lime_plot(custd_lime):

    df = pd.DataFrame(custd_lime)
    print(df)
 
    zero = list(rf_grid.predict_proba([df.values[0]]))[0][0]
    one = list(rf_grid.predict_proba([df.values[0]]))[0][1]

    data = pd.DataFrame({'class': ['0', '1'],
                'prob': [zero*100, one*100],
                "Percentage":[zero, one]
                })
    
    fig = px.bar(data, x=data['class'], y=data['prob'], color= ['Purple(Stay)', 'Red(Exit)'],text=data['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))


    if os.path.exists("./static/img/plot_imgs/prob_lime.jpeg"):
         os.remove("./static/img/plot_imgs/prob_lime.jpeg")
         fig = px.bar(data, x=data['class'], y=data['prob'],
                      color=['Purple(Stay)', 'Red(Exit)'],
                      text=data['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        #  fig.update_layout({
        #         'plot_bgcolor': 'rgba(0,0,0,0)',
        #         'paper_bgcolor': 'rgba(0,0,0,0)'
        #     })
         fig.write_image("./static/img/plot_imgs/prob_lime.jpeg")
    else:
        fig = px.bar(data, x=data['class'], y=data['prob'],
                     color=['Purple(Stay)', 'Red(Exit)'],
                     text=data['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        # fig.update_layout({
        #         'plot_bgcolor': 'rgba(0,0,0,0)',
        #         'paper_bgcolor': 'rgba(0,0,0,0)'
        #     })
        fig.write_image("./static/img/plot_imgs/prob_lime.jpeg")

    prob_lime = "./static/img/plot_imgs/prob_lime.jpeg"

    return prob_lime