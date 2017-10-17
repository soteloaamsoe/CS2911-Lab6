"""

A simple HTTP client
"""

# import the "socket" module -- not using "from socket import *" in order to selectively use items with "socket." prefix
import socket

# import the "regular expressions" module
import re


def main():
    """
    Tests the client on a variety of resources
    """

    # These resource request should result in "Content-Length" data transfer
    get_http_resource('http://seprof.sebern.com/', 'index.html')
    get_http_resource('http://seprof.sebern.com/sebern1.jpg', 'sebern1.jpg')

    # this resource request should result in "chunked" data transfer
    get_http_resource('http://seprof.sebern.com/courses/cs2910-2014-2015/sched.md','sched-file.md')

    # Port 8080 no longer offered by seprof.sebern.com -- this resource will time out
#    get_http_resource('http://seprof.sebern.com:8080/sebern1.jpg', 'sebern2.jpg') 


def tcp_send(server_host, server_port,request):
    """
    - Send multiple messages over a TCP connection to a designated host/port
    - Receive a one-character response from the 'server'
    - Print the received response
    - Close the socket

    :param str server_host: name of the server host machine
    :param int server_port: port number on server to send to
    :authors: Alaa Gaw
    """

    # start the connection
    print('tcp_send: dst_host="{0}", dst_port={1}'.format(server_host, server_port))
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((server_host, server_port))
    tcp_socket.send(request)


# reading the request line
def read_request_line(host,resource):
    request = 'GET {path} HTTP 1.1\r\nHost: {host}\r\nConnection: Close\r\n\r\n'.format(path=resource, host=host)
    return request

# reading the content length header i ndecimal
def read_header():

    return 0


# reading the body
def read_body():
    # loop through
    #
    return 0

def get_http_resource(url, file_name):
    """
    Get an HTTP resource from a server
           Parse the URL and call function to actually make the request.

    :param url: full URL of the resource to get
    :param file_name: name of file in which to store the retrieved resource

    (do not modify this function)
    """

    # Parse the URL into its component parts using a regular expression.
    url_match = re.search('http://([^/:]*)(:\d*)?(/.*)', url)
    url_match_groups = url_match.groups() if url_match else []
    #    print 'url_match_groups=',url_match_groups
    if len(url_match_groups) == 3:
        host_name = url_match_groups[0]
        host_port = int(url_match_groups[1][1:]) if url_match_groups[1] else 80
        host_resource = url_match_groups[2]
        print('host name = {0}, port = {1}, resource = {2}'.format(host_name, host_port, host_resource))
        status_string = make_http_request(host_name.encode(), host_port, host_resource.encode(), file_name)
        print('get_http_resource: URL="{0}", status="{1}"'.format(url, status_string))
    else:
        print('get_http_resource: URL parse failed, request not sent')


def make_http_request(host, port, resource, file_name):
    """
    Get an HTTP resource from a server

    :param bytes host: the ASCII domain name or IP address of the server machine (i.e., host) to connect to
    :param int port: port number to connect to on server host
    :param bytes resource: the ASCII path/name of resource to get. This is everything in the URL after the domain name,
           including the first /.
    :param file_name: string (str) containing name of file in which to store the retrieved resource
    :return: the status code
    :rtype: int
    """

    # start the connection
    #tcp_send(host, port)
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((host, port))
    # create the actual http request
    request = 'GET {path} HTTP 1.1\r\nHost: {host}\r\nConnection: Close\r\n\r\n'.format(path=resource, host=host)
    tcp_socket.send(request.encode())

    #print(request)
    return 500  # Replace this "server error" with the actual status code


main()
