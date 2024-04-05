from javax.swing import JOptionPane
from java.beans import PropertyChangeListener
from com.nomagic.magicdraw.core import Application
from com.nomagic.magicdraw.core import Project
from com.nomagic.magicdraw.core.project import ProjectEventListener

# Listener for projects
# https://jdocs.nomagic.com/182/com/nomagic/magicdraw/core/project/ProjectEventListener.html
class MyProjectListener(ProjectEventListener):
    def projectOpened(self, project):
        #JOptionPane.showMessageDialog( None, "projectOpened")
        print("Nothing to do")

    def projectClosed(self, project):
        #JOptionPane.showMessageDialog( None, "projectClosed")
        print("Nothing to do")

    def projectSaved(self, project):
        #JOptionPane.showMessageDialog( None, "projectSaved")    
        print("Nothing to do")
    
    def projectActivated(self, project):
        #JOptionPane.showMessageDialog( None, "projectActivated")
        print("Nothing to do")

    def projectDeActivated(self, project):
        #JOptionPane.showMessageDialog( None, "projectDeActivated")
        print("Nothing to do")

    def projectReplaced(self, project):
        #JOptionPane.showMessageDialog( None, "projectReplaced")
        print("Nothing to do")

    def projectPreClosed(self, project):
        #JOptionPane.showMessageDialog( None, "projectPreClosed")
        print("Nothing to do")

    def projectPreClosedFinal(self, project):
        #JOptionPane.showMessageDialog( None, "projectPreClosedFinal")    
        print("Nothing to do")
    
    def projectPreSaved(self, project):
        #JOptionPane.showMessageDialog( None, "projectPreSaved")
        print("Nothing to do")

    def projectPreActivated(self, project):
        #JOptionPane.showMessageDialog( None, "projectPreActivated")
        print("Nothing to do")

    def projectPreDeActivated(self, project):
        #JOptionPane.showMessageDialog( None, "projectPreDeActivated")    
        print("Nothing to do")
    
    def projectPreReplaced(self, project):
        #JOptionPane.showMessageDialog( None, "projectPreReplaced")
        print("Nothing to do")

    def projectOpenedFromGUI(self, project):
        JOptionPane.showMessageDialog( None, "projectOpenedFromGUI")
        if project != None:
            propertyListener = MyPropertyListener()    
            project.getRepositoryListenerRegistry().addPropertyChangeListener(propertyListener, None)

    def projectActivatedFromGUI(self, project):
        #JOptionPane.showMessageDialog( None, "projectActivatedFromGUI")
        print("Nothing to do")

# Listener for properties
# https://docs.oracle.com/javase/8/docs/api/java/beans/PropertyChangeListener.html
class MyPropertyListener( PropertyChangeListener ):
    def propertyChange(self, event):
        print("Property changed " + event.getPropertyName())

# Main script starts here
JOptionPane.showMessageDialog( None, "I am the listener on whole project")
projectListener = MyProjectListener()

# https://jdocs.nomagic.com/182/com/nomagic/magicdraw/core/Application.html
Application.getInstance().addProjectEventListener(projectListener)