#!/bin/bash
#python3 -m fastchat.serve.cli --model-path lmsys/fastchat-t5-3b-v1.0 --device npu

#comandos pra api#
python3 -m fastchat.serve.controller &
python3 -m fastchat.serve.model_worker --model-path lmsys/fastchat-t5-3b-v1.0 --device $device &
sleep 30 && python3 -m fastchat.serve.openai_api_server --host localhost --port 8000
