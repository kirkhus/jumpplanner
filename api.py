import time
import os

from esipy import EsiApp
from esipy import EsiClient
from esipy import EsiSecurity

class Api:

    _client = None
    _app = None
    _security = None
    _sleep = 0
    _retry = 5

    def __init__(self):    
        self._app = EsiApp().get_latest_swagger

        self._security = EsiSecurity(
            redirect_uri='http://localhost',
            client_id=os.environ['client_id'],
            secret_key=os.environ['secret_key'],
            headers={'User-Agent': 'lars@kirkhus.org'},
            )

        self._client = EsiClient(
            retry_requests=True,
            headers={'User-Agent': 'lars@kirkhus.org'},
            security=self._security
            )

        self._security.update_token({
                'access_token': '',  # leave this empty
                'expires_in': -1,  # seconds until expiry, so we force refresh anyway
                'refresh_token': os.environ['refresh_token']
                })

    def op(self, op_name, **arguments):
        time.sleep(self._sleep)
        op = self._app.op[op_name](**arguments)

        result = self._client.request(op)
        
        if result.status == 200:
            return result.data
        
        if result.status >= 500 and self._retry > 0:
            self._sleep += 1000
            self._retry -= 1
            print(op, " failed, retrying in ", self._sleep/1000, " seconds, ", self._retry, " attempts left", flush=True)
            return self.op(op, **arguments)

        return None

    



    

