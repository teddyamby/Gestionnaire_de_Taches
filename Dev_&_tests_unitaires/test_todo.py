import pytest
import os
import json
from todo import charger_taches, sauvegarder_taches, FICHIER_TACHES

def setup_module(module):
    """Setup pour les tests"""
    if os.path.exists(FICHIER_TACHES):
        os.rename(FICHIER_TACHES, "taches_backup.json")

def teardown_module(module):
    """Nettoyage après les tests"""
    if os.path.exists(FICHIER_TACHES):
        os.remove(FICHIER_TACHES)
    if os.path.exists("taches_backup.json"):
        os.rename("taches_backup.json", FICHIER_TACHES)

def test_charger_taches_fichier_inexistant():
    """Teste le chargement quand le fichier n'existe pas"""
    assert charger_taches() == []

def test_sauvegarder_et_charger_taches():
    """Teste la sauvegarde et le chargement des tâches"""
    taches_test = [{"id": 1, "titre": "Test", "description": "Description test", "terminee": False}]
    sauvegarder_taches(taches_test)
    taches_chargees = charger_taches()
    assert taches_chargees == taches_test