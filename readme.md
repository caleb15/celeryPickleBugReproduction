## How to reproduce bug:
1. run redis (I used a docker instance for this but how you do it probably doesn't matter)
2. Confirm you can connect to redis via `redis-cli`
3. `pip install -r requirements.txt`
4. Run `celery -A tasks worker --loglevel=info` in one terminal
5. In another terminal run `python runner.py`

### Expected results:
task fails but queue continues to operate

### Actual results:
task fails and then a while later queue fails

### Other notes:

I used Python 3.7.7, not sure if that matters.

Stacktrace:
```
(fifteen5) ╭─caleb@caleb-H110M-A ~/Documents/misc/celeryPickleBug  ‹master*› 
╰─➤  celery -A tasks worker --loglevel=info                                                                                                                                                               1 ↵
 
 -------------- celery@caleb-H110M-A v4.4.5 (cliffs)
--- ***** ----- 
-- ******* ---- Linux-5.4.0-42-generic-x86_64-with-debian-buster-sid 2020-07-29 17:58:07
- *** --- * --- 
- ** ---------- [config]
- ** ---------- .> app:         tasks:0x7f8ef5433c10
- ** ---------- .> transport:   redis://localhost:6379/0
- ** ---------- .> results:     disabled://
- *** --- * --- .> concurrency: 4 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . tasks.add

[2020-07-29 17:58:07,459: INFO/MainProcess] Connected to redis://localhost:6379/0
[2020-07-29 17:58:07,465: INFO/MainProcess] mingle: searching for neighbors
[2020-07-29 17:58:08,482: INFO/MainProcess] mingle: all alone
[2020-07-29 17:58:08,494: INFO/MainProcess] celery@caleb-H110M-A ready.
[2020-07-29 17:59:56,630: INFO/MainProcess] Received task: tasks.add[a20e36a3-850d-4bef-b0f7-dd850748a5ff]  
[2020-07-29 17:59:56,632: ERROR/ForkPoolWorker-4] Task tasks.add[a20e36a3-850d-4bef-b0f7-dd850748a5ff] raised unexpected: ValidationError(b'<?xml version="1.0" encoding="UTF-8"?>\n<error>\n  <symbol>simultaneous_request</symbol>\n  <description>A change for subscription 456ee8a3881160536ad68346fe91eede is already in progress.</description>\n</error>')
Traceback (most recent call last):
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/app/trace.py", line 412, in trace_task
    R = retval = fun(*args, **kwargs)
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/app/trace.py", line 704, in __protected_call__
    return self.run(*args, **kwargs)
  File "/home/caleb/Documents/misc/celeryPickleBug/tasks.py", line 14, in add
    raise recurly.errors.ValidationError(some_xml)
recurly.errors.ValidationError
[2020-07-29 17:59:56,635: CRITICAL/MainProcess] Unrecoverable error: AttributeError("can't set attribute")
Traceback (most recent call last):
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/worker/worker.py", line 208, in start
    self.blueprint.start(self)
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/bootsteps.py", line 119, in start
    step.start(parent)
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/bootsteps.py", line 369, in start
    return self.obj.start()
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/worker/consumer/consumer.py", line 318, in start
    blueprint.start(self)
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/bootsteps.py", line 119, in start
    step.start(parent)
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/worker/consumer/consumer.py", line 599, in start
    c.loop(*c.loop_args())
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/worker/loops.py", line 83, in asynloop
    next(loop)
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/kombu/asynchronous/hub.py", line 364, in create_loop
    cb(*cbargs)
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/concurrency/asynpool.py", line 351, in on_result_readable
    next(it)
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/concurrency/asynpool.py", line 332, in _recv_message
    message = load(bufv)
AttributeError: can't set attribute
[2020-07-29 18:00:27,301: ERROR/MainProcess] Task handler raised error: WorkerLostError('Worker exited prematurely: exitcode 0.')
Traceback (most recent call last):
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/worker/worker.py", line 208, in start
    self.blueprint.start(self)
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/bootsteps.py", line 119, in start
    step.start(parent)
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/bootsteps.py", line 369, in start
    return self.obj.start()
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/worker/consumer/consumer.py", line 318, in start
    blueprint.start(self)
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/bootsteps.py", line 119, in start
    step.start(parent)
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/worker/consumer/consumer.py", line 599, in start
    c.loop(*c.loop_args())
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/worker/loops.py", line 83, in asynloop
    next(loop)
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/kombu/asynchronous/hub.py", line 364, in create_loop
    cb(*cbargs)
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/concurrency/asynpool.py", line 351, in on_result_readable
    next(it)
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/celery/concurrency/asynpool.py", line 332, in _recv_message
    message = load(bufv)
AttributeError: can't set attribute

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/caleb/.pyenv/versions/3.7.7/envs/fifteen5/lib/python3.7/site-packages/billiard/pool.py", line 1267, in mark_as_worker_lost
    human_status(exitcode)),
billiard.exceptions.WorkerLostError: Worker exited prematurely: exitcode 0.
```
