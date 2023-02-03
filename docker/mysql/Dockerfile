FROM mysql:8.0
RUN chown -R mysql:mysql /var/lib/mysql
RUN mkdir /var/log/mysql
RUN chown -R mysql:mysql /var/log/mysql
RUN chmod -R 777 /var/log/mysql
# COPY init/* /docker-entrypoint-initdb.d/
CMD ["mysqld"]
USER mysql