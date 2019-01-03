from PIL import Image
import cv2
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlFile, ControlText, ControlButton
from pyforms_gui.controls.control_image import ControlImage


class ComputerVisionAlgorithm(BaseWidget):

    def __init__(self, *args, **kwargs):
        super().__init__('Computer vision algorithm example')

        # Definition of the forms fields
        self._first_name = ControlText('First Name')
        self._last_name = ControlText('Last Name')
        self._image_file = ControlFile('Image')
        self._image = ControlImage()
        self._start_button = ControlButton('Start')

        # Define the function that will be called when a file is selected
        self._image_file.changed_event = self.__image_file_selection_event
        # Define the event that will be called when the run button is processed
        self._start_button.value = self.run_event

        # Define the organization of the Form Controls
        self._formset = [
            ('_first_name', '_last_name'),
            ('_image_file', '_start_button'),
            '_image'
        ]

    def __image_file_selection_event(self):
        """
        When the videofile is selected instanciate the video in the player
        """

        self._image.value = cv2.imread(self._image_file.value)

    def __process_frame(self, frame):
        """
        Do some processing to the frame and return the result frame
        """
        return frame

    def run_event(self):
        """
        After setting the best parameters run the full algorithm
        """
        print("The function was executed")


if __name__ == '__main__':
    from pyforms import start_app

    start_app(ComputerVisionAlgorithm)
