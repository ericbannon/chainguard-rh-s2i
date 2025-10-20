# Chainguard Python + OpenShift S2I Integration Test

This repository demonstrates how to use Chainguard base images (in this case, the Python 3.12 image) as a Source-to-Image (S2I) builder in OpenShift with minimal friction.

We’re testing a “S2I-lite” approach — keeping the clean, minimal Chainguard runtime but layering on the minimal S2I scripts required for OpenShift builds.

---

## Summary of Tests

* That OpenShift’s S2I build strategy works cleanly with Chainguard Python images.  
* That S2I assemble/run scripts can install dependencies and launch a Python app without requiring Red Hat–specific tooling.  
* That arbitrary UIDs and minimal containers (BusyBox + Python) behave correctly in OpenShift.  

---

## Usage Steps

Chainguard Python-based S2I image here: https://hub.docker.com/repository/docker/bannimal/python-cg-s2i-builder/tags

# Sample Test using public repo builder image

```
oc new-project s2i 2>/dev/null || oc project s2i

oc new-build --strategy=source --name py-s2i-test \
  --image=docker.io/bannimal/python-cg-s2i-builder:v8 --binary

oc start-build py-s2i-test --from-dir ./myapp --follow --wait
oc new-app py-s2i-test
oc expose svc/py-s2i-test
oc get route py-s2i-test -o jsonpath='{.spec.host}{"\n"}'
```

# Full configuration for Openshift

```
# apply configurations
oc apply -f openshift/

# build from your source dir 
oc start-build py-s2i-test --from-dir ./myapp --follow --wait

# DC auto-rolls out (Option A). If you used plain Deployment (Option B), do:
# oc rollout restart deploy/py-s2i-app

# get the URL
oc get route py-s2i-app -o jsonpath='{.spec.host}{"\n"}'
```

Expected output:

```
ROUTE=$(oc get route py-s2i-app -o jsonpath='{.spec.host}')
curl -sS "http://$ROUTE" | head
{"environment":"dev","hostname":"py-s2i-app-5-sc89n","message":"Hello from Chainguard + S2I!"}
```