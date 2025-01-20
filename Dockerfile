FROM public.ecr.aws/docker/library/python:3.13

ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
RUN pip install uv

RUN mkdir /code
WORKDIR /code

COPY pyproject.toml /code
COPY uv.lock /code
RUN uv sync --no-dev

COPY rotator.py /code/

CMD ["uv", "run", "rotator.py"]