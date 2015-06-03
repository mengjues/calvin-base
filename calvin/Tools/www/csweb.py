# -*- coding: utf-8 -*-

# Copyright (c) 2015 Ericsson AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import SimpleHTTPServer
import SocketServer
import argparse

def parse_arguments():
    long_description = """
  Start web server.
  """

    argparser = argparse.ArgumentParser(description=long_description)
    argparser.add_argument('-p', '--port', metavar='<port>', type=int, dest='port',
                           help='port# of tcp server', default=8000)
    return argparser.parse_args()

def main():
    os.chdir(os.path.dirname(__file__))
    args = parse_arguments()
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", args.port), Handler)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
