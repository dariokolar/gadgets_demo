"""

This script read messages from the TURRIS:DONGLE and send them to http server via get

"""

from __future__ import print_function
import sys
import datetime
import urllib2
import urllib

from device import Device

url = 'http://samle.cz/collect.php'

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        device_name = "/dev/ttyUSB0"
    else:
        device_name = sys.argv[1]
    print("Using '{0}' as input device".format(device_name), file=sys.stderr)
    device = Device(device=device_name)
    reader = device.gen_lines()
    while True:
        line = reader.next()
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        values = {}
        values["data"] = date + " " + line
        values["key"] = "--- YOUR API KEY ---"
        data = urllib.urlencode(values)
        request = urllib2.Request(url + "?" + data)
        response = urllib2.urlopen(request)
