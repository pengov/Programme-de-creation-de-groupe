from tkinter.messagebox import showerror
from random import shuffle

a = 0

def generateur( liste_client ) :
        global a
        groupe = []     #       regroupe toute les variables membre_groupe
        membre_groupe = []      #       membre dans le groupe en cours de construction
        shuffle( liste_client ) #       apporte de la diversité aux groupes

        if len( liste_client ) < 4:     #       test si il y a au moins 4 membres
                showerror( 'ERREUR', 'Il n\'y a pas sufisament d\'ahdérents pour la constitution de groupe ( minimum 4 adhérents )' )

        else:
                for client in liste_client:     #       enleve les groupes de tous les clients
                        client.groupe = 0

                #       etape 1.1
                while True:
                        horaire = cherche_horaire( liste_client )  #        trouve l horaire le plus prix
                        if horaire[ 1 ] >= 4:        #       regarde si il y a au moins 4 personnes pottentiel pour faire un groupe
                                membre_groupe = []
                                for i in range( 4 ):    #       trouve les 4 clients avec le moins de possibilite d horaire pour le mettre dans le groupe
                                        client_potentiel = []
                                        for client in liste_client:
                                                if client.groupe == 0 and client.horaire[ horaire[ 0 ] ] == True:
                                                        client_potentiel.append( client )
                                        for client in client_potentiel :
                                                if sum( client.horaire ) == min( [ sum( a.horaire ) for a in client_potentiel ] ):
                                                        membre_groupe.append( client )
                                                        client.groupe = -1
                                                        break
                                groupe.append( { 'membre' : membre_groupe, 'horaire' : horaire[ 0 ], 'activite' : [ None, 1 ] } )

                        else :  break


                #       etape 1.2
                sans_groupe = []
                for client in liste_client:
                        if client.groupe == 0:  #       si le client a pas de groupe
                                for i in groupe:
                                        if len( i[ 'membre' ] ) < 8:    #       si le groupe n est pas remplis
                                                if client.horaire[ i[ 'horaire' ] ] == True:
                                                        i[ 'membre' ].append( client )
                                                        client.groupe = -1
                                                        break
                if len( [ client for client in liste_client if client.groupe == 0 ] ) > 0:
                        groupe.append( { 'membre' : [ client for client in liste_client if client.groupe == 0 ], 'horaire' : None, 'activite' : [ None, 0 ] } )
                #       etape 2
                groupe = reform_groupe( groupe )

                if groupe[ -1 ][ 'horaire' ] == None and a == 0 :
                        a == 1
                        for i in range( 25 ) :
                                groupe = generateur( liste_client )
                                if groupe[ -1 ][ 'horaire' ] != None :
                                        break

                return groupe



def cherche_horaire ( liste_client ):
        nbr_client_horaire = [ 0,0,0,0,0,0,0,0,0,0,0,0 ]        #       trouve les horaires les plus choisis
        for client in liste_client:
                if client.groupe == 0:
                        for i in range( 12 ):
                                nbr_client_horaire[ i ] = nbr_client_horaire[ i ] + client.horaire[ i ]

        for i in range( len( nbr_client_horaire ) ):
                if nbr_client_horaire[ i ] == max( nbr_client_horaire ):
                        return i, nbr_client_horaire[ i ]       #       numero de l horaire et le nbr de clients qui peuvent


def reform_groupe ( groupe ):
        def fonction ( groupe ) :
                for grp in groupe:
                        if grp[ 'horaire' ] != None :
                                note = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
                                for membre in grp[ 'membre' ]:
                                        for i in range( 8 ):
                                                note[ i ] += membre.activite[ i ]
                                for i in range( len( note ) ):
                                        if note[ i ] == max( note ):
                                                grp[ 'activite' ] = [ i, max( note ) / len( grp[ 'membre' ] ) ] #       n. de l activite, moyenne de l activite
                return groupe

        reboot = True
        while reboot :
                groupe = fonction( groupe )
                copy_groupe = groupe[:]
                for grp in groupe :
                        if grp[ 'horaire' ] != None :
                                for membre in grp[ 'membre' ] :
                                        if membre.activite[ grp[ 'activite' ][ 0 ] ] == min( i.activite[ grp[ 'activite' ][ 0 ] ] for i in grp[ 'membre' ] ) :
                                                can_break = False
                                                for grp2 in groupe :
                                                        if grp2[ 'horaire' ] != None :
                                                                if grp2 != grp :
                                                                        for client in grp2[ 'membre' ] :
                                                                                if client.horaire[ grp[ 'horaire' ] ] == True :
                                                                                        if client.activite[ grp[ 'activite' ][ 0 ] ] > membre.activite[ grp[ 'activite' ][ 0 ] ] :
                                                                                                if client.activite[ grp2[ 'activite' ][ 0 ] ] < membre.activite[ grp2[ 'activite' ][ 0 ] ] :
                                                                                                        grp[ 'membre' ].remove( membre )
                                                                                                        grp[ 'membre' ].append( client )
                                                                                                        grp2[ 'membre' ].remove( client )
                                                                                                        grp2[ 'membre' ].append( membre )
                                                                                                        can_break = True
                                                                                if can_break :  break
                                                        if can_break :  break
                                                if can_break :  break

                if copy_groupe == groupe:
                        reboot = False
                        continue

        return groupe







