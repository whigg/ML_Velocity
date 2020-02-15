# ML_Velocity
Flow Velocity Prediction using Machine Learning Algorithms (Supplementary to Publication)  
These Jupyter notebooks can be used to reproduce all the analysis presented in this paper


# Create the environment
conda env create -f environment.yml
To activate this newly create environment, use
conda activate ml_velocity

## Notebooks
01ML_Algorithms_for_Velocity.ipynb
    To run the ML algorithms
    Run this twice (with changing the full feature flag)

02_Feature_Selection_with_RFE.ipynb
    For recursive feature elimination

03_100_Runs_each_Algorithm.ipynb
    For Running each algorithm 100 times based on different partition (takes hours to days)


