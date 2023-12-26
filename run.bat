@echo off

set parametro=%1
if "%parametro%"=="" set parametro=cuda

start cmd /c "python -m fastchat.serve.controller"
start cmd /c "python -m fastchat.serve.model_worker --model-path lmsys/fastchat-t5-3b-v1.0 --device %parametro%"
start cmd /c "python -m fastchat.serve.openai_api_server --host localhost --port 8000"
