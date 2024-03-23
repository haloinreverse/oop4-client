from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from communicator import TCommunicator
from interface import TInterface


class TApplication(QApplication):
    def __init__(self, *args):
        super().__init__(args[0])
        self.__communicator = TCommunicator()
        self.__interface = TInterface()
        # self.save_matrix()
        # self.__interface.save_matrix_pb.clicked.connect(self.save_matrix)
        self.__interface.transpose_pb.clicked.connect(self.__transpose)
        self.__interface.det_pb.clicked.connect(self.__show_det)
        self.__interface.rank_pb.clicked.connect(self.__show_rank)
        self.__communicator.receive_signal.connect(self.__receive_message)

    def __read_matrix(self):
        # new_matrix = [[0 for j in range(self.__interface.__size)] for i in range(self.__interface.__size)]
        str_matrix = ""
        for i in range(self.__interface.size):
            for j in range(self.__interface.size):
                # new_matrix[i][j] = self.__interface.tableWidget.item(i, j).text()
                str_matrix = str_matrix + self.__interface.tableWidget.item(i, j).text()
                if j != self.__interface.size - 1:
                    str_matrix = str_matrix + ' '

            if i != self.__interface.size - 1:
                str_matrix = str_matrix + "|"
        return str_matrix

    def __transpose(self):
        str_matrix = self.__read_matrix()
        # self.save_matrix()
        # self.__matrix.transpose()
        # for i in range(self.__size):
        #     for j in range(self.__size):
        #         self.tableWidget.item(i, j).setText(str(self.__matrix[i][j]))
        str_message = "trans#" + str_matrix
        self.__communicator.send_message(str_message)

    def __show_det(self):
        # self.save_matrix()
        # det = self.__matrix.det()
        # self.result_le.setText(str(det))
        str_matrix = self.__read_matrix()
        str_message = "det#" + str_matrix
        self.__communicator.send_message(str_message)

    def __show_rank(self):
        # self.save_matrix()
        # rank = self.__matrix.rank()
        # self.result_le.setText(str(rank))
        str_matrix = self.__read_matrix()
        str_message = "rank#" + str_matrix
        self.__communicator.send_message(str_message)

    def __receive_message(self, message):
        result_str = message.split('#')[1]
        operation = message.split('#')[0]
        if operation == 'trans':
            new_matrix = []
            for i in result_str.split('|'):
                new_row = []
                for j in i.split(' '):
                    new_row.append(j)
                new_matrix.append(new_row)
            self.__interface.transpose(new_matrix)
        elif operation == 'det':
            self.__interface.show_det(result_str)
        elif operation == 'rank':
            self.__interface.show_det(result_str)
