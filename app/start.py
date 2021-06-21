"""Application entry point: Main app"""

from app.server import init_server


def main() -> None:
    # spin up the server
    init_server()


if __name__ == "__main__":
    main()
