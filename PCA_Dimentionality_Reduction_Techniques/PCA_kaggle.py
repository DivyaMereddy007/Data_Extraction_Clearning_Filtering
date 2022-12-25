#https://www.kaggle.com/code/nirajvermafcb/principal-component-analysis-explained
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from subprocess import check_output
print(check_output(["ls", "../input"]).decode("utf8"))

# Any results you write to the current directory are saved as output.

#1)Let us first import all the necessary libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#2)Loading the dataset¶

df = pd.read_csv('../input/HR_comma_sep.csv')

columns_names=df.columns.tolist()
print("Columns names:")
print(columns_names)

df.shape

df.head()


df.corr()
