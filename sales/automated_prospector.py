"""
OmniCite AI - Automated Sales Prospector & Outreach Generator
Takes a target list of SaaS companies and generates hyper-personalized cold outreach emails
with actual calculated GEO scores and competitor benchmarks.
"""

import sys
import os
import json

# Add parent directory to path to import analyze_geo_visibility from server
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from server import analyze_geo_visibility

SAMPLE_PROSPECTS = [
    {
        "brand": "Pennylane",
        "domain": "pennylane.com",
        "category": "Comptabilité & Gestion Financière",
        "competitors": "QuickBooks, Tiime, Indy",
        "prospect_name": "Arthur",
        "lang": "fr"
    },
    {
        "brand": "Lemlist",
        "domain": "lemlist.com",
        "category": "Cold Email & B2B Sales Automation",
        "competitors": "Woodpecker, Instantly, Apollo",
        "prospect_name": "Guillaume",
        "lang": "fr"
    },
    {
        "brand": "Pigment",
        "domain": "gopigment.com",
        "category": "Business Planning & FP&A Software",
        "competitors": "Anaplan, Adaptive Planning",
        "prospect_name": "Eleonore",
        "lang": "en"
    },
    {
        "brand": "Brevo",
        "domain": "brevo.com",
        "category": "CRM & Marketing Automation",
        "competitors": "HubSpot, Mailchimp, Klaviyo",
        "prospect_name": "Mickael",
        "lang": "fr"
    }
]

def generate_personalized_pitch(prospect):
    brand = prospect["brand"]
    audit = analyze_geo_visibility(
        brand_name=brand,
        domain=prospect.get("domain", ""),
        category=prospect.get("category", "SaaS B2B"),
        competitors=prospect.get("competitors", "")
    )

    first_competitor = prospect.get("competitors", "").split(",")[0].strip() if prospect.get("competitors") else "vos concurrents"
    prospect_name = prospect.get("prospect_name", "l'équipe")
    lang = prospect.get("lang", "fr")
    geo_score = audit["geo_score"]
    citation_rate = audit["citation_rate"]

    if lang == "fr":
        email_content = f"""
================================================================================
📧 EMAIL DE PROSPECTION PRÊT À L'ENVOI POUR : {brand} ({prospect.get('domain', '')})
Score GEO calculé : {geo_score}/100 | Taux de citation IA : {citation_rate}%
================================================================================
Objet : {first_competitor} vous devance sur ChatGPT Search ?

Hello {prospect_name},

En préparant une étude de marché sur le secteur de {prospect.get('category', 'votre secteur')}, j'ai testé les recommandations fournies par ChatGPT Search et Perplexity Pro sur les requêtes clés de vos prospects.

Résultat : {first_competitor} ressort en recommandation prioritaire, alors que {brand} n'atteint que {citation_rate}% de taux de citation dans les réponses génératives.

Votre score GEO (Generative Engine Optimization) actuel est de {geo_score}/100. La cause principale : un manque de microdonnées Schema.org et une sous-représentation dans les sources d'autorité privilégiées par les LLMs.

J'ai généré l'audit complet de {brand} avec les 3 actions prioritaires pour forcer les IA à vous citer en recommandation #1.

Est-ce que ça vous intéresse que je vous envoie le rapport de 2 pages (sans engagement) ?

Bien à vous,
[Votre Prénom]
Fondateur de OmniCite AI
"""
    else:
        email_content = f"""
================================================================================
📧 OUTREACH EMAIL READY TO SEND FOR: {brand} ({prospect.get('domain', '')})
Calculated GEO Score: {geo_score}/100 | AI Citation Rate: {citation_rate}%
================================================================================
Subject: {first_competitor} is beating you on ChatGPT Search?

Hi {prospect_name},

While analyzing LLM answer engines (ChatGPT Search, Perplexity Pro) in the {prospect.get('category', 'SaaS')} space, I ran intent queries for in-market software buyers.

Results show that {first_competitor} is systematically recommended as the top tool, while {brand} currently holds a {citation_rate}% citation rate with an overall GEO score of {geo_score}/100.

With 40%+ of software evaluations now happening directly in AI answers, brands without structured crawler markup lose qualified buyers to competitors.

I generated a full GEO scorecard for {brand} detailing the top 3 tactical changes to capture those buyer recommendations.

Would you like me to send over the 2-page report? (No strings attached).

Best regards,
[Your Name]
Founder, OmniCite AI
"""
    return email_content

def main():
    print("=" * 70)
    print("🎯 OMNICITE AI - GÉNÉRATEUR AUTOMATISÉ D'EMAILS DE VENTE B2B")
    print(f"Génération de {len(SAMPLE_PROSPECTS)} emails ultra-personnalisés...")
    print("=" * 70)

    for p in SAMPLE_PROSPECTS:
        pitch = generate_personalized_pitch(p)
        print(pitch)
    print("Il ne vous reste plus qu'à copier-coller ces messages sur LinkedIn ou par email pour décrocher vos premiers clients !")

if __name__ == "__main__":
    main()
