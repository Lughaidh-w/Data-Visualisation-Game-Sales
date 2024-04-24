import matplotlib.pyplot as plt
import seaborn as sns


def basic_histo(df, col, colour="red", bins=20):
    sns.histplot(df[col], color=colour, bins=bins)

    plt.title(f"Distribution of {col} feature")
    plt.xlabel(col)
    plt.ylabel("Frequency")

    plt.show();



# probability plot, takes a series
def probability_plot(df, title="Probability Plot", colour="skyblue"):
    plt.figure(figsize=(10, 6))
    df.plot(kind='bar', color=colour)
    plt.title(title)
    plt.xlabel('Platform')
    plt.ylabel('Probability')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()


# index must be timeseries and dictionary of columns and colours
def timeseries_compare(df, dict, yaxis, title="Time-Series plot"):
    plt.figure(figsize=(10, 6))

    # create plots
    for key, value in dict.items():
        plt.plot(df.index, df[key], marker='o', linestyle='-', label=key, color=value)
        
    plt.title(title)
    plt.xlabel('Year of Release')
    plt.ylabel(yaxis)
    
    plt.xticks(df.index, rotation=45)
    plt.legend()
    
    #plt.gca().patch.set_facecolor('whitesmoke')
    
    plt.tight_layout()
    plt.show()


def platform_filtering(df, genre, list, output=False):
    df=df[df["Genre"]==genre]
    if output:
        print(f"{genre} Genre Overview\n")
        print(df.Platform_Category.value_counts())
    
    df_grouped = df.groupby("Platform_Category")[list].sum()
    #display(df_grouped)

    df_grouped["Platform"]=genre

    return df_grouped