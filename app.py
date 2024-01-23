import uuid
import os
from flask import *
app = Flask(__name__)

@app.route('/')
def upload():
    files = os.listdir('./media/')
    burl = request.host_url + 'media/'
    return render_template("file_upload_form.html", len = len(files), files = files, burl = burl)

@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        ext = f.filename.split('.')[-1]
        uid = str(uuid.uuid4())
        f.save(f'./media/{uid}.{ext}')
        return render_template("success.html", name = f'{request.host_url}media/{uid}.{ext}')

@app.route('/delete', methods = ['POST'])
def delete():
    if request.method == 'POST':
        file_name = request.form['filename']
        print(file_name)
        if file_name in os.listdir('./media/'):
            print("go for delete")
            os.remove(f'./media/{file_name}')
            return redirect('/', 302)

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug = True)