# color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
# background: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0 #4ca1af, stop:1 #c4e0e5);

bgColor = "rgba(245, 223, 77)"

QAPPLICATION_CSS = """
QApplication{

}
"""

QMAINWINDOW_CSS = """
QMainWindow{
    border-image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/testbg.png) 0 0 0 0 stretch stretch;
}
"""
QMENUSTATUSBAR_CSS = f"""
QMenuBar#menubar{{
    font-size: 33px;
    font-weight: 450;
    background-color: #00FFFFFF;
    color: black;
}}
QMenuBar::item:selected{{
    background-color: rgba(0, 0, 0, 0.2);
}}
QMenu{{
    font-size: 12px;
    background-color: rgba(245, 223, 77, 0.5);
    color: black;
}}
QMenu::item:selected{{
    background-color: rgba(0, 0, 0, 0.2);
}}

QStatusBar#statusbar{{
    font-size: 35px;
    font-weight: 550px;
}}
QStatusBar#statusbar.StatusTip{{
    border: 5px solid black;

}}
"""

QPUSHBUTTON_CSS = """
QPushButton#createNoteBtn{
    font-size: 10px;
    background-color: #00FFFFFF;
}

QPushButton#createNoteBtn{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/bigDisabledButton.png);
}
QPushButton:checked:enabled#createNoteBtn{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/bigActiveButton.png);
}
QPushButton:hover:enabled#createNoteBtn{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/bigNormalButton.png);
}
QPushButton:hover:disabled#createNoteBtn{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/bigNormalButton.png);
}
QPushButton:pressed:enabled#createNoteBtn{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/bigActiveButton.png);
}
QPushButton:pressed:disabled#createNoteBtn{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/bigInactiveButton.png);
}

QPushButton::hover#playPauseBtn{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/bigDisabledButton.png);
}
"""

QLABEL_CSS = """
QLabel{
    font-size: 17px;
    color: #000000;
}
"""
QLINEEDIT_CSS = """
QLineEdit{
    font-family: "VT323";
    font-size: 30px;
    background-color: rgba(255, 255, 255, 0.8);
}

"""
QGROUP_BOX_CSS = """
QGroupBox{
    font-size: 14px;
    font-style: bold;
    margin-top: 17px;
    border: 4px solid black;
    border-radius: 8px;
}
QGroupBox::title{
    subcontrol-origin: margin;
    left: 19px;
    padding: 0px 5px 0px 5px;
}
QGroupBox#projectNameGroupbox{
    margin-top: 25px;
}
QGroupBox::title#projectNameGroupbox{
    left: 100px;
}

"""

QCOMBOBOX_CSS = """
QComboBox#languageComboBox{
    font-size: 50%;
}
"""

QCHECKTEXT_BOX_CSS = """
QCheckBox{
    font-size: 70%;
    font-weight: 500px;
    color: #000000;
}
QCheckBox::indicator{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/checkBox.png);
}
QCheckBox::indicator:unchecked{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/uncheckBoxBordLess.png);
}
QCheckBox::indicator:unchecked:hover{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/checkBox.png);
}
QCheckBox::indicator:checked{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/checkBox.png);
}
QCheckBox:hover{
    font-size: 15px;
    color: #000000;
}
QCheckBox:checked{
    font-size: 15px;
    color: #000000;
}


QCheckBox::indicator#decentStatementCheckbox{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/valStateOKBordLess.png);
}
QCheckBox::indicator:unchecked:hover#decentStatementCheckbox{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/valStateOK.png);
}
QCheckBox::indicator:checked#decentStatementCheckbox{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/valStateOK.png);
}

QCheckBox::indicator#goodStatementCheckbox{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/valStateGoodBordLess.png);
}
QCheckBox::indicator:unchecked:hover#goodStatementCheckbox{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/valStateGood.png);
}
QCheckBox::indicator:checked#goodStatementCheckbox{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/valStateGood.png);
}

QCheckBox::indicator#greatStatementCheckbox{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/valStateGreatBordLess.png);
}
QCheckBox::indicator:unchecked:hover#greatStatementCheckbox{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/valStateGreat.png);
}
QCheckBox::indicator:checked#greatStatementCheckbox{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/valStateGreat.png);
}

QCheckBox::indicator#projectCheckBox{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/projectUnCheckBox.png);
}
QCheckBox::indicator:unchecked:hover#projectCheckBox{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/projectCheckBox.png);
}
QCheckBox::indicator:checked#projectCheckBox{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/projectCheckBox.png);
}


QCheckBox::indicator:checked#playPauseBtn{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/pauseButton.png);
}
QCheckBox::indicator:checked:hover#playPauseBtn{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/playButton.png);
}
QCheckBox::indicator:unchecked#playPauseBtn{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/playButton.png);
}
QCheckBox::indicator:unchecked:hover#playPauseBtn{
    image: url(C:/Users/wesle/PyScripts/Pike13 Template System/V_1.1/Images/pauseButton.png);
}



"""

SNC_CSS_SHEET = QAPPLICATION_CSS + QMAINWINDOW_CSS + QMENUSTATUSBAR_CSS + QLABEL_CSS + QGROUP_BOX_CSS + QCOMBOBOX_CSS + QCHECKTEXT_BOX_CSS + QLINEEDIT_CSS + QPUSHBUTTON_CSS
