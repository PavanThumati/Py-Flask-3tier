FROM mysql:5.7

# Copy initialization script
COPY init.sql /init.sql
COPY custom-entrypoint.sh /custom-entrypoint.sh

# Make the custom entrypoint executable
RUN chmod +x /custom-entrypoint.sh

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=userdb

# Use custom entrypoint script
ENTRYPOINT ["/custom-entrypoint.sh"]
