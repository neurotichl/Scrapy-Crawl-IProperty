# House Property
This simple crawling program is written for my own personal use in comparing house properties in order to facilitate me in decision making to buy a house. I crawled the house informations from a Malaysia house property website: www.iproperty.com.my. Anybody who has the same interest as me can use this program to get an easy overview on house properties. 

# The Outcome:
The crawled result will be displayed on a map, with the following information:
- prices
- house sizes
- locations 
- amenities 
- page link (iproperty.com.my)

# Steps:
1. You must have Scrapy, Folium, ConfigParser and Pandas installed.
2. State your personal preference (budget, area) in the **house_conf.ini** file.
3. Run the program in CMD:
```
python multihouse.py
```
4. View your result in the **map** folder. 

# About the Config:
- There are 4 sections in the config file:
  - Low
  - High 
  - Map
  - MyHouse
  where MyHouse is optional and can be excluded.
  
- Low/High:
State your interested area(state name) and budget(RM). 

- Map: 
State the output folder and output filename.
  
# Future Work:
- Wrap the program into a wheel file

---

### Program flow (As a record):
1. The program first read in the config file and parse them into dictionary using ConfigParser.
2. Two spider crawling the 'Low' and 'High' sectionis are run simultanously using CrawlerProcess. 
3. The result are written to two different csv file as specified in the scrapy Pipeline.
4. The results are then processed using pandas and plotted on the map by Folium.
5. Folium export the map into HTML format.
