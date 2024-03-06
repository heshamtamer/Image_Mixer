from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsView
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsView
from PyQt5.QtGui import QPixmap,QImage,QColor
import numpy as np
import cv2
import logging

# Set up the logging configuration
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

            
def plot_component(main_app, imgview_name, original_array, index):
    try:
        img_view = main_app.findChild(QGraphicsView, imgview_name)
        if img_view:
            # Retrieve the existing scene
            scene = img_view.scene()
            # Clear the existing items in the scene
            scene.clear()
            pixmap_item = QGraphicsPixmapItem()

            # Convert grayscale_pix_map to a NumPy array
            grayscale_array = original_array
            if grayscale_array.size > 0:
                fourier_result = np.fft.fft2(grayscale_array)
                fourier_shifted = np.fft.fftshift(fourier_result)

                if index == 1:  # FT Magnitude
                    result_img = 20 * np.log(np.abs(fourier_shifted))
                    logging.info("Plotted FT Magnitude")
                elif index == 2:  # FT Phase
                    result_img = np.angle(fourier_shifted)
                    logging.info("Plotted FT Phase")
                elif index == 3:  # FT Real
                    result_img = 20*np.log(np.real(fourier_shifted))
                    logging.info("Plotted FT Real")
                elif index == 4:  # FT Imaginary components
                    result_img = np.imag(fourier_shifted)
                    logging.info("Plotted FT Imaginary")
                else:
                    return
            

                if index == 1 :
                    # Normalize the image data to the range [0, 255]
                    result_img = (result_img - np.min(result_img)) / (np.max(result_img) - np.min(result_img)) * 255
                    result_img = result_img.astype(np.uint8)

                    # Create QImage directly from the NumPy array
                    height, width = result_img.shape
                    real_qimage = QImage(result_img.data.tobytes(), width, height, width, QImage.Format_Grayscale8)
                    pixmap_item.setPixmap(QPixmap.fromImage(real_qimage))
                    scene.addItem(pixmap_item)
                else :
                    height, width = result_img.shape
                    bytes_per_line = width
                    real_qimage = QImage(result_img.astype(np.uint8).tobytes(), width, height, bytes_per_line,
                                        QImage.Format_Grayscale8)
                    pixmap_item.setPixmap(QPixmap.fromImage(real_qimage))
                    scene.addItem(pixmap_item)

                # Fit the view to the new pixmap item
                img_view.setScene(scene)
                img_view.fitInView(pixmap_item, Qt.AspectRatioMode.IgnoreAspectRatio)

                return fourier_shifted  # Return the computed FT component
            else:
                logging.warning("Grayscale array is empty.")
    except Exception as e:
        logging.error(f"Error plotting component: {e}")
        raise e

    