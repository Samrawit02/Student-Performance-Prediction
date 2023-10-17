# Student Exam Performance Prediction
#### The dataset goal is to predict Math score
#### Dataset information
* `Gender`: sex of students -> (Male/Female)
* `race/ethnicity`: ethnicity of students -> (Group A,B,C,D,E)
* `parental level of education`: parent's final education -> (bachelor's degree , some college, master's degree, associate's degree, High School)
* `lunch`: having lunch before test(standard or free/reduced)
* `test preparation course`: complete or not complete before test 
* `reading score`: The student's score on a standardized reading test 
* `writing score`: The student's score on a standardized writing test
##### Target variable:
* `math score`: The student's score on a standardized mathematics test
#### Data Source Link:
    [http://roycekimmons.com/tools/generated_data/exams](http://roycekimmons.com/tools/generated_data/exams)

# Approach for the project

1. Data Ingestion:
    * In this phase the data is first read as csv.
    * The the data is split into training and testing and saved as csc file.

2. Data Transformation: 
    * In this phase DataTransformation Pipeline is created.
    * For Numeric Variables first SimpleImpute is applied with media then Standard Scaling is performed on numeric data.
    * For the CategoricalVariable SompleImpute is applied with most frequent strategy, then OneHotEncoder is performed , after this data is scaled with Standard Scaler
    * This preprocessor is saved as pickle file.

3. Model Training: 
    * In this phase base model is tested. The best model is found LinearRegression
    * Model is saved as pickle file.

4. Prediction Pipeline
    * This pipeline converts given data into dataframe and has various functions to load pickle and predict the final results in python

5. Flask App creation:
    * Flask app is created with User Interface to predict the Maths score inside web app.

# Exploratory Data Analysis Notebook
Link: [EDA STUDENT PERFORMANCE](./src/Notebook/EDA%20STUDENT%20PERFORMANCE.ipynb)

# Model Training Notebook
Link: [Model Training](./src/Notebook/Model%20Training.ipynb)



