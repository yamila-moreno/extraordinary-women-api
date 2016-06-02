import bottle
from api.women import *

app = bottle.app()
bottle.route('/extraordinary_women', 'GET', list_women)
bottle.route('/extraordinary_women', 'POST', add_woman)
bottle.route('/extraordinary_women/<woman_id>', 'GET', get_woman)
bottle.route('/extraordinary_women/<woman_id>', 'DELETE', delete_woman)

if __name__ == '__main__':
    bottle.run(app=app, host='0.0.0.0',port=8000)
