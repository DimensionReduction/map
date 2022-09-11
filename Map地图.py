import pandas as pd
from pyecharts.charts import Map
from pyecharts import options as opts

data=pd.read_excel('广东人口.xlsx',sheet_name='Sheet1')
city=data.iloc[:,0]
population=data.iloc[:,1]

z1=[i for i in zip(city,population)]
z2=list(zip(city,population))
z3=[list(i) for i in zip(city,population)]
z4=data[['城市','人口']].values.tolist()
print(z1,z2,z3,z4,sep='\n\n')

map=Map(init_opts=opts.InitOpts(width="1200px",height='600px'))
map.add('广东人口',data_pair=z3,maptype='广东',is_map_symbol_show=False)
map.set_series_opts(label_opts=opts.LabelOpts(is_show=True))
map.set_global_opts(title_opts=opts.TitleOpts(title='广东人口分布图',subtitle='数据来源：广东统计年鉴'),
    visualmap_opts=opts.VisualMapOpts(max_=18676605,is_piecewise=True,range_color=['lightskyblue','yellow','orangered']))
map.render('Map地图.html')
