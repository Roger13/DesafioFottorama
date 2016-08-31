import sys
from PySide.QtCore import Slot
from PySide.QtGui import *
 
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
        #Apply the layout to the page
        self.setLayout(self.layout)
        
        #Create main and configurations page        
        self.mainPage = QWidget(self)
        self.configPage = QWidget(self)
        self.layout.addWidget(self.mainPage)
        self.layout.addWidget(self.configPage)    
        
        
        #Main page definitions begin here        
        
        #Apply the layout to the main page
        self.mainPageLayout = QVBoxLayout()         
        self.mainPage.setLayout(self.mainPageLayout)
        
        # Create the Image Mapper        
        self.imageMap = QPixmap("Images/planet.jpg")             
        # Create label to hold the image
        self.image = QLabel(self.mainPage)
        self.image.setPixmap(self.imageMap)        
        # Add image to the page layout
        self.mainPageLayout.addWidget(self.image)
        
        #Create button to switch view
        self.configButton = QPushButton('&Configurations', self.mainPage)        
        #Add functionality to the button
        self.configButton.clicked.connect(self.configButtonClick)
        #Add button to the page layout
        self.mainPageLayout.addWidget(self.configButton)
        
        
        #Configurations page definition begin here        

        #Apply the layout to the configuration page        
        self.configPageLayout = QFormLayout()
        self.configPage.setLayout(self.configPageLayout)

        #Create dropdown options
        self.imagesNames = ['planet.jpg','cat.png','building.jpg']
        # Create and fill the combo box to choose the salutation
        self.imageName = QComboBox(self.configPage)
        self.imageName.addItems(self.imagesNames)
        # Add it to the form layout with a label
        self.configPageLayout.addRow('Select Image:', self.imageName)             
        
        #Create button to save image chosen
        self.saveButton = QPushButton('&Save', self.configPage)        
        #Add functionality to the button
        self.saveButton.clicked.connect(self.saveButtonClick)
        #Add button to the page layout
        self.configPageLayout.addWidget(self.saveButton)
        
        #Set initial view
        self.mainPage.setVisible(1)
        self.configPage.setVisible(0)

        
    @Slot()
    def configButtonClick(self):
        self.mainPage.setVisible(0)
        self.configPage.setVisible(1)
    @Slot()
    def saveButtonClick(self):
        self.imageMap.load("Images/" + self.imagesNames[self.imageName.currentIndex()])
        self.image.setPixmap(self.imageMap)
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