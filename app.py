from flask import Flask, render_template, request, jsonify
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Rota da API para processar a imagem e extrair texto (OCR)
@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['image']
    img = Image.open(file.stream).convert('RGB')
    
    width, height = img.size
    
    # Executa o OCR. A opção config='--psm 11' ajuda a detetar texto disperso na imagem
    data = pytesseract.image_to_data(img, config='--psm 11', output_type=pytesseract.Output.DICT)
    
    words = []
    for i in range(len(data['text'])):
        text = data['text'][i].strip()
        conf = int(data['conf'][i])
        
        # Filtra palavras vazias ou com baixo nível de confiança (menor que 30%)
        if conf > 0 and text:

            words.append({
                'text': text,
                'conf': conf,
                'x': (data['left'][i] + data['width'][i]/2) / width,
                'y': (data['top'][i] + data['height'][i]/2) / height,
                'h': data['height'][i] / height,
                'bbox': {
                    'x0': data['left'][i],
                    'y0': data['top'][i],
                    'x1': data['left'][i] + data['width'][i],
                    'y1': data['top'][i] + data['height'][i]
                }
            })

    return jsonify({'words': words})

if __name__ == '__main__':
    app.run(debug=True, port=5001)