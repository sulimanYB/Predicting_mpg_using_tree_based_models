import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_features_importance(importance, col_names, title):
    """
    This function plots features importance using horizontal bars.
    Inputs:
        - importance: An numpy.ndarray of size (n,) where n is the number of features.
        - col_names: A list of the features names
        - title: The graph title
    """

    importances = pd.Series(data=importance, index= col_names)

    plt.grid(color='k', linestyle='-', linewidth=0.1)
    sns.barplot(y=col_names, 
                x=importances.sort_values(ascending=False), 
                color='red',
                alpha = 0.9, 
                orient='h')

    plt.title(title, fontsize=16)
    plt.xlabel('Importance')
    plt.ylabel('Feature Name')
    sns.despine(left=True, bottom=True)
    plt.show()