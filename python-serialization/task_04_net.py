#!/usr/bin/env python3
"""Client-Server application with serialization using sockets."""


import socket
import json


def start_server(host='localhost', port=12345):
    """
    Start a server that listens for incoming connections,
    receives serialized data, deserializes it, and prints the dictionary.
    """
    try:
        # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Bind the socket to the address and port
        server_socket.bind((host, port))
        
        # Listen for incoming connections (max 1 queued connection)
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")
        
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        # Receive the serialized data
        data = client_socket.recv(1024).decode('utf-8')
        
        # Deserialize the data
        received_dict = json.loads(data)
        
        # Print the received dictionary
        print("Received Dictionary from Client:")
        print(received_dict)
        
        # Close the connection
        client_socket.close()
        server_socket.close()
        
    except socket.error as e:
        print(f"Socket error: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def send_data(data, host='localhost', port=12345):
    """
    Connect to the server, serialize a Python dictionary,
    and send it to the server.
    
    Args:
        data: Python dictionary to send
        host: Server hostname or IP address
        port: Server port number
    """
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the server
        client_socket.connect((host, port))
        
        # Serialize the dictionary
        serialized_data = json.dumps(data)
        
        # Send the serialized data
        client_socket.send(serialized_data.encode('utf-8'))
        
        # Close the connection
        client_socket.close()
        
    except socket.error as e:
        print(f"Socket error: {e}")
    except json.JSONEncodeError as e:
        print(f"JSON encode error: {e}")
    except Exception as e:
        print(f"Error: {e}")
