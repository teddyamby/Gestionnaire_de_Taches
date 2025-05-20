import json
from pathlib import Path

# Chemins des fichiers
BASE_DIR = Path(__file__).resolve().parent.parent  # Répertoire de base du projet
DATA_DIR = BASE_DIR / "data"  # Dossier pour stocker les données
JSON_FILE = DATA_DIR / "taches.json"  # Fichier JSON pour les tâches

# Créer le dossier data s'il n'existe pas
DATA_DIR.mkdir(exist_ok=True)


def charger_taches():
    """Charge les tâches depuis le fichier JSON"""
    if JSON_FILE.exists():
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)  # Charger les tâches depuis le fichier
            except json.JSONDecodeError:
                return []  # Retourner une liste vide si le fichier est vide ou corrompu
    return []  # Retourner une liste vide si le fichier n'existe pas


def sauvegarder_taches(taches):
    """Sauvegarde les tâches dans le fichier JSON"""
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(
            taches, f, indent=4, ensure_ascii=False
        )  # Sauvegarder les tâches dans le fichier


def ajouter_tache(titre, description):
    """Ajoute une nouvelle tâche"""
    taches = charger_taches()  # Charger les tâches existantes
    taches.append(
        {
            "id": len(taches) + 1,  # Générer un nouvel ID
            "titre": titre,
            "description": description,
            "terminee": False,  # Par défaut, la tâche n'est pas terminée
        }
    )
    sauvegarder_taches(taches)  # Sauvegarder la nouvelle liste de tâches
    return True


def obtenir_toutes_taches():
    """Retourne toutes les tâches"""
    return charger_taches()  # Retourner toutes les tâches


def marquer_tache_terminee(id_tache):
    """Marque une tâche comme terminée"""
    taches = charger_taches()  # Charger les tâches
    for tache in taches:
        if tache["id"] == id_tache:  # Trouver la tâche par ID
            tache["terminee"] = True  # Marquer comme terminée
            sauvegarder_taches(taches)  # Sauvegarder les modifications
            return True
    return False  # Retourner False si l'ID n'existe pas


def supprimer_tache(id_tache):
    """Supprime une tâche"""
    taches = [
        t for t in charger_taches() if t["id"] != id_tache
    ]  # Filtrer la tâche à supprimer
    sauvegarder_taches(taches)  # Sauvegarder la nouvelle liste
    return len(taches) != len(charger_taches())  # Vérifier si une tâche a été supprimée


def menu():
    """Interface en ligne de commande"""
    while True:
        print("\n--- Gestionnaire de Tâches ---")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Marquer une tâche comme terminée")
        print("4. Supprimer une tâche")
        print("5. Quitter")

        choix = input("Choisissez une option (1-5): ")

        if choix == "1":
            titre = input("Entrez le titre de la tâche: ")
            description = input("Entrez la description: ")
            ajouter_tache(titre, description)  # Ajouter une nouvelle tâche
            print("Tâche ajoutée avec succès!")

        elif choix == "2":
            taches = obtenir_toutes_taches()  # Obtenir toutes les tâches
            if not taches:
                print("Aucune tâche pour le moment.")
                continue

            print("\nListe des tâches:")
            for tache in taches:
                statut = "✓" if tache["terminee"] else "✗"  # Afficher statut
                print(
                    f"{tache['id']}. [{statut}] {tache['titre']} - {tache['description']}"
                )

        elif choix == "3":
            taches = obtenir_toutes_taches()
            if not taches:
                print("Aucune tâche à marquer comme terminée.")
                continue

            print("Tâches disponibles:")
            for tache in taches:
                if not tache["terminee"]:
                    print(f"{tache['id']}. {tache['titre']}")

            try:
                id_tache = int(input("ID de la tâche à marquer comme terminée: "))
                if marquer_tache_terminee(id_tache):  # Marquer la tâche comme terminée
                    print("Tâche marquée comme terminée!")
                else:
                    print("ID invalide.")
            except ValueError:
                print("Veuillez entrer un nombre.")

        elif choix == "4":
            taches = obtenir_toutes_taches()
            if not taches:
                print("Aucune tâche à supprimer.")
                continue

            print("Tâches disponibles:")
            for tache in taches:
                print(f"{tache['id']}. {tache['titre']}")

            try:
                id_tache = int(input("ID de la tâche à supprimer: "))
                if supprimer_tache(id_tache):  # Supprimer la tâche
                    print("Tâche supprimée avec succès!")
                else:
                    print("ID invalide.")
            except ValueError:
                print("Veuillez entrer un nombre.")

        elif choix == "5":
            print("Au revoir!")
            break  # Quitter la boucle et le programme

        else:
            print("Option invalide. Veuillez choisir entre 1 et 5.")


if __name__ == "__main__":
    menu()  # Lancer le menu si le script est exécuté directement