import seaborn as sns
import matplotlib.pyplot as plt

class district:
    def __init__(self, dictionary):
        #self.name = str(dictionary)
        self.crops = dictionary['crops']
        self.position = dictionary['position']
        self.close_stations = dictionary['close_stations']
        self.weather_data = dictionary['weather_data']
        self.soil_data = {'SMI_OB': dictionary['SMI_OB'], 'SMI_GB': dictionary['SMI_GB']}
    
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