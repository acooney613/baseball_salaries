## Baseball Salary Predictor (2010 - 2023)


### Project Overview

This repo contains data and code to predict MLB player salary data using machine learning methods such as Neural Networks and Ensemble methods. 

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
