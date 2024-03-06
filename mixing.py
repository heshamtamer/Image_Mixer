import numpy as np
import logging
class Mixer():

    def mix_magnitude_phase(array1, array2, array3, array4, index_1, index_2, 
                        index_3, index_4,weights,dims,roi):
        result_magnitude = 0
        result_phase = 0
        try:
            if roi == "Inner": # Inner
                rect = np.zeros(array1.shape)
                rect[int(dims[0]):int(dims[2])+1,int(dims[1]):int(dims[3])+1] = 1
            else: # Outter
                rect = np.ones(array1.shape)
                rect[int(dims[0]):int(dims[2])+1,int(dims[1]):int(dims[3])+1] = 0

            #Mix magnitude components together
            if index_1 == 1:
                result_magnitude += weights[0] * np.abs((array1))
            if index_2 == 1:
                result_magnitude += weights[1] *np.abs((array2))
            if index_3 == 1:
                result_magnitude += weights[2] *np.abs((array3))
            if index_4 == 1:
                result_magnitude += weights[3] *np.abs((array4))


            # Mix phase components together
            if index_1 == 2:
                result_phase += weights[0] *np.angle((array1))
            if index_2 == 2:
                result_phase += weights[1] *np.angle((array2))
            if index_3 == 2:
                result_phase += weights[2] *np.angle((array3))
            if index_4 == 2:
                result_phase += weights[3] *np.angle((array4))


            # Combine magnitude and phase to produce the result array
            mixed_array = (result_magnitude*rect) * np.exp(1j * (result_phase*rect))

            return mixed_array
        except Exception as e:
            logging.error(f"Error mixing magnitude-phase: {e}")
            raise e

    def mix_real_imaginary(array1, array2, array3, array4, index_1, index_2, 
                            index_3, index_4,weights,dims,roi):
        result_real = 0
        result_imaginary = 0
        try:
            if roi == "Inner": # Inner
                rect = np.zeros(array1.shape)
                rect[int(dims[0]):int(dims[2])+1,int(dims[1]):int(dims[3])+1] = 1
            else: # Outter
                rect = np.ones(array1.shape)
                rect[int(dims[0]):int(dims[2])+1,int(dims[1]):int(dims[3])+1] = 0

            # Mix real components together
            if index_1 == 3:
                result_real += weights[0] * np.real((array1))
            if index_2 == 3:
                result_real += weights[1] * np.real((array2))
            if index_3 == 3:
                result_real += weights[2] * np.real((array3))
            if index_4 == 3:
                result_real += weights[3] * np.real((array4))


            # Mix imaginary components together
            if index_1 == 4:
                result_imaginary += weights[0] * np.imag((array1))
            if index_2 == 4:
                result_imaginary += weights[1] * np.imag((array2))
            if index_3 == 4:
                result_imaginary += weights[2] * np.imag((array3))
            if index_4 == 4:
                result_imaginary += weights[3] * np.imag((array4))

            # Combine real and imaginary to produce the result array
            mixed_array = (result_real*rect) + 1j * (result_imaginary*rect)

            return mixed_array
        except Exception as e:
            logging.error(f"Error mixing real-imaginary: {e}")
            raise e