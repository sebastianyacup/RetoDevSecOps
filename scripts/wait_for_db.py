import socket
import subprocess
import time
import sys


def is_db_ready(host, port):
    try:
        socket.create_connection((host, port))
        return True
    except (socket.error, socket.timeout):
        return False


def wait_for_db(host, port, cmd):
    max_attempts = 60
    attempts = 0

    while not is_db_ready(host, port):
        if attempts >= max_attempts:
            print("Timeout waiting for the database.")
            sys.exit(1)

        print("Postgres is unavailable - sleeping")
        time.sleep(1)
        attempts += 1

    print("Postgres is up - executing command")
    subprocess.run(cmd)


if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: python wait_for_db.py <db_host> <db_port> <cmd>")
        sys.exit(1)

    db_host = sys.argv[1]
    db_port = int(sys.argv[2])
    cmd = sys.argv[3:]

    wait_for_db(db_host, db_port, cmd)
