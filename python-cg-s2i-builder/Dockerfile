FROM cgr.dev/chainguard/python:latest

USER root

LABEL io.openshift.s2i.scripts-url="image:///usr/libexec/s2i" \
      io.openshift.s2i.destination="/tmp/src"

# Prepare S2I script dir and app dir; make them OK for OpenShift arbitrary UID
RUN mkdir -p /usr/libexec/s2i /opt/app \
 && chgrp -R 0 /usr/libexec/s2i /opt/app || true \
 && chmod -R g+rwX /usr/libexec/s2i /opt/app || true

COPY s2i/ /usr/libexec/s2i/
RUN chmod +x /usr/libexec/s2i/*

WORKDIR /opt/app
USER 65532
