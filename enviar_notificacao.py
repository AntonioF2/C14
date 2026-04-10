import os

def enviar_notificacao():
    email_destino = os.environ.get('EMAIL_DESTINO')
    if not email_destino:
        print("Erro: Variável EMAIL_DESTINO não encontrada.")
        return

    print(f"Simulando envio de e-mail para: {email_destino}")
    print("✅ Sucesso: Notificação de pipeline concluído enviada!")

if __name__ == '__main__':
    enviar_notificacao()