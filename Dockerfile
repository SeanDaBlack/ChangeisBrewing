FROM python:3.7-alpine

# ENV TZ=America/Chicago
# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# ARG USER=default
# ENV HOME /home/$USER

# install chromium as root
# RUN apk add chromium chromium-chromedriver

# add new user
# RUN adduser -D $USER
# USER $USER
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
# ENV PATH /home/default/.local/bin:$PATH

CMD "python3 main.py"
