from datetime import datetime
from tools.crosstab.preprocessing import divide_chunks, categorization
from tools.crosstab.handlers import time_it, try_except
from tools.crosstab.Exceptions import *
from tools.crosstab.io import save_dataset
from tools.crosstab.meta_data import encode, load_meta_data

import numpy as np
import pandas
import pandas as pd

import os

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns

import matplotlib as mpl
import matplotlib.patches as mpatches

mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=7)
mpl.rc('ytick', labelsize=7)

gene_class = []
meta_labels = []
n_colors = 0

cmap = ""
meta_colors = []

labels = []
colors = []

handles = []


def pre_plot():
    global gene_class, meta_labels, n_colors, cmap, meta_colors

    gene_class, _, _ = load_meta_data()
    meta_labels = ["Not present"] + gene_class + ["Not found"]
    n_colors = len(meta_labels)

    # cmap = sns.cubehelix_palette(start=0, rot=n_colors, light=1, n_colors=n_colors)
    
    meta_colors = [
        '#FFFFFF',
        '#778899',
        '#0000FF',
        '#FA8072',
        '#FF0000',
        '#808000',
        '#00FFFF',
        '#DDA0DD',
        '#8A2BE2',
        '#8B008B',
        '#8D0000',
        '#FF00FF',
        '#008000',
        '#00FF00',
        '#66CDAA',
        '#4169E1',
        '#000080',
        '#0000CD',
        '#4B0082',
        '#FF1493',
        '#C71585',
        '#DB7093',
        '#FFC0CB',
        '#8B4513',
        '#B8860B',
        '#D2691E',
        '#F4A460',
        '#F5DEB3',
        '#008080',
        '#696969',
        '#00CED1',
        '#FFFF00',
        '#2F4F4F',
        '#5F9EA0',
        '#3C1A2B',
    ]
    
    cmap = ListedColormap(sns.color_palette(meta_colors).as_hex())


def generate_labels_colors(
        encodings_present: list
    ) -> None:

    global meta_labels, meta_colors, labels, colors

    encodings_present_unique = np.unique(encodings_present)
    encodings_freq = [encodings_present.count(each) for each in encodings_present_unique]

    labels = [f"{meta_labels[j]} - {encodings_freq[i]}" for i, j in enumerate(encodings_present_unique)]
    colors = [meta_colors[i] for i in encodings_present_unique]
    

def plot_settings():

    global colors, labels, handles

    plt.switch_backend("AGG")
    print(f"Length of labels: {len(labels)}")
    plt.figure(figsize=(15,10))
    plt.subplot(211)
    sns.set(font_scale=1)
    handles = [mpatches.Patch(color=color, label=label) for color, label in zip(colors, labels)]
    plt.legend(handles=handles, ncol=2, bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
        mode="expand", borderaxespad=0.)
        
    plt.yticks(
        rotation=45, 
        horizontalalignment='right', 
    )

def plot(
        dataset: pandas.core.frame,
        path: str
    ) -> None:
    global cmap, n_colors

    pre_plot()
    chunk_dataset, encodings_present = categorization(dataset)
    generate_labels_colors(encodings_present)
    plot_settings()

    sns.heatmap(chunk_dataset, vmin=0, vmax=n_colors, cmap=cmap, cbar=False )
    # y_ticks = chunk_dataset.reset_index().index.tolist()
    
    # sns.heatmap(chunk_dataset, vmin=0, yticklabels=y_ticks, vmax=n_colors, cmap=cmap, cbar=False )
    # plt.savefig(f"./static/results/images/complete_plot.png", bbox_inches = 'tight', dpi=300)
    plt.savefig(path, bbox_inches = 'tight', dpi=300)


@try_except
def plot_chunks(
        dataset: pandas.core.frame, 
        **kwargs
    ) -> None:
    global cmap, n_colors

    pre_plot()
    column_list = dataset.columns.tolist()
    chunks = list(divide_chunks(column_list, kwargs["n_gene_per_plot"]))

    for i in range(len(chunks)):
        chunk_dataset, encodings_present = categorization(dataset.loc[:, chunks[i]])
        
        generate_labels_colors(encodings_present)
        plot_settings()

        sns.heatmap(chunk_dataset, vmin=0, vmax=n_colors, cmap=cmap, cbar=False)

        plt.savefig(f"./static/results/images/heatmap-{i+1}.png", bbox_inches = 'tight')




range_plot_count = 0

@try_except
def plot_range(dataset, **kwargs):
    global cmap, n_colors, range_plot_count

    if len(kwargs) == 2:
        gene_range, genome_range = kwargs["gene"], kwargs["genome"]
        gene_list = dataset.columns[range(gene_range[0], gene_range[1]+1)].tolist()
        genome_list = dataset.index[range(genome_range[0], genome_range[1]+1)].tolist()

        chunk_dataset, encodings_present = categorization(
            dataset.loc[
                genome_list,
                gene_list
            ]
        )
    elif len(kwargs) == 1 and list(kwargs.keys())[0] == "gene":
        gene_range = kwargs["gene"]
        gene_list = dataset.columns[range(gene_range[0], gene_range[1]+1)].tolist()

        chunk_dataset, encodings_present = categorization(
            dataset.loc[ :,
                gene_list
            ]
        )
    elif len(kwargs) == 1 and list(kwargs.keys())[0] == "genome":
        genome_range = kwargs["genome"]
        genome_list = dataset.index[range(genome_range[0], genome_range[1]+1)].tolist()

        chunk_dataset, encodings_present = categorization(
            dataset.loc[ 
                genome_list, :
            ]
        )

    pre_plot()

    generate_labels_colors(encodings_present)
    plot_settings()

    sns.heatmap(chunk_dataset, vmin=0, vmax=n_colors, cmap=cmap, cbar=False)
    range_plot_count += 1
    plt.savefig(f"./static/results/images/range_plot-{range_plot_count}.png", bbox_inches = 'tight')



def get_plot(file_id):
    dataframe = pd.read_csv(f"./static/{file_id}")
    file_path = f'./static/images/{(str(datetime.now()).replace(" ", "_").replace(":",""))}.jpeg'
    plot(dataframe, file_path)
    return file_path.replace(".", "http://127.0.0.1:8000/media", 1)