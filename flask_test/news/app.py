import os
import json
from flask import Flask,render_template,abort

app=Flask(__name__)

@app.route('/')
def index():
    str=[]
    for i in os.listdir('../files'):
        with open('../files/'+i) as f:
          str.append(json.load(f)['title'])  
    return render_template('index.html',title_list=str)


@app.route('/files/<filename>')
def file(filename):
    path='../files/'+filename+'.json'
    if not os.path.exists(path):
        abort(404)
    else:
        with open(path) as f:
            item=json.load(f)
        return render_template('file.html',item_list=item)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


if __name__=='__main__':
    app.run()
