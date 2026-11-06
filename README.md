# Neon Casino

Casino de simulation en **crédits fictifs** (aucun argent réel) : 11 jeux dans le navigateur, avec un solde partagé.

| Jeu | Fichier |
|---|---|
| Hall (choix du jeu) | `index.html` |
| Mines | `mines.html` |
| Dice | `dice.html` |
| Plinko | `plinko.html` |
| Crash | `crash.html` |
| Wheel | `wheel.html` |
| Keno | `keno.html` |
| Tower | `tower.html` |
| Doors | `doors.html` |
| Couteaux | `couteaux.html` |
| Coffre-fort (3D) | `coffre.html` |
| Orbite (3D) | `orbite.html` |

## Lancer
Ouvre `index.html` dans un navigateur, ou active **GitHub Pages** (Settings → Pages → branche `main`, dossier racine) pour l'avoir en ligne.
Les jeux 3D chargent Three.js r128 depuis cdnjs : il faut une connexion internet.

## Sources
`sources/` contient le gabarit commun (`base.html`), le socle partagé (`kit.js`), un fichier `.game` par jeu et `build.py`, qui assemble les pages :
```
cd sources && python3 build.py dice plinko crash   # régénère les pages dans ../casino/
```
