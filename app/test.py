from geopy.geocoders import Nominatim
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif_data(image_path):
    img = Image.open(image_path)
    exif_data = img._getexif()  # Получаем EXIF-данные

    if not exif_data:
        return None

    decoded_exif = {}
    for tag_id, value in exif_data.items():
        tag = TAGS.get(tag_id, tag_id)
        decoded_exif[tag] = value

    GPSLatitude = decoded_exif["GPSInfo"][2]
    GPSLongitude = decoded_exif["GPSInfo"][4]
    
    geo_location = {}
    geo_location['N'] = str(GPSLatitude)
    geo_location["E"] = str(GPSLongitude)



    return geo_location

def get_geotagging(exif):
    if not exif or 'GPSInfo' not in exif:
        return None

    geotag = exif['GPSInfo']
    
    return {
        GPSTAGS.get(key, key): value
        for key, value in geotag.items()
    }

# Пример использования
image_path = 'img/12.jpg'
exif_data = get_exif_data(image_path)

if exif_data:
    #geolocation = get_geotagging(exif_data)
    for key, value in exif_data.items():
        print(value)
    geotags = Nominatim(user_agent="ATR")
    location = geotags.reverse(exif_data["N"], exif_data["E"])
    print(location.address)
else:
    print("EXIF-данные отсутствуют.")

