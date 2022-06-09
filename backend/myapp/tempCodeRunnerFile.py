
picture_path = "image.jpg"

# Open the image using image module from PIL library
# img = Image.open(picture_path)

# Get the current date and
# time from system
# and use strftime function
# to format the date and time.
curr_datetime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

# Split the picture path
# into root and extension
splitted_path = os.path.splitext(picture_path)

# Add the current date time
# between root and extension
modified_picture_path = splitted_path[0] +curr_datetime + splitted_path[1]
print(modified_picture_path)
# Save the image with modified_picture_path
# img.save(modified_picture_path)
