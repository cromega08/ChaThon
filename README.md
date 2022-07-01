
# ChaThon

ChaThon it's a CLI implementation of a chat application.

Works as a ChatRoom where one of the users as like server for all participants, included itself.

It's a pure python creation and works with built-in modules of python.

## Requirements

* Python 3.10+

* XTerm terminal (this it's commonly included in linux sistems)

## Installation

The project include a setup.py file ready to use with pip.

After cloning the repository, just write:

```bash
pip install /path/to/ChaThon/folder
```

If you want to modify the files and not reinstall every time, write:

```bash
pip install -e /path/to/ChaThon/folder
```

## Usage

* To start a new ChatRoom, acting as the server

    ```bash
    chathon server -n {number of participants}
    ```

    * **Note:** ChaThon generate a random port each time. If you want to use a specific port, write:

    ```bash
    chathon server -n {number of participants} -p {positive number lower than 65000}
    ```

* To join a ChatRoom

    ```bash
    chathon client -ip {ip of the host} -p {the port activated for the host}
    ```

## Examples

* Start a server

```bash
chathon server -n 1 -p 1234
```

* Connect to a server

```bash
chathon client -p 127.0.0.1 -p 1234
```

## Authors

* [@Cromega08](https://www.github.com/cromega08)

## License

* [GNU AGPL v3.0](https://choosealicense.com/licenses/agpl-3.0/)
