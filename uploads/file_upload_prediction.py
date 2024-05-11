import pandas as pd
import random
import joblib
from recommend.recommend_suggest import recommendations_fun


def file_upload_pred(file_name, recommendations_list, model_name=None):
    file = f'./uploads/{file_name}'
    model = model_name
    print(type(file))
    print(f"============{file}==================")
    df = pd.read_csv(file)
    print(df)
    print(df.keys())
    # df = df.drop("Unnamed: 0", axis=True)
    df['Geography'] = df['Geography'].replace(['France', 'Spain', 'Germany'],[0, 1, 2])
    df['Gender'] = df['Gender'].replace(['Female', 'Male'],[0, 1])
    prediction = model.predict(df)
    print(prediction)
    r1_list = []
    r2_list = []

    for i in range(len(df)):
        r1, r2 = recommendations_fun(recommendations_list)
        r1_list.append(r1)
        r2_list.append(r2)
     
    df_new = df.copy(deep=True)
    df_new["prediction"] = prediction
    df_new["recommendations_1"] = r1_list
    df_new["recommendations_2"] = r2_list
    df_new['Geography'] = df_new['Geography'].replace([0, 1, 2],['France', 'Spain', 'Germany'])
    df_new['Gender'] = df_new['Gender'].replace([0, 1],['Female', 'Male'])
    df_new['prediction'] = df_new['prediction'].replace([0, 1],['Stay', 'Exit'])

    for i in range(len(df_new)):
        is_true = df_new['prediction'][i] == 'Stay'
        print(i,is_true)
        if is_true == True:
            df_new["recommendations_1"][i] = "No recommendations"
            df_new["recommendations_2"][i] = "No recommendations"

    

    df_new.to_csv("./uploads/predicted_file.csv")
    
    return "predicted_file.csv"

# ff ="X_test.csv"
# file_upload_pred(ff)