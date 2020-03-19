# -*- coding: utf-8 -*-

"""
theCoderSchool - Note Creation System

[Version 1.1.0]
This program creates notes for finished tutoring sessions with a standardized templating format that includes:
- Learning Platform Used
- Concepts Covered
- Projects Worked on
- Value statments about session noted
Once user has selected/filled all necessary categories, the program will save a text file with a formatted note with information filled

FEATURES ADDED:
 - Moved each section of widgets into QGroupBox Layout
 - Moved each Groupbox into QFrames in order to organize content
 - Added new font "VT323"
 - Created checkbox state changes to indicate successful click

Author: Wesley Nguyen
Last edited: January 2020
"""

import sys
import os
# PyQt5 IMPORTS
from PyQt5.QtWidgets    import *
from PyQt5.QtGui        import *
from PyQt5.QtCore       import *
from PyQt5.QtMultimedia import *
# CSS STYLING IMPORTS
from noteCSS import *
# Font/Image Dir
from fontImgDir import *

# Default Widget Span for Grid Layout
DEFAULT_SPAN = (1, 1)
DEFAULT_WIDTH = 1440
DEFAULT_HEIGHT = 900
class MainWindow:
    # Main Window Object Creation Steps:
        # 1: Create Object
        # 2: Set Size/Geometry Features
        # 3: Set Object Name/Text
        # 4: Set Label Name (Optional)
        # 5: Set Misc Attributes
    "SHARED CLASS ATTRIBUTES"

    "QOBJECT DIMENSIONS"
    # Labels
    LW = 220
    LH = 50
    # Check Boxes
    CBW = 150
    CBH = 50
    """
MAIN OBJECT INITIALIZATION
    """
    def __init__(self):
        "MAIN APP OBJECT (TOP LEVEL)"
        # Main App Creation
        self.app = QApplication(sys.argv)
        # Set QApplication font
        self.mainAppFont = QFont("Pixeled")
        self.mainAppFont.setPointSize(6.5)
        self.app.setFont(self.mainAppFont)


        "MAIN WINDOW OBJECT (MID LEVEL INSIDE MAIN APP)"
        # Main Window Creation
        self.mainWindow = QMainWindow()
        # Set window to open middle of the screen with CONSTANT size as 1024x768
        self.mainWindow.setGeometry(1100, 450, DEFAULT_WIDTH, DEFAULT_HEIGHT)
        # self.mainWindow.setMinimumSize(QSize(DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.mainWindow.setFixedSize(QSize(DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.mainWindow.setObjectName("mainWindow")

        "CENTRAL WIDGET OBJECT (LOW LEVEL INSIDE MAIN WINDOW)"
        # Create Central Widget
        self.centralWidget = QWidget(self.mainWindow)
        self.centralWidget.setFixedSize(QSize(DEFAULT_WIDTH, (DEFAULT_HEIGHT - 41)))
        self.centralWidget.setObjectName("centralWidget")

        # Set mainWindow Central Widget as centralWidget
        self.mainWindow.setCentralWidget(self.centralWidget)

        "INITIALIZE OTHER WINDOWS"
        self.initWinOne()

        "INITIALIZE GUI/GRID/WIDGETS"
        # Initialize Frames
        self.initFrames()
        # Initialize Inner Group Boxes
        self.initInnerGB()
        # Initialize GUI Objects
        self.initGuiObjects()
        # Initialize Menu/Status Bars
        self.initMSBars()
        # Set/Create Grid
        self.populateFrames()
        # Set Text for Objects
        self.retranslateUi()
        # Add Fonts
        self.addFonts()
        # Connect Signal and Slots
        self.connectSignals()
        # Load Music
        self.loadJukeBox()
        "FIND OUT WHAT THIS SHIT DOES"
        QMetaObject.connectSlotsByName(self.mainWindow)
    """
ADD FONTS
    """
    # Font Adding Function
    def addFonts(self, dir_:str=None) -> None:
        if dir_ == None:
            dir_ = FONTS_DIR
        directory = os.fsencode(dir_)
        for file in os.listdir(directory):
             filename = os.fsdecode(file)
             _id = QFontDatabase.addApplicationFont(f"Fonts/{filename}")
             print(f"Added: {QFontDatabase.applicationFontFamilies(_id)}")
             continue
    """
JUKEBOX BABY
    """
    def loadJukeBox(self) -> None:
        "MUSIC BABY!!"
        self.musicPlaylist = QMediaPlaylist()
        url = QUrl.fromLocalFile(STUNNINGNIGHTDIR)
        self.musicPlaylist.addMedia(QMediaContent(url))
        self.musicPlaylist.setPlaybackMode(QMediaPlaylist.Loop)
        self.musicPlayer = QMediaPlayer()
        self.musicPlayer.setPlaylist(self.musicPlaylist)

    def playPauseJukeBox(self) -> None:
        on_off = lambda x: self.musicPlayer.stop() if x else self.musicPlayer.play()
        state = bool(self.musicPlayer.state())
        msg = "Jukebox Off!" if state else "Jukebox On!"
        msg_1 = "Play Button Displaying!" if state else "Pause Button Displaying!"
        print(msg)
        print(msg_1)
        on_off(state)

    """
CREATE MENUBAR AND STATUS BAR
    """
    def initMSBars(self):
        self.appBarsFont = QFont("VT323")
        'MENU BAR'
        # Create menu bar
        self.menubar = QMenuBar(self.mainWindow)
        self.menubar.setGeometry(QRect(0, 0, 1400, 21))
        self.menubar.setObjectName("menubar")
        self.menubar.setFont(self.appBarsFont)
        self.mainWindow.setMenuBar(self.menubar)
        # Create FILE tab
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menubar.addAction(self.menuFile.menuAction())
            # Create SAVE tab (inside FILE tab)
        self.actionSave = QAction(self.mainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())
        # Create VIEW tab
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
            # Create ABOUT tab (inside VIEW tab)
        self.actionAbout = QAction(self.mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuView.addAction(self.actionAbout)
        self.menubar.addAction(self.menuView.menuAction())

        self.statusBarFont = QFont("VT323")
        "STATUS BAR"
        # Create STATUS BAR
        self.statusbar = QStatusBar(self.mainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setFont(self.statusBarFont)
        self.mainWindow.setStatusBar(self.statusbar)

    """
CREATE FRAMES
    """
    def initFrames(self):
        "Frame 1: Student Name and Entry"
        self.frame_1 = QFrame(self.centralWidget)
        self.frame_1.setGeometry(QRect(0, 0, 1350, 125))
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.frame_1Grid = QGridLayout(self.frame_1)
        "Frame 2: Lesson Type"
        self.frame_2 = QFrame(self.centralWidget)
        self.frame_2.setGeometry(QRect(0, 100, 1375, 125))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2Grid = QGridLayout(self.frame_2)
        self.frame_2Grid.setSpacing(40)
        "Frame 3: Session Statement"
        self.frame_3 = QFrame(self.centralWidget)
        self.frame_3.setGeometry(QRect(0, 700, 650, 120))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_3Grid = QGridLayout(self.frame_3)
        "Frame 4: Ok Button"
        self.frame_4 = QFrame(self.centralWidget)
        self.frame_4.setGeometry(QRect(1075, 725, 500, 100))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_4Grid = QGridLayout(self.frame_4)
        "Frame 5: Platforms Used"
        self.frame_5 = QFrame(self.centralWidget)
        self.frame_5.setGeometry(QRect(0, 200, 900, 300))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_5Grid = QGridLayout(self.frame_5)
        "Frame 6: Concepts Covered"
        self.frame_6 = QFrame(self.centralWidget)
        self.frame_6.setGeometry(QRect(0, 475, 900, 250))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_6Grid = QGridLayout(self.frame_6)
        "Frame 7: Play/Pause Button"
        self.frame_7 = QFrame(self.centralWidget)
        self.frame_7.setGeometry(QRect(1360, -25, 100, 100))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_7Grid = QGridLayout(self.frame_7)
        "Frame 8: Open Window Button"
        self.frame_8 = QFrame(self.centralWidget)
        self.frame_8.setGeometry(QRect(1360, 100, 100, 100))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_8Grid = QGridLayout(self.frame_8)


    """
POPULATE FRAMES AND THEIR GRID LAYOUTS
    """
    # Method to add/populate frames with features
    def populateFrames(self):
        "Frame 1"
        # GB3
        self.frame_1Grid.addWidget(self.studentInfoGroupbox, 0, 0)
        "Frame 2"
        # GB1
        self.frame_2Grid.addWidget(self.lessonTypeGroupBox, 0, 0)
        # T2
        self.frame_2Grid.addWidget(self.projectNameGroupbox, 0, 2)
        # Setting Frame 2 Stretches
        # self.frame_2Grid.setRowStretch(0, 6)
        self.frame_2Grid.setColumnStretch(1, 4)
        self.frame_2Grid.setColumnStretch(2, 3)

        "Frame 3"
        # GB2
        self.frame_3Grid.addWidget(self.sessionStatementGroupBox, 0, 0)

        "Frame 4"
        # B1
        self.frame_4Grid.addWidget(self.createNoteBtn, 0, 0)
        "Frame 5"
        self.frame_5Grid.addWidget(self.platformsUsedGroupBox, 0, 0)
        "Frame 6"
        self.frame_6Grid.addWidget(self.conceptsCoveredGroupBox, 0, 0)
        "Frame 7"
        # B2
        self.frame_7Grid.addWidget(self.playPauseBtn, 0, 0)
        "Frame 8"
        # B3
        self.frame_8Grid.addWidget(self.openWindowBtn, 0, 0)



    """
CREATE WIDGETS/LABELS/BUTTONS
    """
    # Method to create/intialize Gui Objects that will go into centralWidget
    def initGuiObjects(self):
        # Populate GUI Window
        "BUTTON INIT"
        """
*ADD FEATURE TO CHANGE STATE TO ACTIVE ONCE FIELDS ARE READY*
        """
        # B1: Create Note Button
        self.createNoteBtn = QPushButton(self.centralWidget)
        self.createNoteBtn.setFixedWidth(140)
        self.createNoteBtn.setFixedHeight(62)
        self.createNoteBtn.setObjectName("createNoteBtn")
        self.createNoteBtn.setEnabled(True)
        # B2: Pause/Play Button
        self.playPauseBtn = QCheckBox(self.centralWidget)
        self.playPauseBtn.setFixedWidth(40)
        self.playPauseBtn.setFixedHeight(40)
        self.playPauseBtn.setObjectName("playPauseBtn")
        self.playPauseBtn.setCheckable(True)
        # B3: Open Window Button
        self.openWindowBtn = QCheckBox(self.centralWidget)
        self.openWindowBtn.setFixedWidth(40)
        self.openWindowBtn.setFixedHeight(40)
        self.openWindowBtn.setObjectName("openWindowBtn")
        self.openWindowBtn.setCheckable(False)



        # GB3: Student Info Groupbox
        """     STUDENT INFO Groupbox       """
        self.studentInfoGroupbox = QGroupBox("Student Info")
        self.studentInfoGroupbox.setCheckable(False)
        self.studentInfoGroupboxLayout = QHBoxLayout(spacing=0)
        self.studentInfoGroupbox.setLayout(self.studentInfoGroupboxLayout)
        self.studentInfoGroupbox.setObjectName("studentInfoGroupbox")
        # L1: Student Name Label
        self.studentNameLabel = QLabel(self.studentInfoGroupbox)
        self.studentNameLabel.setFixedWidth(120)
        self.studentNameLabel.setFixedHeight(self.LH)
        self.studentNameLabel.setObjectName("studentNameLabel")
        # T1: Student Name Line Edit
        self.studentNameBox = QLineEdit(self.studentInfoGroupbox)
        self.studentNameBox.setFixedWidth(350)
        self.studentNameBox.setFixedHeight(self.CBH)
        self.studentNameBox.setObjectName("studentNameBox")
        # L2: Language Used Label
        self.languageUsedLabel = QLabel(self.studentInfoGroupbox)
        self.languageUsedLabel.setFixedWidth(140)
        self.languageUsedLabel.setFixedHeight(self.LH)
        self.languageUsedLabel.setObjectName("languageUsedLabel")
        # ComB1: Language Used
        self.languageComboBox = QComboBox(self.studentInfoGroupbox)
        self.languageComboBox.setFixedWidth(200)
        self.languageComboBox.setFixedHeight(self.CBH)
        self.languageComboBox.setObjectName("languageComboBox")
        # L3: Pronouns Label
        self.pronounsLabel = QLabel(self.studentInfoGroupbox)
        self.pronounsLabel.setFixedWidth(140)
        self.pronounsLabel.setFixedHeight(self.LH)
        self.pronounsLabel.setObjectName("pronounsLabel")
        # ComB2: Student Pronouns
        self.studentPronounComboBox = QComboBox(self.studentInfoGroupbox)
        self.studentPronounComboBox.setFixedWidth(200)
        self.studentPronounComboBox.setFixedHeight(self.CBH)
        self.studentPronounComboBox.setObjectName("studentPronounComboBox")
        # Add Items to Combo Boxes
        [self.languageComboBox.addItem(QIcon(languagesIcon[i]), "  " + languagesText[i]) for i in range(len(languagesText))]
        [self.studentPronounComboBox.addItem(QIcon(pronounsIcon[i]), "  " + pronounsText[i]) for i in range(len(pronounsText))]

        # Add to QGroupBox
        self.studentInfoGroupboxLayout.addWidget(self.studentNameLabel)
        self.studentInfoGroupboxLayout.addWidget(self.studentNameBox)
        self.studentInfoGroupboxLayout.addWidget(self.pronounsLabel)
        self.studentInfoGroupboxLayout.addWidget(self.studentPronounComboBox)
        self.studentInfoGroupboxLayout.addWidget(self.languageUsedLabel)
        self.studentInfoGroupboxLayout.addWidget(self.languageComboBox)


        # GB1: Lesson Type Group Box
        """     LESSON TYPE GROUP BOX        """
        self.lessonTypeGroupBox = QGroupBox("Lesson Type")
        self.lessonTypeGroupBox.setCheckable(False)
        self.lessonTypeGroupBoxLayout = QHBoxLayout()
        self.lessonTypeGroupBox.setLayout(self.lessonTypeGroupBoxLayout)
        self.lessonTypeGroupBox.setObjectName("lessonTypeGroupBox")

        # CBa1: Learn Checkbox
        self.learnCheckBox = QCheckBox(self.lessonTypeGroupBox)
        self.learnCheckBox.setFixedWidth(self.CBW)
        self.learnCheckBox.setFixedHeight(self.CBH)
        self.learnCheckBox.setObjectName("learnCheckBox")
        # CBa2: Review Checkbox
        self.reviewCheckBox = QCheckBox(self.lessonTypeGroupBox)
        self.reviewCheckBox.setFixedWidth(self.CBW)
        self.reviewCheckBox.setFixedHeight(self.CBH)
        self.reviewCheckBox.setObjectName("reviewCheckBox")
        # CBa3: Practice Checkbox
        self.practiceCheckBox = QCheckBox(self.lessonTypeGroupBox)
        self.practiceCheckBox.setFixedWidth(self.CBW)
        self.practiceCheckBox.setFixedHeight(self.CBH)
        self.practiceCheckBox.setObjectName("practiceCheckBox")
        # CBa4: Challenge Checkbox
        self.challengeCheckBox = QCheckBox(self.lessonTypeGroupBox)
        self.challengeCheckBox.setFixedWidth(self.CBW)
        self.challengeCheckBox.setFixedHeight(self.CBH)
        self.challengeCheckBox.setObjectName("challengeCheckBox")
        # CBa5: Project Checkbox
        self.projectCheckBox = QCheckBox(self.lessonTypeGroupBox)
        self.projectCheckBox.setFixedWidth(self.CBW)
        self.projectCheckBox.setFixedHeight(self.CBH)
        self.projectCheckBox.setObjectName("projectCheckBox")
        # Add to QGroupBox
        self.lessonTypeGroupBoxLayout.addWidget(self.learnCheckBox)
        self.lessonTypeGroupBoxLayout.addWidget(self.reviewCheckBox)
        self.lessonTypeGroupBoxLayout.addWidget(self.practiceCheckBox)
        self.lessonTypeGroupBoxLayout.addWidget(self.challengeCheckBox)
        self.lessonTypeGroupBoxLayout.addWidget(self.projectCheckBox)


        """     PROJECT NAME GB       """
        self.projectNameGroupbox = QGroupBox("Project Name")
        self.projectNameGroupbox.setCheckable(False)
        self.projectNameGroupboxLayout = QHBoxLayout()
        self.projectNameGroupbox.setLayout(self.projectNameGroupboxLayout)
        self.projectNameGroupbox.setObjectName("projectNameGroupbox")
        self.projectNameGroupbox.hide()
        # T2: Project Name Line Edit
        self.projectNameBox = QLineEdit(self.projectNameGroupbox)
        self.projectNameBox.setFixedWidth(300)
        self.projectNameBox.setFixedHeight(40)
        self.projectNameBox.setObjectName("projectNameBox")
        # I1: Project Icon
        self.projectIconLabel = QLabel(self.projectNameGroupbox)
        self.projectIconLabel.setFixedWidth(45)
        self.projectIconLabel.setFixedHeight(45)
        self.projectIconLabel.setObjectName("projectIconLabel")
        self.projectIconLabel.setScaledContents(True)
        self.projectIconLabel.setPixmap(QPixmap.fromImage(QImage(projectIconDir)))
        # Add to QGroupBox
        self.projectNameGroupboxLayout.addWidget(self.projectIconLabel)
        self.projectNameGroupboxLayout.addWidget(self.projectNameBox)

        # GB2: Session Statement Group Box
        """     SESSION STATEMENT GROUP BOX        """
        self.sessionStatementGroupBox = QGroupBox("Session Statement")
        self.sessionStatementGroupBox.setCheckable(False)
        self.sessionStatementGroupBoxLayout = QHBoxLayout()
        self.sessionStatementGroupBox.setLayout(self.sessionStatementGroupBoxLayout)
        self.sessionStatementGroupBox.setObjectName("sessionStatementGroupBox")
        "SESSION STATEMENT"
        # CBb1: Decent Statement Checkbox
        self.decentStatementCheckbox = QCheckBox(self.sessionStatementGroupBox)
        self.decentStatementCheckbox.setFixedWidth(self.CBW - 30)
        self.decentStatementCheckbox.setFixedHeight(self.CBH)
        self.decentStatementCheckbox.setObjectName("decentStatementCheckbox")
        # CBb2: Good Statement Checkbox
        self.goodStatementCheckbox = QCheckBox(self.sessionStatementGroupBox)
        self.goodStatementCheckbox.setFixedWidth(self.CBW - 30)
        self.goodStatementCheckbox.setFixedHeight(self.CBH)
        self.goodStatementCheckbox.setObjectName("goodStatementCheckbox")
        # CBb3: Great Statement Checkbox
        self.greatStatementCheckbox = QCheckBox(self.sessionStatementGroupBox)
        self.greatStatementCheckbox.setFixedWidth(self.CBW - 30)
        self.greatStatementCheckbox.setFixedHeight(self.CBH)
        self.greatStatementCheckbox.setObjectName("greatStatementCheckbox")
        # Add to QGroupBox
        self.sessionStatementGroupBoxLayout.addWidget(self.decentStatementCheckbox)
        self.sessionStatementGroupBoxLayout.addWidget(self.goodStatementCheckbox)
        self.sessionStatementGroupBoxLayout.addWidget(self.greatStatementCheckbox)

        # GB4: Platforms Used Group Box
        """     PLATFORMS USED GROUP BOX        """
        self.platformsUsedGroupBox = QGroupBox("Platform Used")
        self.platformsUsedGroupBox.setCheckable(False)
        self.platformsUsedGroupBoxLayout = QGridLayout()
        self.platformsUsedGroupBox.setLayout(self.platformsUsedGroupBoxLayout)
        self.platformsUsedGroupBox.setObjectName("platformsUsedGroupBox")
        # L4: Platforms Additional Fields Label
        self.platformsAddLabel = QLabel(self.platformsUsedGroupBox)
        self.platformsAddLabel.setFixedWidth(240)
        self.platformsAddLabel.setFixedHeight(self.LH)
        self.platformsAddLabel.setObjectName("platformsAddLabel")
        # T3: Platforms Line Edit
        self.platformsNameBox = QLineEdit(self.platformsUsedGroupBox)
        self.platformsNameBox.setFixedWidth(280)
        self.platformsNameBox.setFixedHeight(self.CBH- 10)
        self.platformsNameBox.setObjectName("platformsNameBox")
        # Add to QGroupBox
        "BEGINNER PLATFORM GROUP BOX"
        self.platformsUsedGroupBoxLayout.addWidget(self.beginnerPlatformGroupBox, 0, 0)
        "INTERMEDIATE PLATFORM GROUP BOX"
        self.platformsUsedGroupBoxLayout.addWidget(self.intermediatePlatformGroupBox, 0, 1)
        "ADVANCED PLATFORM GROUP BOX"
        self.platformsUsedGroupBoxLayout.addWidget(self.advancedPlatformGroupBox, 0, 2)
        "OTHER PLATFORM GROUP BOX"
        self.platformsUsedGroupBoxLayout.addWidget(self.otherPlatformGroupBox, 0, 3)
        "ADDTL FIELDS"
        self.platformsUsedGroupBoxLayout.addWidget(self.platformsAddLabel, 1, 0)
        self.platformsUsedGroupBoxLayout.addWidget(self.platformsNameBox, 1, 2)


        # GB5: Concepts Covered Group Box
        """     CONCEPTS COVERED GROUP BOX        """
        self.conceptsCoveredGroupBox = QGroupBox("Concepts Covered")
        self.conceptsCoveredGroupBox.setCheckable(False)
        self.conceptsCoveredGroupBoxLayout = QGridLayout()
        self.conceptsCoveredGroupBox.setLayout(self.conceptsCoveredGroupBoxLayout)
        self.conceptsCoveredGroupBox.setObjectName("conceptsCoveredGroupBox")
        "CONCEPT CHECK GROUP BOXES"

        "ADDTL FIELDS"
        # L5: Concepts Additional Fields Label
        self.conceptsAddLabel = QLabel(self.conceptsCoveredGroupBox)
        self.conceptsAddLabel.setFixedWidth(230)
        self.conceptsAddLabel.setFixedHeight(self.LH)
        self.conceptsAddLabel.setObjectName("conceptsAddLabel")
        # T4: Concepts Line Edit
        self.conceptsNameBox = QLineEdit(self.conceptsCoveredGroupBox)
        self.conceptsNameBox.setFixedWidth(380)
        self.conceptsNameBox.setFixedHeight(self.CBH - 10)
        self.conceptsNameBox.setObjectName("conceptsNameBox")
        # Add to QGroupBox
        "BEGINNER CONCEPTS GROUP BOX"
        self.conceptsCoveredGroupBoxLayout.addWidget(self.beginnerConceptsGroupBox, 0, 0)
        "INTERMEDIATE CONCEPTS GROUP BOX"
        self.conceptsCoveredGroupBoxLayout.addWidget(self.intermediateConceptsGroupBox, 0, 1)
        "ADVANCED CONCEPTS GROUP BOX"
        self.conceptsCoveredGroupBoxLayout.addWidget(self.advancedConceptsGroupBox, 0, 2)
        "ADDTL FIELDS"
        self.conceptsCoveredGroupBoxLayout.addWidget(self.conceptsAddLabel, 1, 0)
        self.conceptsCoveredGroupBoxLayout.addWidget(self.conceptsNameBox, 1, 1)

        "IMAGE INIT"
        #



    """
INNER GROUPBOX AND PROJECT INIT
    """
    # Method to create/intialize inner groupbox Objects that will go into their respective groupboxes
    def initInnerGB(self):
        """ Platforms Used GB """
        "BEGINNER"
        # Beginner GB
        self.beginnerPlatformGroupBox = QGroupBox("Beginner")
        self.beginnerPlatformGroupBox.setCheckable(False)
        self.beginnerPlatformGroupBoxLayout = QVBoxLayout()
        self.beginnerPlatformGroupBox.setLayout(self.beginnerPlatformGroupBoxLayout)
        self.beginnerPlatformGroupBox.setObjectName("beginnerPlatformGroupBox")
        # CBp1: Scratch Checkbox
        self.scratchCheckBox = QCheckBox(self.beginnerPlatformGroupBox)
        self.scratchCheckBox.setFixedWidth(self.CBW)
        self.scratchCheckBox.setFixedHeight(self.CBH)
        self.scratchCheckBox.setObjectName("scratchCheckBox")
        # CBp2: CodeCombat Checkbox
        self.codecombatCheckBox = QCheckBox(self.beginnerPlatformGroupBox)
        self.codecombatCheckBox.setFixedWidth(self.CBW + 20)
        self.codecombatCheckBox.setFixedHeight(self.CBH)
        self.codecombatCheckBox.setObjectName("codecombatCheckBox")
        # CBp3: WoofJs Checkbox
        self.woofjsCheckBox = QCheckBox(self.beginnerPlatformGroupBox)
        self.woofjsCheckBox.setFixedWidth(self.CBW)
        self.woofjsCheckBox.setFixedHeight(self.CBH)
        self.woofjsCheckBox.setObjectName("woofjsCheckBox")
        # Add to QGroupBox
        self.beginnerPlatformGroupBoxLayout.addWidget(self.scratchCheckBox)
        self.beginnerPlatformGroupBoxLayout.addWidget(self.codecombatCheckBox)
        self.beginnerPlatformGroupBoxLayout.addWidget(self.woofjsCheckBox)
        "INTERMEDIATE"
        # Intermediate GB
        self.intermediatePlatformGroupBox = QGroupBox("Intermediate")
        self.intermediatePlatformGroupBox.setCheckable(False)
        self.intermediatePlatformGroupBoxLayout = QVBoxLayout()
        self.intermediatePlatformGroupBox.setLayout(self.intermediatePlatformGroupBoxLayout)
        self.intermediatePlatformGroupBox.setObjectName("intermediatePlatformGroupBox")
        # CBp4: Replit Checkbox
        self.replitCheckBox = QCheckBox(self.intermediatePlatformGroupBox)
        self.replitCheckBox.setFixedWidth(self.CBW)
        self.replitCheckBox.setFixedHeight(self.CBH)
        self.replitCheckBox.setObjectName("replitCheckBox")
        # Add to QGroupBox
        self.intermediatePlatformGroupBoxLayout.addWidget(self.replitCheckBox)
        "ADVANCED"
        # Advanced GB
        self.advancedPlatformGroupBox = QGroupBox("Advanced")
        self.advancedPlatformGroupBox.setCheckable(False)
        self.advancedPlatformGroupBoxLayout = QVBoxLayout()
        self.advancedPlatformGroupBox.setLayout(self.advancedPlatformGroupBoxLayout)
        self.advancedPlatformGroupBox.setObjectName("advancedPlatformGroupBox")
        # CBp5: Personal IDE Checkbox
        self.personalIdeCheckBox = QCheckBox(self.advancedPlatformGroupBox)
        self.personalIdeCheckBox.setFixedWidth(self.CBW + 20)
        self.personalIdeCheckBox.setFixedHeight(self.CBH)
        self.personalIdeCheckBox.setObjectName("personalIdeCheckBox")
        # CBp6: RaspberriPi Checkbox
        self.raspberriPiCheckBox = QCheckBox(self.advancedPlatformGroupBox)
        self.raspberriPiCheckBox.setFixedWidth(self.CBW + 20)
        self.raspberriPiCheckBox.setFixedHeight(self.CBH)
        self.raspberriPiCheckBox.setObjectName("raspberriPiCheckBox")
        # Add to QGroupBox
        self.advancedPlatformGroupBoxLayout.addWidget(self.personalIdeCheckBox)
        self.advancedPlatformGroupBoxLayout.addWidget(self.raspberriPiCheckBox)
        "OTHER"
        # Other GB
        self.otherPlatformGroupBox = QGroupBox("Other")
        self.otherPlatformGroupBox.setCheckable(False)
        self.otherPlatformGroupBoxLayout = QVBoxLayout()
        self.otherPlatformGroupBox.setLayout(self.otherPlatformGroupBoxLayout)
        self.otherPlatformGroupBox.setObjectName("otherPlatformGroupBox")
        # CBp7: Hacker Rank Checkbox
        self.hackerrankCheckBox = QCheckBox(self.otherPlatformGroupBox)
        self.hackerrankCheckBox.setFixedWidth(self.CBW + 20)
        self.hackerrankCheckBox.setFixedHeight(self.CBH)
        self.hackerrankCheckBox.setObjectName("hackerrankCheckBox")
        # CBp8: LeetCode Checkbox
        self.leetcodeCheckBox = QCheckBox(self.otherPlatformGroupBox)
        self.leetcodeCheckBox.setFixedWidth(self.CBW + 20)
        self.leetcodeCheckBox.setFixedHeight(self.CBH)
        self.leetcodeCheckBox.setObjectName("leetcodeCheckBox")
        # CBp9: Checkio Checkbox
        self.checkioCheckBox = QCheckBox(self.otherPlatformGroupBox)
        self.checkioCheckBox.setFixedWidth(self.CBW + 20)
        self.checkioCheckBox.setFixedHeight(self.CBH)
        self.checkioCheckBox.setObjectName("checkioCheckBox")
        # Add to QGroupBox
        self.otherPlatformGroupBoxLayout.addWidget(self.hackerrankCheckBox)
        self.otherPlatformGroupBoxLayout.addWidget(self.leetcodeCheckBox)
        self.otherPlatformGroupBoxLayout.addWidget(self.checkioCheckBox)

        """ Concepts Covered GB """
        "BEGINNER"
        # Beginner Concept GB
        self.beginnerConceptsGroupBox = QGroupBox("Beginner")
        self.beginnerConceptsGroupBox.setCheckable(False)
        self.beginnerConceptsGroupBoxLayout = QVBoxLayout()
        self.beginnerConceptsGroupBox.setLayout(self.beginnerConceptsGroupBoxLayout)
        self.beginnerConceptsGroupBox.setObjectName("beginnerConceptsGroupBox")
        # # CBp1: Scratch Checkbox
        # self.scratchCheckBox = QCheckBox(self.beginnerPlatformGroupBox)
        # self.scratchCheckBox.setFixedWidth(self.CBW)
        # self.scratchCheckBox.setFixedHeight(self.CBH)
        # self.scratchCheckBox.setObjectName("scratchCheckBox")
        # # Add to QGroupBox
        # self.beginnerPlatformGroupBoxLayout.addWidget(self.scratchCheckBox)

        "INTERMEDIATE"
        # Intermediate Concept  GB
        self.intermediateConceptsGroupBox = QGroupBox("Intermediate")
        self.intermediateConceptsGroupBox.setCheckable(False)
        self.intermediateConceptsGroupBoxLayout = QVBoxLayout()
        self.intermediateConceptsGroupBox.setLayout(self.intermediateConceptsGroupBoxLayout)
        self.intermediateConceptsGroupBox.setObjectName("intermediateConceptsGroupBox")
        # # CBp4: Replit Checkbox
        # self.replitCheckBox = QCheckBox(self.intermediatePlatformGroupBox)
        # self.replitCheckBox.setFixedWidth(self.CBW)
        # self.replitCheckBox.setFixedHeight(self.CBH)
        # self.replitCheckBox.setObjectName("replitCheckBox")
        # # Add to QGroupBox
        # self.intermediatePlatformGroupBoxLayout.addWidget(self.replitCheckBox)
        "ADVANCED"
        # Advanced Concept  GB
        self.advancedConceptsGroupBox = QGroupBox("Advanced")
        self.advancedConceptsGroupBox.setCheckable(False)
        self.advancedConceptsGroupBoxLayout = QVBoxLayout()
        self.advancedConceptsGroupBox.setLayout(self.advancedConceptsGroupBoxLayout)
        self.advancedConceptsGroupBox.setObjectName("advancedConceptsGroupBox")
        # # CBp5: Personal IDE Checkbox
        # self.personalIdeCheckBox = QCheckBox(self.advancedPlatformGroupBox)
        # self.personalIdeCheckBox.setFixedWidth(self.CBW + 20)
        # self.personalIdeCheckBox.setFixedHeight(self.CBH)
        # self.personalIdeCheckBox.setObjectName("personalIdeCheckBox")
        #
        # # Add to QGroupBox
        # self.advancedPlatformGroupBoxLayout.addWidget(self.personalIdeCheckBox)

    """
TRANSLATE WIDGETS/LABELS/BUTTONS (SETS TEXT FOR ALL OBJECTS)
    """
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        # Main Window Title
        self.mainWindow.setWindowTitle(_translate("mainWindow", "SNC V.1.0.1 "))

        "MENU/STATUS BAR TEXT"
        self.menubar.setStatusTip(_translate("mainWindow", "File Options"))
        # FILE TAB
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        # INSIDE FILE TAB
            # SAVE TAB
        self.actionSave.setText(_translate("mainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("mainWindow", "| Saves Text File to Application Directory |"))
        # VIEW TAB
        self.menuView.setTitle(_translate("mainWindow", "View"))
        self.menuView.setStatusTip(_translate("mainWindow", "| View Application Information |"))
        # INSIDE VIEW TAB
            # ABOUT TAB
        self.actionAbout.setText(_translate("mainWindow", "About"))
        self.actionAbout.setStatusTip(_translate("mainWindow", "| About the Awesome Developer |"))




        """     STUDENT INFO Groupbox TEXT      """
        # GB3: Student Info Groupbox
        self.studentInfoGroupbox.setStatusTip("| Fill out student information |")
        # L1
        self.studentNameLabel.setText(_translate("studentNameLabel", "Name(s): "))
        # L2
        self.languageUsedLabel.setText(_translate("languageUsedLabel", "Language: "))
        # L3
        self.pronounsLabel.setText(_translate("pronounsLabel", "Pronouns: "))
        # T1
        self.studentNameBox.setPlaceholderText(_translate("studentNameBox", "Enter Student Names, sep=\",\""))
        self.studentNameBox.setStatusTip("| Enter student names here, for multiple students, seperate with a comma |")
        # ComB1
        self.languageComboBox.setStatusTip("| Choose programming language student used |")
        # ComB2
        self.studentPronounComboBox.setStatusTip("| Choose pronouns for student(s) |")


        """     LESSON TYPE GROUP BOX TEXT       """
        # GB1: Lesson Type Group Box
        self.lessonTypeGroupBox.setStatusTip("| Select the nature of the lesson |")
        # CBa1
        self.learnCheckBox.setText(_translate("learnCheckBox", "Learn"))
        # CBa2
        self.reviewCheckBox.setText(_translate("reviewCheckBox", "Review"))
        # CBa3
        self.practiceCheckBox.setText(_translate("practiceCheckBox", "Practice"))
        # CBa4
        self.challengeCheckBox.setText(_translate("challengeCheckBox", "Challenge"))
        # CBa5
        self.projectCheckBox.setText(_translate("projectCheckBox", "Project"))


        """     PROJECT NAME GB TEXT      """
        # T2
        self.projectNameBox.setPlaceholderText(_translate("projectNameBox", "Enter Project Name"))
        self.projectNameBox.setStatusTip("| Enter name of student's project here | OUTPUT -> (STUDENT) worked on their (PROJECT) today |")



        """     SESSION STATEMENT GROUP BOX TEXT      """
        # GB2: Session Statement Group Box
        self.sessionStatementGroupBox.setStatusTip("| OUTPUT -> (STUDENT) did (STATEMENT) today | Ex. Bob did well today... |")
        # CBb1
        self.decentStatementCheckbox.setText(_translate("decentStatementCheckbox", "Decent"))
        # CBb2
        self.goodStatementCheckbox.setText(_translate("goodStatementCheckbox", "Good"))
        # CBb3
        self.greatStatementCheckbox.setText(_translate("greatStatementCheckbox", "Great"))


        """     PLATFORMS USED GROUP BOX TEXT      """
        # GB4: Platforms Used Group Box
        self.platformsUsedGroupBox.setStatusTip("| Select platform(s) student used during session |")
        # L4
        self.platformsAddLabel.setText(_translate("platformsAddLabel", "Addt'l Platforms: "))
        # T3
        self.platformsNameBox.setStatusTip("| Add custom platforms not listed |")
        self.platformsNameBox.setPlaceholderText(_translate("platformsNameBox", "Enter Custom Platform "))
        # CBp1
        self.scratchCheckBox.setText(_translate("scratchCheckBox", "Scratch"))
        # CBp2
        self.codecombatCheckBox.setText(_translate("codecombatCheckBox", "CodeCombat"))
        # CBp3
        self.woofjsCheckBox.setText(_translate("woofjsCheckBox", "WoofJs"))
        # CBp4
        self.replitCheckBox.setText(_translate("replitCheckBox", "Repl.it"))
        # CBp5
        self.personalIdeCheckBox.setText(_translate("personalIdeCheckBox", "Personal IDE"))
        # CBp6
        self.raspberriPiCheckBox.setText(_translate("raspberriPiCheckBox", "RaspberriPi"))
        # CBp7
        self.hackerrankCheckBox.setText(_translate("hackerrankCheckBox", "Hacker Rank"))
        # CBp8
        self.leetcodeCheckBox.setText(_translate("leetcodeCheckBox", "LeetCode"))
        # CBp9
        self.checkioCheckBox.setText(_translate("checkioCheckBox", "Checkio"))



        """     CONCEPTS COVERED GROUP BOX TEXT      """
        # GB5: Concepts Covered Group Box
        self.conceptsCoveredGroupBox.setStatusTip("| Select concept(s) student covered during session |")
        # L5
        self.conceptsAddLabel.setText(_translate("conceptsAddLabel", "Addt'l Concepts: "))
        # T4
        self.conceptsNameBox.setStatusTip("| Add custom concepts not listed |")
        self.conceptsNameBox.setPlaceholderText(_translate("conceptsNameBox", "Enter Addt'l Concepts, sep=\",\""))

        "BUTTON TEXT"
        # B1
        self.createNoteBtn.setText(_translate("createNoteBtn", ""))
        self.createNoteBtn.setStatusTip("| Click to Create Text File  |  Red: Not Ready | Yellow: Ready | Green: Creating File | Grey: Invalid Fields")
        # B2
        self.playPauseBtn.setText(_translate("playPauseBtn", ""))
        self.playPauseBtn.setStatusTip("| Play/Pause Button |")


    """
CREATE SIGNALS AND SLOTS
    """
    def connectSignals(self):
        "Open Window Button"
        self.openWindowBtn.clicked.connect(lambda: self.showHideObject(self.window_1))
        "JukeBox Play/Pause Button"
        self.playPauseBtn.clicked.connect(self.playPauseJukeBox)
        "Project Checkbox to Line Edit"
        self.projectCheckBox.stateChanged.connect(lambda: self.showHideObject(self.projectNameGroupbox))
        "Lesson Type Groupbox Uncheck All Boxes"
        for box in self.lessonTypeGroupBox.findChildren(QCheckBox):
            box.clicked.connect(self.uncheckBoxes)
        "Session Statement Groupbox Uncheck All Boxes"
        for box in self.sessionStatementGroupBox.findChildren(QCheckBox):
            box.clicked.connect(self.uncheckBoxes)

    """
CONNECT FUNCTIONS AND LOGIC
    """
    def showHideObject(self, targetObject:object=None) -> None:
        try:
            if targetObject is None:
                targetObject = self.centralWidget.sender()
            changeState = lambda x: targetObject.show() if x else targetObject.hide()
            senderName = targetObject.objectName()
            isHidden = targetObject.isHidden()
            state = "SHOWING" if isHidden else "HIDING"
            print(f"{state} OBJECT:{senderName}")
            changeState(isHidden)
        except:
            raise AttributeError(f"Check if you connected the right object! {object} does not exist")

    def uncheckBoxes(self, groupObject:object) -> None:
        try:
            sender = self.centralWidget.sender()
            senderGroup = sender.parent()
            print(f"""SENDER:{sender.objectName()} PARENT:{senderGroup.objectName()}""")

            unchk_lst = []
            for box in senderGroup.findChildren(QCheckBox):
                if box != sender:
                    box.setChecked(False)
                    unchk_lst.append(box.objectName())
            print(f"UNCHECKED:{unchk_lst}")
        except:
            raise AttributeError(f"Check if you connected the right object! Object does not exist")

    def validateSend(self) -> None:
        try:
            sender = self.centralWidget.sender()
            senderGroup, senderName = sender.parent(), sender.objectName()
            print(f"{senderName} sent this")
        except:
            raise AttributeError(f"Check if you connected the right object! Object does not exist")

    def showHideWindow(self):
        try:
            sender = self.sender()
            showHide = lambda x: sender.show() if x else sender.hide()
            senderName = sender.objectName()
            isHidden = sender.isHidden()
            state = "SHOWING" if isHidden else "HIDING"
            print(f"{state} OBJECT:{senderName}")
            changeState(isHidden)
        except:
            raise AttributeError(f"Check if you connected the right object! {object} does not exist")


    def initWinOne(self):
        self.window_1 = PopupWindow("Platforms Used")
        # self.window_1 = MyPopup()
        self.window_1.show()
        self.window_1.hide()

class PopupWindow(QMainWindow):
    def __init__(self, winTitle:str="Extra Window"):
        super().__init__()
        self.setWindowTitle(winTitle)
        self.setObjectName(winTitle + " Window")

class MyPopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)

    def paintEvent(self, e):
        dc = QPainter(self)
        dc.drawLine(0, 0, 100, 100)
        dc.drawLine(100, 0, 0, 100)




if __name__ == "__main__":
    MainWindow = MainWindow()
    "EXECUTE COMPLETE APP"
    # Show/Execute GUI - FINAL STEP -
    MainWindow.mainWindow.show()
    MainWindow.app.setStyleSheet(SNC_CSS_SHEET)
    # MainWindow.app.setStyle(QStyleFactory.create('Cleanlooks'))
    # Play Music
    # MainWindow.musicPlayer.play()

    sys.exit(MainWindow.app.exec_())
