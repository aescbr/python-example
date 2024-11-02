FROM python:3.10.11-slim
# Or any preferred Python version.

ENV PYTHONPATH=/app/src
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app

RUN pip install requests beautifulsoup4 python-dotenv

#CMD python -m unittest discover tests
CMD ["python", "./src/main.py"] 

# Or enter the name of your unique directory and parameter set.