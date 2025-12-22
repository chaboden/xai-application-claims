# xai-application-claims

## Installation

Create and activate the virtual environment:

```sh
conda env create -f environment.yaml
conda activate xai-claims
```

## Filtering and selection of literature

Filtering and selection of literature is done by the script "clean-and-filter.ipynb".
For the execution of the file, the folder "data" should contain a subfolder "scopus-download-cited-by-2025-07-17" in which csv files containing all papers that cited the selected XAI method source articles are stored. Please contact me, to get access to that files. Due to large file sizes, they are not stored in git.

## Creating charts of results

The script "create-statistics.ipynb" creates charts using the data extraction form to present the results.

## Creating result table

The script "create-result-table.ipynb" summarized the main results into a latex table.
