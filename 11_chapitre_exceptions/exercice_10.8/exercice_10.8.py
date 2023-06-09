def stats_fichier(fichier):
    try:
        with open(fichier, 'r') as fin:
            num_cars = 0
            num_mots = 0
            num_lignes = 0

            for line in fin:
                num_lignes += 1
                num_cars += len(line.strip())
                mots = line.strip().split()
                num_mots += len(mots)

            return (num_cars, num_mots, num_lignes)
    except FileNotFoundError:
        print(f"Fichier '{fichier}' n'a pas été trouvé!.")
    except PermissionError:
        print(f"Permission d'accès au fichier '{fichier}'.")
    except Exception as e:
        print(f"Erreur de lecture de '{fichier}': {str(e)}")

    return None

if __name__ == '__main__':
    stats = stats_fichier('stats.txt')

    if stats:
        num_cars, num_mots, num_lignes = stats
        print(f"Le fichier  contient {num_cars} caractères, {num_mots} mots et {num_lignes} lignes.")
