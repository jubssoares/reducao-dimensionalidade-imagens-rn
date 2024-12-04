from PIL import Image

def process_image_without_libraries(image_path, threshold=127):
    # Carregar a imagem
    img = Image.open(image_path)
    img = img.convert("RGB")  # Garantir que está no formato RGB

    # Converter para níveis de cinza
    width, height = img.size
    grayscale_image = Image.new("L", (width, height))  # Imagem em tons de cinza
    binary_image = Image.new("1", (width, height))  # Imagem binarizada (1 bit por pixel)

    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            # Conversão para níveis de cinza: fórmula perceptual
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            grayscale_image.putpixel((x, y), gray)
            
            # Binarização usando o limiar (threshold)
            binary_pixel = 255 if gray > threshold else 0
            binary_image.putpixel((x, y), binary_pixel)

    # Salvar os resultados
    grayscale_image.save("grayscale_image.png")
    binary_image.save("binary_image.png")
    print("Imagens salvas como 'grayscale_image.png' e 'binary_image.png'.")

# Caminho para a imagem (substitua pelo caminho correto da imagem)
image_path = "img\lenna.png"
process_image_without_libraries(image_path)
