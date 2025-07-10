‎```python
‎# bot.py
‎import logging
‎from telegram import Update
‎from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
‎
‎from config_loader import TELEGRAM_TOKEN
‎from listener import handle_text  # IA conversationnelle
‎from matchs import afficher_matchs_du_jour
‎from analyses import afficher_analyses
‎from pronostics import afficher_pronostics
‎from glossaire import afficher_glossaire
‎from support import afficher_aide_support
‎from paiements import gerer_abonnement, gerer_paiement
‎from subscriptions import enregistrement_utilisateur
‎from logger import ymb_logger
‎
‎# === CONFIGURATION LOGGING ===
‎logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
‎
‎# === COMMANDES PRINCIPALES ===
‎def start(update: Update, context: CallbackContext) -> None:
‎    update.message.reply_text("🎯 Bienvenue sur YMB Bot v2\nTapez une commande comme /matchs_du_jour ou posez une question à l’IA.")
‎
‎# === INITIALISATION DU BOT ===
‎def main():
‎    updater = Updater(TELEGRAM_TOKEN, use_context=True)
‎    dp = updater.dispatcher
‎
‎    # === ROUTAGE DES COMMANDES ===
‎    dp.add_handler(CommandHandler("start", start))
‎    dp.add_handler(CommandHandler("matchs_du_jour", afficher_matchs_du_jour))
‎    dp.add_handler(CommandHandler("analyses", afficher_analyses))
‎    dp.add_handler(CommandHandler("pronostics", afficher_pronostics))
‎    dp.add_handler(CommandHandler("glossaire", afficher_glossaire))
‎    dp.add_handler(CommandHandler("aide_support", afficher_aide_support))
‎    dp.add_handler(CommandHandler("abonnement", gerer_abonnement))
‎    dp.add_handler(CommandHandler("paiement", gerer_paiement))
‎    dp.add_handler(CommandHandler("enregistrement", enregistrement_utilisateur))
‎
‎    # ÉCOUTE DES QUESTIONS TEXTUELLES
‎    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))
‎
‎    # Lancement
‎    updater.start_polling()
‎    updater.idle()
‎
‎if __name__ == "__main__":
‎    ymb_logger.info("✅ Lancement du bot YMB v2")
‎    main()
‎```
‎
‎
‎
‎
