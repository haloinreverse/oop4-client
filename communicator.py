from PyQt5.QtNetwork import QUdpSocket, QHostAddress
from PyQt5.QtCore import pyqtSignal


class TCommunicator(QUdpSocket):
    receive_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()

        self.__my_port = 12344
        self.__srv_port = 12345
        self.bind(self.__my_port)
        self.readyRead.connect(self.receive_response)
        self.__host = QHostAddress("127.0.0.1")

    def send_message(self, message):
        # message = "Hello, server!"

        self.writeDatagram(message.encode(), self.__host, self.__srv_port)  # Отправляем на локальный хост, порт 12345
        print(f"Отправлено сообщение: {message}")

    def receive_response(self):
        while self.hasPendingDatagrams():
            datagram, _, _ = self.readDatagram(self.pendingDatagramSize())
            print(f"Received response: {datagram.decode()}")
            self.receive_signal.emit(datagram.decode())


