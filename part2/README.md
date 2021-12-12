## 1. Determine the dataset with high similarity to the assigned dataset
Here we use Jaccard Similarity to determine the similarity between our assigned dataset (DOB Job Application Filings, ic3t-wcy2) and all the other datasets in NYC Open Data. The result is the top 50 datasets that have the highest similarity to the assigned dataset. To obtain the result, please follow the steps below:
1. upload getSimilarity.py to peel.hpc.nyu.edu
2. go to the directory where getSimilarity.py is located
3. execute "spark-submit getSimilarity06.py" to run the file
4. execute "hfs -getmerge similarityRank.out similarityRank.csv" to retrieve the result

## 2. Fix the sample dataset with unimproved cleaning methods

## 3. Fix the sample dataset with improved cleaning methods

## 4. Calculate the *Precision* and *Recall* of the unimproved and improved cleaning methods.
A jupyter notebook (evaluation.ipynb) is created to calculate and compare the precision and recall of the unimproved and improved cleaning methods. To calculate the precision and recall of the results, please follow the steps below:
1. Make sure the csv files are in the same directory evaluation.ipynb is located.
    a. raw.csv is the file containing the raw, uncleaned data.
    b. groundTruth.csv is the file containing the corrected data.
    c. unimproved_result.csv is the file containing the data cleaned by unimproved cleaning method.
    d. improved_result.csv is the file containing the data cleaned by improved cleaning method.
