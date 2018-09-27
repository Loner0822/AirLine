from pyecharts import GeoLines, Style


style = Style(
    title_top="#fff",
    title_pos = "center",
    width=1200,
    height=600,
    background_color="#404a59"
)

style_geo = style.add(
    is_label_show=True,
    line_curve=0.2,
    line_opacity=0.6,
    legend_text_color="#eee",
    legend_pos="right",
    geo_effect_symbol="plane",
    geo_effect_symbolsize=15,
    label_color=['#a6c84c', '#ffa022', '#46bee9'],
    label_pos="right",
    label_formatter="{b}",
    label_text_color="#eee",
)

data_zhengzhou = [
    ["郑州", "广州"],
    ["郑州", "深圳"],
    ["郑州", "珠海"],
    ["郑州", "福州"],
    ["郑州", "厦门"],
    ["郑州", "温州"],
    ["郑州", "大连"],
    ["郑州", "海口"],
    ["郑州", "三亚"],
    ["郑州", "上海"],
    ["郑州", "晋江"],
    ["郑州", "宁波"],
    ["郑州", "青岛"],
    ["郑州", "杭州"],
    ["郑州", "成都"],
    ["郑州", "贵阳"],
    ["郑州", "昆明"],
    ["郑州", "南宁"],
    ["郑州", "重庆"],
    ["郑州", "哈尔滨"],
    ["郑州", "沈阳"],
    ["郑州", "乌鲁木齐"],
    ["郑州", "北京"],
    ["郑州", "桂林"],
    ["郑州", "西宁"],
    ["郑州", "天津"],
#    ["郑州", "丽江"],
    ["郑州", "南昌"],
#    ["郑州", "乌兰察布"],
    ["郑州", "南通"],
    ["郑州", "呼和浩特"],
    ["郑州", "包头"],
    ["郑州", "克拉玛依"],
    ["郑州", "阿勒泰"],
    ["郑州", "库尔勒"],
    ["郑州", "海拉尔"],
    ["郑州", "拉萨"],
    ["郑州", "烟台"],
    ["郑州", "绵阳"],
    ["郑州", "银川"],
    ["郑州", "长春"],
    ["郑州", "遵义"],
    ["郑州", "阿克苏"],
 #   ["郑州", "博鳌"],
    ["郑州", "大理"],
    ["郑州", "东营"],
    ["郑州", "鄂尔多斯"],
    ["郑州", "哈密"],
    ["郑州", "合肥"],
    ["郑州", "黄山"],
    ["郑州", "六盘水"],
    ["郑州", "梅县"],
    ["郑州", "南京"],
    ["郑州", "汕头"],
    ["郑州", "邵阳"],
    ["郑州", "铜仁"],
    ["郑州", "吐鲁番"],
#    ["郑州", "乌拉浩特"],
    ["郑州", "襄阳"],
    ["郑州", "延吉"],
    ["郑州", "湛江"],
    ["郑州", "常德"],
    ["郑州", "柳州"],
    ["郑州", "台州"]
]
geolines = GeoLines("郑州机场航线图", **style.init_style)
geolines.add("从郑州出发", data_zhengzhou, maptype='world', is_legend_show=False, **style_geo)
geolines.render()
