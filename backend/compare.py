from functions import *
from recorte import *

imagesFolderPath = "./Images/"
similarImagesFolderPath = "./SimilarImages/"
referenceImage = "0039678800_3_1_1.png"

compareSetNumber = 5 
compareMinSimilarity = 10
compareNumberOfComparations = 50

def compare_images(imagen_reference_cv2):
    imagesInFolder = os.listdir(imagesFolderPath)
    maskImgRef = crearMascara(imagen_reference_cv2)

    bestImages = []

    plantilla = eliminar_contorno(imagen_reference_cv2)


    for image in imagesInFolder:
        if (image.endswith(".png")):
            imagen_cv2 = cv2.imread(imagesFolderPath + image, 1)

            maskImgCompare = crearMascara(imagen_cv2)

            if compareReferenceWithImage(imagen_reference_cv2, imagen_cv2, maskImgRef, maskImgCompare, plantilla, imagesFolderPath, image) > 0.1:
                imagen_cv2 = cv2.resize(imagen_cv2, (1024,1024))
                bestImages.append(imagen_cv2)
    
    return bestImages

def main():
    #descargar_imagenes_csv('inditextech_hackupc_challenge_images.csv', './Images')
    
    imagen_reference_cv2 = cv2.imread(imagesFolderPath + referenceImage, 1)


    bestImages = compare_images(imagen_reference_cv2)
    
    
    i = 0
    bestImagesCount = len(bestImages)
    for image in bestImages:
        i += 1
        cv2.imshow(str(i) + " de " + str(bestImagesCount) + "bestImages", image)
        cv2.waitKey(0)

if __name__ == "__main__":
    main()