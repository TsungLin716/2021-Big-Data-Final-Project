# Determine the dataset with high similarity to the assigned dataset
Here we use Jaccard Similarity to determine the similarity between our assigned dataset (DOB Job Application Filings, ic3t-wcy2) and all the other datasets in NYC Open Data. The result is the top 50 datasets that have the highest similarity to the assigned dataset. To calculate obtain the result, please follow the steps below:
1. upload getSimilarity.py to peel.hpc.nyu.edu
2. go to the directory where getSimilarity.py is located
3. execute "spark-submit getSimilarity06.py" to run the file
4. execute "hfs -getmerge similarityRank.out similarityRank.csv" to retrieve the result
