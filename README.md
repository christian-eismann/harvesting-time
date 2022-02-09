# Harvesting time

Harvesting time is a project to predict the harvest quantity of ten different crops based on the weather and soil data of German districts (Landkreise).

## data generation

I gathered the data from different sources:
* crop data from official German sources called "Erträge ausgewählter landwirtschaftlicher Feldfrüchte - Jahressumme - regionale Tiefe: Kreise und krfr. Städte", available [here](https://www.regionalstatistik.de/genesis//online?operation=table&code=41241-01-03-4&bypass=true&levelindex=1&levelid=1644440058901)
* Geographical data on German districts, available [here](https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/_inhalt.html)
* Weather data (temperature, precipitation, sunshine, wind) from Deutscher Wetterdienst (DWD), available [here](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/monthly/climate_indices/kl/historical/)
* Soil data (soil moisture index) from UFZ Dürremonitor, available [here](https://www.ufz.de/index.php?de=37937)