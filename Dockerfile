FROM python:3.10.11-slim
# Or any preferred Python version.

ENV PYTHONPATH=/app/src
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY Pipfile .
#COPY Pipfile.lock .
RUN pip install pipenv==2023.5.19
RUN pipenv lock --pre
RUN pipenv requirements > requirements.txt

RUN pip install -r requirements.txt

COPY . /app


#CMD python -m unittest discover tests
CMD ["python", "./src/main.py"] 

# Or enter the name of your unique directory and parameter set.