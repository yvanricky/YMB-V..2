# YMB-V..2

‎```markdown
‎# 🧠 YMB v2 — Your Match Bot
‎
‎YMB est un assistant intelligent spécialisé dans l’analyse de matchs et les stratégies de paris sportifs. Plus qu’un bot Telegram, il s’agit d’une **plateforme conversationnelle stratégique**, alliant IA, ergonomie, sécurité et monétisation.
‎
‎---
‎
‎## 🎯 Objectif
‎
‎Créer un assistant performant et conversationnel pour:
‎- Afficher les matchs du jour et à venir
‎- Proposer des analyses tactiques et des pronostics
‎- Répondre aux questions sportives ou stratégiques
‎- Gérer les statuts d’abonnement et les paiements P2P
‎- Offrir une expérience fluide pour tous les profils: passionnés, amateurs ou professionnels du pari
‎
‎---
‎
‎## 🧱 Architecture modulaire
‎
‎Le projet est divisé en modules spécialisés:
‎
‎| Fichier | Rôle |
‎|--------|------|
‎| `bot.py` | Point d’entrée principal du bot |
‎| `matchs.py` | Affichage des matchs du jour |
‎| `analyses.py` | Analyse IA enrichie |
‎| `pronostics.py` | Suggestions IA avec justification |
‎| `listener.py` | Écoute des requêtes utilisateur |
‎| `conversation_ai.py` | Réponse IA avec contexte |
‎| `paiement.py` | Instructions de paiement et validation |
‎| `subscriptions.py` | Statuts utilisateurs, expiration, activation |
‎| `support.py` | Notice utilisateur & commande `/aide_support` |
‎| `config_loader.py` | Chargement des clés sécurisées |
‎| `logger.py` | Suivi des actions et erreurs |
‎| `error_handler.py` | Fallbacks et erreurs OpenRouter |
‎| `glossaire.py` | Dictionnaire des termes des paris |
‎
‎---
‎
‎## 🔐 Sécurité
‎
‎- Gestion des identifiants via `.env` (jamais publié)
‎- Fichier `.gitignore` pour protéger les données
‎- Clés chargées avec `python-dotenv`
‎- Paiements en P2P (pas d’intermédiaire tiers)
‎  - ORANGE Money
‎  - MTN Money
‎  - Cryptos: BTC, ETH, USDT, ZEC, BNB
‎  - PayPal: [odmtssarl@gmail.com](mailto:odmtssarl@gmail.com)
‎
‎---
‎
‎## 📲 Commandes principales (13 modules)
‎
‎```text
‎/start                 → Accueil
‎/matchs_du_jour       → Top championnats du jour
‎/grand_format         → Matchs internationaux
‎/live                 → Matchs en direct
‎/programme            → Matchs à venir
‎/analyses             → Lecture tactique IA
‎/pronostics           → Suggestions IA
‎/conseils_paris       → Coupons optimisés
‎/glossaire            → Dictionnaire des termes
‎/aide_support         → Notice explicative
‎/donateurs            → Reconnaissance des contributeurs
‎/enregistrement       → Création de profil
‎/paiement             → Instructions de paiement
‎/abonnement           → Choix de formule + activation
‎```
‎
‎Chaque commande intègre un système d’écoute IA:
‎🔍 L’utilisateur peut poser une question librement → le bot répond immédiatement selon le contexte (match, analyse, pronostic…).
‎
‎---
‎
‎*🔎 IA conversationnelle*
‎
‎- Routage des modèles IA:
‎  - `mistral-7b`
‎  - `gemini-1.5-flash`
‎  - `llama-3-70b`, `llama-8b`, etc.
‎- Prise en compte du contexte utilisateur
‎- Réponses stylisées: raisonnement, storytelling, rapidité, risque
‎
‎---
‎
‎*💳 Paiement & abonnement*
‎
‎- Paiements via Mobile Money, Crypto et PayPal
‎- Génération d’un code de référence unique
‎- Envoi de preuve (capture, hash…)
‎- Activation automatique en base Supabase
‎- Statuts:
‎  - `standard`
‎  - `VIP`
‎  - `donateur`
‎  - `gratuit` (tactique ou test)
‎
‎---
‎
‎*📊 Base Supabase*
‎TableContenu`users`ID Telegram, profil`subscriptions`Statut, expiration`payments`Méthode, montant, code`prompts`Requêtes IA`logs`Actions et navigation`crypto_payments`Paiements cryptos vérifiés`usage_logs`Consommation IA et performance---
‎
‎*🚀 Déploiement*
‎ComposantPlateforme recommandéeBot backendRender / RailwayMini App frontendVercel / Netlify
‎[10/07 à 14:57] Copilote 1: | Base Supabase | Supabase Cloud |
‎| Paiement crypto | Cryptomus ou wallet personnel |
‎| Paiement mobile | P2P manuel |
‎| Nom de domaine | Optionnel |
‎
‎---
‎
‎*📖 Aide et support*
‎
‎La notice complète est disponible via `/aide_support` dans le bot.
‎Elle explique chaque fonction et chaque commande de manière accessible.
‎
‎---
‎
‎*🔧 Installation*
‎
‎```bash
‎git clone https://github.com/votrenom/YMB_v2
‎cd YMB_v2
‎pip install -r requirements.txt
‎python bot.py
‎```
‎
‎Créer un fichier `.env` avec vos clés privées.
‎
‎---
‎
‎*🧠 Auteur*
‎
‎Développé et piloté par *ODMTS SARL CAMEROUN*
‎Visionnaire & stratège digital dans le monde du pari sportif
‎
‎---
‎
‎*☄️ Licence*
‎
‎Projet conçu pour usage professionnel ou personnel.
‎Distribution ou revente non autorisée sans accord explicite.
‎
‎```
‎
