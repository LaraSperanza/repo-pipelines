import json

def lambda_handler(event, context):
    print("Iniciando la función hello-world-demo...")
    
    message = "¡Hola desde la función hello-world-demo! Versión inicial (v1.2)"
    
    return {
        'statusCode': 200,
        'body': message
    }