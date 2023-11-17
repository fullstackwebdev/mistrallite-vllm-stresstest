
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

```
(base) ➜  vllm git:(master) ✗ python -m vllm.entrypoints.openai.api_server --help
usage: api_server.py [-h] [--host HOST] [--port PORT] [--allow-credentials] [--allowed-origins ALLOWED_ORIGINS] [--allowed-methods ALLOWED_METHODS] [--allowed-headers ALLOWED_HEADERS] [--served-model-name SERVED_MODEL_NAME] [--model MODEL]
                     [--tokenizer TOKENIZER] [--revision REVISION] [--tokenizer-revision TOKENIZER_REVISION] [--tokenizer-mode {auto,slow}] [--trust-remote-code] [--download-dir DOWNLOAD_DIR] [--load-format {auto,pt,safetensors,npcache,dummy}]
                     [--dtype {auto,half,float16,bfloat16,float,float32}] [--max-model-len MAX_MODEL_LEN] [--worker-use-ray] [--pipeline-parallel-size PIPELINE_PARALLEL_SIZE] [--tensor-parallel-size TENSOR_PARALLEL_SIZE] [--block-size {8,16,32}]
                     [--seed SEED] [--swap-space SWAP_SPACE] [--gpu-memory-utilization GPU_MEMORY_UTILIZATION] [--max-num-batched-tokens MAX_NUM_BATCHED_TOKENS] [--max-num-seqs MAX_NUM_SEQS] [--disable-log-stats] [--quantization {awq,None}]
                     [--engine-use-ray] [--disable-log-requests] [--max-log-len MAX_LOG_LEN]

vLLM OpenAI-Compatible RESTful API server.

options:
  -h, --help            show this help message and exit
  --host HOST           host name
  --port PORT           port number
  --allow-credentials   allow credentials
  --allowed-origins ALLOWED_ORIGINS
                        allowed origins
  --allowed-methods ALLOWED_METHODS
                        allowed methods
  --allowed-headers ALLOWED_HEADERS
                        allowed headers
  --served-model-name SERVED_MODEL_NAME
                        The model name used in the API. If not specified, the model name will be the same as the huggingface name.
  --model MODEL         name or path of the huggingface model to use
  --tokenizer TOKENIZER 
                        name or path of the huggingface tokenizer to use
  --revision REVISION   the specific model version to use. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version.
  --tokenizer-revision TOKENIZER_REVISION
                        the specific tokenizer version to use. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version.
  --tokenizer-mode {auto,slow}
                        tokenizer mode. "auto" will use the fast tokenizer if available, and "slow" will always use the slow tokenizer.
  --trust-remote-code   trust remote code from huggingface
  --download-dir DOWNLOAD_DIR
                        directory to download and load the weights, default to the default cache dir of huggingface
  --load-format {auto,pt,safetensors,npcache,dummy}
                        The format of the model weights to load. "auto" will try to load the weights in the safetensors format and fall back to the pytorch bin format if safetensors format is not available. "pt" will load the weights in the pytorch
                        bin format. "safetensors" will load the weights in the safetensors format. "npcache" will load the weights in pytorch format and store a numpy cache to speed up the loading. "dummy" will initialize the weights with random
                        values, which is mainly for profiling.
  --dtype {auto,half,float16,bfloat16,float,float32}
                        data type for model weights and activations. The "auto" option will use FP16 precision for FP32 and FP16 models, and BF16 precision for BF16 models.
  --max-model-len MAX_MODEL_LEN
                        model context length. If unspecified, will be automatically derived from the model.
  --worker-use-ray      use Ray for distributed serving, will be automatically set when using more than 1 GPU
  --pipeline-parallel-size PIPELINE_PARALLEL_SIZE, -pp PIPELINE_PARALLEL_SIZE
                        number of pipeline stages
  --tensor-parallel-size TENSOR_PARALLEL_SIZE, -tp TENSOR_PARALLEL_SIZE
                        number of tensor parallel replicas
  --block-size {8,16,32}
                        token block size
  --seed SEED           random seed
  --swap-space SWAP_SPACE
                        CPU swap space size (GiB) per GPU
  --gpu-memory-utilization GPU_MEMORY_UTILIZATION
                        the percentage of GPU memory to be used forthe model executor
  --max-num-batched-tokens MAX_NUM_BATCHED_TOKENS
                        maximum number of batched tokens per iteration
  --max-num-seqs MAX_NUM_SEQS
                        maximum number of sequences per iteration
  --disable-log-stats   disable logging statistics
  --quantization {awq,None}, -q {awq,None}
                        Method used to quantize the weights
  --engine-use-ray      use Ray to start the LLM engine in a separate process as the server process.
  --disable-log-requests
                        disable logging requests
  --max-log-len MAX_LOG_LEN
                        max number of prompt characters or prompt ID numbers being printed in log. Default: unlimited.
(base) ➜  vllm git:(master) ✗ 
