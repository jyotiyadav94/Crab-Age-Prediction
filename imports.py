#main libraries
import os
import numpy as np
import pandas as pd
import warnings

#visualization libraries
import plotly 
import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px
from plotly.offline import iplot, init_notebook_mode
from sklearn.impute import SimpleImputer
#import cufflinks as cf

#machine learning libraries:
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_validate, train_test_split, KFold, cross_val_score
from sklearn.preprocessing  import StandardScaler, LabelEncoder, RobustScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import ElasticNet, Lasso,  BayesianRidge, LassoLarsIC
from sklearn.kernel_ridge import KernelRidge
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error as mae 

# Instantiate BayesianRidge without the 'normalize' argument
bayesian_ridge = BayesianRidge()

# You can go offline on demand by using
#cf.go_offline() 

# initiate notebook for offline plot
#init_notebook_mode(connected=False)         

# set some display options:
colors = px.colors.qualitative.Prism
pio.templates.default = "plotly_white"

# see our files:
# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

#warnings.filterwarnings('ignore')
#print("Warnings were ignored")