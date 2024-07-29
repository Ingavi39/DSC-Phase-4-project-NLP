# DSC-Phase-4-project-NLP
# Sentiment Analysis of Tweets

## Introduction
This project performs sentiment analysis on tweets. The steps include data cleaning, preprocessing, sentiment analysis, and visualization of results.

## Project Structure
- `data/`: [Directory containing data](https://github.com/Ingavi39/DSC-Phase-4-project-NLP/tree/main/data)
- `notebooks/`: [Directory containing Jupyter Notebooks.](https://github.com/Ingavi39/DSC-Phase-4-project-NLP/blob/main/Index.ipynb)
- `images/`: [Directory containing images.](https://github.com/Ingavi39/DSC-Phase-4-project-NLP/tree/main/images)
- `README.md`: [Project documentation.](https://github.com/Ingavi39/DSC-Phase-4-project-NLP/blob/main/README.md)
- `.gitignore`: [Git ignore file.](https://github.com/Ingavi39/DSC-Phase-4-project-NLP/blob/main/.gitignore)
- `presentation/`: [Directory containing presentation materials.](https://github.com/Ingavi39/DSC-Phase-4-project-NLP/blob/main/Presentation.pdf)

## Requirements
- Python 3
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
    git clone https://github.com/Ingavi39/DSC-Phase-4-project-NLP
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

2. Open the notebook `notebooks/Index.ipynb` and run the cells step-by-step.

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
- [Directory containing images.](https://github.com/Ingavi39/DSC-Phase-4-project-NLP/tree/main/images)

## Conclusion
The project has addressed the problem statements to a certain extent:

1. **Sentiment Identification:** Achieved with varying degrees of accuracy. Improvements are needed, particularly in handling class imbalance and improving positive sentiment detection.
2. **Target Identification:** Partially addressed through brand/product association with sentiment. More detailed analysis could provide deeper insights.
3. **Trends and Insights:** Initial insights were provided, highlighting the need for further analysis to uncover detailed trends and public perceptions.

Overall, while the project successfully built and evaluated models for sentiment analysis, further work is needed to refine the models, address identified issues, and explore additional dimensions of the data to fully meet the project objectives and problem statements.


Let's assess how the project addressed the research questions:

### Research Question 1: Sentiment Classification
- **Objective:** What is the distribution of positive, negative, and neutral sentiments across the dataset?

**Achievement:**
- The dataset was analyzed to identify the distribution of sentiments. The models primarily classified tweets into positive and negative categories.
- Results from the models showed that a significant portion of the tweets expressed negative sentiments, while a substantial number also expressed positive sentiments. The challenge was more pronounced in correctly classifying positive sentiments due to class imbalance.

**Outcome:**
- The analysis provided a clear picture of sentiment distribution, although the focus was on binary classification (positive vs. negative) rather than including a neutral category. The findings highlighted the need for better handling of positive sentiment classification.

### Research Question 2: Brand/Product Association
- **Objective:** Which brands and products are most frequently mentioned, and what is the associated sentiment for each?

**Achievement:**
- The data included information on the brands/products mentioned in the tweets, allowing for an association between sentiments and specific brands/products.
- The EDA revealed that Apple and Google products were among the most frequently mentioned, with a majority of positive sentiments associated with these brands.

**Outcome:**
- While the primary focus was on sentiment classification, the analysis did reveal some insights into brand/product association. However, more detailed analysis, such as sentiment breakdown by brand or product, would provide deeper insights into public perception towards specific brands/products.

### Research Question 3: Temporal Trends
- **Objective:** Are there any notable trends in sentiment over time for specific brands or products?

**Achievement:**
- This aspect was not fully explored due to the focus on sentiment classification and the technical challenges faced during the modeling process. Temporal analysis would require timestamp data and further exploration of trends over time.

**Outcome:**
- The research question regarding temporal trends was not directly addressed in the current analysis. To answer this question, additional steps would be needed to analyze how sentiments toward specific brands/products change over time.

### Conclusion
The project made significant strides in addressing the research questions, particularly in understanding sentiment distribution and associating sentiments with specific brands/products. However, some areas, such as temporal trends and a deeper exploration of brand-specific sentiments, were not fully explored.

### Recommendations for Further Analysis:
1. **Incorporate Neutral Sentiment:** Expanding the classification to include a neutral category would provide a more comprehensive view of sentiment distribution.
2. **Brand/Product-Specific Analysis:** A more detailed breakdown of sentiments for each brand/product can provide targeted insights into public perception.
3. **Temporal Analysis:** Including a temporal component to analyze how sentiments evolve over time can uncover trends and shifts in public opinion.
4. **Enhanced Feature Representation:** Exploring advanced NLP techniques (like word embeddings or BERT) could improve sentiment classification accuracy and provide richer insights.

These steps would help in fully addressing the research questions and providing a more comprehensive understanding of the data.

## Troubleshooting
If you encounter any issues or have questions, please check the [FAQ](FAQ.md) or open an [issue](https://github.com/Ingavi39/DSC-Phase-4-project-NLP/issues) on GitHub.

## Members
    - Ingavi Kilavuka
    - Calvin Omwega
    - Alvin Kimathi
    - Ronny Kabiru

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [NLTK](https://www.nltk.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
