from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from nestaweb import app
from nestautils import send_notification
import sys
import os
import tornado.options as options

args = sys.argv
args.append("--log_file_prefix=" + os.environ['HOME'] + "/nestaweb.log")
options.parse_command_line(args)

http_server = HTTPServer(WSGIContainer(app), xheaders=True)
http_server.listen(8080)
IOLoop.instance().start()

