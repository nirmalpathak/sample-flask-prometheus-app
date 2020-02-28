FROM python:3.7-alpine

WORKDIR /usr/src/app

#COPY sample_app.py test_sample_app.py requirements.txt ./
COPY src/ ./
#RUN pip install --no-cache-dir -r requirements.txt && pytest --cov=sample_app
RUN pwd && ls && pip install --no-cache-dir -r requirements.txt && PYTHONPATH=. pytest --cov=sample_app tests/test_sample_app.py

#COPY sample_app.py .

EXPOSE 5000

CMD [ "python", "./sample_app.py" ]
