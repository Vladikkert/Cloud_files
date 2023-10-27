import os
from datetime import datetime
# from PyQt6.QtWidgets import QApplication, QWidget
#
# import sys # Только для доступа к аргументам командной строки
#
# # Приложению нужен один (и только один) экземпляр QApplication.
# # Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
# # Если не будете использовать аргументы командной строки, QApplication([]) тоже работает
# app = QApplication(sys.argv)
#
# # Создаём виджет Qt — окно.
# window = QWidget()
# window.show()  # Важно: окно по умолчанию скрыто.
#
# # Запускаем цикл событий.
# app.exec()
#
#
# # Приложение не доберётся сюда, пока вы не выйдете и цикл
# # событий не остановится.

print("Введите путь к диску или папке")
fold_path = input()
# обработка неверного запроса
class Info:
    def __init__(self, fold_path):
        self.os_path = os.path.dirname(fold_path)
        os.chdir(self.os_path)
        self.list_dir = os.listdir(self.os_path)
    def files(self):
        files_list = []
        for i in self.list_dir:
            if os.path.isfile(i) == True:
                file_name = i
                file_size = os.path.getsize(i)
                file_abs_path = os.path.join(self.os_path, i)
                file_date_cr = str(datetime.fromtimestamp(round(os.path.getctime(i))))
                file_date_ch = str(datetime.fromtimestamp(round(os.path.getmtime(i))))
                files_list.append([f'Имя файла: {file_name}', f'Размер файла: {file_size}B', f'Полный путь к файлу: {file_abs_path}', f'Дата создания файла: {file_date_cr}',
                                   f'Дата изменения файла: {file_date_ch}'])
        with open('files.csv', 'w') as file:
            print('зашли в  файл файлов и отредактировали его')
            for k in files_list:
                file.writelines(', '.join(k))
                file.writelines('\n')

    def folders(self):
        folders_list = []
        for j in self.list_dir:
            if os.path.isdir(j) == True:
                fold_name = j
                fold_abs_path = os.path.join(self.os_path, j)
                fold_date_cr = str(datetime.fromtimestamp(round(os.path.getctime(j))))
                folders_list.append([f'Имя папки: {fold_name}', f'Полный путь к папке: {fold_abs_path}', f'Дата создания папки: {fold_date_cr}'])
        with open('folders.csv', 'w') as folder:
            print('зашли в  файл папок и отредактировали его')
            for r in folders_list:
                folder.writelines(', '.join(r))
                folder.writelines('\n')



if __name__ == '__main__':
    NewClass = Info(fold_path)
    NewClass.files()
    NewClass.folders()

#написать ексепшены
#написать логику даты создания для линуха
#сделать black