import cv2
import cvzone
from flask import Flask, request,flash, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

upload = 'static/uploads'

app.config['UPLOAD'] = upload

cloth = ''

def button_matching(button_Id):
    match button_Id:
        case 'cloth1':
            return '1.PNG'
        case 'cloth2':
            return '2.PNG'
        case 'cloth3':
            return '3.PNG'
        case 'cloth4':
            return '4.PNG'
        case 'cloth5':
            return '5.PNG'
        case 'cloth6':
            return '6.PNG'
        case 'cloth7':
            return '7.PNG'
        case 'cloth8':
            return '8.PNG'
        case 'cloth9':
            return '9.png'
        case default:
            return ''

@app.route('/', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        if 'file' not in request.files or request.files['file'].filename == '':
            flash('No file selected for uploading')
            return render_template('render.html')

        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD'], filename))
        button_id = request.form.get('item')
        cloth = button_matching(button_id)
        if cloth == '':
            flash('Please select a cloth to try on')
        else:
            imgdisp = male_try(filename,cloth)
            if imgdisp is None:
                flash("Please select an appropriate image")
            else:
                cv2.imwrite('static/uploads/output.png',imgdisp)
                return send_from_directory(app.config['UPLOAD'], 'output.png')
    return render_template('render.html')

def male_try(filename,cloth_name):
    from cvzone.PoseModule import PoseDetector

    detector = PoseDetector()

    cap = cv2.imread("static/uploads/"+filename)

    fixedRatio = 460/190
    shirtRatioHeightWidth = 680 / 650

    img = detector.findPose(cap, draw=False)
    if img is None:
        return


    lmList, bboxInfo = detector.findPosition(cap , draw=False)


    imgShirt = cv2.imread("static/used/"+cloth_name,cv2.IMREAD_UNCHANGED)
    if len(lmList) < 11:
        return

    lm11 = lmList[11][1:3]
    lm12 = lmList[12][1:3]

    widthOfShirt = int((lm11[0] - lm12[0]) * fixedRatio)
    print(widthOfShirt)
    imgShirt = cv2.resize(imgShirt, (widthOfShirt, int( widthOfShirt * shirtRatioHeightWidth)))
    currentScale = (lm11[0] - lm12[0]) / 190
    offset = int(142 * currentScale), int(112 * currentScale)


    img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))

    cv2.imwrite('static/upload/manasclot.png', img)
    return img
if __name__ == '__main__':
    app.run('0.0.0.0',5001,debug=False)
