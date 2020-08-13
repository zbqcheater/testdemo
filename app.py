from flask import Flask, url_for, Markup, Response, request, session, escape, redirect
from flask import render_template
import crawl_img
import os, json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('hahaha.html')


@app.route('/a', methods=['GET'])
def a():
    img_idct = {}
    files = []
    kw = request.args['keyword']
    qu = int(request.args['q'])
    base_path = os.path.abspath(os.path.dirname(__file__))  # D:\py workspace\1218flask
    s = os.listdir(base_path + '/static/img')
    if kw not in s:
        os.mkdir(base_path + '/static/img/' + kw)
        # 开始
        ci = crawl_img.CrawlImg(kw, qu)
        data = ci.start()
        for i in data:
            this_url = i['thumbURL']
            f = crawl_img.save_img(this_url, kw)
            img_idct.update({f.strip(kw + '/'): i['fromPageTitleEnc']})
            files.append(f)
        # ph = f'D:/py workspace/1218flask/static/img/{kw}/{kw}.json'
        with open(f'{base_path}' + f'/static/img/{kw}/{kw}.json', 'w') as dump_f:
            json.dump(img_idct, dump_f)
        return render_template('imgs.html', files=img_idct, kw=kw)
    else:
        with open(f'{base_path}' + f'/static/img/{kw}/{kw}.json', 'r')as load_f:
            files = json.load(load_f)
        print(type(files))
        return render_template('imgs.html', files=files, kw=kw)


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
