# Projet Python
* **Création : 11/12/2018**
* **Auteur : CASTERA Julien**
* **Ecole : Ynov Informatique Bordeaux**
* **1 ère année**

## Fonctionnalités 

* **Lot 1 - Prototype technique :**
    * Un écran de jeu
    * Une balle
        * Spawn au milieu de l'écran
        * Mouvement perpétuel
        * Rebonds
* **Lot 2 - Prototype gameplay :**
    * Un menu principal
    * Deux raquettes
        * Une raquette par joueur
        * Mouvements en axe Y contrôlables au clavier
        * Font rebondir la balle
    * Principe de Victoire :
        * Zone de "But dans chaque camp.
        * Retour au menu quand Victoire.
* **Lot 3 - Généricité :**
    * Un écran de paramétrage
        * Intermédiaire entre le menu principal et l’écran de jeu.
        * Paramétrage du nombre de points gagnants.
        * Paramétrage de la vitesse de la balle.
    * Un écran de fin de partie
        * Stats basiques : Points par Joueur, gagnant, temps.
        * Rejouer ou Menu
* **Lot 4 - Evolution :**
    * “Bulles” de bonus, comme dans “Curve Fever” ou encore “Sports Head Football”.
        * Activé si la balle touche la bulle
        * Nombre, type, couleur, temps et position des bonus aléatoires
        * Affecte les joueurs en fonction de la couleur du bonus
            * Jaune
                * Affecte les deux joueurs
                * Vitesse de la Raquette augmentée
            * Vert
                * Affecte les deux joueurs
                * Taille de la raquette augmentée
            * Rouge
                * Affecte le joueur qui a touché la balle en dernier
                * Vitesse de la Raquette augmentée
            * Bleu
                * Affecte le joueur qui a touché la balle en dernier
                * Taille de la raquette augmentée
            * Violet
                * Affecte le joueur adversaire de celui qui a touché la balle en dernier
                * Vitesse de la raquette ralentie
            * Rose
                * Affecte le joueur adversaire de celui qui a touché la balle en dernier
                * Contrôles de la raquette inversés