import os
import sys

sys.path.append(".")


from PySide6.QtCore import QProcess
from PySide6.QtGui import QGuiApplication
from PySide6.QtNetwork import QNetworkProxy
from PySide6.QtQml import QQmlApplicationEngine

import example.helpers.Log as Log
import example.resources.example_rc as example_rc
import FluentUI
from example.AppInfo import AppInfo
from example.components.CircularReveal import CircularReveal
from example.components.FileWatcher import FileWatcher
from example.components.FpsItem import FpsItem
from example.helpers.SettingsHelper import SettingsHelper

_ = (
    example_rc,
    CircularReveal,
    FileWatcher,
    FpsItem,
)


def main():
    Log.setup("example")
    QNetworkProxy.setApplicationProxy(QNetworkProxy.ProxyType.NoProxy)
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Basic"
    QGuiApplication.setOrganizationName("ZhuZiChu")
    QGuiApplication.setOrganizationDomain("https://zhuzichu520.github.io")
    QGuiApplication.setApplicationName("FluentUI")
    SettingsHelper().init()
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    rootContext = engine.rootContext()
    rootContext.setContextProperty("SettingsHelper", SettingsHelper())
    rootContext.setContextProperty("AppInfo", AppInfo())
    FluentUI.init(engine)
    print(engine.importPathList())
    qml_file = "qrc:/example/qml/App.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    exec = app.exec()
    if exec == 931:
        args = QGuiApplication.arguments()[1:]
        QProcess.startDetached(QGuiApplication.applicationFilePath(), args)
    return exec


if __name__ == "__main__":
    main()
