import cv2

from FieldManagement import FieldManagement


def tryModel(input_file, output_file):
    fieldManager = FieldManagement(input_file)

    # Read sketch of the field
    image = cv2.imread('media/field.png')
    # Set quality for output file as mp4
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(output_file, fourcc, 30,
                             (image.shape[1], image.shape[0]), True)

    while fieldManager.isNotEmpty():
        # Create copy of the sketch
        img = image.copy()
        # Write the current data of the objects over the sketch
        writer.write(fieldManager.updateField(img))

    # Release everything if job is finished
    writer.release()
    print("File {} created successfully!".format(output_file))
    cv2.destroyAllWindows()