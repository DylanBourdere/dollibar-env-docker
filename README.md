# Dolibarr multi-version dev environment (16 → 22)

Ce dépôt contient un environnement de développement Docker pour Dolibarr (versions 16 à 22) avec un dashboard de suivi.

## Pré-requis

- Docker + Docker Compose
- Git (pour cloner les sources Dolibarr)

## Installation rapide

1. Copier la configuration d'environnement :

```bash
cp .env.example .env
```

2. Cloner les versions Dolibarr 16 → 22 :

```bash
./scripts/clone_dolibarr_versions.sh
```

3. Lancer l'environnement :

```bash
docker compose up -d
```

## Accès

- Dashboard : http://localhost:8080
- Dolibarr 16 : http://localhost:8016
- Dolibarr 17 : http://localhost:8017
- Dolibarr 18 : http://localhost:8018
- Dolibarr 19 : http://localhost:8019
- Dolibarr 20 : http://localhost:8020
- Dolibarr 21 : http://localhost:8021
- Dolibarr 22 : http://localhost:8022

## Développement core + modules customs

- **Core Dolibarr** : chaque version est montée depuis `./dolibarr/<version>` dans `/var/www/html`.
- **Modules customs** : placez vos modules dans `./custom-modules` (monté sur `/var/www/html/custom`).

Les modifications sont visibles en direct dans les conteneurs.

## Notes

- Chaque version utilise sa propre base MariaDB (`db16`, `db17`, etc.).
- Pour n'exécuter qu'une version, vous pouvez commenter des services dans `docker-compose.yml`.
