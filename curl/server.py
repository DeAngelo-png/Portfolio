from flask import Flask, Response, redirect, request
from gevent.pywsgi import WSGIServer
from gevent.queue import Queue

app = Flask(__name__)

ascii_art = '''
\x1b[32mroot@hotbockets\x1b[37m:\x1b[34m~\x1b[37m$ \x1b[37m
                              \x1b[36m      ....                                        
                              \x1b[36m  .xH888888Hx.                                    
                              \x1b[36m .H8888888888888:                                 
                              \x1b[36m 888*"""?""*88888X                                
                              \x1b[36m'f     d8x.   ^%88k                               
                              \x1b[36m'>    <88888X   '?8                               
                              \x1b[36m `:..:`888888>    8>                              
                              \x1b[36m        `"*88     X                               
                              \x1b[36m   .xHHhx.."      !                               
\x1b[37m┌────────────────────────     \x1b[36m  X88888888hx. ..!       \x1b[37m────────────────────────┐
\x1b[37m│                             \x1b[36m !   "*888888888"                                \x1b[37m│
\x1b[37m│                             \x1b[36m        ^"***"`                                  \x1b[37m│
\x1b[37m│                                                                              \x1b[37m│
\x1b[37m│ ---- About Myself ---------------------------------------------------------- \x1b[37m│
\x1b[37m│                                                                              \x1b[37m│
\x1b[37m│   • Hi, I'm DeAngelo I like to code in my spare time for fun and to explore  \x1b[37m│
\x1b[37m│     computer science and languages. I know Python, Bash, a little bit of C,  \x1b[37m│
\x1b[37m│     and more listed below here. When I was starting to find interest in      \x1b[37m│
\x1b[37m│     Linux, networking, and IoT. I started off with Termux and moved on to an \x1b[37m│
\x1b[37m│     actual Linux machine then VPS servers.                                   \x1b[37m│
\x1b[37m│                                                                              \x1b[37m│
\x1b[37m│ ---- Knowledge ------------------------------------------------------------- \x1b[37m│
\x1b[37m│                                                                              \x1b[37m│
\x1b[37m│   \x1b[33m:: \x1b[37mWeb Design   8/10 \x1b[33m********\x1b[37m**                                            \x1b[37m│
\x1b[37m│   \x1b[33m:: \x1b[37mPython       8/10 \x1b[33m********\x1b[37m**                                            \x1b[37m│
\x1b[37m│   \x1b[33m:: \x1b[37mWordpress    7/10 \x1b[33m*******\x1b[37m***                                            \x1b[37m│
\x1b[37m│   \x1b[33m:: \x1b[37mLinux        7/10 \x1b[33m*******\x1b[37m***                                            \x1b[37m│
\x1b[37m│   \x1b[33m:: \x1b[37mBash         7/10 \x1b[33m*******\x1b[37m***                                            \x1b[37m│
\x1b[37m│   \x1b[33m:: \x1b[37mC++          2/10 \x1b[33m**\x1b[37m********                                            \x1b[37m│
\x1b[37m│                                                                              \x1b[37m│
\x1b[37m│ ---- What I Do ------------------------------------------------------------- \x1b[37m│
\x1b[37m│                                                                              \x1b[37m│
\x1b[37m│   • Coding, Exploitation, Web Design                                         \x1b[37m│
\x1b[37m│                                                                              \x1b[37m│
\x1b[37m│ ---- Portfolio ------------------------------------------------------------- \x1b[37m│
\x1b[37m│                                                                              \x1b[37m│
\x1b[37m│   • Coming Soon                                                              \x1b[37m│
\x1b[37m│                                                                              \x1b[37m│
\x1b[37m│                                                                              \x1b[37m│
\x1b[37m│                                                                              \x1b[37m│
\x1b[37m└──────────────────────────────────────────────────────────────────────────────┘
'''

stream_queue = Queue()


def streamer():
    yield "\033[2J\033[3J\033[H" + ascii_art


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent', '')
    if 'curl' in user_agent.lower():
        return Response(streamer(), content_type='text/plain; charset=utf-8')
    else:
        return redirect('https://deangelo.ftp.sh')


if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        http_server.stop()
