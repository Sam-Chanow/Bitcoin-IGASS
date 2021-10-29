# Bitcoin-IGASS
* **
## Bitcoin Investment Growth Analysis through Similarity Scoring
* **
## File Structure
* **Bitcoin-IGASS/** - Main project directory
  * **data/** - Contains project datasets and data compilers
    * **compiled-datasets** - Labeled and ready to use datasets 
      * **BPRI** - Labeled price, to post dataset 
      * **backup** -Backup zipped data
    * **raw-datasets** - The raw collected data from reddit and Bitcoin's price index
      * **backup** - Backup zipped data
      * **bitcoin-posts** - r/Bitcoin posts data
      * **bitcoin-price** - Bitcoin price data
      * **cryptocurrency-posts** - r/Cryptocurrency posts data
    * **postDownloader.py** - Manipulates the pushshift.io to retrieve reddit post data
  * **model/** -Contains model folder and model information
  * **Predict.py** - Main python file to predict next days Bitcoin price data
  * **Readme.md** - Readme file
  * **data.py** - Provide and manipulate the compiled datasets
    * When run on its own, it can search by date through the whole r-cryptocurrency-posts dataset and return the posts from that date
    * It can also search price data from a specific day
    * When used with -Compile, creates a dataset for the compiled-datasets folder
  * **model.py** - The model used for price prediction
* **
## Compiled Datasets
### Bitcoin Price by Reddit Indicators (BPRI) Dataset
**Purpose:**
This dataset correlates reddit posts from the subreddits r/Cryptocurrency and r/Bitcoin to the price change in Bitcoin the following day

**Format:** [CHANGE] //POSTDATACOMPILED// [POST-DATA]

**Specifics:** [CHANGE] is the price change of Bitcoin (UP or DOWN) the day after the posts [POST-DATA] were posted in YYYY-MM-DD format. [POST-DATA] is a string that contains all of the post bodies from the given day concatenated and seperated by ' '. The dataset contains data from 2018-10-26 -> 2021-07-06.
* **
## Model
### Vectorization
**Bert-as-Service:** We are using the Bert model provided at https://github.com/hanxiao/bert-as-service to vectorize our post data. We encode a list of posts from a single day and <average/add them> (haven't decided which yet). We are using the Bert model uncased_L-24_H-1024_A-16, for more information read model/MODEL_INFO.txt.

### Learning Model
**BERT**: Return list of vectors representing the posts from that day

**Classifier**
* **RNN**: Possibly run this list of vectors through the RNN and train an RNN, maybe positional relationships will help the classifier.
* **Logistic Regression**: Most likely we will average or add all of those vectors and run it through a Logistic regression Model
* **

## Outcome
