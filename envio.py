import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del servidor SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # Puerto estándar para SMTP
smtp_user = 'SENDER@gmail.com'  #Sender  Remitente
smtp_password = 'xxxxx xxxxxxx xxxxxx xxxxxx'  #Contraseñas de aplicaciones , verificacion de dos pasos 

# Crear el mensaje de correo electrónico
message = MIMEMultipart()
message['From'] = smtp_user
message['To'] = 'DESTINATARY@gmail.com' # Destinatario
message['Subject'] = 'Test Correo Electrónico HTML'

# Lista de productos
products = [
    {
        'name': 'Product 1',
        'price': '$10',
        'image_url': 'https://picsum.photos/200/300'
    },
    {
        'name': 'Product 2',
        'price': '$50',
        'image_url': 'https://picsum.photos/200/300'
    }
]

variable="hello variable"
# Contenido HTML del correo electrónico
# Contenido HTML del correo electrónico
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Confirmación de Compra</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 500px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border: 1px solid #ddd;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
        header {{
            text-align: center;
        }}
        .number-order {{
            font-weight: bold;
            text-align: right;
        }}
        p {{
            color: #777;
            font-size: 14px;
            text-align: justify;
        }}
        .div-boton {{
            display: flex;
            align-items: left;
        }}
        h1 {{
            color: #333;
        }}
        h3, h4 {{
            text-align: left;
        }}
        main {{
            padding: 20px 0;
        }}
        ul {{
            list-style: none;
            padding: 0;
        }}
        h5 {{
            text-align: left;
        }}
        li {{
            margin-bottom: 5px;
        }}
        img {{
            width: 100px;
            height: 100px;
            border-radius: 5px;
            padding: 2px;
        }}
        .btn-view-order {{
            color: #fff;
            background-color: #2174c2;
            border-radius: 5px;
            padding: 10px 20px;
            border: none;
            margin-right: 5px;
        }}
        .order-summary {{
            display: flex;
            border-bottom: 1px solid #ccc;
        }}
        .div-price-unit {{
            width: 50%;
        }}
        .price-unit {{
            text-align: right;
        }}
        .price-unit-sum, .price-unit-total {{
            text-align: right;
            font-weight: bold;
        }}
        .div-image {{
            width: 50%;
            display: flex;
        }}
        .name-product {{
            text-align: left;
            color: #333;
            font-weight: bold;
            padding-left: 5px;
        }}
        .div-sum {{
            display: flex;
            border-bottom: 1px solid #ccc;
            margin-left: 0px;
        }}
        .div-sum-right {{
            width: 100%;
        }}
        footer {{
            text-align: center;
            color: #777;
            font-size: 14px;
            margin-top: 20px;
        }}
        .div-footer {{
            display: flex;
            align-items: left;
        }}
        .div-footer-information {{
            width: 50%;
        }}
        @media screen and (max-width: 767px) {{
            .div-sum {{
                margin-left: 0px;
            }}
            .div-footer-information {{
                margin-right: 42px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        
        <main>
            <br />
            <br />
            <h5>Order summary</h5>
"""

for product in products:
    html_content += f"""
            <div class="order-summary">
                <div class="div-image">
                    <img src="{product['image_url']}" alt="">
                    <p class="name-product">{product['name']}</p>
                </div>
                <div class="div-price-unit">
                    <p class="price-unit">{product['price']}</p>
                </div>
            </div>
    """

html_content += """
            <div class="div-sum">
                <div>
                    <p>Subtotal</p>
                    <p>Shipping</p>
                    <p>Taxes</p>
                </div>
                <div class="div-sum-right">
                    <p class="price-unit-sum">$60</p>
                    <p class="price-unit-sum">$4</p>
                    <p class="price-unit-sum">$0</p>
                </div>
            </div>
            <div class="div-sum">
                <div>
                    <p>Total</p>
                </div>
                <div class="div-sum-right">
                    <p class="price-unit-total">$ 64 USD</p>
                </div>
            </div>
            <br />
            <br />
        </main>
        <footer>
            <div class="div-footer">
                <div class="div-footer-information">
                    <h5>information variables</h5>
                    <p>""" + variable + """</p>
                 
        </footer>
    </div>
</body>
</html>
"""

# Adjuntar el contenido HTML al mensaje
message.attach(MIMEText(html_content, 'html'))

# Iniciar una conexión segura con el servidor SMTP
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)

    # Enviar el correo electrónico
    server.sendmail(smtp_user, 'DESTINATARY@gmail.com', message.as_string())#Destinatario
    print("El correo electrónico se envió correctamente.")
except Exception as e:
    print(f"Error al enviar el correo electrónico: {str(e)}")
finally:
    # Cerrar la conexión con el servidor SMTP
    server.quit()
