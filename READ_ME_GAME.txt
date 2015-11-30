Voici les mécanismes de base du jeu au titre indéterminé.
Suggestion :  jouer en mode plein écran 16 : 9 pour un ratio optimal
La version actuelle comporte les éléments suivants :
-	Création de deux civilisations dont une contrôlée par l’Ai. 
-	2 bâtiments disponibles (QG, Barrack)
-	3 différentes unités (harvesters, marksman, shocker)   
-	2 différents types de munitions (basic, zapper)
-	3 ressources  (gold, crystal, wood)

Le tout entièrement codé (PEP 8 :P) et ne comporte que 3 sensors.  

La majorité des actions possibles sont géré au travers de l’UI.
Sélectionnez un des harvester ou le batiment avec le clique gauche
Cliquez sur le bouton du UI correspondant à un  bâtiment
KEY ‘R’ = rotation du building lorsqu’il est stade de placement
KEY ‘N’ = placer le bâtiment à l’ endroit actuel (oui oui vraiment étrange, c’est à modifier)
KEY ‘W,A,S,D’ = bouger la camera (tout comme bouger la souris dans le côtés de l’écran)
MOUSE drag and drop = sélectionne tout dans le périmètre 
MOUSE wheel ‘up, down’ = zoom in / zoom out
MOUSE right click = harvest resource OR attack OR move (selon sur quell objet on clique)
Sélectionner une seule unité ouvre le UI correspondant à droite de l’écran, cliquez sur les boutons de ce panneau pour créer les objets
Lorsque les unités sont immobiles, elles attaquent a vue n’importe quel ennemie dans son rayon
Lorsque les unités sont en attaque, elles suivent la cible si elle se déplace
Il est possible d’attaquer les unités et bâtiments adverses
L’adversaire attaquera lorsqu’il aura atteint un nombre d’unités

Work in progress : 
-	Peaufinage de l’Ai
-	Gameplay (map simple et efficace, avec beaucoup de micro gestion, 1v1) 
-	Graphics (les mesh actuelles sont temporaire et servent qu’à tester les mécaniques)
-	Plus de building, plus d’unités
-	Hero
-	Multiplayer (le serveur existe déjà et fonctionne)
-	Plus! Autant que faire se peut!
