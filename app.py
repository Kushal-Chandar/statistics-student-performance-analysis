import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import dabl

data = pd.read_csv("StudentsPerformance.csv")

plt.rcParams["figure.figsize"] = (15, 9)
plt.style.use("tableau-colorblind10")

sns.countplot(data["math score"], palette="BuPu")
plt.title("Comparison of math scores", fontweight=30, fontsize=20)
plt.xlabel("score")
plt.ylabel("count")
plt.xticks(rotation=90)
plt.show()
