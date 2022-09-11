import pandas as pd
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
from pyecharts import options as opts

data=pd.read_excel('广东人口.xlsx',sheet_name='Sheet1')
city=data.iloc[:,0]
population=data.iloc[:,1]

z1=[i for i in zip(city,population)]
z2=list(zip(city,population))
z3=[list(i) for i in zip(city,population)]
z4=data[['城市','人口']].values.tolist()
print(z1,z2,z3,z4,sep='\n\n')

geo=Geo(init_opts=opts.InitOpts(width="1200px",height='600px'))
geo.add_schema(maptype='广东',itemstyle_opts=opts.ItemStyleOpts(color='#333333',border_color='#FFFF22'))
geo.add('广东人口',z1,label_opts=opts.LabelOpts(is_show=True),type_=ChartType.EFFECT_SCATTER)
geo.set_global_opts(title_opts=opts.TitleOpts(title='广东人口分布图',subtitle='数据来源：广东统计年鉴'),
    visualmap_opts=opts.VisualMapOpts(max_=18676605,is_piecewise=True,range_color=['lightskyblue','yellow','orangered']))
geo.render('Geo动态涟漪散点图.html')
