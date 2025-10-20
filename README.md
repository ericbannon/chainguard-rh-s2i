## Chainguard Python + OpenShift S2I Integration Test

This repository demonstrates how to use **Chainguard base images** (in this case, the Python 3.12 image) as a **Source-to-Image (S2I) builder** in OpenShift with minimal friction.

We’re testing a “**S2I-lite**” approach — keeping the clean, minimal Chainguard runtime but layering on the minimal S2I scripts required for OpenShift builds.

---

## Summary of Tests

* That OpenShift’s S2I build strategy works cleanly with Chainguard Python images.  
* That S2I assemble/run scripts can install dependencies and launch a Python app without requiring Red Hat–specific tooling.  
* That arbitrary UIDs and minimal containers (BusyBox + Python) behave correctly in OpenShift.  

---

## Usage

### 1. Build & Test in Openshift
---
Build the S2I-enabled Builder Image

```bash
oc new-build --binary --name python-cg-s2i-builder
oc start-build python-cg-s2i-builder --from-dir ./python-cg-s2i-builder --follow
```

### 2. Build the sample Flask App

```
oc new-build --strategy=source \
  --name py-s2i-test \
  --image-stream=python-cg-s2i-builder\
  --binary

oc start-build py-s2i-test --from-dir ./myapp --follow
```

### 3. Deploy the App

```
oc new-app py-s2i-test
oc expose svc/py-s2i-test
oc get route py-s2i-test -o jsonpath='{.spec.host}{"\n"}'
```

### 4. Test the browser

```
curl http://<route>/
# {"message": "Hello from Chainguard + S2I!", "hostname": "...", "environment": "dev"}
```
