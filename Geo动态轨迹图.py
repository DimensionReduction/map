from pyecharts.charts import Geo
from pyecharts.globals import ChartType
from pyecharts import options as opts

z1=[('深圳','广州'),('梅州','惠州'),('韶关','清远'),('茂名','肇庆')]
z2=[['深圳','广州'],['梅州','惠州'],['韶关','清远'],['茂名','肇庆']]
print(z1,z2,sep='\n\n')

geo=Geo(init_opts=opts.InitOpts(width="1200px",height='600px'))
geo.add_schema(maptype='广东',itemstyle_opts=opts.ItemStyleOpts(color='#99CCCC',border_color='black'),label_opts=opts.LabelOpts(is_show=True))
geo.add('广东人口流动',z1,label_opts=opts.LabelOpts(is_show=False),type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(symbol_size=8,color='blue'),linestyle_opts=opts.LineStyleOpts(curve=0.3))
geo.set_global_opts(title_opts=opts.TitleOpts(title='广东人口流动轨迹图'))
geo.render('Geo动态轨迹图.html')
