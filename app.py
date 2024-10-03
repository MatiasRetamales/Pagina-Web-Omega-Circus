from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuración del servidor SMTP de Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'matiasretamalescarrera@gmail.com'  # Reemplaza con tu correo de Gmail
app.config['MAIL_PASSWORD'] = 'kcfs byof dkes kusu'  # Reemplaza con la contraseña de tu correo
app.config['MAIL_DEFAULT_SENDER'] = 'matiasretamalescarrera@gmail.com'  # Remitente por defecto

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')  # Ajusta este archivo según tu página principal

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/enviar-formulario', methods=['POST'])
def enviar_formulario():
    # Obtén los datos del formulario
    nombre = request.form['nombre']
    email = request.form['email']
    asunto = request.form['asunto']
    mensaje = request.form['mensaje']

    # Crear el mensaje de correo
    msg = Message(asunto,
                  recipients=['matiasretamalescarrera@gmail.com'])  # Reemplaza con el correo donde quieres recibir los mensajes
    msg.body = f"Nombre: {nombre}\nCorreo: {email}\nAsunto: {asunto}\n\nMensaje:\n{mensaje}"

    # Enviar el correo
    try:
        mail.send(msg)
        print('Correo enviado con éxito')
    except Exception as e:
        print(f'Error al enviar correo: {e}')

    # Redirige a una página de agradecimiento
    return redirect(url_for('gracias'))

@app.route('/gracias')
def gracias():
    return render_template('gracias.html')  # Crea un archivo gracias.html si no lo tienes

if __name__ == '__main__':
    app.run(debug=True)
