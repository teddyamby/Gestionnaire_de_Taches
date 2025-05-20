import pytest
import os
import json
import shutil
from pathlib import Path
from controller.todo import charger_taches, sauvegarder_taches, JSON_FILE, DATA_DIR

@pytest.fixture(autouse=True)
def setup_teardown():
    # Sauvegarde le fichier original si il existe
    original_exists = JSON_FILE.exists()
    if original_exists:
        backup = DATA_DIR / "taches_backup.json"
        shutil.copyfile(JSON_FILE, backup)
    
    yield  # Exécution des tests
    
    # Nettoyage après les tests
    if original_exists:
        shutil.move(backup, JSON_FILE)
    elif JSON_FILE.exists():
        os.remove(JSON_FILE)

def test_charger_taches_fichier_inexistant():
    assert charger_taches() == []

def test_sauvegarder_et_charger_taches():
    taches_test = [{"id": 1, "titre": "Test", "description": "Test", "terminee": False}]
    sauvegarder_taches(taches_test)
    assert charger_taches() == taches_test

def test_ajouter_tache():
    from controller.todo import ajouter_tache, obtenir_toutes_taches
    ajouter_tache("Tâche test", "Description test")
    taches = obtenir_toutes_taches()
    assert len(taches) == 1
    assert taches[0]["titre"] == "Tâche test"

def test_marquer_terminee():
    from controller.todo import ajouter_tache, marquer_tache_terminee, obtenir_toutes_taches
    ajouter_tache("Tâche à terminer", "")
    assert marquer_tache_terminee(1) is True
    taches = obtenir_toutes_taches()
    assert taches[0]["terminee"] is True

def test_supprimer_tache():
    from controller.todo import ajouter_tache, supprimer_tache, obtenir_toutes_taches
    ajouter_tache("Tâche à supprimer", "")
    assert supprimer_tache(1) is True
    assert len(obtenir_toutes_taches()) == 0