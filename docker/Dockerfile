FROM python:3.10

WORKDIR /drf_app

ENV PYTHONPATH "${PYTHONPATH}:/drf_app/"
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /drf_app/requirements.txt

RUN pip install -U pip && pip install --no-cache-dir --upgrade -r /drf_app/requirements.txt

COPY . /drf_app

EXPOSE 8001

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8001", "--settings", "core.settings.dev"]