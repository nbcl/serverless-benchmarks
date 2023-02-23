import datetime
import os
import sys
import uuid
from json.decoder import JSONDecodeError

import bottle
from bottle import route, run, template, request

CODE_LOCATION='/function'

@route('/', method='POST')
def flush_log():
    begin = datetime.datetime.now()
    from function import function
    end = datetime.datetime.now()
    # FIXME: measurements?

    try:
        # The following assignment could raise a JSONDecodeError
        data = request.json

        # Error if empty JSON content or Content-Type is not application/json
        if not data:
            ret = 'Error: Empty JSON content or invalid Content-Type in request.'

        # If no parsing error is found, the data can be recieved by the handler
        else:
            ret = function.handler(data)
    except JSONDecodeError as err:
        ret = 'Error: Unable to decode JSON content in request.'

    return {
        'begin': begin.strftime('%s.%f'),
        'end': end.strftime('%s.%f'),
        "request_id": str(uuid.uuid4()),
        "is_cold": False,
        "result": {
            "output": ret
        }
    }

sys.path.append(os.path.join(CODE_LOCATION))
sys.path.append(os.path.join(CODE_LOCATION, '.python_packages/lib/site-packages/'))
run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)

