from flask import Flask, jsonify, render_template, url_for
import random
import socket

app = Flask(__name__)

app.config['STATIC_FOLDER'] = 'static'

pokeneas = [
    {
        "id": 1,
        "nombre": "Informático",
        "altura": "1.75m",
        "habilidad": "Experto visualizador de muñequitas anime",
        "imagen": "informatico.jpg",  # Nombre de tu archivo
        "frase": "Sabes por qué te fuiste baneado, juanceto01?"
    },
    {
        "id": 2,
        "nombre": "Bailarin",
        "altura": "1.68m",
        "habilidad": "Bailar con sonidos de tuerca oxidada",
        "imagen": "bailarin.png", 
        "frase": "Están hablando con un tipo, que muchos lo tildan de boludo, de que eh, uh, mirá como lo descansan, que esto, que el otro, y yo tengo tres propiedades."
    },
    {
        "id": 3,
        "nombre": "Boxeador",
        "altura": "1.88m",
        "habilidad": "Ser la bolsa de boxeo de Viruzz",
        "imagen": "boxeador.png", 
        "frase": "Tengo dos ladrilos en las manos."
    },
    {
        "id": 4,
        "nombre": "Feliz",
        "altura": "1.58m",
        "habilidad": "Capaz de crear y destruir universos",
        "imagen": "feliz.png", 
        "frase": "ANASHE."
    },
    {
        "id": 5,
        "nombre": "Matemático",
        "altura": "1.98m",
        "habilidad": "Capaz de hacer cálculos extremadamente complejos",
        "imagen": "matematico.png", 
        "frase": "77 + 33 = 100"
    },
    {
        "id": 6,
        "nombre": "Enano",
        "altura": "0.58m",
        "habilidad": "Su baja estatura le permite morder los tobillos de sus oponentes",
        "imagen": "pesaje.png", 
        "frase": "Ella me llama, me llama y no sé qué hacer."
    },
    {
        "id": 7,
        "nombre": "Silla de ruedas",
        "altura": "1.38m",
        "habilidad": "Análisis instantaneo de la bolsa de valores",
        "imagen": "silla_de_ruedas.png", 
        "frase": "Clases de historia los jueves."
    },
    {
        "id": 8,
        "nombre": "Vendedor de galletas",
        "altura": "1.78m",
        "habilidad": "Vender galletitas baratas, simplemente un tipazo",
        "imagen": "vendedor_de_galletas.png", 
        "frase": "Momo quien te cortó el pelo para no ir."
    }
]

def get_random_pokenea():
    return random.choice(pokeneas)

# Ruta para el JSON
@app.route('/pokenea/json')
def pokenea_json():
    pokenea = get_random_pokenea()
    return jsonify({
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "container_id": socket.gethostname()
    })

# Ruta para mostrar imagen y frase
@app.route('/pokenea/html')
def pokenea_html():
    pokenea = get_random_pokenea()
    
    image_url = url_for('static', filename=pokenea['imagen'])
    
    return render_template('pokenea.html',
                         image_url=image_url,
                         frase=pokenea['frase'],
                         container_id=socket.gethostname())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)