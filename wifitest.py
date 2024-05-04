import socket


# 設定伺服器的 IP 位址與通訊埠
host = '10.20.2.162'
port = 12345


# 建立 socket 物件
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 連線至伺服器
client_socket.connect((host, port))


 #傳送資料給伺服器
client_socket.sendall("Unlock1".encode())


 #關閉連線
client_socket.close()
'''
import serial

def attempt_connection(devices):
    for device in devices:
        try:
            ser = serial.Serial(device,115200,timeout=1)
            print(f"Connected to {device}")
            return ser
        except serial.SerialException:
                print(f"Failed to connect to {device}")
    return None
    
def send_serial_command(ser,command):
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    ser.write(command.encode())
    
devices= ["/dev/ttyACM0","/dev/ttyACM1"]

ser=attempt_connection(devices)
    
send_serial_command(ser,"SystemSwitchOff\r\n")
'''
