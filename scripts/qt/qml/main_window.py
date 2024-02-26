import sys
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQuick import QQuickView
from PySide6.QtQml import QQmlApplicationEngine
from model_class import Model


if __name__ == "__main__":
    app = QGuiApplication([])
    
    # Создание QML движка
    engine = QQmlApplicationEngine()

    # Создаем экземпляр модели
    model = Model()



    # Регистрируем экземпляр модели в QML контексте
    engine.rootContext().setContextProperty("model", model)
    
    # Загрузка QML файла
    engine.load(QUrl.fromLocalFile("qml/file.qml"))
    
    if not engine.rootObjects():
        sys.exit(-1)
    
    # Запуск приложения
    sys.exit(app.exec())
