from flask import Flask,render_template
import os
from flask_wtf import FlaskForm
from wtforms import FileField,SubmitField
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

class UploadFileForm(FlaskForm):
    audio = FileField("Audio File")
    submit = SubmitField("Upload File")


app.config['UPLOAD_FOLDER'] = 'static/images'

@app.route('/',methods=['GET',"POST"])
def home():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'abc.png')
    form = UploadFileForm()
    if form.validate_on_submit():
        audio = form.audio.data
        audio_filename = secure_filename(audio.filename)
        audio.save(os.path.join(app.config['UPLOAD_FOLDER'], audio_filename))
        return "File Uploaded Successfully."
    return render_template('index.html',user_image = pic1,form=form)


if __name__=="__main__":
    app.run(debug=True)
