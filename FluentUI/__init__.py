from pathlib import Path

from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication


def init(engine: QQmlApplicationEngine):
    qml_import_path = Path(__file__).parent.absolute() / "qml"
    engine.addImportPath(qml_import_path)


def __test():
    QApplication()
    engine = QQmlApplicationEngine()
    init(engine)
    print(engine.importPathList())


if __name__ == "__main__":
    __test()
