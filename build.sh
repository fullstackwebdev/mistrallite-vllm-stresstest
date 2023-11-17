cd vllm
DOCKER_BUILDKIT=1 docker build . --target vllm --tag vllm-openai:latest --build-arg max_jobs=8

# After running this command, the vllm-openai:latest image will be available for Docker Compose to use as specified in the docker-compose.yml file. Remember to replace any file paths or other configurations in the Docker Compose file to suit your specific setup.

# DOCKER_BUILDKIT=1 docker build . --target vllm --tag vllm --build-arg max_jobs=8
# docker build --target vllm-openai -t vllm-openai:latest .

# docker run --runtime nvidia --gpus all -v /home/fullstack/models:/models -p 6000:6000 vllm-openai --quantization awq --model /models/OpenHermes-2.5-Mistral-7B-16k-AWQ --dtype half --gpu-memory-utilization .95 --max-model-len 8192 --port 6000 --served-model-name gpt-3.5-turbo
