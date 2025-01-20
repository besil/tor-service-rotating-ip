# Tor Service Rotating IP

This project sets up a service that periodically changes the IP address used for outgoing requests through the Tor network. It uses a Dockerized environment to run a Tor proxy and a Python script that handles the IP rotation.

## Components

- **Tor Proxy**: A Docker container running a Tor proxy server.
- **IP Rotator**: A Python script that connects to the Tor control port to request a new IP address at regular intervals.

## How It Works

1. The Tor proxy container exposes ports for HTTP, SOCKS, and control access.
2. The IP Rotator script runs in a separate container and periodically sends a signal to the Tor control port to change the IP address.
3. The script then makes a request to `http://httpbin.org/ip` to verify and print the new IP address.

## Configuration

- **TOR_CONTROL_PASSWORD**: Password for the Tor control port (default: `password`).
- **RENEW_LEASE_SECONDS**: Interval in seconds to renew the IP address (default: `10` seconds, minimum: `10` seconds).

## Usage

1. Set up the environment variables `TOR_CONTROL_PASSWORD` and `RENEW_LEASE_SECONDS` as needed.
2. Build and run the Docker containers using `docker-compose`.

For example:

```sh
RENEW_LEASE_SECONDS=15 docker-compose up --remove-orphans --build
```

The IP address will be renewed at the specified interval, and the new IP will be printed to the console.

## Disclaimer

This project was done for educational purposes. Use it at your own risk and responsibility.

