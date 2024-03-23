import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtNetwork import QUdpSocket, QHostAddress
from application import TApplication

# class UDPClient(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         layout = QVBoxLayout()
#         self.send_button = QPushButton("Send Message")
#         self.send_button.clicked.connect(self.send_message)
#         layout.addWidget(self.send_button)
#         self.setLayout(layout)
#
#         self.socket = QUdpSocket()
#         self.socket.bind(12344)  # Привязываемся к порту 12345 для получения ответа
#         self.socket.readyRead.connect(self.receive_response)
#
#     def send_message(self):
#         message = "Hello, server!"
#         host = QHostAddress("127.0.0.1")
#         self.socket.writeDatagram(message.encode(), host, 12345)  # Отправляем на локальный хост, порт 12345
#
#     def receive_response(self):
#         while self.socket.hasPendingDatagrams():
#             datagram, _, _ = self.socket.readDatagram(self.socket.pendingDatagramSize())
#             print(f"Received response: {datagram.decode()}")


if __name__ == '__main__':
    app = TApplication(sys.argv)
    # client = UDPClient()
    # client.show()  # Показываем окно клиента
    sys.exit(app.exec_())
