from unifiticket import app
from werkzeug.serving import WSGIRequestHandler

class ScriptNameHandler(WSGIRequestHandler):
    def make_environ(self):
        environ = super().make_environ()
        script_name = environ.get('HTTP_X_SCRIPT_NAME', '')
        if script_name:
            environ['SCRIPT_NAME'] = script_name
            path_info = environ['PATH_INFO']
        if path_info.startswith(script_name):
            environ['PATH_INFO'] = path_info[len(script_name):]
        scheme = environ.get('HTTP_X_SCHEME', '')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return environ


if __name__ == "__main__":
    app.run(request_handler=ScriptNameHandler)
