from app import socket
from app.services import add_host, get_hosts

@socket.on('connect')
def connection_handler():
    try:
        hosts = [ host.to_json() for host in get_hosts() ]
        #print(hosts)
        if hosts:
            socket.emit('server:send-hosts', { 'status':'success', 'data':hosts})

    except Exception as e:
        return { 'status':'error', 'data': 'here goes a descriptive error'}

@socket.on('client:add-host')
def add_host_handler(request):
    try:
        host = add_host(request)

        socket.emit('server:add-host', {'status': 'success','data': host.to_json(), 'message': 'Host added successfuly'})

    except Exception as e:
        return { 'status': 'error', 'data': '', 'message': 'Here goes a descriptive error'}
