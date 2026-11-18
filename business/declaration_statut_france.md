# 🏛️ Guide Juridique & Fiscal : Lancer et Déclarer son SaaS B2B en France

Pour vendre légalement votre logiciel SaaS (**OmniCite AI**), encaisser des abonnements avec Stripe et être 100% en règle avec l'administration fiscale et l'URSSAF, voici la démarche pas-à-pas.

---

## 1. Quel Statut Choisir pour Démarrer ?

### Option Recommandée : La Micro-Entreprise (Auto-Entrepreneur)
C'est la solution la plus simple, la plus rapide (création gratuite en 15 minutes en ligne) et sans frais fixes.
- **Plafond de Chiffre d'Affaires :** 77 700 € / an en prestation de services.
- **Cotisations Sociales URSSAF :** ~21,2% uniquement sur ce que vous encaissez. Si vous faites 0 €, vous payez 0 €.
- **Code APE / NAF :** `6201Z` (Programmation informatique) ou `6311Z` (Traitement de données, hébergement).

### Quand Passer en Société (SASU / EURL) ?
Dès que vous dépassez 40 000 € à 50 000 € de CA récurrent ou si vous souhaitez déduire des investissements lourds (serveurs, publicité, sous-traitance) ou vous associer.

---

## 2. Démarche de Création Pas-à-Pas (15 minutes)

1. Rendez-vous sur le site officiel du gouvernement : **[formalites.entreprises.gouv.fr](https://formalites.entreprises.gouv.fr)** (Guichet unique de l'INPI).
2. Créez un compte via FranceConnect.
3. Remplissez le formulaire de création d'entreprise :
   - Activité : *Développement de logiciels SaaS, édition d'applications web et conseil en référencement numérique.*
   - Option fiscale : Choisissez le **Versement Libératoire de l'IR** si votre revenu fiscal de référence le permet (cela bloque l'impôt sur le revenu à seulement 2,2% supplémentaire du CA).
   - Demandez l'**ACRE** (exonération partielle de cotisations la première année, réduisant le taux URSSAF à environ 11%).
4. En 3 à 7 jours ouvrés, vous recevez votre **numéro SIRET** officiel et votre notification INSEE.

---

## 3. Vendre en France, en Europe et à l'International (TVA)

* **Clients en France (B2B ou B2C) :**
  En dessous de **39 100 € de CA**, vous bénéficiez de la *Franchise en base de TVA*. Vous facturez sans TVA avec la mention obligatoire sur vos factures :  
  *« TVA non applicable - article 293 B du CGI »*.

* **Clients Entreprises dans l'Union Européenne (B2B) :**
  Demandez gratuitement votre **numéro de TVA Intracommunautaire** sur votre espace impots.gouv.fr.  
  Vous pouvez facturer en *autoliquidation de TVA* (Reverse Charge) si votre client européen fournit son numéro de TVA intracommunautaire.

* **Clients Hors Union Européenne (USA, Canada, Asie, etc.) :**
  Exportation de services numériques = Facturation sans TVA (0%). Stripe gère automatiquement la détection géographique via son module *Stripe Tax*.

---

## 4. Configuration Bancaire & Stripe

1. Ouvrez un compte bancaire dédié à votre activité (ex: Shine, Qonto, BoursoBank Pro ou Revolut Business).
2. Créez votre compte sur **[stripe.com](https://stripe.com)** :
   - Renseignez votre numéro SIRET.
   - Liez votre compte bancaire pour recevoir vos virements automatiques.
   - Récupérez votre `STRIPE_SECRET_KEY` et collez-la dans le fichier `.env` d'OmniCite.

---

## 5. Obligations Légales Incluses dans OmniCite
Le projet intègre déjà par défaut :
- ✅ **Mentions Légales** (Loi pour la Confiance dans l'Économie Numérique - LCEN).
- ✅ **CGV B2B** avec renonciation expresse au délai de rétractation pour les logiciels dématérialisés.
- ✅ **Politique de Confidentialité RGPD** pour la collecte des emails de prospection.
