import PIL

## TODo: Import the image into an array

## TODO: Determine how many pixels corresponds to how many mm.
# For now, assume camera taking photo of fiber sample remains at a static location, a fixed distance away.
# In future, add a reference calibration of known mm length, to determine how many pixels per mm.
# Question: Do diagonal pixels have the same length as horizontal or vertical ones? no.

## TODO: Isolate each fibre in the image.
# Assume the background is a solid colour and all fibre samples are roughly the same colour.
# Assume no samples overlap.
# Convert all of the background to white.

## TODO: Create a hunt algorithm that hunts for each fiber individually.
# When a fibre is located, all necessary information is collected, including the coordinates of all pixels belonging to the fibre.
# Fibre is found by identifying a correctly coloured pixel from the image's 2D pixel matrix.
# Once all information is collected, all of the fibre's pixels are converted to the background colour. (To ensure no double counting.)

## TODO: Create an algorithm that finds all remaining fibre pixels, once the initial pixel is identified.
# Check 8 pixels surrounding initial pixel.
# If a fiber pixel is identified, continue search.
# Come up with clever algorithm to make sure you don't get pinged back and forth between the same two pixel positions.
# Consider tracking direction of movement? COnsider changing past pixel colour as marker, before moving to new pixel.
# Look into linear algebra ways of simplifying. 

## TODO: Create bin sizes (eg 3mm-4mm)

## TODO: Count how many fibers there are for each bin size.
