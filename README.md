# Image_Mixer
## Overview
This desktop program is designed to provide an interactive and educational experience about the importance of magnitude and phase components in a signal, using 2D grayscale images. The program allows users to open and view four grayscale images, each in a separate viewport. The sizes of the images are unified to the smallest size among them. Users can explore Fourier Transform (FT) components, customize image weights, and apply region-based mixing for output images.

## Features

### Image Viewers
- **Open and View Images:** Users can open and view four grayscale images. Colored images are automatically converted to grayscale.
- **Uniform Sizing:** The sizes of the opened images are unified to the smallest size among them.
- **FT Components Display:** Each image has two displays - one fixed display for the image and the second for FT components (Magnitude, Phase, Real, Imaginary).
- **Easy Browse:** Users can change any image by double-clicking on its viewer.

### Output Viewports
- **Two Output Ports:** The mixer result can be shown in one of two output viewports, each similar to the input image viewport.

### Brightness/Contrast
- **Adjustable Brightness/Contrast:** Users can change the brightness/contrast of the image via mouse dragging. This can be done for any of the four FT components as well.

### Components Mixer
- **Customizable Weights:** The output image is the inverse Fourier transform (ifft) of a weighted average of the FT of the input four images. Users can customize the weights of each image FT via sliders.

### Regions Mixer
- **Region Selection:** Users can pick regions for each FT component - inner region (low frequencies) or outer region (high frequencies). A rectangle drawn on each FT represents the selected region, with customizable size via sliders.

### Realtime Mixing
- **Progress Bar:** A progress bar is shown during the ifft operation, indicating the update of the mixing process.
- **Thread Management:** If a user changes mixing settings while a previous operation is running, the program cancels the previous operation and starts the new request.

![Image Viewer](https://github.com/heshamtamer/Image_Mixer/assets/100705845/b550e18d-d92d-4517-9408-18d9b35cd757)
## Getting Started
1. **Opening Images:** Open up to four grayscale images.
2. **Exploring FT Components:** View and analyze FT components (Magnitude, Phase, Real, Imaginary) for each image.
3. **Customizing Weights:** Adjust the weights of each image FT using sliders.
4. **Selecting Regions:** Pick regions (inner/outer) for each FT component using customizable rectangles.
5. **Realtime Mixing:** Observe the mixing process with a progress bar.
