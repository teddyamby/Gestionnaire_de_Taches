import json
import os

# Fichier pour stocker les tâches
FICHIER_TACHES = "taches.json"

def charger_taches():
    """Charge les tâches depuis le fichier JSON"""
    if os.path.exists(FICHIER_TACHES):
        with open(FICHIER_TACHES, 'r') as f:
            return json.load(f)
    return []

def sauvegarder_taches(taches):
    """Sauvegarde les tâches dans le fichier JSON"""
    with open(FICHIER_TACHES, 'w') as f:
        json.dump(taches, f, indent=4)

def ajouter_tache():
    """Ajoute une nouvelle tâche"""
    titre = input("Entrez le titre de la tâche: ")
    description = input("Entrez la description: ")
    
    taches = charger_taches()
    taches.append({
        "id": len(taches) + 1,
        "titre": titre,
        "description": description,
        "terminee": False
    })
    sauvegarder_taches(taches)
    print("Tâche ajoutée avec succès!")

def afficher_taches():
    """Affiche toutes les tâches"""
    taches = charger_taches()
    
    if not taches:
        print("Aucune tâche pour le moment.")
        return
    
    print("\nListe des tâches:")
    for tache in taches:
        statut = "✓" if tache["terminee"] else "✗"
        print(f"{tache['id']}. [{statut}] {tache['titre']} - {tache['description']}")

def marquer_terminee():
    """Marque une tâche comme terminée"""
    afficher_taches()
    taches = charger_taches()
    
    if not taches:
        return
    
    try:
        id_tache = int(input("Entrez l'ID de la tâche à marquer comme terminée: "))
        for tache in taches:
            if tache["id"] == id_tache:
                tache["terminee"] = True
                sauvegarder_taches(taches)
                print("Tâche marquée comme terminée!")
                return
        print("ID de tâche non trouvé.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")

def supprimer_tache():
    """Supprime une tâche"""
    afficher_taches()
    taches = charger_taches()
    
    if not taches:
        return
    
    try:
        id_tache = int(input("Entrez l'ID de la tâche à supprimer: "))
        taches = [t for t in taches if t["id"] != id_tache]
        sauvegarder_taches(taches)
        print("Tâche supprimée avec succès!")
    except ValueError:
        print("Veuillez entrer un nombre valide.")

def menu():
    """Affiche le menu principal"""
    while True:
        print("\n--- Gestionnaire de Tâches ---")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Marquer une tâche comme terminée")
        print("4. Supprimer une tâche")
        print("5. Quitter")
        
        choix = input("Choisissez une option (1-5): ")
        
        if choix == "1":
            ajouter_tache()
        elif choix == "2":
            afficher_taches()
        elif choix == "3":
            marquer_terminee()
        elif choix == "4":
            supprimer_tache()
        elif choix == "5":
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez choisir entre 1 et 5.")

if __name__ == "__main__":
    menu()