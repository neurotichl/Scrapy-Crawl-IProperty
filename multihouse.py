from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from iproperty.spiders.house import HouseSpider, HouseSpiderExp
from configparser import ConfigParser 
from datetime import datetime
import pandas as pd
import folium
import re

def facilities(x):
	try:
		return x.replace('Bedroom(s)','Bed').replace('Bathroom(s)','Bath').replace('Parking Bay(s)','Park')
	except:
		pass

def add_frame(index,name,price,size,facilities,link,**kwargs):
	html="""
<pre>
{0}
Name      : {1}
Price     : {2}
Amenities : {3}
sq. ft    : {4}
link      : {5}
</pre>
	"""
	return folium.IFrame(html= html.format(index+1,name,price,facilities,size,link), width=400, height=100)

def plot_map(df,html_name):
	color_group = {'High':'red','Low':'blue'}

	m = folium.Map(location=[3.139, 101.6869], zoom_start = 10)

	for row in df.to_dict(orient='records'):
		iframe = add_frame(**row)
		popup = folium.Popup(iframe, max_width=2650)
		folium.Marker([row['lat'], row['lon']], popup=popup, icon=folium.Icon(color=color_group[row['prize_range']])).add_to(m)

	folium.Marker([3.1173752,101.763286],popup='Tat Yau Home', icon=folium.Icon(color='green')).add_to(m)
	m.save('{}.html'.format(html_name))

def process_result():
	df1 = pd.read_csv('house_cheap.csv')
	df2 = pd.read_csv('house_exp.csv')
	df = df1.append(df2, ignore_index=True)
	df['facilities'] = df['amenities'].map(facilities)
	df = df[df['lat'].notnull()]
	return df.reset_index(drop=True).reset_index()

############################################################################################################
if __name__ == '__main__':
	house_conf = ConfigParser()
	house_conf.read('house_conf.ini')

	process = CrawlerProcess(get_project_settings())
	process.crawl(HouseSpider,**dict(house_conf['Low']))
	process.crawl(HouseSpiderExp,**dict(house_conf['High']))
	process.start()

	df = process_result()
	plot_map(df,'{0}_{1}.html'.format(house_conf['Map']['file'],datetime.today().date().isoformat().replace('-','')))