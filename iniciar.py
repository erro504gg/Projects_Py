import subprocess
import os
import ctypes
from PIL import Image

def open_spotify():
    try:
        subprocess.Popen([r"C:\Users\walter.silva\AppData\Local\Microsoft\WindowsApps\Spotify.exe"], shell=True)
        print("Spotify aberto.")
    except Exception as e:
        print(f"Erro ao tentar abrir o Spotify: {e}")

def open_teams():
    try:
        subprocess.Popen([r"C:\Users\walter.silva\AppData\Local\Microsoft\WindowsApps\ms-teams.exe"], shell=True)
        print("Teams aberto.")
    except Exception as e:
        print(f"Erro ao tentar abrir o Teams: {e}")
        
def open_vsCode():
    try:
        vs_code_path = r"C:\Users\walter.silva\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        if os.path.exists(vs_code_path):
            print(f"Abrindo VS Code em: {vs_code_path}") 
            subprocess.Popen([vs_code_path])
            print("VS Code aberto.")
        else:
            print(f"Caminho do VS Code não encontrado: {vs_code_path}")
    except Exception as e:
        print(f"Erro ao tentar abrir o VS Code: {e}")

def open_edge(url="https://www.example.com"):
    try:
        subprocess.Popen(["start", "msedge", url], shell=True)
        print("Microsoft Edge aberto.")
    except Exception as e:
        print(f"Erro ao tentar abrir o Microsoft Edge: {e}")

def convert_image_to_bmp(image_path):
    bmp_path = os.path.splitext(image_path)[0] + '.bmp'
    try:
        if os.path.exists(image_path):  
            img = Image.open(image_path)
            img.save(bmp_path, 'BMP')
            return bmp_path
        else:
            print(f"Erro: A imagem não foi encontrada no caminho {image_path}")
            return None
    except Exception as e:
        print(f"Erro ao converter a imagem: {e}")
        return None

def combine_images(image_path_1, image_path_2):
    try:
        img1 = Image.open(image_path_1)
        img2 = Image.open(image_path_2)
        
        new_width = img1.width + img2.width
        new_height = max(img1.height, img2.height)
        
        combined_img = Image.new('RGB', (new_width, new_height))
        
        combined_img.paste(img1, (0, 0))
        combined_img.paste(img2, (img1.width, 0))
        
        return combined_img
    except Exception as e:
        print(f"Erro ao combinar as imagens: {e}")
        return None

def set_background(image_path):
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Imagem não encontrada: {image_path}")
        
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        print(f"Plano de fundo alterado para {image_path}.")
    except Exception as e:
        print(f"Erro ao tentar alterar o plano de fundo: {e}")

if __name__ == "__main__":
    image_path_1 = r"C:\Users\walter.silva\Pictures\Tela2.bmp"
    image_path_2 = r"C:\Users\walter.silva\Pictures\Tela1.bmp"
    
    bmp_path_1 = convert_image_to_bmp(image_path_1)
    bmp_path_2 = convert_image_to_bmp(image_path_2)

    if bmp_path_1 and bmp_path_2:

        combined_image = combine_images(bmp_path_1, bmp_path_2)

        if combined_image:

            combined_bmp_path = os.path.splitext(bmp_path_1)[0] + '_combined.bmp'
            combined_image.save(combined_bmp_path, 'BMP')

            set_background(combined_bmp_path)


    open_spotify()

    open_teams()

    open_vsCode()

    open_edge("https://servicos.cofen.gov.br")
