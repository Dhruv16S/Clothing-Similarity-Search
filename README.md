<details open>

  <h2>Objective</h2>
<p>The goal of this project is to create a machine learning model capable of receiving text describing a clothing item and returning a ranked list of links to similar items from different websites. The solution must be a function deployed on Google Cloud that accepts a text string and returns JSON responses with ranked suggestions.
  <b>Note</b>The solution was not deployed over Google Cloud due to issues with containerizing the application and creating Docker images. Any help in this regard will be highly appreciated.<p>
  <ol>
    
    <li>Introduction</li>
      <p>For the purposes of this project, all the product information was scraped from the <a href="https://www.asos.com/">ASOS Website.</a>More particularly the products were retrieved from the Men and Women category and included product sub categories such as shoes, t-shirts, shirts, party dresses, trainers, skirts and accessories such as sunglasses and watches.</p>
    <li>Project Structure</li>
      <ul>
        <li><b>./data<b>: Is the folder that contains all relevant .csv files such as the scraped data, pre-processed data and the word embeddings.</li>
        <li><b>./jupyter-files<b>: Contains all relevant jupyter notebook files</li>
        <li><b>./static and ./template<b>: Supporting folders containing the HTML and CSS code for the Flask application</li>
         <li>app.py is the executable Flask application</li>
      </ul>
    <li>Installations</li>
          <p>Clone this repository</p>
          <p>git clone https://github.com/your-username/clothing-similarity-search.git</p>
          <p>Additionally also ensure that Chrome driver has been properly installed for your corresponding Chrome version, to enable selenioum to work properly. Follow this link to install the suitable version of <a href="https://chromedriver.chromium.org/downloads">Chrome Driver</a></p>
          <p>Install required dependencies through</p>
          <p>pip install -r requirements.txt</p>
    <li>Project Components<li>
      <ol>
        <li>Web Scraaping</li>
        <p>Web scraping for the project was implemented using selenium. For further details, kindly refer the jupyter notebook </p>
        <li>Text Preprocessing</li>
        <li>Text Embedding</li>
        <li>Text Similarity</li>
        <li>Deployment and Usage</li>
      </ol>
  </ol>
  
</details>
