import cv2
import numpy as np

# img = cv2.imread("leaf.jpg", cv2.IMREAD_GRAYSCALE)
# print(img)
import numpy as np

# Criar imagem preta com uma pequena região branca
image = np.zeros((100, 100), dtype=np.uint8)
image[50:55, 50:55] = 255

# Converter imagem para formato de array numpy
leaf_disease_image = np.array(image)


# leaf_disease_image = cv2.imread("leaf.jpg")
if leaf_disease_image is None:
    print("Não foi possível carregar a imagem.")
    # Saia da função ou trate a exceção de acordo com as suas necessidades
else:
    gray_image = cv2.cvtColor(leaf_disease_image, cv2.COLOR_BGR2GRAY)



def measure_severity_scale(leaf_disease_image):
    """
    Essa função mede a escala de severidade de uma doença em folha a partir de uma imagem.
    
    :param leaf_disease_image: Imagem da folha com a doença.
    :return: Escala de severidade da doença em folha, com valores de 0 a 100.
    """
    # Etapa 1: Pré-processamento da imagem
    # Converta a imagem para escala de cinza
    gray_image = cv2.cvtColor(leaf_disease_image, cv2.COLOR_BGR2GRAY)
    
    # Aplique filtros para suavizar a imagem e remover ruído
    smoothed_image = cv2.GaussianBlur(gray_image, (3, 3), 0)
    
    # Etapa 2: Detecção de bordas
    # Aplique a detecção de bordas para destacar as bordas da folha e da doença
    edges = cv2.Canny(smoothed_image, 50, 150)
    
    # Etapa 3: Extração de características
    # Encontre os contornos da folha e da doença na imagem
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Calcule a área total da folha
    total_leaf_area = cv2.contourArea(contours[0])
    
    # Calcule a área total da doença
    total_disease_area = 0
    for i in range(1, len(contours)):
        total_disease_area += cv2.contourArea(contours[i])
    
    # Etapa 4: Cálculo da escala de severidade
    # Calcule a porcentagem da folha que é afetada pela doença
    disease_severity = (total_disease_area / total_leaf_area) * 100
    
    # Retorne a escala de severidade, com valores de 0 a 100
    return disease_severity
measure_severity_scale(img)
