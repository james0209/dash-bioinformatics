FROM python:3.8.5

ENV DASH_DEBUG_MODE True
COPY ./app /app
WORKDIR /app
RUN pip install --trusted-host pypi.python.org -r app/requirements.txt
EXPOSE 8050
CMD ["python", "index.py"]