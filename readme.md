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
cisco-nso-dev         5.3                 b0f08179570d        12 days ago         1.4GB
cisco-nso-dev         5.3-jtdub           b0f08179570d        12 days ago         1.4GB
cisco-nso-base        5.3                 774bf7740cbb        12 days ago         586MB
cisco-nso-base        5.3-jtdub           774bf7740cbb        12 days ago         586MB
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

## Mounting external volumes to a container

## Getting containers to talk to each other

## Docker logs

## Learning materials:
- [] https://developer.cisco.com/learning/lab/docker-101/step/1
- [] https://developer.cisco.com/learning/lab/docker-201/step/1
