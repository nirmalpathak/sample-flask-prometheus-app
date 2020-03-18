FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY src/ ./

RUN pip install --no-cache-dir -r requirements.txt \
	&& PYTHONPATH=. pytest --cov-report term-missing --cov=sample_app tests/test_sample_app.py \
	&& rm -rf __pycache__/

EXPOSE 5000

CMD [ "python", "./sample_app.py" ]
