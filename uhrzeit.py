#uhrzeit.py
import time
# PEP 8
class Uhr(object):
	"""Zeigt die Uhrzeit an."""
	def __init__(self):
		self.a = 0
	def dec(self):
		"""Verschoenert die Ausgabe"""
		def wrap():
			print("Jetzt betraegt die Zeit")
			print("========================")
			self.texton = self.timenow()
			print("========================")
			print("Und alle sind froh darueber")
		return wrap()
	def timenow(self):
		"""Gibt die Uhrzeit an."""
		print(time.asctime())
	def shitlisting(self):
		"""Die Funktion fuer die Uhr"""
		while True:
			self.a += 1
			self.dec()
			if self.a == 1:
				self.a = 0
				self.derp()
				break
	def derp(self):
		"""Der Zeit intervall fuer die Ausgabe"""
		while True:
			time.sleep(1)
			self.a += 1
			if self.a == 60:
				self.a = 0
				self.shitlisting()
				break