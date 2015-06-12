from flask import Flask, render_template
from os.path import join

from app_config import COPY_PATH

import copytext

main = Flask(__name__, static_url_path='/static')

def url_for_static(filename):
    root = main.config.get('STATIC_ROOT', 'static')
    return join(root, filename)

@main.route('/')
def index():
    context = {
        'COPY': copytext.Copy(COPY_PATH)
    }

    return render_template('index.html', **context)
    return main.send_static_file('index.html')

# RUN APP
if __name__ == '__main__':
	main.debug = True
	main.run()
