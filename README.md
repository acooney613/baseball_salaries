## Baseball Salary Predictor (2010 - 2023)


### Project Overview

This repo contains data and code to predict MLB player salary using machine learning methods such as Neural Networks and Ensemble methods. This repo contains several important files in my data analysis, model tuning, and model model analysis process. The Data folder contains the code to clean and merge the data into the final dataset called "baseball.csv". The models_and_pca.ipynb file is a jupyter notebook containing EDA and ensemble models I fit on the data. The dnn.ipynb file is a jupyter notebook containing the model training and fitting process used in the creation of the optimal model, a DNN. The optimal model is stored in the best_model folder. The shap.ipynb file contains a SHAP analysis of the model to determine key features as I continue to explore this data. 

### Data
Note: The data was sourced from [baseball-reference.com](https://www.baseball-reference.com/)

There are several folders that contain the data gathered, each with code within to clean, merge, and feature engineer the data into the final dataset called baseball.csv found [here](https://github.com/acooney613/baseball_salaries/tree/main/data)

**Baseball contains:** 
- **Salary:** Target
- **Tm:** Team player plays for (If more than 1 in a season then MULTIPLE)
- **Lg:** American (AL), National (NL), MLB (If 2 or more)
- **Fld%:** Fielding percentage
- **Rdrs:** Defensive runs saved above average
- **Season:** Year season took place
- **RAA:** Runs Above Average
- **WAA:** Wins Above Average
- **RAR:** Runs Above Replacement
- **WAR:** Wins Above Replacement
- **Acquired:** How player was acquired
- **BA:** Batting Average
- **OBP:** On Base Percentage
- **SLG:** Slugging (1B + 2Bx2 + 3Bx3 + HRx4)/AB
- **OPS:** (H + BB + HBP) / PA
- **OPS+:** 100 * ((OBP / lgOBP) + (SLG / lgSLG) -1)
- **Bat:** Handedness of batter
- **Pos_C:** Is Catcher
- **Pos_1B:** Is First Base
- **Pos_2B:** Is Second Base
- **Pos_3B:** Is Third Base
- **Pos_SS:** Is Short-Stop
- **Pos_OF:** Is Outfield
- **Num_Pos:** Number of positions played
- **R/AB:** Runs per at-bat
- **2B/AB:** Doubles per at-bat
- **3B/AB:** Triples per at-bat
- **HR/AB:** Home runs per at-bat
- **RBI/AB:** Runs Batted In per at-bat
- **BB/PA:** Walks per plate appearance
- **SB - CS:** Stolen Bases - Caught Stealing
- **BB - SO:** Walks - Strikeouts
- **E/Def-Inn:** Errors per Defensive Innings Played
- **DP/Def-Inn:** Double Plays per Defensive Innings Played


### Files

- **[dnn.ipynb](https://github.com/acooney613/baseball_salaries/blob/main/dnn.ipynb):** file containing for neural network
- **[models_and_pca.ipynb](https://github.com/acooney613/baseball_salaries/blob/main/models_and_pca.ipynb):** file containing all other models 
- **[best_model](https://github.com/acooney613/baseball_salaries/tree/main/best_model):** folder containing the saved neural network
- **[shap.ipynb](https://github.com/acooney613/baseball_salaries/blob/main/shap.ipynb):** code to run shap analysis on the best model
- **[salary_clean.ipynb](https://github.com/acooney613/baseball_salaries/blob/main/data/salary/salary_clean.ipynb):** code to merge salary data
- **[field_clean.ipynb](https://github.com/acooney613/baseball_salaries/blob/main/data/field/field_clean.ipynb):** code to merge defensive data
- **[batter_clean.ipynb](https://github.com/acooney613/baseball_salaries/blob/main/data/batter/batter_clean.ipynb):** code to merge batter data
- **[feature_engineer_and_merge.py](https://github.com/acooney613/baseball_salaries/blob/main/data/feature_engineer_and_merge.py):** code to merge each of the three datasets and feature engineer to prepare for model fit
