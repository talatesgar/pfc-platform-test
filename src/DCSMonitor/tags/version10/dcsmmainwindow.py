# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dcsmmainwindow.ui'
#
# Created: Sat Jan  7 21:22:33 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(752, 790)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.groupBox_graphic = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_graphic.sizePolicy().hasHeightForWidth())
        self.groupBox_graphic.setSizePolicy(sizePolicy)
        self.groupBox_graphic.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox_graphic.setObjectName(_fromUtf8("groupBox_graphic"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_graphic)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.mplWidget = MplWidget(self.groupBox_graphic)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplWidget.sizePolicy().hasHeightForWidth())
        self.mplWidget.setSizePolicy(sizePolicy)
        self.mplWidget.setObjectName(_fromUtf8("mplWidget"))
        self.verticalLayout_4.addWidget(self.mplWidget)
        self.verticalLayout_6.addWidget(self.groupBox_graphic)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_saturation = QtGui.QLabel(self.centralwidget)
        self.label_saturation.setObjectName(_fromUtf8("label_saturation"))
        self.horizontalLayout.addWidget(self.label_saturation)
        self.slider_saturation = QtGui.QSlider(self.centralwidget)
        self.slider_saturation.setOrientation(QtCore.Qt.Horizontal)
        self.slider_saturation.setObjectName(_fromUtf8("slider_saturation"))
        self.horizontalLayout.addWidget(self.slider_saturation)
        self.label_percent_value = QtGui.QLabel(self.centralwidget)
        self.label_percent_value.setMinimumSize(QtCore.QSize(18, 0))
        self.label_percent_value.setToolTip(_fromUtf8(""))
        self.label_percent_value.setStatusTip(_fromUtf8(""))
        self.label_percent_value.setLineWidth(2)
        self.label_percent_value.setMidLineWidth(2)
        self.label_percent_value.setText(_fromUtf8("0"))
        self.label_percent_value.setTextFormat(QtCore.Qt.AutoText)
        self.label_percent_value.setScaledContents(True)
        self.label_percent_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_percent_value.setMargin(0)
        self.label_percent_value.setObjectName(_fromUtf8("label_percent_value"))
        self.horizontalLayout.addWidget(self.label_percent_value)
        self.label_percent_symbol = QtGui.QLabel(self.centralwidget)
        self.label_percent_symbol.setToolTip(_fromUtf8(""))
        self.label_percent_symbol.setStatusTip(_fromUtf8(""))
        self.label_percent_symbol.setObjectName(_fromUtf8("label_percent_symbol"))
        self.horizontalLayout.addWidget(self.label_percent_symbol)
        self.pushButton_save = QtGui.QPushButton(self.centralwidget)
        self.pushButton_save.setEnabled(False)
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_6.addWidget(self.textBrowser)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox_state = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_state.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_state.setObjectName(_fromUtf8("groupBox_state"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_state)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.lineEdit_state = QtGui.QLineEdit(self.groupBox_state)
        self.lineEdit_state.setEnabled(False)
        self.lineEdit_state.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_state.setObjectName(_fromUtf8("lineEdit_state"))
        self.verticalLayout_7.addWidget(self.lineEdit_state)
        self.pushButton_connect = QtGui.QPushButton(self.groupBox_state)
        self.pushButton_connect.setCheckable(True)
        self.pushButton_connect.setObjectName(_fromUtf8("pushButton_connect"))
        self.verticalLayout_7.addWidget(self.pushButton_connect)
        self.verticalLayout_5.addWidget(self.groupBox_state)
        self.groupBox_links = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_links.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_links.setObjectName(_fromUtf8("groupBox_links"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_links)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.listWidget_link = QtGui.QListWidget(self.groupBox_links)
        self.listWidget_link.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget_link.setObjectName(_fromUtf8("listWidget_link"))
        self.verticalLayout_3.addWidget(self.listWidget_link)
        self.pushButton_reload = QtGui.QPushButton(self.groupBox_links)
        self.pushButton_reload.setEnabled(False)
        self.pushButton_reload.setCheckable(True)
        self.pushButton_reload.setObjectName(_fromUtf8("pushButton_reload"))
        self.verticalLayout_3.addWidget(self.pushButton_reload)
        self.verticalLayout_5.addWidget(self.groupBox_links)
        self.groupBox_options = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_options.sizePolicy().hasHeightForWidth())
        self.groupBox_options.setSizePolicy(sizePolicy)
        self.groupBox_options.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_options.setObjectName(_fromUtf8("groupBox_options"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_options)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.textBrowser_color_r = QtGui.QTextBrowser(self.groupBox_options)
        self.textBrowser_color_r.setMaximumSize(QtCore.QSize(15, 15))
        self.textBrowser_color_r.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_color_r.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_color_r.setObjectName(_fromUtf8("textBrowser_color_r"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.textBrowser_color_r)
        self.checkBox_R = QtGui.QCheckBox(self.groupBox_options)
        self.checkBox_R.setChecked(True)
        self.checkBox_R.setTristate(False)
        self.checkBox_R.setObjectName(_fromUtf8("checkBox_R"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.checkBox_R)
        self.checkBox_U = QtGui.QCheckBox(self.groupBox_options)
        self.checkBox_U.setChecked(True)
        self.checkBox_U.setObjectName(_fromUtf8("checkBox_U"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.checkBox_U)
        self.textBrowser_color_u = QtGui.QTextBrowser(self.groupBox_options)
        self.textBrowser_color_u.setMaximumSize(QtCore.QSize(15, 15))
        self.textBrowser_color_u.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_color_u.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_color_u.setObjectName(_fromUtf8("textBrowser_color_u"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.textBrowser_color_u)
        self.checkBox_x1 = QtGui.QCheckBox(self.groupBox_options)
        self.checkBox_x1.setChecked(True)
        self.checkBox_x1.setObjectName(_fromUtf8("checkBox_x1"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.checkBox_x1)
        self.textBrowser_color_x1 = QtGui.QTextBrowser(self.groupBox_options)
        self.textBrowser_color_x1.setMaximumSize(QtCore.QSize(15, 15))
        self.textBrowser_color_x1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_color_x1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_color_x1.setObjectName(_fromUtf8("textBrowser_color_x1"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.textBrowser_color_x1)
        self.checkBox_x0 = QtGui.QCheckBox(self.groupBox_options)
        self.checkBox_x0.setChecked(True)
        self.checkBox_x0.setObjectName(_fromUtf8("checkBox_x0"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.checkBox_x0)
        self.textBrowser_color_x0 = QtGui.QTextBrowser(self.groupBox_options)
        self.textBrowser_color_x0.setMaximumSize(QtCore.QSize(15, 15))
        self.textBrowser_color_x0.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_color_x0.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_color_x0.setObjectName(_fromUtf8("textBrowser_color_x0"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.textBrowser_color_x0)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.pushButton_monitor = QtGui.QPushButton(self.groupBox_options)
        self.pushButton_monitor.setEnabled(False)
        self.pushButton_monitor.setCheckable(True)
        self.pushButton_monitor.setChecked(False)
        self.pushButton_monitor.setAutoDefault(False)
        self.pushButton_monitor.setDefault(False)
        self.pushButton_monitor.setFlat(False)
        self.pushButton_monitor.setObjectName(_fromUtf8("pushButton_monitor"))
        self.verticalLayout_2.addWidget(self.pushButton_monitor)
        self.pushButton_clear = QtGui.QPushButton(self.groupBox_options)
        self.pushButton_clear.setEnabled(True)
        self.pushButton_clear.setObjectName(_fromUtf8("pushButton_clear"))
        self.verticalLayout_2.addWidget(self.pushButton_clear)
        self.verticalLayout_5.addWidget(self.groupBox_options)
        self.groupBox_statistics = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_statistics.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_statistics.setObjectName(_fromUtf8("groupBox_statistics"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_statistics)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_T = QtGui.QLabel(self.groupBox_statistics)
        self.label_T.setObjectName(_fromUtf8("label_T"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_T)
        self.label_T_value = QtGui.QLabel(self.groupBox_statistics)
        self.label_T_value.setMinimumSize(QtCore.QSize(50, 0))
        self.label_T_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_T_value.setObjectName(_fromUtf8("label_T_value"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_T_value)
        self.label_fps = QtGui.QLabel(self.groupBox_statistics)
        self.label_fps.setObjectName(_fromUtf8("label_fps"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_fps)
        self.label_fps_value = QtGui.QLabel(self.groupBox_statistics)
        self.label_fps_value.setMinimumSize(QtCore.QSize(50, 0))
        self.label_fps_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_fps_value.setObjectName(_fromUtf8("label_fps_value"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.label_fps_value)
        self.label_samples = QtGui.QLabel(self.groupBox_statistics)
        self.label_samples.setObjectName(_fromUtf8("label_samples"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_samples)
        self.label_samples_value = QtGui.QLabel(self.groupBox_statistics)
        self.label_samples_value.setMinimumSize(QtCore.QSize(50, 0))
        self.label_samples_value.setLineWidth(1)
        self.label_samples_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_samples_value.setObjectName(_fromUtf8("label_samples_value"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.label_samples_value)
        self.label_rx_buff = QtGui.QLabel(self.groupBox_statistics)
        self.label_rx_buff.setObjectName(_fromUtf8("label_rx_buff"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_rx_buff)
        self.label_rx_buff_value = QtGui.QLabel(self.groupBox_statistics)
        self.label_rx_buff_value.setMinimumSize(QtCore.QSize(50, 0))
        self.label_rx_buff_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_rx_buff_value.setObjectName(_fromUtf8("label_rx_buff_value"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.label_rx_buff_value)
        self.label_Est = QtGui.QLabel(self.groupBox_statistics)
        self.label_Est.setObjectName(_fromUtf8("label_Est"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_Est)
        self.label_Est_value = QtGui.QLabel(self.groupBox_statistics)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        self.label_Est_value.setFont(font)
        self.label_Est_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Est_value.setObjectName(_fromUtf8("label_Est_value"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.label_Est_value)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_5.addWidget(self.groupBox_statistics)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 752, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuPreferencies = QtGui.QMenu(self.menubar)
        self.menuPreferencies.setObjectName(_fromUtf8("menuPreferencies"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionPC_Controlador = QtGui.QAction(MainWindow)
        self.actionPC_Controlador.setCheckable(True)
        self.actionPC_Controlador.setChecked(True)
        self.actionPC_Controlador.setEnabled(False)
        self.actionPC_Controlador.setIconVisibleInMenu(False)
        self.actionPC_Controlador.setObjectName(_fromUtf8("actionPC_Controlador"))
        self.actionPC_Sensor_Actuador = QtGui.QAction(MainWindow)
        self.actionPC_Sensor_Actuador.setCheckable(True)
        self.actionPC_Sensor_Actuador.setObjectName(_fromUtf8("actionPC_Sensor_Actuador"))
        self.actionPC_Monitor = QtGui.QAction(MainWindow)
        self.actionPC_Monitor.setCheckable(True)
        self.actionPC_Monitor.setChecked(True)
        self.actionPC_Monitor.setEnabled(False)
        self.actionPC_Monitor.setObjectName(_fromUtf8("actionPC_Monitor"))
        self.actionCatala = QtGui.QAction(MainWindow)
        self.actionCatala.setCheckable(True)
        self.actionCatala.setChecked(False)
        self.actionCatala.setEnabled(True)
        self.actionCatala.setWhatsThis(_fromUtf8(""))
        self.actionCatala.setShortcut(_fromUtf8(""))
        self.actionCatala.setObjectName(_fromUtf8("actionCatala"))
        self.actionEspanol = QtGui.QAction(MainWindow)
        self.actionEspanol.setCheckable(True)
        self.actionEspanol.setEnabled(True)
        self.actionEspanol.setWhatsThis(_fromUtf8(""))
        self.actionEspanol.setShortcut(_fromUtf8(""))
        self.actionEspanol.setObjectName(_fromUtf8("actionEspanol"))
        self.actionEnglish = QtGui.QAction(MainWindow)
        self.actionEnglish.setCheckable(True)
        self.actionEnglish.setChecked(True)
        self.actionEnglish.setEnabled(False)
        self.actionEnglish.setWhatsThis(_fromUtf8(""))
        self.actionEnglish.setShortcut(_fromUtf8(""))
        self.actionEnglish.setIconVisibleInMenu(True)
        self.actionEnglish.setObjectName(_fromUtf8("actionEnglish"))
        self.actionFrench = QtGui.QAction(MainWindow)
        self.actionFrench.setCheckable(True)
        self.actionFrench.setWhatsThis(_fromUtf8(""))
        self.actionFrench.setShortcut(_fromUtf8(""))
        self.actionFrench.setIconVisibleInMenu(True)
        self.actionFrench.setObjectName(_fromUtf8("actionFrench"))
        self.menuPreferencies.addSeparator()
        self.menuPreferencies.addAction(self.actionPC_Sensor_Actuador)
        self.menuPreferencies.addAction(self.actionPC_Monitor)
        self.menuPreferencies.addSeparator()
        self.menuPreferencies.addAction(self.actionCatala)
        self.menuPreferencies.addAction(self.actionEspanol)
        self.menuPreferencies.addAction(self.actionEnglish)
        self.menuPreferencies.addAction(self.actionFrench)
        self.menuPreferencies.addSeparator()
        self.menubar.addAction(self.menuPreferencies.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Distributed Control Systems Monitor", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_graphic.setTitle(QtGui.QApplication.translate("MainWindow", "Graphic", None, QtGui.QApplication.UnicodeUTF8))
        self.label_saturation.setText(QtGui.QApplication.translate("MainWindow", "Saturation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_percent_symbol.setText(QtGui.QApplication.translate("MainWindow", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save.setText(QtGui.QApplication.translate("MainWindow", "Save Image", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_state.setTitle(QtGui.QApplication.translate("MainWindow", "Monitor State", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_connect.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_links.setTitle(QtGui.QApplication.translate("MainWindow", "Control links", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_reload.setText(QtGui.QApplication.translate("MainWindow", "Update List", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_options.setTitle(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_color_r.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\" bgcolor=\"#0101df\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_R.setText(QtGui.QApplication.translate("MainWindow", "Reference (r)", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_U.setText(QtGui.QApplication.translate("MainWindow", "Input Value (u)", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_color_u.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\" bgcolor=\"#ff0000\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_x1.setText(QtGui.QApplication.translate("MainWindow", "First Integral (x1)", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_color_x1.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\" bgcolor=\"#bdbdbd\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_x0.setText(QtGui.QApplication.translate("MainWindow", "Second Integral (x0)", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_color_x0.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\" bgcolor=\"#ff8000\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_monitor.setText(QtGui.QApplication.translate("MainWindow", "Monitorize", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_clear.setText(QtGui.QApplication.translate("MainWindow", "Clean Text", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_statistics.setTitle(QtGui.QApplication.translate("MainWindow", "Statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.label_T.setText(QtGui.QApplication.translate("MainWindow", "TOTAL Links", None, QtGui.QApplication.UnicodeUTF8))
        self.label_T_value.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fps.setText(QtGui.QApplication.translate("MainWindow", "Frames per Second", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fps_value.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_samples.setText(QtGui.QApplication.translate("MainWindow", "Link Samples ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_samples_value.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rx_buff.setText(QtGui.QApplication.translate("MainWindow", "Input Buffer Bytes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rx_buff_value.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Est.setText(QtGui.QApplication.translate("MainWindow", "Statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Est_value.setText(QtGui.QApplication.translate("MainWindow", "|", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPreferencies.setTitle(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPC_Controlador.setText(QtGui.QApplication.translate("MainWindow", "PC -> Controlador", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPC_Sensor_Actuador.setText(QtGui.QApplication.translate("MainWindow", "PC -> Sensor/Actuator", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPC_Monitor.setText(QtGui.QApplication.translate("MainWindow", "PC -> Monitor", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCatala.setText(QtGui.QApplication.translate("MainWindow", "Català", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEspanol.setText(QtGui.QApplication.translate("MainWindow", "Español", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnglish.setText(QtGui.QApplication.translate("MainWindow", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFrench.setText(QtGui.QApplication.translate("MainWindow", "Française", None, QtGui.QApplication.UnicodeUTF8))

from mplwidget import MplWidget
