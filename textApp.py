#!/usr/bin/env python
# encoding: utf-8

import warnings
warnings.filterwarnings("ignore")
#import torch

#pip install bert-extractive-summarizer
from summarizer import Summarizer
from flask import Flask,request,jsonify
import simplejson as json


app = Flask(__name__)

result = {}

def text_summarizer(body):
    bert_model = Summarizer()
    bert_summary = ''.join(bert_model(body, min_length=60))
    return bert_summary


@app.route('/',methods = ['GET','POST'])
def text_request():
    if request.method == 'POST':
        body = request.form['q']
        print('hello')

    else :
        body = request.args.get('q')
        print(request.args)
        print(body)
        
    
    sent = text_summarizer(body)
    result['text_summarizer'] = {'summary' : sent}
 
    return jsonify(result)


if __name__=='__main__':
    app.run(debug=True)
#     app.listen(process.env.PORT || 3000, function(){
#     console.log("Express server listening on port %d in %s mode", this.address().port, app.settings.env);
#     });
