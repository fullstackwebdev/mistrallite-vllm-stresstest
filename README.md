
```
pip install vllm
```


```
python -m vllm.entrypoints.api_server --model TheBloke/MistralLite-7B-AWQ --quantization awq --dtype half --gpu-memory-utilization .95 --max-model-len 8192
```



```
INFO 10-26 02:48:42 llm_engine.py:624] Avg prompt throughput: 109.4 tokens/s, Avg generation throughput: 1003.7 tokens/s, Running: 18 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 8.9%, CPU KV cache usage: 0.0%
INFO:     ::1:39160 - "POST /generate HTTP/1.1" 200 OK
INFO 10-26 02:48:47 llm_engine.py:624] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 982.4 tokens/s, Running: 19 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 13.7%, CPU KV cache usage: 0.0%
INFO 10-26 02:48:52 llm_engine.py:624] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 957.3 tokens/s, Running: 18 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 17.2%, CPU KV cache usage: 0.0%
INFO 10-26 02:48:57 llm_engine.py:624] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 890.3 tokens/s, Running: 18 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 21.3%, CPU KV cache usage: 0.0%
INFO:     ::1:35284 - "POST /generate HTTP/1.1" 200 OK
INFO 10-26 02:49:02 llm_engine.py:624] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 846.3 tokens/s, Running: 19 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 25.4%, CPU KV cache usage: 0.0%
INFO:     ::1:39156 - "POST /generate HTTP/1.1" 200 OK
INFO 10-26 02:49:07 llm_engine.py:624] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 847.0 tokens/s, Running: 19 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 27.8%, CPU KV cache usage: 0.0%

```

