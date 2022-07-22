#hide earrings 
import warnings
warnings.filterwarnings('ignore')
#import necessary modules
import pandas as pd
# Read in the data with `read_csv()
df = pd.read_csv('C:\\Users\\haier\\Downloads\\WA_Fn-UseC_-Sales-Win-Loss.csv')

df[['Opportunity Result','Route To Market']].head(50)

#import the necessary module
from sklearn import preprocessing
# create the Labelencoder object
le = preprocessing.LabelEncoder()
def get_LabelEncoder(labelencoders_list):
    for labelencoder_list in labelencoders_list:
        df[labelencoder_list] = le.fit_transform(df[labelencoder_list])
get_LabelEncoder(['Supplies Subgroup','Region','Route To Market','Opportunity Result','Supplies Group','Competitor Type'])
