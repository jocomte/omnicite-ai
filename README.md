# ⚡ OmniCite AI - Generative Engine Optimization (GEO) SaaS

OmniCite AI est un Micro-SaaS B2B prêt pour la production conçu pour auditer, surveiller et optimiser la présence de n'importe quelle marque dans les moteurs de recherche IA : **ChatGPT Search, Perplexity Pro, Google Gemini / AI Overviews et Claude 3.5**.

---

## 📁 Architecture du Projet

```text
omnicite-saas/
│
├── server.py                       # Serveur REST API autonome Python (SQLite ORM, Stripe Checkout, capture de leads)
├── index.html                      # Interface Web moderne (Tailwind CSS, Chart.js, Audit interactif, Modals légaux)
├── start.bat                       # Lanceur Windows 1-clic
├── Dockerfile                      # Image Docker de production ultra-légère
├── render.yaml                     # Déploiement 1-clic gratuit sur Render
├── Procfile                        # Déploiement Railway / Heroku
├── .env.example                    # Modèle de variables d'environnement (Stripe, Clés IA)
│
├── business/
│   └── declaration_statut_france.md # Guide légal pas-à-pas : Micro-entreprise, SIRET, URSSAF, TVA, Stripe
│
└── sales/
    ├── cold_email_france.md        # Séquence de prospection 3 étapes en Français (CMO / Fondateurs)
    ├── cold_email_international.md # High-converting 3-step sequence in English for US/Global SaaS
    ├── automated_prospector.py     # Script Python d'audit automatique et génération d'emails personnalisés
    └── lead_generation_guide.md    # Méthode pour extraire 500 prospects qualifiés gratuitement
```

---

## 🚀 Lancement Local Immédiat

### Méthode 1 : Lanceur Windows
Double-cliquez sur `start.bat`.

### Méthode 2 : Ligne de Commande
```bash
python server.py
```
Ouvrez ensuite votre navigateur sur **[http://localhost:8000](http://localhost:8000)**.

---

## ☁️ Déploiement Cloud Gratuit (1 Clic)

### Sur Render (Recommandé) :
1. Poussez ce dossier sur un dépôt GitHub (public ou privé).
2. Rendez-vous sur **[render.com](https://render.com)** et créez un nouveau *Blueprint Instance*.
3. Sélectionnez votre repo : Render détectera automatiquement `render.yaml` et déploiera votre application en HTTPS gratuit avec un sous-domaine `.onrender.com`.

### Sur Railway :
1. Créez un projet sur **[railway.app](https://railway.app)** et liez votre GitHub.
2. Railway exécutera automatiquement le `Procfile` et fournira un domaine public sécurisé.

---

## 💼 Déclaration & Encaissement Bancaire
Consultez le guide complet :
* [Guide Déclaration Micro-Entreprise & Stripe](business/declaration_statut_france.md)
