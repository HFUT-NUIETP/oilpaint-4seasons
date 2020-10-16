from flask import Flask
import os
import base64
app = Flask(__name__)

@app.route('/demo', method = ['POST'])
def demo(img, model):
    img_ori = base64.b64decode(img, txt)
    with open('./input/input.jpg', 'wb') as f:
        f.write(img_ori)
    if model == 0:
        # winter2summer
        nm_model = 'models/winter2summer.pb'
    elif model == 1:
        nm_model = 'models/summer2winter.pb'
    else:
        return -1
    cmd = ['python', '--model']
    cmd_run = cmd[0] + ' ' + 'main.py' + ' ' + cmd[1] + ' ' + nm_model
    os.system(cmd_run)

    with open('output/output.jpg', 'rb') as f:
        img_return = f.read()
    img_return_decode = base64.b64encode(img_return)

    return img_return_decode