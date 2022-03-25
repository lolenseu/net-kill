import os

while True:
  print("Starting...")
  os.system('wget https://speed.hetzner.de/100MB.bin && rm -rf 100MB.bin')
  print("Done!")
  os.system('clear')
