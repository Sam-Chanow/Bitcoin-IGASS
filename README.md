# Bitcoin-IGASS
## Bitcoin Investment Growth Analysis through Similarity Scoring

## File Structure
* **Bitcoin-IGASS/** - Main project directory
  * **data/** - Contains project datasets and data compilers
    * **compiled-datasets** - Labeled and ready to use datasets 
    * **raw-datasets** - The raw collected data from reddit and Bitcoin's price index
      * **backup** - Backup zipped data
      * **bitcoin-posts** - r/Bitcoin posts data
      * **bitcoin-price** - Bitcoin price data
      * **cryptocurrency-posts** - r/Cryptocurrency posts data
    * **postDownloader.py** - Manipulates the pushshift.io to retrieve reddit post data
  * **Predict.py** - Main python file to predict next days Bitcoin price data
  * **Readme.md** - Readme file
  * **data.py** - Provide and manipulate the compiled datasets
    * When run on its own, it can search by date through the whole r-cryptocurrency-posts dataset and return the posts from that date
    * It can also search price data from a specific day
  * **model.py** - The model used for price prediction
## Compiled Datasets

## Model

## Outcome
