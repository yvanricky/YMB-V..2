```python
from telegram import Update
from telegram.ext import CallbackContext
from context_store import get_context_for_user
from conversation_ai import route_to_model
from logger import ymb_logger
from buttons import generate_contextual_buttons

INDICATEURS_QUESTION = ["?", "penses-tu", "crois-tu", "est-ce que", "tu dirais", "est-il", "as-tu", "quelle", "comment", "pourquoi"]

def is_question_like(text: str) -> bool:
    return any(ind in text.lower() for ind in INDICATEURS_QUESTION)

def handle_text(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    user_text = update.message.text.strip()

    if not is_question_like(user_text):
        return

    context_actif = get_context_for_user(user_id)

    ymb_logger.info(f"[LISTENER] Question détectée | User: {user_id} | Contexte: {context_actif} | Texte: {user_text}")

    try:
        response = route_to_model(user_text, context_actif)
    except Exception as e:
        ymb_logger.error(f"[LISTENER] Erreur IA | {e}")
        response = "🤖 L’analyse n’est pas disponible pour le moment. Merci de réessayer dans quelques instants."

    update.message.reply_text(
        response,
        reply_markup=generate_contextual_buttons(context_actif)
)
```
