# Pip-Photocopy  
*Clone / Dupliquez votre environnement Python*

> **EN :** Stupid Tiny helper that snapshots the **exact** state of your current Python
> environment and ships a ready-to-run installer so you can replay it anywhere.  
> **FR :** Mini-outil stupide qui capture l’**état exact** de votre environnement Python et
> fournit un script d’installation pour le reconstituer ailleurs.

---

## Features · Fonctionnalités

| 🛠 | English | Français |
|----|---------|----------|
| **Freeze** | Generates `pyenv_clone.txt` with `pip freeze`. | Génère `pyenv_clone.txt` via `pip freeze`. |
| **Installer** | Creates `install_env.sh` (Unix) or `install_env.bat` (Windows). | Crée `install_env.sh` (Unix) ou `install_env.bat` (Windows). |
| **Self-contained** | Everything lives inside **`Pip-Photocopy/`**. | Tout est placé dans **`Pip-Photocopy/`**. |
| **Pause** | Keeps the console open until you press **Enter**. | Garde la fenêtre ouverte jusqu’à ce que vous appuyiez sur **Entrée**. |

---

## Quick Start · Démarrage Rapide

```bash
# 1 – Place export_env.py at the root of the working project
python export_env.py

## Good Practices · Bonnes pratiques
Use a virtual environment (python -m venv .venv) to avoid system pollution.

Regenerate pyenv_clone.txt whenever you add or upgrade packages.

Test the installer on a fresh container/VM to ensure reproducibility.
