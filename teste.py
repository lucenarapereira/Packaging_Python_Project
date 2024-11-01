import sys
print(sys.path)

import os
from image_processing_clahe.algoritmo import process_image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'image_processing_clahe')))

# Altere para o caminho da sua imagem ou forneça como argumento
if len(sys.argv) > 1:
    image_path = sys.argv[1]  
else:
    image_path = 'C:\\Users\\..........\\cactos.jpg'  # Caminho da imagem

# Chama a função para processar a imagem
process_image(image_path)
