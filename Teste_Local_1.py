import sys
import os

# Adiciona o diretório onde o pacote 'image_processing_clahe' está localizado
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'image_processing_clahe')))

# Importa as funções process_image e plot_img do módulo 'algoritmo'
from image_processing_clahe.algoritmo import process_image, plot_img

# Altere para o caminho da sua imagem ou forneça como argumento
if len(sys.argv) > 1:
    image_path = sys.argv[1]  # Obtém o caminho da imagem da linha de comando
else:
    image_path = 'C:\\Users\\lucenara.pereira\\Downloads\\Bootcamp_Engenharia_Dados\\2. Pacote_Python\\cactos.jpg' 

# Chama a função para processar a imagem
img, final_img = process_image(image_path)

# Plota a imagem com a função já implementada no algoritmo
plot_img(img, final_img )



