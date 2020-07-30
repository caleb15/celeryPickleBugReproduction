from celery import Celery
import recurly

app = Celery("tasks", broker="redis://localhost:6379/0")


@app.task
def add(x, y):
    some_xml = b"""<?xml version="1.0" encoding="UTF-8"?>
<error>
  <symbol>simultaneous_request</symbol>
  <description>A change for subscription 456ee8a3881160536ad68346fe91eede is already in progress.</description>
</error>"""
    raise recurly.errors.ValidationError(some_xml)
    return x + y
