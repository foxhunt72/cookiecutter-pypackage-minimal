FROM python:latest

WORKDIR /usr/src/app

COPY . .

RUN pip install . && pip install -r requirements-dev.txt
RUN useradd --uid 1000 -m user
USER user
WORKDIR /home/user
ENTRYPOINT ["/usr/local/bin/{{ cookiecutter.project_name }}"]
#docker buildx build --platform linux/arm64,linux/amd64 --tag rdevos72/{{ cookiecutter.project_name }}:latest --tag rdevos72/{{ cookiecutter.project_name }}:{{ cookiecutter.package_version }} --push .
