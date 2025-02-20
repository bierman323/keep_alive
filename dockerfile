FROM python:3.9-slim

RUN pip install pyautogui

COPY keep_awake.py /app/keep_awake.py

WORKDIR /app

CMD ["python", "keep_awake.py"]