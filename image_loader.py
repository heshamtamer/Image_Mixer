# imageloader.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsView
from PyQt5.QtGui import QPixmap,QImage
# from skimage import io
import numpy as np
import cv2
import logging

# Set up the logging configuration
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Loader():
    def load_image(main_app, file_name, imgview_name,expected_size=None):
        try:
            img_view = main_app.findChild(QGraphicsView, imgview_name)
            if img_view:
                scene = QGraphicsScene()
                pixmap_item = QGraphicsPixmapItem()
                # Load the image using OpenCV
                original_image = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
                # Convert NumPy array to QImage
                height, width = original_image.shape
                bytes_per_line = width
                q_image = QImage(original_image.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

                # Set the QPixmap from the QImage
                pixmap = QPixmap.fromImage(q_image)

                pixmap_item.setPixmap(pixmap)
                scene.addItem(pixmap_item)
                img_view.setScene(scene)
                img_view.fitInView(pixmap_item, Qt.AspectRatioMode.IgnoreAspectRatio)

                logging.info(f"Loaded image: {file_name} into {imgview_name}")
                
                return original_image,pixmap
        except Exception as e:
            logging.error(f"Error loading image: {e}")
            raise e
        

        