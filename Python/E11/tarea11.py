import requests
import os
import bs4
import argparse
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os

description =""" Modo de uso:) :
    tarea11.py -link "Link de donde se extraerán las fotos" """

msj1 = "Extract data from web images"
parser = argparse.ArgumentParser(description=msj1,
                                epilog=description, 
                                formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-link", dest="link", help="link de busqueda", required=True)
params = parser.parse_args()

def extract_images():
    url = params.link 
    os.makedirs('web_images', exist_ok=True) 
    
    # Solo sirve si las imagenes estan enbebidas de la 
    # siguiente forma: http(s)://www.example.com/foto.jpg
    
    print("Haciendo la petición...")
    res = requests.get(url)
    html = res.content
    soup = bs4.BeautifulSoup(html, "html.parser")
    elem = soup.find_all('img')
    if elem == []:
        print('No se encontraron imagenes.')
    else:
        for img in elem:
            try:
                urlfoto = img.get("src")
                picture = requests.get(urlfoto)
                with open(os.path.join('web_images', os.path.basename(urlfoto)), 'wb') as nombre:
                    nombre.write(picture.content)
            except:
                print("No se pudo descargar esta imagen :(")

    print('Proceso finalizado. :)')

def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        #Parse geo references.
        Nsec = exif['GPSInfo'][2][2] 
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][3] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}
        input()
 
 
def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret
    

def printMeta():
    ruta = './web_images/'
    os.chdir(ruta)
    for root, dirs, files in os.walk(".", topdown=False):
        i = 1
        for name in files:
            try:
                exifData = {}
                exif = get_exif_metadata(name)
                f = open("metadata" + str(i) + ".txt", 'w')
                i = i + 1
                f.write("¡SI NO HAY NADA AQUÍ SIGNIFICA QUE LA IMAGEN NO TIENE METADATA!\n\n")
                f.write("Imagen: %s " %(name) + "\n")
                for metadata in exif:
                    f.write("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                    f.write("\n")
                f.close()
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)


if __name__ == "__main__":
    extract_images()
    printMeta()