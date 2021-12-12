# 2021-Big-Data-Final-Project(CS-GY_6513)
This is the final project of the Big Data course at NYU Tandon School of Engineering. The goal is to create a process model for NYU Open Data(DOB). This project implemented techniques such as data profiling, data cleaning, similarity calculation, precision and recall.

## Group Members
- Peng Yuan Chen(pc2973)
- Tsung Lin Yang(ty2065)
- Chun Yen Liou(cyl625)

## Structure
The structure of this project is as below:
- part1
	- data profiling
	- unimproved cleaning methods
- part2
	- unimproved cleaning methods
	- improved cleaning methods
	- (Files for result evaluation)

**Data Profiling** is to extract the actionable metrics about the data's quality. It allows us to determine which column is having issues. Then, we can categorize our research problem.

**Data Cleaning** is to address the problems we found from Data Profiling. This includes the mispelled and unstandarized data that lurking within the datasets. We applied our code with several customized functions and algorithms to modify the data so that they are in a unite and correct format for further utilization.

**Similarity Calculation** is the technique to determine the degree of similarity between two datasets. If we encounter a huge amount of datasets, we can find a group of datasets that have considerably large overlap. Then, we can extract an amount of sample data which based on the confidence interval and confidence level. In our project, we decided to use Jaccard Similarity.

**Precision and Recall** is the metrics we applied to evaluate the effectiveness of our data cleaning method.

## How to run the project?
You can follow the Readme.md files in folder **part1** and **part2** to run the code. It is recommended to start from **part1**

## Result
The objective, the method to achieve, and the result is documented in the final report. For further detail of this project, please refer to the report.pdf.
