

from define import Singleton
from PySide6.QtCore import (
    QByteArray,
    QDataStream,
    QIODevice,
    QObject,
    QSettings,
    QStandardPaths,
    Slot,
)


@Singleton
class SettingsHelper(QObject):
    def __init__(self, par=None):
        super().__init__(parent=par)
        self._settings = QSettings()

    def init(self):
        iniFileName = "example.ini"
        iniFilePath = (
            QStandardPaths.writableLocation(QStandardPaths.AppLocalDataLocation)
            + "/"
            + iniFileName
        )
        self._settings = QSettings(iniFilePath, QSettings.IniFormat)
        print("Application configuration file path ->", self._settings.fileName())

    def _save(self, key, val):
        data = QByteArray()
        stream = QDataStream(data, QIODevice.WriteOnly)
        stream.setVersion(QDataStream.Qt_5_6)
        stream.writeQVariant(val)
        self._settings.setValue(key, data)

    def _get(self, key):
        data = QByteArray(self._settings.value(key))
        if data.isEmpty():
            return
        stream = QDataStream(data)
        stream.setVersion(QDataStream.Qt_5_6)
        val = stream.readQVariant()
        return val

    @Slot(result=str)
    def getRender(self):
        return self._get("render")

    @Slot(str)
    def saveRender(self, render):
        self._save("render", render)

    @Slot(result=int)
    def getDarkMode(self):
        return self._get("darkMode")

    @Slot(int)
    def saveDarkMode(self, darkMode):
        self._save("darkMode", darkMode)

    @Slot(result=bool)
    def getVsync(self):
        return self._get("vsync")

    @Slot(bool)
    def saveVsync(self, vsync):
        self._save("vsync", vsync)

    @Slot(result=bool)
    def getUseSystemAppBar(self):
        return self._get("useSystemAppBar")

    @Slot(bool)
    def saveUseSystemAppBar(self, useSystemAppBar):
        self._save("useSystemAppBar", useSystemAppBar)
