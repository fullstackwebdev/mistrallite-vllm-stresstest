import argparse
import dill
from multiprocessing import Pool
from time import time
from typing import Iterable, List

import requests


def post_http_request(prompt: str,
                      api_url: str,
                      n: int = 1,
                      stream: bool = False) -> requests.Response:
  headers = {"User-Agent": "Test Client"}
  pload = {
      "prompt": prompt,
      "n": n,
#      "use_beam_search": True,
      "temperature": 0.0,
      "max_tokens": 1600,
      "stream": stream,
  }
  response = requests.post(api_url, headers=headers, json=pload, stream=True)
  return response


def get_response(response: requests.Response) -> List[str]:
  data = json.loads(response.content)
  output = data["text"]
  return output


def worker(prompt: str, api_url: str) -> List[str]:
  response = post_http_request(prompt, api_url, n=1)
  output = get_response(response)
  return output


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--host", type=str, default="localhost")
  parser.add_argument("--port", type=int, default=8000)
  args = parser.parse_args()

  with open("warewolfsatmall.txt", "r") as f:
    file_contents = f.read()

  chunks = []
  for i in range(0, len(file_contents), 1000):
    chunk = file_contents[i:i + 1000]
    chunks.append(chunk)

  start_time = time()

  pool = Pool(processes=20)
  results = []
  for chunk in chunks:
    result = pool.apply_async(worker, args=(chunk, f"http://{args.host}:{args.port}/generate"))
    results.append(result)

  pool.close()
  pool.join()

  end_time = time()

  total_time = end_time - start_time
  print(f"Generated 1000 tokens for each of {len(chunks)} chunks in parallel with two jobs at a time in {total_time} seconds.")

  for result in results:
    output = dill.loads(result.get())
    print(output)

