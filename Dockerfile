FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY sample_app.py test_sample_app.py requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && pytest --cov=sample_app

#COPY sample_app.py .

EXPOSE 5000

CMD [ "python", "./sample_app.py" ]
