# Docker Talk

## Dockerfile review

Docker is a containerization technology that allows developers to package and deploy applications in a repeatable manner.

Docker containers are built from instructions in a `Dockerfile`. The `Dockerfile` tells docker what image to use to build the container, what packages to construct the container with, and how to run the application in the container.

## Building an image

Here is an example of a `Dockerfile`
```
# This tells Docker to use the Debian (Buster) based
# image loaded with Python 3.8.
FROM python:3.8-buster

# This tells Docker to execute `pip install flask`
# to install the flask python package while
# building the image.
RUN pip install flask

# This specifies the directory which to work out of.
WORKDIR /src

# This tells Docker to copy `app.py` from the host
# OS to the container in the `/src` directory.
COPY app.py .

# This is the command that Docker will execute
# while running the container.
CMD python /src/app.py
```

The `docker build` command tells docker to build a container from the instructions in the `Dockerfile`. There are many options that can be invoked to build an image. The `-t` option is the most common. The `-t` option, or `--tag` option allows the user to diferentiate and version container images.

```
% docker build -t ntc-docker-app-demo:01 .
[+] Building 0.9s (9/9) FINISHED
 => [internal] load .dockerignore                                                                                         0.0s
 => => transferring context: 2B                                                                                           0.0s
 => [internal] load build definition from Dockerfile                                                                      0.0s
 => => transferring dockerfile: 36B                                                                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.8-buster                                                      0.9s
 => [internal] load build context                                                                                         0.0s
 => => transferring context: 28B                                                                                          0.0s
 => [1/4] FROM docker.io/library/python:3.8-buster@sha256:0598f5cb3942c525325099fc6f4e6111e75c2043701d9f76147321ff0c3a34  0.0s
 => CACHED [2/4] RUN pip install flask                                                                                    0.0s
 => CACHED [3/4] WORKDIR /src                                                                                             0.0s
 => CACHED [4/4] COPY app.py .                                                                                            0.0s
 => exporting to image                                                                                                    0.0s
 => => exporting layers                                                                                                   0.0s
 => => writing image sha256:8aea11ce54a633df6f3002e76bb6abb87f7218e0218b4067b18333c87dc52c1f                              0.0s
 => => naming to docker.io/library/ntc-docker-app-demo:01
```

When the image is done building, you will be able to see it in your local inventory of images.

```
% docker images
REPOSITORY            TAG                 IMAGE ID            CREATED             SIZE
ntc-docker-app-demo   01                  8aea11ce54a6        27 minutes ago      892MB
```

## Running a container

Running a container is easy. There are a number of arguments that can be utilized to run a container.

```
% docker run --help

Usage:	docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

Run a command in a new container

Options:
      --add-host list                  Add a custom host-to-IP mapping (host:ip)
  -a, --attach list                    Attach to STDIN, STDOUT or STDERR
      --blkio-weight uint16            Block IO (relative weight), between 10 and 1000, or 0 to disable (default 0)
      --blkio-weight-device list       Block IO weight (relative device weight) (default [])
      --cap-add list                   Add Linux capabilities
      --cap-drop list                  Drop Linux capabilities
      --cgroup-parent string           Optional parent cgroup for the container
      --cidfile string                 Write the container ID to the file
      --cpu-period int                 Limit CPU CFS (Completely Fair Scheduler) period
      --cpu-quota int                  Limit CPU CFS (Completely Fair Scheduler) quota
      --cpu-rt-period int              Limit CPU real-time period in microseconds
      --cpu-rt-runtime int             Limit CPU real-time runtime in microseconds
  -c, --cpu-shares int                 CPU shares (relative weight)
      --cpus decimal                   Number of CPUs
      --cpuset-cpus string             CPUs in which to allow execution (0-3, 0,1)
      --cpuset-mems string             MEMs in which to allow execution (0-3, 0,1)
  -d, --detach                         Run container in background and print container ID
      --detach-keys string             Override the key sequence for detaching a container
      --device list                    Add a host device to the container
      --device-cgroup-rule list        Add a rule to the cgroup allowed devices list
      --device-read-bps list           Limit read rate (bytes per second) from a device (default [])
      --device-read-iops list          Limit read rate (IO per second) from a device (default [])
      --device-write-bps list          Limit write rate (bytes per second) to a device (default [])
      --device-write-iops list         Limit write rate (IO per second) to a device (default [])
      --disable-content-trust          Skip image verification (default true)
      --dns list                       Set custom DNS servers
      --dns-option list                Set DNS options
      --dns-search list                Set custom DNS search domains
      --domainname string              Container NIS domain name
      --entrypoint string              Overwrite the default ENTRYPOINT of the image
  -e, --env list                       Set environment variables
      --env-file list                  Read in a file of environment variables
      --expose list                    Expose a port or a range of ports
      --gpus gpu-request               GPU devices to add to the container ('all' to pass all GPUs)
      --group-add list                 Add additional groups to join
      --health-cmd string              Command to run to check health
      --health-interval duration       Time between running the check (ms|s|m|h) (default 0s)
      --health-retries int             Consecutive failures needed to report unhealthy
      --health-start-period duration   Start period for the container to initialize before starting health-retries
                                       countdown (ms|s|m|h) (default 0s)
      --health-timeout duration        Maximum time to allow one check to run (ms|s|m|h) (default 0s)
      --help                           Print usage
  -h, --hostname string                Container host name
      --init                           Run an init inside the container that forwards signals and reaps processes
  -i, --interactive                    Keep STDIN open even if not attached
      --ip string                      IPv4 address (e.g., 172.30.100.104)
      --ip6 string                     IPv6 address (e.g., 2001:db8::33)
      --ipc string                     IPC mode to use
      --isolation string               Container isolation technology
      --kernel-memory bytes            Kernel memory limit
  -l, --label list                     Set meta data on a container
      --label-file list                Read in a line delimited file of labels
      --link list                      Add link to another container
      --link-local-ip list             Container IPv4/IPv6 link-local addresses
      --log-driver string              Logging driver for the container
      --log-opt list                   Log driver options
      --mac-address string             Container MAC address (e.g., 92:d0:c6:0a:29:33)
  -m, --memory bytes                   Memory limit
      --memory-reservation bytes       Memory soft limit
      --memory-swap bytes              Swap limit equal to memory plus swap: '-1' to enable unlimited swap
      --memory-swappiness int          Tune container memory swappiness (0 to 100) (default -1)
      --mount mount                    Attach a filesystem mount to the container
      --name string                    Assign a name to the container
      --network network                Connect a container to a network
      --network-alias list             Add network-scoped alias for the container
      --no-healthcheck                 Disable any container-specified HEALTHCHECK
      --oom-kill-disable               Disable OOM Killer
      --oom-score-adj int              Tune host's OOM preferences (-1000 to 1000)
      --pid string                     PID namespace to use
      --pids-limit int                 Tune container pids limit (set -1 for unlimited)
      --platform string                Set platform if server is multi-platform capable
      --privileged                     Give extended privileges to this container
  -p, --publish list                   Publish a container's port(s) to the host
  -P, --publish-all                    Publish all exposed ports to random ports
      --read-only                      Mount the container's root filesystem as read only
      --restart string                 Restart policy to apply when a container exits (default "no")
      --rm                             Automatically remove the container when it exits
      --runtime string                 Runtime to use for this container
      --security-opt list              Security Options
      --shm-size bytes                 Size of /dev/shm
      --sig-proxy                      Proxy received signals to the process (default true)
      --stop-signal string             Signal to stop a container (default "SIGTERM")
      --stop-timeout int               Timeout (in seconds) to stop a container
      --storage-opt list               Storage driver options for the container
      --sysctl map                     Sysctl options (default map[])
      --tmpfs list                     Mount a tmpfs directory
  -t, --tty                            Allocate a pseudo-TTY
      --ulimit ulimit                  Ulimit options (default [])
  -u, --user string                    Username or UID (format: <name|uid>[:<group|gid>])
      --userns string                  User namespace to use
      --uts string                     UTS namespace to use
  -v, --volume list                    Bind mount a volume
      --volume-driver string           Optional volume driver for the container
      --volumes-from list              Mount volumes from the specified container(s)
  -w, --workdir string                 Working directory inside the container
```

To run a simple container, the arguments `-i`, or `--interactive`, `-t`, or `--tty`, and `--name` are the most common minimum arguments.
```
% docker run -it --name ntc-demo ntc-docker-app-demo:01
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Running a container with these arguments keeps your terminal locked to the container STDOUT. In another terminal, you can see the status of the container. You can also attempt to connect to the containers listening TCP port, but will be unable to, since we haven't exposed a port for the docker container to listen to.

```
% docker ps -a
CONTAINER ID        IMAGE                    COMMAND                  CREATED             STATUS              PORTS               NAMES
eaef9d1b977b        ntc-docker-app-demo:01   "/bin/sh -c 'python …"   2 minutes ago       Up 2 minutes                            ntc-demo

% curl localhost:5000
curl: (7) Failed to connect to localhost port 5000: Connection refused
```
## Exposing a container to the world

To expose the containers tcp port to external environments, will need to allow the port to be exposed in the `Dockerfile`, build a new image, and then run the new image; telling docker to expose the port.

In the `Dockerfile`, a new instruction will need to be added, telling docker to expose a tcp/ip port to the container. I've also modified the `Dockerfile` for a couple flask specific arguments.

```
FROM python:3.8-buster

RUN pip install flask

WORKDIR /src

COPY app.py .

ENV FLASK_APP=/src/app.py

EXPOSE 5000/tcp

CMD python -m flask run --host=0.0.0.0
```
With the `Dockerfile` modified, the docker image can be updated with the new instruction sets.

```
% docker build -t ntc-docker-app-demo:02 .
[+] Building 0.8s (9/9) FINISHED
 => [internal] load build definition from Dockerfile                                                                      0.0s
 => => transferring dockerfile: 37B                                                                                       0.0s
 => [internal] load .dockerignore                                                                                         0.0s
 => => transferring context: 2B                                                                                           0.0s
 => [internal] load metadata for docker.io/library/python:3.8-buster                                                      0.7s
 => [1/4] FROM docker.io/library/python:3.8-buster@sha256:0598f5cb3942c525325099fc6f4e6111e75c2043701d9f76147321ff0c3a34  0.0s
 => [internal] load build context                                                                                         0.0s
 => => transferring context: 28B                                                                                          0.0s
 => CACHED [2/4] RUN pip install flask                                                                                    0.0s
 => CACHED [3/4] WORKDIR /src                                                                                             0.0s
 => CACHED [4/4] COPY app.py .                                                                                            0.0s
 => exporting to image                                                                                                    0.0s
 => => exporting layers                                                                                                   0.0s
 => => writing image sha256:474bbcfaf555631e92d474c84b822850fb102bc8153df381464bed409aaffae6                              0.0s
 => => naming to docker.io/library/ntc-docker-app-demo:02
```
With the image upated, the old container can be stopped. Since we executed the container in interactive mode and didn't detatch from the container, we can use CNTRL-C to stop the container and then use the `docker rm` to remove the container.

```
% docker rm ntc-demo
ntc-demo
```

Now we can start up the new container, adding the `-p` or `--publish` flag to expose the tcp/ip port that we wish to expose to the outside world.

```
% docker run -it --name ntc-demo -p 5000:5000 ntc-docker-app-demo:02
 * Serving Flask app "/src/app.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

With the updated container running, we can use another terminal to see that docker is exposing the tcp/ip port.

```
% docker ps -a
CONTAINER ID        IMAGE                    COMMAND                  CREATED             STATUS              PORTS                    NAMES
c40ed8c8cab7        ntc-docker-app-demo:02   "/bin/sh -c 'python …"   5 minutes ago       Up 5 minutes        0.0.0.0:5000->5000/tcp   ntc-demo
```

We can also use `curl` to test the connection.

```
% curl -i localhost:5000
HTTP/1.0 405 METHOD NOT ALLOWED
Content-Type: text/html; charset=utf-8
Allow: POST, OPTIONS
Content-Length: 178
Server: Werkzeug/1.0.1 Python/3.8.6
Date: Tue, 01 Dec 2020 15:39:07 GMT

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>

% curl -i -X POST localhost:5000
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 228
Server: Werkzeug/1.0.1 Python/3.8.6
Date: Tue, 01 Dec 2020 15:39:22 GMT

[
    {
        "id": 1,
        "name": "joe",
        "balance": 10
    },
    {
        "id": 2,
        "name": "bob",
        "balance": -1
    },
    {
        "id": 3,
        "name": "fred",
        "balance": 40
    }
]% 
```
You should also be able to see logs indicating the connections as well.

```
172.17.0.1 - - [01/Dec/2020 15:39:22] "POST / HTTP/1.1" 200 -
```

## Mounting external volumes to a container

It's often handy to be able to have data read on storage that's external to the container. It can make the container smaller and can make the container more flexible. The downside is that the container can only run on hosts that have access to the data that the container needs to access.

To simulate this, we'll offload the data that the flask app uses and store it as a json file outside of the container.

Code before change:

```python
#!/usr/bin/env python3

import json
from flask import Flask


app = Flask(__name__)

@app.route("/", methods=["POST"])
def get_balance():
	data = [
		{"id": 1, "name": "joe", "balance": 10},
		{"id": 2, "name": "bob", "balance": -1},
		{"id": 3, "name": "fred", "balance": 40},
	]

	return json.dumps(data, indent=4)


if __name__ == "__main__":
	app.run()
```

JSON file:

```
% cat ./data/data.json
[
    {"id": 1, "name": "joe", "balance": 10},
    {"id": 2, "name": "bob", "balance": -1},
    {"id": 3, "name": "fred", "balance": 40}
]
```

Code after change:

```python
#!/usr/bin/env python3

import json
from flask import Flask


app = Flask(__name__)

@app.route("/", methods=["POST"])
def get_balance():

	with open("./data/data.json") as f:
		data = json.loads(f.read())

	return json.dumps(data, indent=4)


if __name__ == "__main__":
	app.run()
```

With the JSON data pulled out and the code modified, we just need to update the image.

```
% docker build -t ntc-docker-app-demo:03 .
[+] Building 1.1s (9/9) FINISHED
 => [internal] load .dockerignore                                                                                         0.0s
 => => transferring context: 2B                                                                                           0.0s
 => [internal] load build definition from Dockerfile                                                                      0.0s
 => => transferring dockerfile: 37B                                                                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.8-buster                                                      0.9s
 => [1/4] FROM docker.io/library/python:3.8-buster@sha256:0598f5cb3942c525325099fc6f4e6111e75c2043701d9f76147321ff0c3a34  0.0s
 => [internal] load build context                                                                                         0.0s
 => => transferring context: 317B                                                                                         0.0s
 => CACHED [2/4] RUN pip install flask                                                                                    0.0s
 => CACHED [3/4] WORKDIR /src                                                                                             0.0s
 => [4/4] COPY app.py .                                                                                                   0.0s
 => exporting to image                                                                                                    0.0s
 => => exporting layers                                                                                                   0.0s
 => => writing image sha256:0d72789132d0037e3a3a43c8a8c4d0c840eec06f3963975e102ea649a59d5c6d                              0.0s
 => => naming to docker.io/library/ntc-docker-app-demo:03
```
Now, when we run the container, we need to specify the external volume to mount. This is done with the `-v` or `--volume` argument.
```
% docker run -it --name ntc-demo -p 5000:5000 -v ${PWD}/data:/src/data ntc-docker-app-demo:03
 * Serving Flask app "/src/app.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```
`${PWD}/data` maps the local data path to the container `/src/data` path.

Issuing a `curl` should result in the same result as the previous test.
```
% curl -i -X POST localhost:5000
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 228
Server: Werkzeug/1.0.1 Python/3.8.6
Date: Tue, 01 Dec 2020 21:16:57 GMT

[
    {
        "id": 1,
        "name": "joe",
        "balance": 10
    },
    {
        "id": 2,
        "name": "bob",
        "balance": -1
    },
    {
        "id": 3,
        "name": "fred",
        "balance": 40
    }
]%
```
The JSON can be modified, with the container running and a subsequent `curl` request will display the updated content.
```
% cat data/data.json
[
    {"id": 1, "name": "joe", "balance": 10},
    {"id": 2, "name": "bob", "balance": -1},
    {"id": 3, "name": "fred", "balance": 40},
    {"id": 4, "name": "ed", "balance": 20}
]
```
```
% curl -i -X POST localhost:5000
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 302
Server: Werkzeug/1.0.1 Python/3.8.6
Date: Tue, 01 Dec 2020 21:20:14 GMT

[
    {
        "id": 1,
        "name": "joe",
        "balance": 10
    },
    {
        "id": 2,
        "name": "bob",
        "balance": -1
    },
    {
        "id": 3,
        "name": "fred",
        "balance": 40
    },
    {
        "id": 4,
        "name": "ed",
        "balance": 20
    }
]%
```
## Getting containers to talk to each other
Docker containers can communicate to other containers. By default, all containers are spun up on `bridge` network (172.17.0.0/16).
```
% docker network inspect bridge
[
    {
        "Name": "bridge",
        "Id": "6cf132e1e0b4db3c54c610e0fd5166f57d8f8d5827a9f29429da129019e51864",
        "Created": "2020-11-11T21:41:55.799662895Z",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {},
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]
```
Any container on this network can ping and communicate with any other container by IP. If the containers know the name of another container on the network, it can ping it by name as well.

To test this, spin up two containers. The second container will utilize the `--link` flag to specify the name of another container to connect to.
```
% docker run -itd --name ntc1 ntc-docker-app-demo:03
ab94eb0c4f39cf22548d7d960e837fb10e1f94f4ae272eb03cd1b8b612eff2a5
% docker run -itd --name ntc2 --link ntc1 ntc-docker-app-demo:03
19ff532dd5988d3e28249c64ba087cad9009de6731ba9c506f4897a90c405f6b
```
Connect to the shell of the second container.
```
% docker exec -it ntc2 bash
```
In the shell you will notice that the containers `/etc/hosts` was updated with the entry of `ntc1`. Docker performed this action when the `--link` argument was passed.
```
root@19ff532dd598:/src# cat /etc/hosts
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
172.17.0.2	ntc1 ab94eb0c4f39
172.17.0.3	19ff532dd598
```
This allows you to communicate with the neighboring container by name.
```
root@19ff532dd598:/src# ping -c 2 ntc1
PING ntc1 (172.17.0.2) 56(84) bytes of data.
64 bytes from ntc1 (172.17.0.2): icmp_seq=1 ttl=64 time=0.089 ms
64 bytes from ntc1 (172.17.0.2): icmp_seq=2 ttl=64 time=0.281 ms

--- ntc1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 36ms
rtt min/avg/max/mdev = 0.089/0.185/0.281/0.096 ms
```
DNS, however, does not know how to resolve to `ntc1`:
```
root@19ff532dd598:/src# dig ntc1

; <<>> DiG 9.11.5-P4-5.1+deb10u2-Debian <<>> ntc1
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 13916
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;ntc1.				IN	A

;; Query time: 1 msec
;; SERVER: 192.168.65.1#53(192.168.65.1)
;; WHEN: Tue Dec 01 21:43:37 UTC 2020
;; MSG SIZE  rcvd: 22
```
The corresponding `ntc1` container does not know how to communicate with `ntc2` by name, because it was not spun up with the `--link` argument. The `--link` argument can not be issued until the container being linked exists. It can communicate with the corresponding container by IP, however.
```
root@ab94eb0c4f39:/src# ping ntc2
ping: ntc2: Name or service not known
root@ab94eb0c4f39:/src# ping -c 3 172.17.0.3
PING 172.17.0.3 (172.17.0.3) 56(84) bytes of data.
64 bytes from 172.17.0.3: icmp_seq=1 ttl=64 time=0.235 ms
64 bytes from 172.17.0.3: icmp_seq=2 ttl=64 time=0.126 ms
64 bytes from 172.17.0.3: icmp_seq=3 ttl=64 time=0.220 ms

--- 172.17.0.3 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 50ms
rtt min/avg/max/mdev = 0.126/0.193/0.235/0.050 ms
```
With that in mind, let's create a container that fetches the data from the `ntc-docker-app-demo` and presents some data.
```
% docker build -t ntc-docker-app1-demo:01 -f Dockerfile1 .
[+] Building 5.8s (9/9) FINISHED
 => [internal] load build definition from Dockerfile1                                                                     0.0s
 => => transferring dockerfile: 215B                                                                                      0.0s
 => [internal] load .dockerignore                                                                                         0.0s
 => => transferring context: 2B                                                                                           0.0s
 => [internal] load metadata for docker.io/library/python:3.8-buster                                                      0.8s
 => CACHED [1/4] FROM docker.io/library/python:3.8-buster@sha256:0598f5cb3942c525325099fc6f4e6111e75c2043701d9f76147321f  0.0s
 => [internal] load build context                                                                                         0.0s
 => => transferring context: 459B                                                                                         0.0s
 => [2/4] RUN pip install flask requests                                                                                  4.6s
 => [3/4] WORKDIR /src                                                                                                    0.0s
 => [4/4] COPY app1.py .                                                                                                  0.0s
 => exporting to image                                                                                                    0.3s
 => => exporting layers                                                                                                   0.3s
 => => writing image sha256:889097ab766ffbadeb91c8e47536a4be49d82380660e140724e01f779c4f80aa                              0.0s
 => => naming to docker.io/library/ntc-docker-app1-demo:01
```
```
% docker images
REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
ntc-docker-app1-demo   01                  889097ab766f        24 seconds ago      895MB
ntc-docker-app-demo    03                  0d72789132d0        About an hour ago   892MB
ntc-docker-app-demo    02                  474bbcfaf555        8 hours ago         892MB
ntc-docker-app-demo    01                  8aea11ce54a6        8 hours ago         892MB
```
The new app is simple. It simply performs an HTTP GET to `ntc1` and returns the results.
```
#!/usr/bin/env python

import json
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def accounts():
	return json.dumps(requests.get('http://ntc1:5000').json(), indent=2)


if __name__ == "__main__":
	app.run()
```
With the new image created, we can spin up the two containers and watch their interactions.
```
% docker run -itd --name ntc1 -v ${PWD}/data:/src/data ntc-docker-app-demo:03
fc419fca7f4ae6d40bce55677674af6a9a5ee38aa56dd0a38b9c3ceaf3fcadb8
% docker run -itd --name ntc2 --link ntc1 -p 5000:5000 ntc-docker-app1-demo:01
bde63fa7ed47cb870ec93d57e9a9c46955947c436fda11d45613be5a716e4ef4
```
We can verify that the containers are running.
```
% docker ps -a
CONTAINER ID        IMAGE                     COMMAND                  CREATED             STATUS              PORTS                    NAMES
3f11adba93e8        ntc-docker-app1-demo:01   "/bin/sh -c 'python …"   56 seconds ago      Up 54 seconds       0.0.0.0:5000->5000/tcp   ntc2
fc419fca7f4a        ntc-docker-app-demo:03    "/bin/sh -c 'python …"   7 minutes ago       Up 7 minutes        5000/tcp                 ntc1
```
We can use `curl` to fetch the data from `ntc2`, which is listening on tcp port 5000.
```
% curl -i localhost:5000
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 238
Server: Werkzeug/1.0.1 Python/3.8.6
Date: Tue, 01 Dec 2020 22:38:32 GMT

[
  {
    "id": 1,
    "name": "joe",
    "balance": 10
  },
  {
    "id": 2,
    "name": "bob",
    "balance": -1
  },
  {
    "id": 3,
    "name": "fred",
    "balance": 40
  },
  {
    "id": 4,
    "name": "ed",
    "balance": 20
  }
]%
```

## Docker logs
Docker logs can be used to determine what is happening within a container. We can use the logs to see the network communications between `ntc1` and `ntc2` and the curl client to `ntc2`.
```
% docker logs ntc1
 * Serving Flask app "/src/app.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.17.0.3 - - [01/Dec/2020 22:30:45] "GET / HTTP/1.1" 200 -
172.17.0.3 - - [01/Dec/2020 22:34:48] "GET / HTTP/1.1" 200 -
172.17.0.3 - - [01/Dec/2020 22:36:35] "GET / HTTP/1.1" 200 -
172.17.0.3 - - [01/Dec/2020 22:38:32] "GET / HTTP/1.1" 200 -
% docker logs ntc2
 * Serving Flask app "/src/app1.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.17.0.1 - - [01/Dec/2020 22:36:35] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [01/Dec/2020 22:38:32] "GET / HTTP/1.1" 200 - 
```
As you can see, `docker logs` can be useful for troubleshooting container problems.

## Learning materials:
- [] https://developer.cisco.com/learning/lab/docker-101/step/1
- [] https://developer.cisco.com/learning/lab/docker-201/step/1
