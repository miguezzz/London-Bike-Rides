import pandas as pd

# use this to extract the file downloaded from Kaggle
import zipfile

# use this to download the dataset programatically from Kaggle
import kaggle

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()
api.dataset_download_files('hmavrodiev/london-bike-sharing-dataset', path='.', unzip=True)

# or just download dataset from kaggle using the Kaggle API (terminal):
# kaggle datasets download -d hmavrodiev/london-bike-sharing-dataset

# extract the file from the downloaded zip file
zipfile_name = 'london-bike-sharing-dataset.zip'
with zipfile.ZipFile(zipfile_name, 'r') as file:
    file.extractall()
    
# read in the csv file as a pandas dataframe
bikes = pd.read_csv("london_merged.csv")

# explore the data
bikes.info()
print()

print(bikes.columns)
print()

# count the unique values in the weather_code column
print(bikes.weather_code.value_counts())
print()

# count the unique values in the season column
print(bikes.season.value_counts())
print()

# dict specifying the column names that I want to use
new_cols_dict ={
    'timestamp':'time',
    'cnt':'count', 
    't1':'temp_real_C',
    't2':'temp_feels_like_C',
    'hum':'humidity_percent',
    'wind_speed':'wind_speed_kph',
    'weather_code':'weather',
    'is_holiday':'is_holiday',
    'is_weekend':'is_weekend',
    'season':'season'
}

# Renaming the columns to the specified column names

# Axis: Especifica se você deseja renomear os rótulos das linhas (axis=0)
# ou das colunas (axis=1). Para renomear colunas, você deve usar axis=1.

# Inplace: Se inplace=True, a alteração é feita diretamente no DataFrame original
# e nada é retornado. Se inplace=False (o padrão), uma nova cópia do DataFrame com
# os rótulos alterados é retornada, e o DataFrame original permanece inalterado.
bikes.rename(new_cols_dict, axis=1, inplace=True)

# changing the humidity values to percentage (a value between 0 and 1)
bikes.humidity_percent = bikes.humidity_percent / 100

# creating a season dictionary so that we can map the integers 0-3 to the actual written values
season_dict = {
    '0.0':'spring',
    '1.0':'summer',
    '2.0':'autumn',
    '3.0':'winter'
}

# creating a weather dictionary so that we can map the integers to the actual written values
weather_dict = {
    '1.0':'Clear',
    '2.0':'Scattered clouds',
    '3.0':'Broken clouds',
    '4.0':'Cloudy',
    '7.0':'Rain',
    '10.0':'Rain with thunderstorm',
    '26.0':'Snowfall',
    '94.0': 'Freezing Fog'
}

# changing the seasons column data type to string
# to avoid type errors when mapping values!!!
bikes.season = bikes.season.astype('str')
# mapping the values 0-3 to the actual written seasons
bikes.season = bikes.season.map(season_dict)

print(bikes.season)
print()

# changing the weather column data type to string
# to avoid type errors when mapping values!!!
bikes.weather = bikes.weather.astype('str')
# mapping the values to the actual written weathers
bikes.weather = bikes.weather.map(weather_dict)

print(bikes.weather)
print()

# checking our dataframe to see if the mappings have worked
print(bikes.head())

# writing the final dataframe to an excel file that we will use in our Tableau visualisations.
# The file will be the 'london_bikes_final.xlsx' file and the sheet name is 'Data'
bikes.to_excel('london_bikes_final.xlsx', sheet_name='Data')