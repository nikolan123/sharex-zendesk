from flask import Flask, request, json
from PIL import Image
import requests
import io
import os
from os.path import splitext
import secrets


secret_key = 'secret'
allowed_extension = ['.png', '.jpeg', '.jpg', '.gif']
zenurl = "https://datasupport.nysed.gov/api/v2/uploads.json"

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        if request.form.to_dict(flat=False)['secret_key'][0] == secret_key:
            file = request.files['image']
            extension = splitext(file.filename)[1]
            file.flush()
            size = os.fstat(file.fileno()).st_size
            if extension not in allowed_extension:
                return 'File type is not supported', 415

            elif size > 47185920:
                return 'File size too large', 400

            else:
                image = Image.open(file)
                data = list(image.getdata())
                file_without_exif = Image.new(image.mode, image.size)
                file_without_exif.putdata(data)
                filename = secrets.token_urlsafe(5)
                byte_io = io.BytesIO()
                file_without_exif.save(byte_io, format=image.format)
                imgbytes = byte_io.getvalue()
                byte_io.close()
                req = requests.post(f"{zenurl}?filename={filename}", headers={"Content-Type": "image/png"}, data=imgbytes)
                return json.dumps({"url": req.json()['upload']['attachments'][0]['mapped_content_url']}), 200
        else:
            print(request.form.to_dict(flat=False)['secret_key'][0])
            return 'Unauthorized use', 401


if __name__ == '__main__':
    app.run(port=80)
