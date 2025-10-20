FROM cgr.dev/chainguard/python:latest-dev

USER root
# Let arbitrary UID/GID write during S2I builds
RUN mkdir -p /usr/libexec/s2i /opt/app \
 && chmod -R 0777 /usr/libexec/s2i /opt/app

# S2I scripts (non-privileged assemble + proper run)
COPY s2i/ /usr/libexec/s2i/
RUN chmod +x /usr/libexec/s2i/*

# Ensure pip user installs (gunicorn, etc.) are on PATH
ENV PATH="/home/nonroot/.local/bin:${PATH}"

# Default port for your apps; OpenShift will detect EXPOSE for Services
ENV PORT=8080
EXPOSE 8080

WORKDIR /opt/app
USER 65532

# 👇 This makes the final app image start via your S2I run script automatically
ENTRYPOINT ["/usr/libexec/s2i/run"]