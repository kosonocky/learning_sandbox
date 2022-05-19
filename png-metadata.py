
from PIL import Image
from PIL.ExifTags import TAGS


def main():
    imagename = './example.HEIC'
    image = Image.open(imagename)
    exifdata = image.getexif()

    info_dict = {
        "Filename": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1)
    }
    for label, value in info_dict.items():
        print(f"{label:25}: {value}")

    print(exifdata)
    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:25}: {data}")
    pass


if __name__ == '__main__':
    main()
