import os
import sys
import webbrowser

osOSX = sys.platform.startswith('darwin')
osLinux = sys.platform.startswith('linux')
osWin = 'win' in sys.platform and not osOSX

if osWin:
	pydio_runtime_data = r"%APPDATA%\Pydio"
else:
	raise NotImplementedError

pydio_runtime_data =  os.path.expandvars(pydio_runtime_data)

with open(os.path.join(pydio_runtime_data, "ports_config")) as ports_config:
	_ = ports_config.readline()
	config = ports_config.readline()
	pydio, port, user, password = config.split(':')
	if pydio != "pydio":
		raise NotImplementedError
	webbrowser.open("http://%s:%s@localhost:%s/" % (user, password, port))

