# harvesting-time

the data set contains information on 

1) weather (temperature, sunshine, wind, precipitation), 
2) soil moisture (surface an deep), and
3) crop yields for ten crops 
4) for each of the German districts (Landkreise) between 1999 and 2020. 

Weather and soil data on monthly basis, crop yields for each year. 
Temperature in °C (mean), Sunshine in hours, wind in in Bft (mean), precipitation in mm

all data gathered from public and open access sources:
- weather data from Deutscher Wetterdienst 
  https://opendata.dwd.de/
- soil moisture data from UFZ Helmholtz Centre for Environmental Research 
  https://www.ufz.de/index.php?en=37937
- crop yields data from Statistisches Bundesamt
  https://www.regionalstatistik.de/genesis/online
  
  import with pandas:
  pd.read_csv('crop_and_weather_data.csv', sep=';', index_col=0, header=[0,1], dtype={'district': str})
