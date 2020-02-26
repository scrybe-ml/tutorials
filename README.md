# Scrybe.ml Tutorials
This repository contains samples showing different usages of Scrybe.ml. It contains several notebooks and helper scripts to help you get familiarised with basic to advanced usage of the Scrybe tool. 

# Prerequisites
The tutorial assumes you are already signed up as a Scrybe user. Currently Scrybe.ml is in private beta and new user sign-ups are invitation only. If you are interested in getting an invite, please [contact us](mailto:admin@scrybe.ml?subject=[GitHub]%20Scrybe%20Trial).

## Setup
You can either use the linked Binder to run the tutorial or set it up locally.

For the latter, clone this repository and setup your environment. All required dependencies are stored in the environment.yml file. 

# Tutorial Structure
You can go through the tutorial in two ways: scenario basis or feature basis. The tutorial is structured into scenarios but if you are interested in learning about a specific API or feature, you can just jump into the corresponding notebook. 

## Scenarios  
There is one notebook for each of the following scenarios: 

* Data Exploration: data_exploration.ipynb
    * Contains basic data exploration activities such as plots
    * Shows how Scrybe captures and indexes plots
* Training Traditional Models (using Scikit/LGB/XGB): models_traditional.ipynb
    * Loads preprocessed train/test datasets and builds various models
    * Helps understand how Scrybe captures model details and grid search summaries
* Training Deep Learning Models (using Keras): models_deep_learning.ipynb
    * Loads preprocessed train/test datasets and trains a deepnet
    * Shows how Scrybe captures model architecture and epoch-level performance
    * Shows examples of logging custom metrics and custom feature importance

## Features
Following table shows which notebooks aid exploring specific features of Scrybe:

| Scrybe Feature | data_exploration.ipynb | models_traditional.ipynb | models_deep_learning.ipynb |  
| ------------- | ------------- | ------------- | ------------- | 
| Plot Capture | &#x2714;  | . | .  | 
| Model Capture | .  | &#x2714; | &#x2714;  | 
| Bookmarking | &#x2714;  | &#x2714; | .  | 
| Labelling/Tagging | .  | &#x2714; | &#x2714;  | 
| Custom Metrics | .  | . | &#x2714;  | 
| Custom Feature Importance | .  | . | &#x2714;  | 

