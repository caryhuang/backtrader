import sys
import os
import subprocess

for subdir, dirs, files in os.walk(r'.'):
	for folder in dirs:
		if not folder.endswith("__pycache__"):
			os.chdir(folder)
			for script in os.listdir("."):
				if not script.endswith("__pycache__") and not script.endswith(".ipynb"):
					#os.system(mypython + " " + script)
					if script.endswith("ib-cash-bid-ask.py"):
						print("=====> Skipping " + script + " because it requires communication to Interactive Broker for LIVE trading <=====")
					elif script.endswith("ibtest.py"):
						print("=====> Skipping " + script + " because it requires communication to Interactive Broker for LIVE trading <=====")
					elif script.endswith("oandatest.py"):
						print("=====> Skipping " + script + " because it requires communication to OANDA broker for LIVE trading <=====")
					elif script.endswith("observers-default.py"):
						print("=====> Skipping " + script + " because it requires matplotlib in python 3.9 to work <=====")
					elif script.endswith("resample-tickdata.py"):
						print("=====> Skipping " + script + " because it requires matplotlib in python 3.9 to work <=====")
					elif script.endswith("pyfoliotest.py"):
						print("=====> Skipping " + script + " because it contains outdated usages of pyfolio lib <=====")
					elif script.endswith("macd-settings.py"):
						print("=====> Running " + script + " <=====")
						subprocess.run(["python", script, "--data", "../../datas/yhoo-2003-2005.txt"], stdout=subprocess.DEVNULL)
					elif script.endswith("order_target.py"):
						print("=====> Running " + script + " <=====")
						subprocess.run(["python", script, "--target-percent"], stdout=subprocess.DEVNULL)
					elif script.endswith("yahoo-test.py") or script.endswith("sigsmacross.py") or script.endswith("tcal.py"):
						print("=====> Running " + script + " <=====")
						subprocess.run(["python", script, "--data", "../../datas/yhoo-2003-2005.txt", "--fromdate", "2003-01-01", "--todate", "2004-05-05"], stdout=subprocess.DEVNULL)
					elif script.endswith("weekdaysaligner.py"):
						print("=====> Running " + script + " <=====")
						subprocess.run(["python", script, "--data0", "../../datas/yhoo-2003-2005.txt"], stdout=subprocess.DEVNULL)
					elif script.endswith("vctest.py"):
						print("=====> Running " + script + " <=====")
						subprocess.run(["python", script, "--data0", "../../datas/yhoo-2003-2005.txt"], stdout=subprocess.DEVNULL)
					elif script.endswith("tcal-intra.py"):
						print("=====> Running " + script + " <=====")
						subprocess.run(["python", script, "--data0", "../../datas/yhoo-2003-2005.txt"], stdout=subprocess.DEVNULL)
					elif script.endswith("stop-loss-approaches.py"):
						print("=====> Running " + script + " <=====")
						subprocess.run(["python", script, "auto"], stdout=subprocess.DEVNULL)
					else:	
						print("=====> Running " + script + " <=====")
						subprocess.run(["python", script], stdout=subprocess.DEVNULL)
			os.chdir("../")
