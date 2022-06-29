from server import stream
import argparse
import re

parser = argparse.Argumentparser(prog="Chyt",
                                description="A CLI Chat Application with per to per connecctions",
                                usage="One of the users need to init the connection, after oter people could connect",
                                epilog="Connect with all yout friends!")

parser.add_argument("create",
                    nargs=1,
                    choices=["c", "s", "client", "server"],
                    action="store",
                    type=str,
                    default="server",
                    required=True,
                    metavar="[client|server]",
                    help="Set Chyt to act as server or client")
parser.add_argument("-n", "--num_clients",
                    nargs=1,
                    action="store",
                    type=int,
                    metavar="1",
                    help="port number opened by the server(required if started a server)")
parser.add_argument("-h", "--host",
                    nargs=1,
                    action="store",
                    type=str,
                    metavar="123.456.7.89",
                    help="IP address of the host (required if started a client)")
parser.add_argument("-p", "--port",
                    nargs=1,
                    action="store",
                    type=int,
                    metavar="0000",
                    help="port number opened by the server(required if started a client)")

arguments = parser.parse_args()

match arguments.create:

    case ("c"|"create"):

        validation = [re.search("[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}", arguments.host) != None, 0 < arguments.port < 65536]

        if all(validation): stream(arguments.host, arguments.port).create_client()

    case ("s"|"server"):

        if arguments.num_clients > 0: stream().create_server()

    case _: print("Incorrect parameters, use \"-h\" to get help")