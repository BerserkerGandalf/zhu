from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

import csv, re, operator

# from textblob import TextBlob

app = Flask(__name__)

person = {
    'name': '祝祥瑞',
    'address': '湖北省·宜昌市',
    'job': '在校学生',
    'tel': '123456789',
    'email': '123456789@yahoo.com',
    'description': '我身体健康，性格随和，五官端正，不怕苦不怕累。两年多的程序员生活锻炼了我坚强的意志，缜密的思维，以及强的抗压性;我做事有耐心，并且乐于学习新知识，更注重巩固旧知识。作为一名程序员，更重要的品质就是要懂得团队合作，而我恰好拥有团队合作精神，对工作认真负责。 　',
    'social_media': [
        {
            'link': 'https://www.facebook.com/nono',
            'icon': 'fa-facebook-f'
        },
        {
            'link': 'https://github.com/nono',
            'icon': 'fa-github'
        },
        {
            'link': 'linkedin.com/in/nono',
            'icon': 'fa-linkedin-in'
        },
        {
            'link': 'https://twitter.com/nono',
            'icon': 'fa-twitter'
        }
    ],
    'img': 'img/img_nono.jpg',
    'experiences': [
        {
            'title': 'python爬虫爬取图片',
            'description': '用python爬虫爬取网页上的图片，并将图片以文件格式打包，保存到本地文件中',
            'timeframe': '2020.10-2020.12'
        },
        {
            'title': 'web商城',
            'description': '实现web商城的制作，能实现基本的购物，支付，登录，加入购物车等功能',
            'timeframe': '2019.9-2019.12'
        },
        {
            'title': '文本识别微信小程序',
            'description': '制作文本识别的微信小程序，实现文本识别，文字编辑，文字翻译等多种功能',
            'timeframe': '2021.4-2021.6'
        }
    ],
    'education': [
        {
            'university': '湖北师范大学',
            'description': '软件工程',
            'timeframe': '2018 - 2022'
        },
    ],
    'programming_languages': {
        'HMTL': ['fa-html5', '100'],
        'CSS': ['fa-css3-alt', '100'],
        'SASS': ['fa-sass', '90'],
        'JS': ['fa-js-square', '90'],
        'Wordpress': ['fa-wordpress', '80'],
        'Python': ['fa-python', '70'],
        'Mongo DB': ['fa-database', '60'],
        'MySQL': ['fa-database', '60'],
        'NodeJS': ['fa-node-js', '50']
    },
    'languages': {'French': 'Native', 'English': 'Professional', 'Spanish': 'Professional',
                  'Italian': 'Limited Working Proficiency'},
    'interests': ['Dance', 'Travel', 'Languages']
}


@app.route('/')
def cv(person=person):
    return render_template('index.html', person=person)


@app.route('/callback', methods=['POST', 'GET'])
def cb():
    return gm(request.args.get('data'))


@app.route('/chart')
def index():
    return render_template('chartsajax.html', graphJSON=gm())


def gm(地区='北京'):
    df = pd.read_csv('./14-19年各省高考分数线.csv')
    fig = px.line(df[df['地区']==地区], x="年份", y="分数线",color="批次",line_group="考生类别")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@app.route('/iris')
def iris():
    return render_template('iris.html',graphJSON=ir(),graphJSON1=ir1())

def ir():
    df=pd.DataFrame(px.data.iris())
    fig = px.scatter(df,x='sepal_length',y='sepal_width',color='species')
    graphJSON = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def ir1():
    df = pd.DataFrame(px.data.iris())
    fig = px.density_heatmap(df, x='sepal_length', y='sepal_width',marginal_x='rug',marginal_y='histogram')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@app.route('/gapminder')
def gapminder():
    return render_template('gapminder.html', graphJSON=gap(),graphJSON1=gap1(),graphJSON2=gap2())

def gap():
    df = pd.DataFrame(px.data.gapminder())
    fig = px.scatter(df, x='gdpPercap', y='lifeExp',color='continent')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gap1():
    df = pd.DataFrame(px.data.gapminder())
    fig = px.scatter(df, x='gdpPercap', y='lifeExp',size_max=60,color='continent',hover_name='country',
                     animation_frame='year',animation_group='country',log_x=True,range_x=[100,100000],range_y=[25,90],
                     labels=dict(pop="Population",gdpPercap="GDP per Capita",lifeExp="life Expectancy"))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gap2():
    df = pd.DataFrame(px.data.gapminder())
    fig = px.choropleth(df, locations="iso_alpha", color="lifeExp",
                        hover_name="country", animation_frame="year",
                        range_color=[20, 80], projection="natural earth")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@app.route('/tips')
def tips():
    return render_template('tips.html', graphJSON=tp(),graphJSON1=tp1(),graphJSON2=tp2())

def tp():
    df = pd.DataFrame(px.data.tips())
    fig = px.parallel_categories(df, color="size", color_continuous_scale=px.colors.sequential.Inferno)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def tp1():
    df = pd.DataFrame(px.data.tips())
    fig = px.scatter(df, x="total_bill", y="tip",color="size",facet_col="sex")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def tp2():
    df = pd.DataFrame(px.data.tips())
    fig = px.box(df,x="day",y="total_bill",color="smoker",notched=True)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@app.route('/wind')
def wind():
    return render_template('wind.html', graphJSON=wd(),graphJSON1=wd1(),graphJSON2=wd2())

def wd():
    df = pd.DataFrame(px.data.wind())
    fig = px.scatter_polar(df,r="frequency",theta="direction",color="strength",symbol="strength"
                      ,color_discrete_sequence=px.colors.sequential.Plasma_r)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def wd1():
    df = pd.DataFrame(px.data.wind())
    fig = px.line_polar(df, r="frequency", theta="direction", color="strength", line_close=True
                        , color_discrete_sequence=px.colors.sequential.Plasma_r)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def wd2():
    df = pd.DataFrame(px.data.wind())
    fig = px.bar_polar(df, r="frequency", theta="direction", color="strength", template="plotly_dark"
                       , color_discrete_sequence=px.colors.sequential.Plasma_r)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
# @app.route('/senti')
# def main():
#     text = ""
#     values = {"positive": 0, "negative": 0, "neutral": 0}
#
#     with open('ask_politics.csv', 'rt') as csvfile:
#         reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
#         for idx, row in enumerate(reader):
#             if idx > 0 and idx % 2000 == 0:
#                 break
#             if 'text' in row:
#                 nolinkstext = re.sub(
#                     r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''',
#                     '', row['text'], flags=re.MULTILINE)
#                 text = nolinkstext
#
#             blob = TextBlob(text)
#             for sentence in blob.sentences:
#                 sentiment_value = sentence.sentiment.polarity
#                 if sentiment_value >= -0.1 and sentiment_value <= 0.1:
#                     values['neutral'] += 1
#                 elif sentiment_value < 0:
#                     values['negative'] += 1
#                 elif sentiment_value > 0:
#                     values['positive'] += 1
#
#     values = sorted(values.items(), key=operator.itemgetter(1))
#     top_ten = list(reversed(values))
#     if len(top_ten) >= 11:
#         top_ten = top_ten[1:11]
#     else:
#         top_ten = top_ten[0:len(top_ten)]
#
#     top_ten_list_vals = []
#     top_ten_list_labels = []
#     for language in top_ten:
#         top_ten_list_vals.append(language[1])
#         top_ten_list_labels.append(language[0])
#
#     graph_values = [{
#         'labels': top_ten_list_labels,
#         'values': top_ten_list_vals,
#         'type': 'pie',
#         'insidetextfont': {'color': '#FFFFFF',
#                            'size': '14',
#                            },
#         'textfont': {'color': '#FFFFFF',
#                      'size': '14',
#                      },
#     }]

    # layout = {'title': '<b>意见挖掘</b>'}

    # return render_template('sentiment.html', graph_values=graph_values, layout=layout)


if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)
