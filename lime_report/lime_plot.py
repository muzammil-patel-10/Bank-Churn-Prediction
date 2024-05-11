# LIME SECTION
import sklearn
import sklearn.datasets
import sklearn.ensemble
import numpy as np
import lime
import lime.lime_tabular
import pandas as pd
import joblib
from pathlib import Path
import matplotlib.pyplot as plt
import os
plt.figure(figsize=(8, 8))

# load model
filename = 'models/nate_random_forest.sav'
rf_grid = joblib.load(filename)   

# read the train file 
X_train_path = 'Resources/X_train.csv'
X_train = pd.read_csv(X_train_path)
X_train = X_train.drop('Unnamed: 0', axis=1)
print(X_train)


def lime_plot(custd_lime):

    predict_fn_rf = lambda x: rf_grid.predict_proba(x).astype(float)

    # Line-up the feature names
    num_columns = X_train.select_dtypes(include='number').columns.tolist()
    print(num_columns)

    # Create the LIME Explainer
    explainer = lime.lime_tabular.LimeTabularExplainer(
        X_train.values,
        feature_names=num_columns,
        class_names=['0', '1'],
        kernel_width=3)
    df = pd.DataFrame(custd_lime)
    exp = explainer.explain_instance(df.values[0], 
                                     predict_fn_rf, 
                                     num_features=10)
   
    if os.path.exists("./static/img/plot_imgs/lime.jpeg"):
         os.remove("./static/img/plot_imgs/lime.jpeg")
         plt = exp.as_pyplot_figure()
         plt.savefig('./static/img/plot_imgs/lime.jpeg',bbox_inches='tight')
    else:
         plt = exp.as_pyplot_figure()
         plt.savefig('./static/img/plot_imgs/lime.jpeg',bbox_inches='tight')


    lime_path = "./static/img/plot_imgs/lime.jpeg"
    print(lime_path)

    return lime_path

