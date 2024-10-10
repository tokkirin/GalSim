import sys
import os
import math
import logging
import yaml
import galsim
import os

def load_yaml(file):
    """Load YAML file from the specified directory."""
    file_path = os.path.join(os.path.dirname(__file__), file)  # Full path
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def main(argv):
    """Generate a blended image using galaxy properties from YAML files."""
    logging.basicConfig(format="%(message)s", level=logging.INFO, stream=sys.stdout)
    logger = logging.getLogger("demo_blended")

    # Load galaxy properties
    blend_params = load_yaml('blend.yaml')
    blendset_params = load_yaml('blendset.yaml')

    logger.info('Starting blended demo with:')
    logger.info('    - PSF (sigma = %.1f)', blendset_params['psf_sigma'])
    logger.info('    - Pixel scale = %.2f', blendset_params['pixel_scale'])
    logger.info('    - Gaussian noise (sigma = %.2f)', blendset_params['noise'])

    # Define the PSF profile
    psf = galsim.Gaussian(flux=1.0, sigma=blendset_params['psf_sigma'])

    # Create an empty image to hold the blended galaxies
    final_image = galsim.ImageF(100, 100, scale=blendset_params['pixel_scale'])

    # Loop over the galaxies and add each one to the final image
    for galaxy in blend_params['galaxies']:
        logger.info(f'Adding galaxy with flux {galaxy["flux"]} and sigma {galaxy["sigma"]}')
        gal = galsim.Gaussian(flux=galaxy['flux'], sigma=galaxy['sigma'])
        final = galsim.Convolve([gal, psf])
        
        # Draw the galaxy image
        gal_image = final.drawImage(scale=blendset_params['pixel_scale'])
        
        # Set position and add to the final image
        position = galaxy['position']
        gal_image.setCenter(position[0], position[1])
        final_image += gal_image

    # Add Gaussian noise to the final image
    final_image.addNoise(galsim.GaussianNoise(sigma=blendset_params['noise']))
    
    # Save the final blended image
    if not os.path.isdir('output'):
        os.mkdir('output')
    file_name = os.path.join('output', 'blended_demo.fits')
    final_image.write(file_name)
    logger.info(f'Wrote blended image to {file_name}')

if __name__ == "__main__":
    main(sys.argv)
