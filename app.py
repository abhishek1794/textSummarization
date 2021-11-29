#!/usr/bin/env python
# encoding: utf-8

import warnings
warnings.filterwarnings("ignore")
#import torch

#pip install bert-extractive-summarizer
from summarizer import Summarizer
from flask import Flask,request,jsonify, render_template
import simplejson as json


app = Flask(__name__)

result = {}

def text_summarizer(body):
    bert_model = Summarizer()
    bert_summary = ''.join(bert_model(body))
    return bert_summary


@app.route('/',methods = ['POST','GET'])
def text_request():
    try:
        if request.method == 'POST':
            body = request.form['content']
            print('hello')

        else:
            body = request.args.get('content')
            print(request.args)
            print(body)
        
        sent = text_summarizer(body)
        result['text_summarizer'] = {'summary' : sent}
 
        return jsonify(result)


    except:
        content = "Please input text"
        return render_template('index.html', tasks= content)
        
    
if __name__=='__main__':
    app.run(debug=True)
#     app.listen(process.env.PORT || 3000, function(){
#     console.log("Express server listening on port %d in %s mode", this.address().port, app.settings.env);
#     });
