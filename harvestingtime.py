import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class district:
    def __init__(self, dictionary):
        self.crops = dictionary['crops']
        self.position = dictionary['position']
        self.close_stations = dictionary['close_stations']
        self.weather_data = dictionary['weather_data']
        self.soil_data = {'SMI_OB': dictionary['SMI_OB'], 'SMI_GB': dictionary['SMI_GB']}


    def to_crop(self, crop):
        fltr = self._create_filter(crop)
        filtered_indicators = self._apply_filter(fltr)

        return filtered_indicators


    def _create_filter(self, crop):
        croptimes = {
            'Wintergerste': np.array([10, 11, 12, 1, 2, 3, 4, 5]), 
            'Sommergerste': np.array([3, 4, 5, 6, 7]),
            'Zuckerrüben':  np.array([4, 5, 6, 7, 8]),
            'Kartoffeln':   np.array([4, 5, 6, 7]),
            'Silomais':     np.array([5, 6, 7, 8]),
            'Winterweizen': np.array([11, 12, 1, 2, 3, 4, 5, 6])
            }
        
        if croptimes[crop][0] > croptimes[crop][-1]:
            empty_filter = np.repeat(False, 24)
            start = np.where(croptimes[crop]==1)[0][0]
            filter = empty_filter
            filter[(12-start):(12-start+len(croptimes[crop]))] = True
            filter = filter.reshape(2, 12)
            winter = True
        else:
            empty_filter = np.repeat(False, 12)
            filter = empty_filter
            filter[croptimes[crop]-1] = True
            winter = False
        
        return winter, filter


    def _apply_filter(self, filter):
        filtered_indicators = {}
        weather_indicators = ['TT', 'SD', 'FK', 'RR']
        soil_indicators = ['SMI_OB', 'SMI_GB']

        if filter[0]==False: # growing season NOT in winter
            for wi in weather_indicators:
                dx = self.weather_data[wi].to_numpy()
                de = np.empty((len(dx), filter[1].sum()))
                for year in np.arange(dx.shape[0]):
                    de[year] = dx[year][filter[1]]
                filtered_indicators[wi] = de
            
            for si in soil_indicators:
                dx = self.soil_data[si].to_numpy()
                de = np.empty((len(dx), filter[1].sum()))
                for year in np.arange(dx.shape[0]):
                    de[year] = dx[year][filter[1]]
                filtered_indicators[si] = de

        elif filter[0]==True: # growing season IN winter
            pass

        else:
            pass

        return filtered_indicators

    
    def plot_weather(self):
        rain = self.weather_data['RR'].mean(axis=0).tolist()
        temp = self.weather_data['TT'].mean(axis=0).tolist()
        
        fig, ax = plt.subplots()
        ax.set_title('climate chart')
        ax.set_ylabel('temperature')
        ax2 = ax.twinx()
        ax2.set_ylabel('precipitation')
        sns.barplot(x=np.arange(1, 13), y=temp, color='tomato', ax=ax)
        sns.lineplot(x=np.arange(1, 13), y=rain, color='dodgerblue', linewidth=2, ax=ax2)
        plt.show()        