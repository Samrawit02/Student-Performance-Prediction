from IPython.display import Markdown, display



class Explore_Data():
    '''
    Print info, head, shape , misssing values of dataset 
    Paramenter: 
        data DataFrame: pandas dataframe
    '''

    def __init__(self, data):
        self.data = data
        pass
           
    def __str__(self):
        self.summary()
        return ''
    
    def data(self):
        '''Return the dataset of current instance'''
        return self.data
    
    def summary(self):
        '''print summary of the dataset'''
        self.info()
        self.divider()
        self.head()
        self.divider()
        self.shape()
        self.divider()
        self.duplicated()
        self.missing_values()
        self.number_of_unique_values()
        self.statistics()
    
    def divider(self):
        '''print a horzontal line'''
        display(Markdown('---'))
    
    def info(self):
        '''print a concise summary of a DataFrame'''
        print('\nDataframe summary')
        display(self.data.info())

    def head(self, n=5):
        '''print out the first 5 rows of a dataframe'''
        print('\nFirst 5 rows')
        display(self.data.head(n))

    def shape(self):
        '''print out shape of a dataframe'''
        print('\nShape of the dataset')
        display(self.data.shape)

    def duplicated(self):
        '''print out count of  duplicated value of a dataframe'''
        print('\nDuplication values count')
        display(self.data.duplicated().sum())

    
    def missing_values(self):
        '''print out count of  missing value of a dataframe'''
        print('\nMissing values count')
        display(self.data.isna().sum())

    def number_of_unique_values(self):
        '''print out count of  Unique values of a dataframe'''
        print('\nUnique values')
        display(self.data.nunique())

    def statistics(self):
        '''print out statistics of data set of a dataframe'''
        print('\nCheck statistics of data set')
        display(self.data.describe())
