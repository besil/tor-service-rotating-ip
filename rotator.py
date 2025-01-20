import requests
import time
from stem import Signal
from stem.control import Controller
import os

control_port: int = 9051
control_password: str = os.environ.get("TOR_CONTROL_PASSWORD", "password")
tor_host: str = "191.20.0.10"  # fixed, change docker compose if you need it
renew_lease: int = int(os.environ.get("RENEW_LEASE_SECONDS", 10))

if renew_lease < 10:
    print("Renew lease must be at least 10 seconds")
    renew_lease = 10


def changeIP():
    with Controller.from_port(address=tor_host, port=control_port) as controller:
        controller.authenticate(password=control_password)
        controller.signal(Signal.NEWNYM)


if __name__ == "__main__":
    print("Renewing lease every ", renew_lease, " seconds")
    # new tor session
    tor_session = requests.session()
    tor_session.proxies = {
        "http": f"http://{tor_host}:8118",
        "https": f"http://{tor_host}:8118",
    }

    while True:
        time.sleep(renew_lease)
        changeIP()
        r = tor_session.get("http://httpbin.org/ip").json()
        print("New ip: ", r["origin"])
