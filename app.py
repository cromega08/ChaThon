from server import stream
import argparse
import re

parser = argparse.ArgumentParser(prog="ChaThon",
                                description="A CLI Chat Application with per to per connecctions",
                                usage="ChaThon start_as [-h] [-n 1] [-ho 123.456.7.89] [-p 0000]",
                                epilog="Connect with all yout friends!")
parser.add_argument("create",
                    nargs=1,
                    choices=["c", "s", "client", "server"],
                    action="store",
                    type=str,
                    default="server",
                    metavar="start_as",
                    help="Set ChaThon to act as server or client. Options are: 'c'|'s'|'client'|'server'")
parser.add_argument("-n", "--num_clients",
                    nargs=1,
                    action="store",
                    type=int,
                    default=-1,
                    metavar="1",
                    help="port number opened by the server(required if started a server)")
parser.add_argument("-ip", "--host",
                    nargs=1,
                    action="store",
                    type=str,
                    default="",
                    metavar="123.456.7.89",
                    help="IP address of the host (required if started a client)")
parser.add_argument("-p", "--port",
                    nargs=1,
                    action="store",
                    type=int,
                    default=-1,
                    metavar="0000",
                    help="port number opened by the server(required if started a client)")

arguments = parser.parse_args()

match arguments.create[0]:

    case ("c"|"create"):

        validation = [re.search("[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}", arguments.host[0]) != None, 0 < arguments.port[0] < 65536, arguments.num_clients < 0]

        if all(validation): stream(arguments.host[0], arguments.port[0]).create_client()
        else: print("Incorrect use of client option, use \"-h\" to get help")

    case ("s"|"server"):

        validation = [arguments.host == "", arguments.port == -1, arguments.num_clients[0] > 0]

        if all(validation): stream().create_server(arguments.num_clients[0])
        else: print("Incorrect use of server option, use \"-h\" to get help")

    case _: print("Incorrect parameters, use \"-h\" to get help")