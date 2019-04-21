from static import app
from flask_dropzone import Dropzone

dropzone = Dropzone(app)

if __name__ == "__main__":
    app.run(debug=True, host= '0.0.0.0')
