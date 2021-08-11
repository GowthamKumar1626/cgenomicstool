from tools.crosstab.preprocessing import divide_chunks, categorization
from tools.crosstab.handlers import time_it, try_except
from tools.crosstab.Exceptions import *
from tools.crosstab.io import save_dataset
from tools.crosstab.meta_data import encode, load_meta_data

import numpy as np
import pandas

import os

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns

import matplotlib as mpl
import matplotlib.patches as mpatches

mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

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

    cmap = sns.cubehelix_palette(start=0, rot=n_colors, light=1, n_colors=n_colors)
    meta_colors = list(cmap.as_hex())


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
    plt.figure(figsize=(15,10))
    plt.subplot(211)
    sns.set(font_scale=1)
    handles = [mpatches.Patch(color=color, label=label) for color, label in zip(colors, labels)]
    plt.legend(handles=handles, ncol=2, bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
        mode="expand", borderaxespad=0.)

def plot(
        dataset: pandas.core.frame,
        path: str
    ) -> None:
    global cmap, n_colors

    pre_plot()
    chunk_dataset, encodings_present = categorization(dataset)
    generate_labels_colors(encodings_present)
    plot_settings()

    sns.heatmap(chunk_dataset, vmin=0, vmax=n_colors, cmap=cmap, cbar=False)
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

    