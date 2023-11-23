# BERT-NER-Mountains
Pre-trained BERT fine-tuned on mountains dataset for Named entity recognition 

**Description:**

The files are designed specifically to work in Google Colab, because most of the work was done there. Upload Train_NER_BERT.ipynb or Test_NER_BERT.ipynb to Google Colab for direct use.

Files: 

- data folder - contains a data and data specific scripts
- data/mountains_data.json - chatGPT-3.5 generated data in IOB format
- data/mountains_data.csv - data converted to .csv format

- requirements.txt - library that was used
- Train_NER_BERT.ipynb - jupyter file to train and test
- Test_NER_BERT.ipynb - jupyter file to load model and test


## Problems with Data:

1) Most of labels are on start of the sentence. Model is overfited to search for mountains at the start of the sentence. 

2) There are few mountain names in the dataset, so it will be difficult for the model to find new mountains in the data

3) ChatGPT 3.5 made a lot of mistakes when generate a sentences and labels for each words. This problem is partially solved by using this file **search_data_issues.py**

## How to Solve:

Steps: 
1) Increase dataset to total 100 sentence (49 total sentence currently). 
2) Train a model on that data
3) Sample a dataset from wikipedia (mountains specific)
4) Map a dataset by using model existing model
5) Fix dataset manually 
6) Go to step 2 until results are acceptable 
7) Model are done!
