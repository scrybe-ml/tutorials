import matplotlib.pyplot as plt
import seaborn as sns


def plot_correlations(data, target=None, limit=50, figsize=(12, 10), **kwargs):
    """
    This function  plots the correlation matrix of a dataframe
    If a target feature is provided, it will display only a certain amount of features, the ones correlated the most
    with the target. The number of features displayed is controlled by the parameter limit
    """

    corr = data.corr()
    cor_target = None
    if target:
        corr['abs'] = abs(corr[target])
        cor_target = corr.sort_values(by='abs', ascending=False)[target]
        cor_target = cor_target[:limit]
        del corr['abs']
        corr = corr.loc[cor_target.index, cor_target.index]
    plt.figure(figsize=figsize)
    ax = sns.heatmap(corr, cmap='RdBu_r', **kwargs)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    return cor_target


def plot_distribution(data, column, bins=50, correlation=None):
    """
    Plots a histogram of a given column
    If a Pandas Series is provided with the correlation values, it will be displayed in the title.
    """

    plt.figure(figsize=(12, 8))
    data[column].hist(bins=bins)
    if not correlation is None:
        value = correlation[column]
        column = column + f' - {round(value, 2)}'
    plt.title(f'Distribution of {column}', fontsize=18)
    plt.grid(False)


def plot_bivariate(data, x, y, hue=None, **kwargs):
    """
    Scatterplot of the feature x vs the feature y with the possibility of adding a hue
    """

    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=data, x=x, y=y, hue=hue, **kwargs)
    if hue:
        plt.title(f'{x} vs {y}, by {hue}', fontsize=18)
    else:
        plt.title(f'{x} vs {y}', fontsize=18)


def plot_target_corr(data, target, cols, x_estimator=None):
    """
    Scatterplot + linear regression of a list of columns against the target.
    A correlation matrix is also printed.
    It is possible to pass an estimator.
    """

    print(data[cols + [target]].corr())
    num = len(cols)
    rows = int(num / 2) + (num % 2 > 0)
    cols = list(cols)
    y = data[target]
    fig, ax = plt.subplots(rows, 2, figsize=(12, 5 * (rows)))
    i = 0
    j = 0
    for feat in cols:
        x = data[feat]
        if (rows > 1):
            sns.regplot(x=x, y=y, ax=ax[i][j], x_estimator=x_estimator)
            j = (j + 1) % 2
            i = i + 1 - j
        else:
            sns.regplot(x=x, y=y, ax=ax[i], x_estimator=x_estimator)
            i = i + 1

