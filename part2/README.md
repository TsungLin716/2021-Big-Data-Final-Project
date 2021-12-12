## 1. Determine the dataset with high similarity to the assigned dataset
Here we use Jaccard Similarity to determine the similarity between our assigned dataset (DOB Job Application Filings, ic3t-wcy2) and all the other datasets in NYC Open Data. The result is the top 50 datasets that have the highest similarity to the assigned dataset. To obtain the result, please follow the steps below:
1. upload getSimilarity.py to peel.hpc.nyu.edu
2. go to the directory where getSimilarity.py is located
3. execute "spark-submit getSimilarity06.py" to run the file
4. execute "hfs -getmerge similarityRank.out similarityRank.csv" to retrieve the result

## 2. Fix the sample dataset with unimproved cleaning methods
In this step, we will apply the cleaning method from part1 on the new 10 datasets we found based on the result of similarity. Inside our code, we will extract an amount of sample data from each original data based on the result of sample size calculator. The steps are as follows:
1. go to the file "unimproved_cleaning_methods"
2. execute each jupyter notebook file(.ipynb). Make sure to run the files under this directory.
3. you will see that there are 10 files"[name_of_dataset]_ program_modify.csv", open them and you will see the result run by unimproved cleaning method.


## 3. Fix the sample dataset with improved cleaning methods
In this step, we will apply our new cleaning method on the raw data we extract from the last step. We had manually combined them to a single csv file so you do not have to worry that part. The steps are as follows:
1. go to the file "improved_cleaning_methods"
2. execute the jupyter notebook file "improved_method.ipynb". Make sure to run the file under this directory
3. you will see that there is a file "improved_result.csv" which is the result after applying the new cleaning method, we will be using this file at 
   at the evaluation step.

## 4. Calculate the *Precision* and *Recall* of the unimproved and improved cleaning methods.
A jupyter notebook (evaluation.ipynb) is created to calculate and compare the precision and recall of the unimproved and improved cleaning methods. To calculate the precision and recall of the results, please follow the steps below:
1. Make sure the csv files are in the same directory evaluation.ipynb is located.
2. raw.csv is the file containing the raw, uncleaned data.
3. groundTruth.csv is the file containing the corrected data.
4. unimproved_result.csv is the file containing the data cleaned by unimproved cleaning method.
5. improved_result.csv is the file containing the data cleaned by improved cleaning method.
6. Open evaluation.ipynb and execute.
