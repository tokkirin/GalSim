import galsim
import matplotlib.pyplot as plt

# Specify the path to your FITS file
fits_file = '/u/trang34/Desktop/GalSim/examples/output/demo2.fits'

# Read the FITS file into a GalSim Image
image = galsim.fits.read(fits_file)

# Convert the GalSim Image to a NumPy array
img_array = image.array

# Save the image as a PNG file
output_file = '/u/trang34/Desktop/GalSim/examples/output/demo2.png'
plt.imsave(output_file, img_array, cmap='gray')

print(f'Image saved to {output_file}')