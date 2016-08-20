# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:18:16 2016

@author: winpython
"""

import os
from flask import Flask, request, send_file, send_from_directory
from werkzeug import secure_filename
from run_v5_predict import run
import numpy as np


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/'
app.config['ALLOWED_EXTENSIONS'] = set(['jpeg','jpg'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1] in app.config['ALLOWED_EXTENSIONS']



@app.route("/",methods=['get','POST'])
def index():
    if request.method == 'POST' :
        file = request.files['file']
    
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('uploaded_file',filename = filename))
            tag = ['青椒牛肉燴飯','牛肉燴飯','滑蛋牛肉燴飯','滑蛋羊肉燴飯','雞腿飯'
                    ,'雞排飯','排骨飯','鱈魚飯','卡拉雞腿飯','裹粉排骨飯','蠔油香菇雞'
                    ,'黑胡椒牛柳','青菜豆腐湯','糖醋排骨','辣子雞丁','五更腸旺'
                    ,'牛肉炒麵','肉絲炒麵','蛋花湯','燕丸湯']
            ans = run(filename)
            
            return  tag[ans]
    return'''
    <doctype html>
    <title>test upload</title>
    <h1>Upload</h1>
    <form action="" method="post" enctype=multipart/form-data>
        <p><input type=file name=file>
           <input type=submit name=upload></p>
    </form>
    '''

@app.route("/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__ == "__main__" :
    app.run(host='120.125.83.91',port=80)