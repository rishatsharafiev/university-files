FROM rabbitmq:3.7-management-alpine

MAINTAINER Rishat Sharafiev <rishatsharafiev@ya.ru>

# Set timezone
RUN apk add tzdata && cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime && echo "Europe/Moscow" >  /etc/timezone

CMD ["rabbitmq-server"]

EXPOSE 5672
