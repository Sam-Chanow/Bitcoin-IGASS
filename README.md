<div style="text-align: center; color: rgb(255, 100, 1); background-image: url('style/btcimage.jpg'); ">
  <h1 style="font-size: 50px;">Bitcoin-IGASS</h1>
</div>

* **
<h2 style="text-align: center; color: rgb(255, 100, 1); font-size: 15px; "> Bitcoin Investment Growth Analysis through Similarity Scoring </h2>

* **
<h2 style="text-align: center; color: rgb(255, 100, 1); font-size: 20px; ">File Structure</h2>
* **Bitcoin-IGASS/** - Main project directory
  * **data/** - Contains project datasets and data compilers
    * **compiled-datasets** - Labeled and ready to use datasets 
      * **BPRI** - Labeled price, to post dataset 
      * **BPRI-POSTSPLIT** -Modified BPRI dataset where posts are split by '/ENDPOST'
      * **BVBPRI** - Bert Vectorized compilation of the BPRI dataset
      * **backup** -Backup zipped data
    * **raw-datasets** - The raw collected data from reddit and Bitcoin's price index
      * **backup** - Backup zipped data
      * **bitcoin-posts** - r/Bitcoin posts data
      * **bitcoin-price** - Bitcoin price data
      * **cryptocurrency-posts** - r/Cryptocurrency posts data
    * **data.py** - Provide and manipulate the compiled datasets
      * When run on its own, it can search by date through the whole r-cryptocurrency-posts dataset and return the posts from that date
      * It can also search price data from a specific day
      * When used with -Compile, creates a dataset for the compiled-datasets folder
    * **postDownloader.py** - Manipulates the pushshift.io to retrieve reddit post data
  * **model/** -Contains model folder and model information
  * **Predict.py** - Main python file to predict next days Bitcoin price data
  * **Readme.md** - Readme file
  * **dataset.py** - Iterable object that will read and parse all data from BPRI formatted files
  * **model.py** - The model used for price prediction
* **
<h2 style="text-align: center; color: rgb(255, 100, 1); font-size: 20px; ">Compiled Datasets</h2>
### Bitcoin Price by Reddit Indicators (BPRI) Dataset
**Purpose:**
This dataset correlates reddit posts from the subreddits r/Cryptocurrency and r/Bitcoin to the price change in Bitcoin the following day.

**Format:** [CHANGE] //POSTDATACOMPILED// [POST-DATA]

**Specifics:** [CHANGE] is the price change of Bitcoin (UP or DOWN) the day after the posts [POST-DATA] were posted in YYYY-MM-DD format. [POST-DATA] is a string that contains all of the post bodies from the given day concatenated and seperated by ' '. The dataset contains data from 2018-10-26 -> 2021-07-06.

### Bitcoin Price by Reddit Indicators Postsplit (BPRI-POSTSPLIT) Dataset
**Purpose:** This is the same data as the BPRI Dataset. This dataset correlates reddit posts from the subreddits r/Cryptocurrency and r/Bitcoin to the price change in Bitcoin the following day.

**Format:** [CHANGE] //POSTDATACOMPILED// [POST-DATA] /ENDPOST/ [POST-DATA] ...

**Specifics:** Everything in this dataset is the same as above, however the individual posts are separated by the /ENDPOST/ tag. [CHANGE] is the price change of Bitcoin (UP or DOWN) the day after the posts [POST-DATA] were posted in YYYY-MM-DD format. [POST-DATA] is a string that contains all of the post bodies from the given day concatenated and seperated by ' '. The dataset contains data from 2018-10-26 -> 2021-07-06.

### Bert-Vectorized Bitcoin Price by Reddit Indicators (BVBPRI) Dataset
**Purpose:** IN PROGRESS

**Format:** IN PROGRESS

**Specifics:** IN PROGRESS
* **
<h2 style="text-align: center; color: rgb(255, 100, 1); font-size: 20px; ">Model</h2>
### Vectorization
**Bert-as-Service:** We are using the Bert model provided at https://github.com/hanxiao/bert-as-service to vectorize our post data. We encode a list of posts from a single day and <average/add them> (haven't decided which yet). We are using the Bert model uncased_L-24_H-1024_A-16, for more information read model/MODEL_INFO.txt.

### Learning Model
**BERT**: Return list of vectors representing the posts from that day

**Classifier**
* **RNN**: Possibly run this list of vectors through the RNN and train an RNN, maybe positional relationships will help the classifier.
* **Logistic Regression**: Most likely we will average or add all of those vectors and run it through a Logistic regression Model
* **

<h2 style="text-align: center; color: rgb(255, 100, 1); font-size: 20px; ">Outcome</h2>

