# DSC-Phase-4-project-NLP
# Sentiment Analysis of Tweets

## Introduction
This project performs sentiment analysis on tweets. The steps include data cleaning, preprocessing, sentiment analysis, and visualization of results.

## Project Structure
- `data/`: Directory containing the dataset.
- `notebooks/`: Directory containing Jupyter Notebooks.
- `scripts/`: Directory containing Python scripts for data processing and analysis.
- `README.md`: Project documentation.
- `.gitignore`: Git ignore file.

## Requirements
- Python 3.x
- Jupyter Notebook
- pandas
- numpy
- matplotlib
- seaborn
- nltk
- textblob

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/sentiment-analysis-tweets.git
    cd sentiment-analysis-tweets
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Download necessary NLTK data:
    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    ```

## Usage
1. Start Jupyter Notebook:
    ```sh
    jupyter notebook
    ```

2. Open the notebook `notebooks/sentiment_analysis.ipynb` and run the cells step-by-step.

## Data Cleaning and Preprocessing
- Remove URLs, special characters, and stopwords from the tweet text.
- Tokenize the cleaned text for further analysis.

## Sentiment Analysis
- Analyze the sentiment of tweets using TextBlob.
- Classify sentiments into Positive, Negative, and Neutral categories.
- Visualize the frequency of each sentiment category.

## Brand/Product Analysis
- Identify the most frequently mentioned brands/products in the tweets.
- Analyze the sentiment distribution for each of the top brands/products.
- Create a pivot table to show the percentage distribution of sentiments for each brand/product.

## Visualization
- Visualize the sentiment analysis results using bar graphs and other plots.

## Conclusion
Summarize your findings and potential next steps for further analysis and improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [NLTK](https://www.nltk.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)