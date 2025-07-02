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
# 1 – Place Pip-Photocopy.py at the root of the working project
python Pip-Photocopy.py

## Good Practices · Bonnes pratiques
Use a virtual environment (python -m venv .venv) to avoid system pollution.

Regenerate pyenv_clone.txt whenever you add or upgrade packages.

Test the installer on a fresh container/VM to ensure reproducibility.
```
---

# Guide d'utilisation : Pip‑Photocopy

il faut mettre le script "Pip-photocopy.py" dans le même répertoire que votre script python qui marche sur votre machine puis le lancer.
copiez les deux fichiers du contenu du répertoire "Pip-Photocopy" qui s'est créé ("pyenv_clone.txt" et "install_env.sh" OU "install_env.bat"...)

## 1. Copier ces fichiers de ce répertoire créé
 **Pip-Photocopy/** sur la nouvelle machine ou dans le répertoire de travail souhaité.

```bash
cd /chemin/vers/your-project
```

---

## 2. Créer puis activer un environnement virtuel
### Linux / macOS
```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows
```powershell
python -m venv .venv
.venv\Scripts\activate    # PowerShell ou Cmd
```

> Lorsque le venv est actif, l'invite de commande contient souvent le préfixe « (.venv) ».

---

## 3. Lancer le script d'installation
mettez les deux fichiers créés à la racine de votre projet ("pyenv_clone.txt" et "install_env.sh" OU "install_env.bat"...),
Puis lancez la commande selon votre plateforme:

| Plateforme | Commande |
|------------|----------|
| Linux / macOS | `./install_env.sh` |
| Windows       | `install_env.bat` |


Le script :
1. met **pip** à jour ;
2. installe **exactement** les versions listées dans `pyenv_clone.txt`.

---

## 4. Vérification (optionnel)
```bash
python -m pip list   # compare les versions
python -m pip check  # détecte d'éventuels conflits
```

---

## 5. Utilisation
Tant que le venv est actif :
```bash
python votre_script.py
```

---

# Usage Guide : Pip‑Photocopy

You need to place the "Pip-photocopy.py" script in the same directory as your running Python script on your machine and then run it.
Copy the two files from the contents of the "Pip-Photocopy" directory that was created ("pyenv_clone.txt" and "install_env.sh" OR "install_env.bat"...)

## 1. Copy the files
Copy the files ("pyenv_clone.txt" et "install_env.sh" OU "install_env.bat"...) of **Pip-Photocopy/** (or the whole project) to the new machine or working directory.

```bash
cd /path/to/your-project
```

---

## 2. Create and activate a virtual environment
### Linux / macOS
```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows
```powershell
python -m venv .venv
.venv\Scripts\activate    # PowerShell or Cmd
```

> When the venv is active, the prompt usually shows the prefix "(.venv)".

---

## 3. Run the installation script
copy "pyenv_clone.txt" and "install_env.sh" OR "install_env.bat" into your new folder with the new virtual enrionnement,
And launch:

| Platform | Command |
|----------|---------|
| Linux / macOS | `./install_env.sh` |
| Windows       | `install_env.bat` |

The script will:
1. upgrade **pip**;
2. install **exactly** the versions listed in `pyenv_clone.txt`.

---

## 4. Verify (optional)
```bash
python -m pip list   # check versions
python -m pip check  # ensure no conflicts
```

---

## 5. Use your project
While the venv is active:
```bash
python your_script.py
```
