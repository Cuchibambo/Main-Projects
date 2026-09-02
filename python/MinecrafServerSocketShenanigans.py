import socket
import struct
import json
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

def write_varInt(value):
    out = bytearray()

    while True:
        temp = value & 0b01111111 # get last 7 bits
        value >>= 7 # bit shift value
        if value:
            temp |= 0b10000000 # add a leading bit to the byte
        out.append(temp) # append to out
        if not value:
            break
    
    return out


def write_string(string:str):
    encoded = string.encode("utf-8")
    return write_varInt(len(encoded)) + encoded

def write_ArrayofBytes(data):
    return write_varInt(len(data)) + data

def send_packet(conection, packet):
    conection.sendall(write_varInt(len(packet)) + packet)

def read_exact(conection, length) -> bytes:
    data = b""
    while len(data) < length:
        chunk = conection.recv(length - len(data))
        if not chunk:
            raise ConnectionError("Connection closed")
        data += chunk
    return data

def read_varInt(conection):
    value = 0
    position = 0
    
    while True:
        current = read_exact(conection, 1)[0]
        value |= (current & 0b01111111) << position
        if (current & 0b10000000) == 0:
            break

        position += 7
            
        if position >= 35:
            raise ValueError("VarInt too big")
    
    return value

def read_string(conection):
    string_length = read_varInt(conection)
    string = read_exact(conection,string_length)
    string = string.decode("utf-8")
    return string

def read_ArrayofBytes(conection):
    length = read_varInt(conection)
    return read_exact(conection,length)

def handshake_gen(host,port,next_step):
    handshake = bytearray()
    handshake += write_varInt(0) # Packet Id
    handshake += write_varInt(767) # Protocol Version
    handshake += write_string(host) # Server address
    handshake += struct.pack(">H", port) # Server port
    handshake += write_varInt(next_step)
    return handshake

def login_start_packet_gen(username,UUID):
    login_start_packet = bytearray()
    login_start_packet += write_varInt(0) # Packet Id
    login_start_packet += write_string(username) # Username
    UUID_bytes = int(UUID, 16).to_bytes(16,"big")
    login_start_packet += UUID_bytes # UUID
    return login_start_packet

def encryption_response_gen(public_key,verify_token):
    packet = bytearray()
    packet += write_varInt(1) # Packet ID
    
    shared_secret = os.urandom(16)
    key = RSA.import_key(public_key)
    cipher = PKCS1_v1_5.new(key)
    encrypted_secret = cipher.encrypt(shared_secret)
    encrypted_token = cipher.encrypt(verify_token)
    
    packet += write_ArrayofBytes(encrypted_secret)
    packet += write_ArrayofBytes(encrypted_token)
    return packet
    
def status(host,port):
    conection = socket.create_connection((host, port), timeout=5)
    handshake = handshake_gen(host,port,1)
    send_packet(conection, handshake) # send handshake
    send_packet(conection, write_varInt(0)) # status request packet
    _length_of_response = read_varInt(conection)
    packet_id = read_varInt(conection)

    if packet_id != 0:
        raise ValueError(f"packed Id should be 0 currently is {packet_id}")

    string = read_string(conection)
    json_string = json.loads(string)
    conection.close()
    return json_string

def login(host,port,username,UUID):
    conection = socket.create_connection((host, port), timeout=5)
    handshake = handshake_gen(host,port,2)
    send_packet(conection, handshake) # send handshake
    login_start_packet = login_start_packet_gen("Cuchibambo_P","c889c7a166c649b8a62c555bc7f28353")
    send_packet(conection, login_start_packet)

    _packet_length = read_varInt(conection)
    packet_Id = read_varInt(conection)
    
    if packet_Id != 1:
        raise ValueError(f"packed Id should be 1 currently is {packet_Id}")
    
    server_id = read_string(conection)
    public_key = read_ArrayofBytes(conection)
    verify_token = read_ArrayofBytes(conection)
    isAuth = bool(read_exact(conection, 1)[0])
    
    encryption_response_packet = encryption_response_gen(public_key,verify_token)
    send_packet(conection,encryption_response_packet)
    
    conection.close()
    



if __name__ == "__main__":
    host = "5025.mystrator.com"
    port = 25603
    Status = status(host,port)
    print(json.dumps(Status, indent=4))
    print("player count:",Status["players"]["online"],"/",Status["players"]["max"])
    print("version:",Status["version"]["name"])
    # login(host,port,"Cuchibambo_P","c889c7a166c649b8a62c555bc7f28353")
    