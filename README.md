Objective
---------

The goal of this project is to create a machine learning model capable of receiving text describing a clothing item and returning a ranked list of links to similar items from different websites. The solution must be a function deployed on Google Cloud that accepts a text string and returns JSON responses with ranked suggestions.

**Note**: The solution was not deployed over Google Cloud due to issues with containerizing the application and creating Docker images. Any help in this regard will be highly appreciated.

## 1. Introduction

For the purposes of this project, all the product information was scraped from the [ASOS Website.](https://www.asos.com/) More particularly the products were retrieved from the Men and Women category and included product sub categories such as shoes, t-shirts, shirts, party dresses, trainers, skirts and accessories such as sunglasses and watches.

## 2. Project Structure

`./data`: Is the folder that contains all relevant .csv files such as the scraped data, pre-processed data and the word embeddings.<br>
`./jupyter-files`: Contains all relevant jupyter notebook files.<br>
`./static and ./template`: Supporting folders containing the HTML and CSS code for the Flask application<br>
`app.py` is the executable Flask application

## 3. Installations

1. Clone this repository

```
git clone https://github.com/your-username/clothing-similarity-search.git
```

2. Additionally also ensure that Chrome driver has been properly installed for your corresponding Chrome version, to enable selenioum to work properly. Follow this link to install the suitable version of [Chrome Driver](https://chromedriver.chromium.org/downloads)

3. Install required dependencies through

```
pip install -r requirements.txt
```

## 4. Project Components
1.  Web Scraping: 
    Web scraping for the project was implemented using selenium. For further details, kindly refer the jupyter notebook web-scraping.ipynb under the directory jupyter-files
    
2. Text Preprocessing: 
    Text Preprocessing was performed using the nltk library. The source code can be found in preprocesing.ipynb
    
3. Text Embedding: 
    Text Embedding was performed using the Sentence Transformer library and the relevant dataset can be found in the `data` directory and is labelled as `embeddings.csv`
    
4. Text Similarity: 
    The cosine similarity was used to compare the input text with the database of products available.
    
5. Deployment and Usage: 
    After cloning the repository and installing the necessary packages, run the following command from the root of the cloned repo
    ```
    python app.py 
    ```
    The application will open at the following address locally:
    ```
    localhost:5000
    ```
As mentioned the project was not deployed over Google Cloud due to issues with containerization and Docker images. The project is live at the following URL [Clothing Similarity Search](https://clothing-similarity-search-422k.onrender.com).
