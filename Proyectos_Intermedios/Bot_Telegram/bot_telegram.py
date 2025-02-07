from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Token del bot (Reemplázalo con el tuyo)
TOKEN = "TU_TOKEN_AQUÍ"

# Función para manejar el comando /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("¡Hola! Soy tu bot de Telegram. ¿En qué puedo ayudarte? 😊")

# Función para responder mensajes de texto
async def responder_mensaje(update: Update, context: CallbackContext):
    texto_usuario = update.message.text
    await update.message.reply_text(f"Has dicho: {texto_usuario}")

# Configuración del bot
def main():
    app = Application.builder().token(TOKEN).build()

    # Handlers (Manejadores de comandos y mensajes)
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_mensaje))

    print("🤖 Bot en ejecución...")
    app.run_polling()

# Ejecutar el bot
if __name__ == "__main__":
    main()
