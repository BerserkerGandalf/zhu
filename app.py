from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

import csv, re, operator

# from textblob import TextBlob

app = Flask(__name__)

person = {
    'name': '李凯',
    'address': '银河系·太阳系·m78·洛圣都',
    'job': '程序猿',
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
            'title': '程序员',
            'company': '华为',
            'description': '为HarmonyOS的发展奠定基础',
            'timeframe': '2015.4--2016.8'
        },
        {
            'title': '项目主官',
            'company': '网易',
            'description': '担任过抖音的制作',
            'timeframe': '2016.9-2018.2'
        },
        {
            'title': '部门经理',
            'company': '腾讯',
            'description': '负责王者荣耀、DNF、CF等多个大型网游的管理工作',
            'timeframe': '2018.5--'
        }
    ],
    'education': [
        {
            'university': '清华大学',
            'degree': '学士',
            'description': '多次荣获国家奖',
            'timeframe': '2008 - 2012'
        },
        {
            'university': '新加坡国立大学',
            'degree': '硕士',
            'description': '参与过多个大型实验室，完成过多个大型项目',
            'timeframe': '2012-2015'
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


# @app.route('/callback', methods=['POST', 'GET'])
# def cb():
#     return gm(request.args.get('data'))
#
#
# @app.route('/chart')
# def index():
#     return render_template('chartsajax.html', graphJSON=gm())
#
#
# def gm(country='United Kingdom'):
#     df = pd.DataFrame(px.data.gapminder())
#
#     fig = px.line(df[df['country'] == country], x="year", y="gdpPercap")
#
#     graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#     return graphJSON


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
