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
        
        # Create the Image Mapper        
        self.imageMap = QPixmap("Images/cat.png")
        
        # Create label to hold the image
        self.image = QLabel(self)
        self.image.setPixmap(self.imageMap)
        
        # Add image to the page layout
        self.layout.addWidget(self.image)
        
        #Create button to switch view
        self.switchButton =  QPushButton('Configurations', self)
        
        #Add button to the page layout
        self.layout.addWidget(self.switchButton)
        
        #Apply the layout to the page
        self.setLayout(self.layout)
        
       
    def run(self):
        # Show the form
        self.show()
        # Run the qt application
        qt_app.exec_()
 
# Create an instance of the application window and run it
app = LayoutExample()
app.run()