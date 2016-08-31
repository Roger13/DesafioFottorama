import sys

import sqlite3
# Set the DB interface 
conn = sqlite3.connect('users.db')
c = conn.cursor()  

from os import listdir
from os.path import isfile, join
from PySide.QtCore import Slot
from PySide.QtCore import Qt
from PySide.QtGui import *
 
mypath = "Images/" 

# Every Qt application must have one and only one QApplication object;
# it receives the command line arguments passed to the script, as they
# can be used to customize the application's appearance and behavior
qt_app = QApplication(sys.argv)
 
class LayoutExample(QWidget):
    ''' An example of PySide absolute positioning; the main window
        inherits from QWidget, a convenient widget for an empty window. '''
 
    def __init__(self):
        
        # Initialize the object as a QWidget and
        # set its title and minimum width
        QWidget.__init__(self)
        self.setWindowTitle('Show, Image!')
        self.setMinimumWidth(400)
        self.setMinimumHeight(500)
        
        # Create the QVBoxLayout that lays out the whole form
        self.layout = QVBoxLayout()
        # Apply the layout to the page
        self.setLayout(self.layout)
        
        # Create main and configurations page        
        self.mainPage = QWidget(self)
        self.configPage = QWidget(self)
        self.layout.addWidget(self.mainPage)
        self.layout.addWidget(self.configPage)    
        
        
        # Main page definitions begin here        
        
        # Apply the layout to the main page
        self.mainPageLayout = QVBoxLayout()         
        self.mainPage.setLayout(self.mainPageLayout)
        
        # Create the Image Mapper with the image from users database  
        imgPref = "cat.png" # Default image
        for name in (c.execute("SELECT image FROM users WHERE id = 1")):
            imgPref = name[0]            
        self.imageMap = QPixmap("Images/" + imgPref)             
        # Create label to hold the image
        self.image = QLabel(self.mainPage)
        self.image.setAlignment(Qt.AlignCenter)
        self.image.setPixmap(self.imageMap)        
        # Add image to the page layout
        self.mainPageLayout.addWidget(self.image)
        
        # Create button to switch view
        self.configButton = QPushButton('&Configurations', self.mainPage)        
        # Add functionality to the button
        self.configButton.clicked.connect(self.configButtonClick)
        # Add button to the page layout
        self.mainPageLayout.addWidget(self.configButton)
        
        
        # Configurations page definition begin here        

        # Apply the layout to the configuration page        
        self.configPageLayout = QFormLayout()
        self.configPage.setLayout(self.configPageLayout)

        # Create dropdown options
        self.imagesNames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        # Create and fill the combo box
        self.imageName = QComboBox(self.configPage)
        self.imageName.addItems(self.imagesNames)
        self.imageName.setCurrentIndex(self.imageName.findText(imgPref, Qt.MatchFixedString))
        # Add it to the form layout with a label
        self.configPageLayout.addRow('Select Image:', self.imageName)             
        
        # Create button to save image chosen
        self.saveButton = QPushButton('&Save', self.configPage)        
        # Add functionality to the button
        self.saveButton.clicked.connect(self.saveButtonClick)
        # Add button to the page layout
        self.configPageLayout.addWidget(self.saveButton)
        
        # Set initial view
        self.mainPage.setVisible(1)
        self.configPage.setVisible(0)

        
    @Slot()
    def configButtonClick(self):
        # Change visible page        
        self.mainPage.setVisible(0)
        self.configPage.setVisible(1)
    @Slot()
    def saveButtonClick(self):
        # Apply selected name to the Image Mapper and update it  
        imgPref = self.imagesNames[self.imageName.currentIndex()]
        self.imageMap.load("Images/" + imgPref)
        self.image.setPixmap(self.imageMap)
        
        # Save preference on the database
        c.execute("UPDATE users SET image = '"+ imgPref +"' WHERE id = 1")
        conn.commit()
                
        # Change visible page            
        self.mainPage.setVisible(1)
        self.configPage.setVisible(0)
       
    def run(self):
        # Show the form
        self.show()
        # Run the qt application
        qt_app.exec_()
 
# Create an instance of the application window and run it
app = LayoutExample()
app.run()