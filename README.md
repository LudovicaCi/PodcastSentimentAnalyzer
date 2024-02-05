# Data Mining and Machine Learning Project
# Podcast Sentiment Analysis

## Overview

This project focuses on Sentiment Analysis for podcast reviews, utilizing classification techniques to categorize sentiments as positive, neutral, or negative. The analysis is complemented by Streaming Analysis, enabling dynamic tracking of sentiment evolution over time to adapt the classifier accordingly.

## Objectives

1. **Sentiment Analysis:**
    - Implement classification techniques for precise sentiment labeling.
    - Evaluate and compare classifiers for optimal performance.

2. **Streaming Analysis:**
    - Dynamically monitor the evolution of sentiments towards podcasts.
    - Assess classifier adaptability to changing trends, allowing for retraining.

## Dataset

The dataset selected for the project is available at [Kaggle Podcast Reviews Dataset](https://www.kaggle.com/datasets/thoughtvector/podcastreviews). It includes 2 million podcast reviews related to 100,000 podcasts, updated monthly. Our focus lies in the dataset containing information about the reviews that users left on podcasts.

The dataset comprises the following attributes:
- Podcast ID
- Title
- Content
- Rating
- Author ID
- Created At

## Usage

Follow these steps to utilize the code for sentiment analysis:

1. **Download the Dataset:**
   - Download the dataset from the provided link: [Podcast Reviews Dataset](https://www.kaggle.com/datasets/thoughtvector/podcastreviews)

2. **Prepare the Data:**
   - Extract the `reviews.json` file from the downloaded dataset.

3. **Convert JSON to CSV:**
   - Execute the provided script `JsonToCsvConverter.py` in your Python environment to convert the dataset to a CSV file.

4. **Data Preprocessing:**
   - Execute the Jupyter notebook `DataPreprocessing.ipynb` to preprocess the dataset.

5. **Training Set Building:**
   - Execute the Jupyter notebook `TrainingsetBuilding.ipynb` to build the training set.

6. **Classifier Construction:**
   - Execute the Jupyter notebook `Classifiers.ipynb` to construct classifiers for sentiment analysis.

7. **Streaming Analysis:**
   - Execute the Jupyter notebook `StreamingAnalysis.ipynb` to perform streaming analysis on sentiments.

## Additional Information

For further information, consult the [Documentation.pdf](Docs/Documentation.pdf) file.
