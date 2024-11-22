import sys
import os

import cv2
import matplotlib.pyplot as plt  # Importando o matplotlib para plotagem

# Importa as funções process_image e plot_img do módulo 'algoritmo'
from image_processing_clahe.algoritmo import process_image

# Altere para o caminho da sua imagem ou forneça como argumento
if len(sys.argv) > 1:
    image_path = sys.argv[1]  # Obtém o caminho da imagem da linha de comando
else:
    image_path = 'C:\\Users\\lucenara.pereira\\Downloads\\Bootcamp_Engenharia_Dados\\2. Pacote_Python\\cactos.jpg'  # Caminho padrão

# Chama a função para processar a imagem
img, final_img = process_image(image_path)

# Visualiza a imagem original e a processada. Neste caso, não estamos usando a função de plot que existe no algoritmo
plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Converte de BGR para RGB
plt.title('Imagem Original')
plt.xlabel('Pixels')
plt.ylabel('Pixels')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(final_img, cv2.COLOR_BGR2RGB))  # Converte de BGR para RGB
plt.title('Imagem com CLAHE')
plt.xlabel('Pixels')
plt.ylabel('Pixels')

plt.show()  # Exibe as imagens
