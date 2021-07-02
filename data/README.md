# Dataset Extraction
Contains the notebooks utilized by our research in order to fetch data from GitHub API

The order of execution is as follows:-

1- Repositories are collected by executing the 'Extract repos' notebook.
These repositories are then saved in a csv file in the same directly, named 'repos.csv' by default. We fetch the repositories associated with the IEEE Spectrum list of top programming languages.
The original list can be found at https://spectrum.ieee.org/static/interactive-the-top-programming-languages-2020

2- Issues from the repositories extracted in the first step are collected by running the 'Extract issues' notebook.
This fetches information for the repositories such as body, description, labels, etc. 
