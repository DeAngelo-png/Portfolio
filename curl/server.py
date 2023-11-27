from flask import Flask, Response, redirect, request
from gevent.pywsgi import WSGIServer
from gevent.queue import Queue

app = Flask(__name__)

ascii_art = '''
                                    ....                                        
                                .xH888888Hx.                                    
                               .H8888888888888:                                 
                               888*"""?""*88888X                                
                              'f     d8x.   ^%88k                               
                              '>    <88888X   '?8                               
                               `:..:`888888>    8>                              
                                      `"*88     X                               
                                 .xHHhx.."      !                               
┌────────────────────────       X88888888hx. ..!       ────────────────────────┐
│                              !   "*888888888"                                │
│                                     ^"***"`                                  │
│                                                                              │
│ ---- About Myself ---------------------------------------------------------- │
│                                                                              │
│   • Hi, I'm DeAngelo I like to code in my spare time for fun and to explore  │
│     computer science and languages. I know Python, Bash, a little bit of C,  │
│     and more listed below here. When I was starting to find interest in      │
│     Linux, networking, and IoT. I started off with Termux and moved on to an │
│     actual Linux machine then VPS servers.                                   │
│                                                                              │
│ ---- Knowledge ------------------------------------------------------------- │
│                                                                              │
│   :: Web Design   8/10 **********                                            │
│   :: Python       8/10 **********                                            │
│   :: Wordpress    7/10 **********                                            │
│   :: Linux        7/10 **********                                            │
│   :: Bash         7/10 **********                                            │
│   :: Exploiting   6/10 **********                                            │
│   :: C++          2/10 ********** ( SLACKING )                               │
│                                                                              │
│ ---- What I Do ------------------------------------------------------------- │
│                                                                              │
│   • Coding, Exploitation, Web Design                                         │
│                                                                              │
│ ---- Portfolio ------------------------------------------------------------- │
│                                                                              │
│   • Coming Soon                                                              │
│                                                                              │
│                                                                              │
│                                   Click Me                                   │
└──────────────────────────────────────────────────────────────────────────────┘
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
        return redirect('https://www.deangelo.tk')


if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        http_server.stop()
