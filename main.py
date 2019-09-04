# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:11:41 2019

@author: i
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

import sys, os.path, time

from ahk import AHK
from ahk.window import Window, WindowNotFoundError

import PySide2

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
from widget import Ui_Form


@dataclass
class MonitorKill():
    """
    此类是独立的，可不用 ui 独立使用。
    """
    monitering: bool = False

    # 最近跟踪的窗口
    last_focus_win: Window = None
    last_focus: str = ''

    # seconds
    last_time: float = 0

    min_focus_time: int = 5 * 60

    # 每个跟踪窗口 至少持续激活时间 达不到就 kill
    lasting: int = 60 * 5

    # 切换到这些窗口可忽略 不做惩戒
    ignore_windows: List[str] = field(default_factory=list)

    target_windows: List[str] = field(default_factory=list)

    ui: MainWindow = None

    def __post_init__(self):
        self.safe_config()
        self.ui.init(self, self.min_focus_time)

    def safe_config(self):
        self.ignore_windows = list(map(lambda s: s.lower(), self.ignore_windows))
        self.target_windows = list(map(lambda s: s.lower(), self.target_windows))

    def start(self):

        self.monitering = True

        self.last_time = time.time()

        # ui 里用 timer ，为什么？不用 timer 而用循环，那会造成堵塞，程序一直停留在循环中，ui 不能运行。
        if self.ui:
            self.ui.start_timer()
        else:
            time.sleep(2)
            while self.monitering:
                self.check()
                time.sleep(1)

    def stop(self):
        if self.ui:
            self.ui.timer.stop()

        self.monitering = False

    def check(self):
        current_win = ahk.active_window

        current = os.path.basename(current_win.process).lower()

        used_time = round(time.time() - self.last_time, 2)
        left_time = self.min_focus_time - used_time
        self.ui.show_time(used_time, left_time)

        if current in self.ignore_windows:
            self.msg(f'ignore {current}')
            return

        if not current_win is self.last_focus_win:

            if current in self.target_windows:

                self.setLast(current_win, current)

            elif self.min_focus_time > time.time() - self.last_time:

                self.kill(current)

            else:
                self.win()

    def setLast(self, current_win, current):

        self.msg(f'set {current}')

        self.last_focus_win = current_win
        self.last_focus = current

        self.last_time = time.time()

    def kill(self, current, demo=False):
        if self.last_focus_win is None:
            return

        to_kill = self.last_focus

        if demo:
            self.msg(f'demo close {to_kill} because {current}')
        else:
            time.sleep(1)
            self.msg(f'close {to_kill} because {current}')
            try:
                self.last_focus_win.close()
            except WindowNotFoundError:
                self.msg('win has closed')
            finally:
                self.last_focus_win = None
                self.last_focus = ''

    def win(self):
        self.msg('conga!')

    def msg(self, text):
        # ahk.run_script(f'msgbox {text}', blocking=False)
        self.ui.info(text)

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        # 也可以在初始化时设置flags
        # super(MainWindow, self).__init__(None,  QtCore.Qt.WindowStaysOnTopHint)
        super(MainWindow, self).__init__(None, )
        # 无边框
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint);
        # 透明
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 为调用它的控件增加一个遮罩，遮住所选区域以外的部分使之看起来是透明的
        # https://www.cnblogs.com/dcb3688/p/4237204.html
        # self.setMask()

        self.setupUi(self)

        # timer 是必须的，让 MonitorKill 调用。
        self.timer = QtCore.QTimer(self)

        self.monitor = None


    # 通过三个鼠标事件来移动窗口
    # 无边框后窗口的移动方法 https://blog.csdn.net/FanMLei/article/details/79433229
    def mousePressEvent(self, event):
        if event.button()==QtCore.Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  #更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def init(self, m, max):
        self.monitor = m

        self.processSlider.setMinimum(0)
        self.processSlider.setMaximum(max)
        self.show_time(0, max)

    def check(self):
        self.monitor.check()

    def start_timer(self):
        self.timer.timeout.connect(self.check)
        self.timer.start(2000)

    def info(self, text):
        self.infoLabel.setText(text)

    def show_time(self, used_time, left):
        self.timeLabel.setText(str(left))
        self.processSlider.setValue(used_time)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    ahk = AHK()
    to_focus = ['evernote.exe', 'pycharm64.exe', ]
    # this script need python.exe
    to_ignore = ['emeditor.exe', 'chrome.exe', 'ConEmu64.exe', 'python.exe', ]
    min_focus_time = 5 * 60
    monitor = MonitorKill(target_windows=to_focus, ignore_windows=to_ignore, min_focus_time=min_focus_time, ui=window)
    monitor.start()

    window.show()
    sys.exit(app.exec_())
