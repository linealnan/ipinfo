FROM nginx:1.20-alpine

COPY ./deploy/nginx/dummy.html /etc/nginx/html/index.html

RUN rm /etc/nginx/conf.d/default.conf
COPY ./deploy/nginx/nginx.conf /etc/nginx/
