from tkinter import *
from tkinter.messagebox import askquestion, showerror
from constructeur import generateur
import pickle



######################################################### VARIABLE
jour = 'nouveau'
page = [ 0, 0 ]
client_recherche = None


######################################################### CLASSE
class Client:
        liste = []
        def __init__ ( self ):
                Client.liste.append( self )
                self.groupe = 0
                self.historique = []
                self.nom = ''
                self.prenom = ''
                self.horaire = [ False, False, False, False, False, False, False, False, False, False, False, False ]
                self.activite = [ 1, 1, 1, 1, 1, 1, 1, 1 ]

class Groupe:
        liste = []
        def __init__ ( self, membre, activite, horaire ):
                Groupe.liste.append( self )
                self.membre = membre
                self.activite = activite
                self.horaire = horaire
                self.tkinter = {}
                self.save_tkinter = {}

        def charge_tkinter ( self ):
                self.tkinter = {
                                        'numero' : Label( tk, text = self.save_tkinter[ 'numero' ] ),
                                        'membre': [ Label( tk, text = membre ) for membre in self.save_tkinter[ 'membre' ] ],
                                        'activite' : Label( tk, text = self.save_tkinter[ 'activite' ] ),
                                        'horaire' : Label( tk, text = self.save_tkinter[ 'horaire' ] )
                                        }


######################################################### FONCTION
def Quitter ():
        save = askquestion( 'Sauvegarder ?', 'Voulez-vous sauvegarder ?' )
        if save == 'yes':
                Sauvegarder()
        tk.destroy()

def Sauvegarder ():
        a = []
        for groupe in Groupe.liste:
                a.append( groupe.tkinter )
                del groupe.tkinter
        pickle.dump( [ Client.liste, Groupe.liste ], open( 'donnees.dr', 'wb' ) )
        for n_groupe in range( len( Groupe.liste ) ):
                Groupe.liste[ n_groupe ].tkinter = a[ n_groupe ]

def Nouveau ():
        Affichage( 'nouveau' )

def Recherche ():
        Affichage( 'recherche' )

def NouveauGroupe ():
        global page

        for groupe in Groupe.liste:
                groupe.tkinter[ 'numero' ].place( x = -100, y = -100)
                for membre in groupe.tkinter[ 'membre' ]:
                                membre.place( x = -100, y = -100 )
                groupe.tkinter[ 'activite' ].place( x = -100, y = -100)
                groupe.tkinter[ 'horaire' ].place( x = -100, y = -100)

        #       genere les new groupe
        Groupe.liste = []
        for groupe in generateur( Client.liste ):
                new_groupe = Groupe( groupe[ 'membre' ], groupe[ 'activite' ], groupe[ 'horaire' ] )
                new_groupe.save_tkinter = {
                                                'numero' : str( len( Groupe.liste ) ),
                                                'membre': [ i.prenom + '\n' + i.nom for i in new_groupe.membre ] ,

                                                'activite' : 'musique' if new_groupe.activite[ 0 ] == 0
                                                        else 'soutien\nscolaire' if new_groupe.activite[ 0 ] == 1
                                                        else 'sport' if new_groupe.activite[ 0 ] == 2
                                                        else 'journalisme' if new_groupe.activite[ 0 ] == 3
                                                        else 'litterature' if new_groupe.activite[ 0 ] == 4
                                                        else 'nouvelles\ntechnologies' if new_groupe.activite[ 0 ] == 5
                                                        else 'environnement' if new_groupe.activite[ 0 ] == 6
                                                        else 'photographie' if new_groupe.activite[ 0 ] == 7
                                                        else 'None' if new_groupe.activite[ 0 ] == None
                                                        else showerror( 'ERREUR', 'Erreur inconnus veuillez contacter le programmeur' ),
                                                'horaire' : 'mercredi\n15h-16h' if new_groupe.horaire == 0
                                                        else 'mercredi\n16h-17h' if new_groupe.horaire == 1
                                                        else 'mercredi\n17h-18h' if new_groupe.horaire == 2
                                                        else 'mercredi\n18h-19h' if new_groupe.horaire == 3
                                                        else 'samedi\n15h-16h' if new_groupe.horaire == 4
                                                        else 'samedi\n16h-17h' if new_groupe.horaire == 5
                                                        else 'samedi\n17h-18h' if new_groupe.horaire == 6
                                                        else 'samedi\n18h-19h' if new_groupe.horaire == 7
                                                        else 'dimanche\n15h-16h' if new_groupe.horaire == 8
                                                        else 'dimanche\n16h-17h' if new_groupe.horaire == 9
                                                        else 'dimanche\n17h-18h' if new_groupe.horaire == 10
                                                        else 'dimanche\n18h-19h' if new_groupe.horaire == 11
                                                        else 'None' if new_groupe.horaire == None
                                                        else showerror( 'ERREUR', 'Erreur inconnus veuillez contacter le programmeur' )
                                                        }
                new_groupe.charge_tkinter()

        for client in Client.liste:
                for groupe in Groupe.liste:
                        if client in groupe.membre:
                                client.groupe = groupe

        #       sauvegarde des groupe dans l'historique
        for client in Client.liste:
                if client.groupe != 0:
                                client.historique.append( [ client.groupe.activite, client.groupe.horaire ] )
                                print(  )

        page[ 1 ] = len( Groupe.liste )
        Affichage()

def RetourGroupe ():
        global page
        page[ 0 ] -= 1
        Affichage()

def SuivantGroupe ():
        global page
        page[ 0 ] += 1
        Affichage()

def SuivantNouveau ():
        global jour
        if jour == 'nouveau':      jour = 'horaire'
        Affichage( jour )

def RetourNouveau ():
        global jour
        if jour == 'horaire':     jour = 'nouveau'
        Affichage( jour )

def NouveauTerminer ():
        if VarNouveauNom.get() == '' or VarNouveauPrenom.get() == '':
                showerror( "ERREUR", "Nom et/ou prénom invalides !" )

        elif 0 == [ horaire[ i ][ j ].get() for i in horaire for j in horaire[ i ] ].count( True ):
                showerror( "ERREUR", "Aucun horaire coché!" )
        else:
                question = askquestion( 'Validation', 'Veuillez valider le nouveau adhérent' )
                if question == 'yes':
                        client = Client()

                        client.nom = VarNouveauNom.get().lower()
                        client.prenom = VarNouveauPrenom.get().lower()

                        client.horaire = [ horaire[ 'mercredi' ][ '15h16h' ].get(), horaire[ 'mercredi' ][ '16h17h' ].get(), horaire[ 'mercredi' ][ '17h18h' ].get(), horaire[ 'mercredi' ][ '18h19h' ].get(), horaire[ 'samedi' ][ '15h16h' ].get(), horaire[ 'samedi' ][ '16h17h' ].get(), horaire[ 'samedi' ][ '17h18h' ].get(), horaire[ 'samedi' ][ '18h19h' ].get(), horaire[ 'dimanche' ][ '15h16h' ].get(), horaire[ 'dimanche' ][ '16h17h' ].get(), horaire[ 'dimanche' ][ '17h18h' ].get(), horaire[ 'dimanche' ][ '18h19h' ].get() ]
                        try:
                                client.activite[ 0 ] = activite[ 'musique' ].get()
                                client.activite[ 1 ] = activite[ 'soutien scolaire' ].get()
                                client.activite[ 2 ] = activite[ 'sport' ].get()
                                client.activite[ 3 ] = activite[ 'journalisme' ].get()
                                client.activite[ 4 ] =activite[ 'litterature' ].get()
                                client.activite[ 5 ] = activite[ 'nouvelles technologies' ].get()
                                client.activite[ 6 ] = activite[ 'environnement' ].get()
                                client.activite[ 7 ] = activite[ 'photographie' ].get()
                        except:
                                showerror( "ERREUR", "Les nombres d'entrées des Activités sont invalides !" )
                                del client
                                del Client.liste[ -1 ]

def ConfirmerChangement ():
        if VarNouveauNom.get() == '' or VarNouveauPrenom.get() == '':
                showerror( "ERREUR", "Nom et/ou prénom invalides !" )

        elif 0 == [ horaire[ i ][ j ].get() for i in horaire for j in horaire[ i ] ].count( True ):
                showerror( "ERREUR", "Aucun horaire coché!" )
        else:
                question = askquestion( 'Validation', 'Veuillez valider le nouveau adhérent' )
                if question == 'yes':
                        client = client_recherche

                        client.nom = VarNouveauNom.get().lower()
                        client.prenom = VarNouveauPrenom.get().lower()

                        client.horaire = [ horaire[ 'mercredi' ][ '15h16h' ].get(), horaire[ 'mercredi' ][ '16h17h' ].get(), horaire[ 'mercredi' ][ '17h18h' ].get(), horaire[ 'mercredi' ][ '18h19h' ].get(), horaire[ 'samedi' ][ '15h16h' ].get(), horaire[ 'samedi' ][ '16h17h' ].get(), horaire[ 'samedi' ][ '17h18h' ].get(), horaire[ 'samedi' ][ '18h19h' ].get(), horaire[ 'dimanche' ][ '15h16h' ].get(), horaire[ 'dimanche' ][ '16h17h' ].get(), horaire[ 'dimanche' ][ '17h18h' ].get(), horaire[ 'dimanche' ][ '18h19h' ].get() ]
                        try:
                                client.activite[ 0 ] = activite[ 'musique' ].get()
                                client.activite[ 1 ] = activite[ 'soutien scolaire' ].get()
                                client.activite[ 2 ] = activite[ 'sport' ].get()
                                client.activite[ 3 ] = activite[ 'journalisme' ].get()
                                client.activite[ 4 ] =activite[ 'litterature' ].get()
                                client.activite[ 5 ] = activite[ 'nouvelles technologies' ].get()
                                client.activite[ 6 ] = activite[ 'environnement' ].get()
                                client.activite[ 7 ] = activite[ 'photographie' ].get()
                        except:
                                showerror( "ERREUR", "Les nombres d'entrées des Activités sont invalides !" )
                                del client
                                del Client.liste[ -1 ]

def RechercheMembre ():
        global client_recherche
        client_recherche = None
        nom = VarRechercheNom.get().lower()
        prenom = VarRecherchePrenom.get().lower()
        for client in Client.liste:
                if client.nom == nom and client.prenom == prenom:
                        client_recherche = client
                        Affichage( 'recherche' )
                        break

def Historique ():
        Affichage( 'historique' )

def HistoriqueRetour ():
        Affichage( 'recherche' )

def Affichage ( fenetre = 'accueil' ):
        if fenetre == 'accueil' or fenetre == 'nouveau':        jour = 'nouveau'
        BoutonAccueil.place( x = 5, y = 5 )
        BoutonNouveauGroupe.place( x = -100, y = -100 )

        BoutonRetourGroupe.place( x = -100, y = -100 )
        BoutonSuivantGroupe.place( x = -100, y = -100 )

        for groupe in Groupe.liste:
                groupe.tkinter[ 'numero' ].place( x = -100, y = -100)
                for membre in groupe.tkinter[ 'membre' ]:
                                membre.place( x = -100, y = -100 )
                groupe.tkinter[ 'activite' ].place( x = -100, y = -100)
                groupe.tkinter[ 'horaire' ].place( x = -100, y = -100)

        EntryNouveauNom.place( x = -100, y = -100 )
        LabelNouveauNom.place( x = -100, y = -100 )
        EntryNouveauPrenom.place( x = -100, y = -100 )
        LabelNouveauPrenom.place( x = -100, y = -100 )

        LabelGroupe.place( x = -100, y = -100 )
        LabelMembre.place( x = -100, y = -100 )
        LabelActivite.place( x = -100, y = -100 )
        LabelHoraire.place( x = -100, y = -100 )

        EntryRechercheNom.place( x = -100, y = - 100 )
        EntryRecherchePrenom.place( x = -100, y = - 100 )
        BoutonRechercheOK.place( x = -100, y = -100 )
        BoutonConfirmerChangement.place( x = -100, y = -100 )
        LabelAucunResultat.place( x = -100, y = -100 )
        BoutonHistorique.place( x = -100, y = - 100 )
        BoutonHistoriqueRetour.place( x = -100, y = -100 )
        LabelInfoHistorique[ 'nbr groupe' ].place( x = -100, y = -100 )
        LabelInfoHistorique[ 'musique' ].place( x = -100, y = -100 )
        LabelInfoHistorique[ 'soutien scolaire' ].place( x = -100, y = -100 )
        LabelInfoHistorique[ 'sport' ].place( x = -100, y = -100 )
        LabelInfoHistorique[ 'journalisme' ].place( x = -100, y = -100 )
        LabelInfoHistorique[ 'litterature' ].place( x = -100, y = -100 )
        LabelInfoHistorique[ 'nouvelles technologies' ].place( x = -100, y = -100 )
        LabelInfoHistorique[ 'environnement' ].place( x = -100, y = -100 )
        LabelInfoHistorique[ 'photographie' ].place( x = -100, y = -100 )

        LabelActiviteNote.place( x = -100, y = -100 )
        SpinboxSoutienScolaire.place( x = -100, y = -100 )
        LabelSoutienScolaire.place( x = -100, y = -100 )
        SpinboxPhotographie.place( x = -100, y = -100 )
        LabelPhotographie.place( x = -100, y = -100 )
        SpinboxEnvironnement.place( x = -100, y = -100 )
        LabelEnvironnement.place( x = -100, y = -100 )
        SpinboxNouvellesTechnologies.place( x = -100, y = -100 )
        LabelNouvellesTechnologies.place( x = -100, y = -100 )
        SpinboxLitterature.place( x = -100, y = -100 )
        LabelLitterature.place( x = -100, y = -100 )
        SpinboxJournalisme.place( x = -100, y = -100 )
        LabelJournalisme.place( x = -100, y = -100 )
        SpinboxSport.place( x = -100, y = -100 )
        LabelSport.place( x = -100, y = -100 )
        SpinboxMusique.place( x = -100, y = -100 )
        LabelMusique.place( x = -100, y = -100 )

        LabelMercredi.place( x = -100, y = -100 )
        CheckbuttonMercredi[ '15h16h' ].place( x = -100, y = -100 )
        CheckbuttonMercredi[ '16h17h' ].place( x = -100, y = -100 )
        CheckbuttonMercredi[ '17h18h' ].place( x = -100, y = -100 )
        CheckbuttonMercredi[ '18h19h' ].place( x = -100, y = -100 )
        LabelSamedi.place( x = -100, y = -100 )
        CheckbuttonSamedi[ '15h16h' ].place( x = -100, y = -100 )
        CheckbuttonSamedi[ '16h17h' ].place( x = -100, y = -100 )
        CheckbuttonSamedi[ '17h18h' ].place( x = -100, y = -100 )
        CheckbuttonSamedi[ '18h19h' ].place( x = -100, y = -100 )
        LabelDimanche.place( x = -100, y = -100 )
        CheckbuttonDimanche[ '15h16h' ].place( x = -100, y = -100 )
        CheckbuttonDimanche[ '16h17h' ].place( x = -100, y = -100 )
        CheckbuttonDimanche[ '17h18h' ].place( x = -100, y = -100 )
        CheckbuttonDimanche[ '18h19h' ].place( x = -100, y = -100 )

        BoutonSuivantNouveau.place( x= -100, y = -100 )
        BoutonRetourNouveau.place( x = -100, y = -100 )
        BoutonNouveau.place( x = -100, y = -100 )


        if fenetre == 'accueil':
                BoutonNouveauGroupe.place( x = 350, y = 450 )
                if page[ 0 ] > 0 :
                        BoutonRetourGroupe.place( x = 3, y = 200 )
                if page[ 0 ] < page[ 1 ] - 1:
                        BoutonSuivantGroupe.place( x= 447, y = 200)

                LabelGroupe.place( x = 75, y = 35 )
                LabelMembre.place( x = 175, y = 35 )
                LabelActivite.place( x = 275, y = 35 )
                LabelHoraire.place( x = 375, y = 35 )

                if page[ 1 ] != 0:
                        Groupe.liste[ page[ 0 ] ].tkinter[ 'numero' ].place( x = 100, y = 100 )
                        y = 75
                        for membre in Groupe.liste[ page[ 0 ] ].tkinter[ 'membre' ]:
                                membre.place( x = 175, y = y )
                                y = y + 45
                        Groupe.liste[ page[ 0 ] ].tkinter[ 'activite' ].place( x = 275, y = 100 )
                        Groupe.liste[ page[ 0 ] ].tkinter[ 'horaire' ].place( x = 375, y = 100 )

        elif fenetre == 'recherche' :
                VarRechercheNom.set( 'Nom' )
                VarRecherchePrenom.set( 'Prenom' )

                EntryRechercheNom.place( x = 100, y = 10 )
                EntryRecherchePrenom.place( x = 250, y = 10 )
                BoutonRechercheOK.place( x = 400, y = 10 )

                if client_recherche != None :
                        VarNouveauNom.set( client_recherche.nom )
                        EntryNouveauNom.place( x = 150, y = 50 )
                        LabelNouveauNom.place( x = 300, y = 50 )
                        VarNouveauPrenom.set( client_recherche.prenom )
                        EntryNouveauPrenom.place( x = 150, y = 75 )
                        LabelNouveauPrenom.place( x =300, y = 75 )

                        SpinboxMusique.place( x = 100, y = 125 )
                        activite[ 'musique' ].set( client_recherche.activite[ 0 ] )
                        LabelMusique.place( x = 250, y = 125 )
                        SpinboxSoutienScolaire.place( x = 100, y = 150 )
                        activite[ 'soutien scolaire' ].set( client_recherche.activite[ 1 ] )
                        LabelSoutienScolaire.place( x = 250, y = 150 )
                        SpinboxSport.place( x = 100, y = 175 )
                        activite[ 'sport' ].set( client_recherche.activite[ 2 ] )
                        LabelSport.place( x = 250, y = 175 )
                        SpinboxJournalisme.place( x = 100, y = 200 )
                        activite[ 'journalisme' ].set( client_recherche.activite[ 3 ] )
                        LabelJournalisme.place( x = 250, y = 200 )
                        SpinboxLitterature.place( x = 100, y = 225 )
                        activite[ 'litterature' ].set( client_recherche.activite[ 4 ] )
                        LabelLitterature.place( x = 250, y = 225 )
                        SpinboxNouvellesTechnologies.place( x = 100, y = 250 )
                        activite[ 'nouvelles technologies' ].set( client_recherche.activite[ 5 ] )
                        LabelNouvellesTechnologies.place( x = 250, y = 250 )
                        SpinboxEnvironnement.place( x = 100, y = 275 )
                        activite[ 'environnement' ].set( client_recherche.activite[ 6 ] )
                        LabelEnvironnement.place( x = 250, y = 275 )
                        SpinboxPhotographie.place( x = 100, y = 300 )
                        activite[ 'photographie' ].set( client_recherche.activite[ 7 ] )
                        LabelPhotographie.place( x = 250, y = 300 )

                        LabelMercredi.place( x = 50, y = 350 )
                        CheckbuttonMercredi[ '15h16h' ].place( x = 50, y = 375 )
                        horaire[ 'mercredi' ][ '15h16h' ].set( client_recherche.horaire[ 0 ] )
                        CheckbuttonMercredi[ '16h17h' ].place( x = 50, y = 400 )
                        horaire[ 'mercredi' ][ '16h17h' ].set( client_recherche.horaire[ 1 ] )
                        CheckbuttonMercredi[ '17h18h' ].place( x = 50, y = 425 )
                        horaire[ 'mercredi' ][ '17h18h' ].set( client_recherche.horaire[ 2 ] )
                        CheckbuttonMercredi[ '18h19h' ].place( x = 50, y = 450 )
                        horaire[ 'mercredi' ][ '18h19h' ].set( client_recherche.horaire[ 3 ] )
                        LabelSamedi.place( x = 200, y = 350 )
                        CheckbuttonSamedi[ '15h16h' ].place( x = 200, y = 375 )
                        horaire[ 'samedi' ][ '15h16h' ].set( client_recherche.horaire[ 4 ] )
                        CheckbuttonSamedi[ '16h17h' ].place( x = 200, y = 400 )
                        horaire[ 'samedi' ][ '16h17h' ].set( client_recherche.horaire[ 5 ] )
                        CheckbuttonSamedi[ '17h18h' ].place( x = 200, y = 425 )
                        horaire[ 'samedi' ][ '17h18h' ].set( client_recherche.horaire[ 6 ] )
                        CheckbuttonSamedi[ '18h19h' ].place( x = 200, y = 450 )
                        horaire[ 'samedi' ][ '18h19h' ].set( client_recherche.horaire[ 7 ] )
                        LabelDimanche.place( x = 350, y = 350 )
                        CheckbuttonDimanche[ '15h16h' ].place( x = 350, y = 375 )
                        horaire[ 'dimanche' ][ '15h16h' ].set( client_recherche.horaire[ 8 ] )
                        CheckbuttonDimanche[ '16h17h' ].place( x = 350, y = 400 )
                        horaire[ 'dimanche' ][ '16h17h' ].set( client_recherche.horaire[ 9 ] )
                        CheckbuttonDimanche[ '17h18h' ].place( x = 350, y = 425 )
                        horaire[ 'dimanche' ][ '17h18h' ].set( client_recherche.horaire[ 10 ] )
                        CheckbuttonDimanche[ '18h19h' ].place( x = 350, y = 450 )
                        horaire[ 'dimanche' ][ '18h19h' ].set( client_recherche.horaire[ 11 ] )

                        BoutonConfirmerChangement.place( x = 400, y = 175 )
                        BoutonHistorique.place( x = 400,  y = 225 )

                else:
                        LabelAucunResultat.place( x = 200, y = 100 )

        elif fenetre == 'historique' :
                LabelInfoHistorique[ 'nbr groupe' ].config( text = 'Nombre de groupe ayant rejoint :\t' + str( len( client_recherche.historique ) ) )
                LabelInfoHistorique[ 'musique' ].config( text = 'Qui avait comme thème musique :\t' + str( len( [ groupe for groupe in client_recherche.historique if groupe[ 0 ][ 0 ] == 0 ] ) ) )
                LabelInfoHistorique[ 'soutien scolaire' ].config( text = 'Qui avait comme thème soutien scolaire :\t' + str( len( [ groupe for groupe in client_recherche.historique if groupe[ 0 ][ 0 ] == 1 ] ) ) )
                LabelInfoHistorique[ 'sport' ].config( text = 'Qui avait comme thème sport :\t' + str( len( [ groupe for groupe in client_recherche.historique if groupe[ 0 ][ 0 ] == 2 ] ) ) )
                LabelInfoHistorique[ 'journalisme' ].config( text = 'Qui avait comme thème journalisme :\t' + str( len( [ groupe for groupe in client_recherche.historique if groupe[ 0 ][ 0 ] == 3 ] ) ) )
                LabelInfoHistorique[ 'litterature' ].config( text = 'Qui avait comme thème litterature :\t' + str( len( [ groupe for groupe in client_recherche.historique if groupe[ 0 ][ 0 ] == 4 ] ) ) )
                LabelInfoHistorique[ 'nouvelles technologies' ].config( text = 'Qui avait comme thème nouvelles tecnologies :\t' + str( len( [ groupe for groupe in client_recherche.historique if groupe[ 0 ][ 0 ] == 5 ] ) ) )
                LabelInfoHistorique[ 'environnement' ].config( text = 'Qui avait comme thème environnement :\t' + str( len( [ groupe for groupe in client_recherche.historique if groupe[ 0 ][ 0 ] == 6 ] ) ) )
                LabelInfoHistorique[ 'photographie' ].config( text = 'Qui avait comme thème photographie :\t' + str( len( [ groupe for groupe in client_recherche.historique if groupe[ 0 ][ 0 ] == 7 ] ) ) )

                LabelInfoHistorique[ 'nbr groupe' ].place( x = 50, y = 100 )
                LabelInfoHistorique[ 'musique' ].place( x = 50, y = 125 )
                LabelInfoHistorique[ 'soutien scolaire' ].place( x = 50, y = 150 )
                LabelInfoHistorique[ 'sport' ].place( x = 50, y = 300 )
                LabelInfoHistorique[ 'journalisme' ].place( x = 50, y = 275 )
                LabelInfoHistorique[ 'litterature' ].place( x = 50, y = 250 )
                LabelInfoHistorique[ 'nouvelles technologies' ].place( x = 50, y = 225 )
                LabelInfoHistorique[ 'environnement' ].place( x = 50, y = 200 )
                LabelInfoHistorique[ 'photographie' ].place( x = 50, y = 175 )

                BoutonHistoriqueRetour.place( x = 10, y = 450 )

        elif fenetre == 'nouveau':
                EntryNouveauNom.place( x = 150, y = 50 )
                LabelNouveauNom.place( x = 300, y = 50 )
                EntryNouveauPrenom.place( x = 150, y = 75 )
                LabelNouveauPrenom.place( x =300, y = 75 )

                LabelActiviteNote.place( x = 100, y = 150 )
                SpinboxMusique.place( x = 150, y = 175 )
                LabelMusique.place( x = 300, y = 175 )
                SpinboxSoutienScolaire.place( x = 150, y = 200 )
                LabelSoutienScolaire.place( x = 300, y = 200 )
                SpinboxSport.place( x = 150, y = 225 )
                LabelSport.place( x = 300, y = 225 )
                SpinboxJournalisme.place( x = 150, y = 250 )
                LabelJournalisme.place( x = 300, y = 250 )
                SpinboxLitterature.place( x = 150, y = 275 )
                LabelLitterature.place( x = 300, y = 275 )
                SpinboxNouvellesTechnologies.place( x = 150, y = 300 )
                LabelNouvellesTechnologies.place( x = 300, y = 300 )
                SpinboxEnvironnement.place( x = 150, y = 325 )
                LabelEnvironnement.place( x = 300, y = 325 )
                SpinboxPhotographie.place( x = 150, y = 350 )
                LabelPhotographie.place( x = 300, y = 350 )

                BoutonSuivantNouveau.place( x= 400, y = 450 )

        elif fenetre == 'horaire':
                LabelMercredi.place( x = 200, y = 50 )
                CheckbuttonMercredi[ '15h16h' ].place( x = 200, y = 75 )
                CheckbuttonMercredi[ '16h17h' ].place( x = 200, y = 100 )
                CheckbuttonMercredi[ '17h18h' ].place( x = 200, y = 125 )
                CheckbuttonMercredi[ '18h19h' ].place( x = 200, y = 150 )
                LabelSamedi.place( x = 200, y = 200 )
                CheckbuttonSamedi[ '15h16h' ].place( x = 200, y = 225 )
                CheckbuttonSamedi[ '16h17h' ].place( x = 200, y = 250 )
                CheckbuttonSamedi[ '17h18h' ].place( x = 200, y = 275 )
                CheckbuttonSamedi[ '18h19h' ].place( x = 200, y = 300 )
                LabelDimanche.place( x = 200, y = 350 )
                CheckbuttonDimanche[ '15h16h' ].place( x = 200, y = 375 )
                CheckbuttonDimanche[ '16h17h' ].place( x = 200, y = 400 )
                CheckbuttonDimanche[ '17h18h' ].place( x = 200, y = 425 )
                CheckbuttonDimanche[ '18h19h' ].place( x = 200, y = 450 )

                BoutonNouveau.place( x = 400, y = 450 )
                BoutonRetourNouveau.place( x = 10, y = 450 )

        tk.update()



######################################################### TKINTER
tk = Tk()
tk.title("Constructeur de Groupe" )
tk.resizable( 0, 0 )
tk.wm_attributes( "-topmost", 0 )
tk.geometry( "500x500+100+100" )
tk.protocol( "WM_DELETE_WINDOW", Quitter )

#       menu
menu = Menu( tk )
menu.add_command( label = "Nouveau", command = Nouveau )
menu.add_command( label = "Recherher Adhérents", command = Recherche )
menu.add_command( label = "Sauvegarder", command = Sauvegarder )
menu.add_command( label = "Quitter", command = Quitter )
tk.config( menu = menu )

#       objet tkinter
BoutonAccueil = Button( tk, text = 'Accueil', command = Affichage )
BoutonNouveauGroupe = Button( tk, text = 'Reconstruire les Groupes', command = NouveauGroupe )

BoutonSuivantGroupe = Button( tk, text = 'Groupe\nSuivant', command = SuivantGroupe )
BoutonRetourGroupe = Button( tk, text = 'Groupe\nPrécédent', command = RetourGroupe )

#       pour afficher groupe
LabelGroupe = Label( tk, text = 'Groupe N°' )
LabelMembre = Label( tk, text = 'Membres' )
LabelActivite = Label( tk, text = 'Activité' )
LabelHoraire = Label( tk, text = 'Horaire' )

#       pour la recheche de membre
VarRechercheNom = StringVar()
EntryRechercheNom = Entry( tk, textvariable = VarRechercheNom )
VarRecherchePrenom = StringVar()
LabelAucunResultat = Label( tk, text = 'Aucun résultat' )
EntryRecherchePrenom = Entry( tk, textvariable = VarRecherchePrenom )
BoutonRechercheOK = Button( tk, text = 'Rechercher', command = RechercheMembre )
BoutonConfirmerChangement = Button( tk, text = 'Confirmer Les\n Changements', command = ConfirmerChangement )
BoutonHistorique = Button( tk, text = 'Afficher\n  L\'Historique  ', command = Historique )
BoutonHistoriqueRetour = Button( tk, text = 'Retour', command = HistoriqueRetour )
LabelInfoHistorique = { 'nbr groupe' : Label( tk ),
                                        'musique' : Label( tk ),
                                        'soutien scolaire' : Label( tk ),
                                        'sport' : Label( tk ),
                                        'journalisme' : Label( tk ),
                                        'litterature' : Label( tk ),
                                        'nouvelles technologies' : Label( tk ),
                                        'environnement' : Label( tk ),
                                        'photographie' : Label( tk ),
                                        'membre' : Label( tk ),
                                        'actvite' : Label( tk ),
                                        'horaire' : Label( tk ) }

#       pour nouveau membre
VarNouveauNom = StringVar()
EntryNouveauNom = Entry( tk, textvariable = VarNouveauNom )
LabelNouveauNom = Label( tk, text = 'Nom' )
VarNouveauPrenom = StringVar()
EntryNouveauPrenom = Entry( tk, textvariable = VarNouveauPrenom )
LabelNouveauPrenom = Label( tk, text = 'Prenom' )

LabelActiviteNote = Label( tk, text = 'Noter les activités de 1 à 10 celon vos préférences.\n' )
activite = { 'musique' : IntVar(), 'sport' : IntVar(), 'journalisme' : IntVar(), 'litterature' : IntVar(), 'nouvelles technologies' : IntVar(), 'environnement' : IntVar(), 'photographie' : IntVar(), 'soutien scolaire' : IntVar() }
SpinboxMusique = Spinbox( tk, textvariable = activite[ 'musique' ], from_ = 1, to = 10 )
LabelMusique = Label( tk, text = 'Musique' )
SpinboxSoutienScolaire = Spinbox( tk, textvariable = activite[ 'soutien scolaire' ], from_ = 1, to = 10 )
LabelSoutienScolaire = Label( tk, text = 'Soutien Scolaire' )
SpinboxSport = Spinbox( tk, textvariable = activite[ 'sport' ], from_ = 1, to = 10 )
LabelSport = Label( tk, text = 'Sport' )
SpinboxJournalisme = Spinbox( tk, textvariable = activite[ 'journalisme' ], from_ = 1, to = 10 )
LabelJournalisme = Label( tk, text = 'Journalisme' )
SpinboxLitterature = Spinbox( tk, textvariable = activite[ 'litterature' ], from_ = 1, to = 10 )
LabelLitterature = Label( tk, text = 'Litterature' )
SpinboxNouvellesTechnologies = Spinbox( tk, textvariable = activite[ 'nouvelles technologies' ], from_ = 1, to = 10 )
LabelNouvellesTechnologies = Label( tk, text = 'Nouvelle Technologies' )
SpinboxEnvironnement = Spinbox( tk, textvariable = activite[ 'environnement' ], from_ = 1, to = 10 )
LabelEnvironnement = Label( tk, text = 'Environnement' )
SpinboxPhotographie = Spinbox( tk, textvariable = activite[ 'photographie' ], from_ = 1, to = 10 )
LabelPhotographie = Label( tk, text = 'Photographie' )

horaire = {
                'mercredi' : { '15h16h' : BooleanVar(), '16h17h' : BooleanVar(), '17h18h' : BooleanVar(), '18h19h': BooleanVar() },
                'samedi' : { '15h16h' : BooleanVar(), '16h17h' : BooleanVar(), '17h18h' : BooleanVar(), '18h19h': BooleanVar() },
                'dimanche' : { '15h16h' : BooleanVar(), '16h17h' : BooleanVar(), '17h18h' : BooleanVar(), '18h19h': BooleanVar() }
                }
LabelMercredi = Label( tk, text = 'Mercredi :' )
CheckbuttonMercredi = { '15h16h' : Checkbutton( tk, text = 'de 15h à 16h', variable = horaire[ 'mercredi' ][ '15h16h' ], onvalue = True, offvalue = False ),
                                        '16h17h' : Checkbutton( tk, text = 'de 16h à 17h', variable = horaire[ 'mercredi' ][ '16h17h' ], onvalue = True, offvalue = False ),
                                        '17h18h' : Checkbutton( tk, text = 'de 17h à 18h', variable = horaire[ 'mercredi' ][ '17h18h' ], onvalue = True, offvalue = False ),
                                        '18h19h' : Checkbutton( tk, text = 'de 18h à 19h', variable = horaire[ 'mercredi' ][ '18h19h' ], onvalue = True, offvalue = False )}
LabelSamedi = Label( tk, text = 'Samedi :' )
CheckbuttonSamedi = { '15h16h' : Checkbutton( tk, text = 'de 15h à 16h', variable = horaire[ 'samedi' ][ '15h16h' ], onvalue = True, offvalue = False ),
                                        '16h17h' : Checkbutton( tk, text = 'de 16h à 17h', variable = horaire[ 'samedi' ][ '16h17h' ], onvalue = True, offvalue = False ),
                                        '17h18h' : Checkbutton( tk, text = 'de 17h à 18h', variable = horaire[ 'samedi' ][ '17h18h' ], onvalue = True, offvalue = False ),
                                        '18h19h' : Checkbutton( tk, text = 'de 18h à 19h', variable = horaire[ 'samedi' ][ '18h19h' ], onvalue = True, offvalue = False )}
LabelDimanche = Label( tk, text = 'Dimanche :' )
CheckbuttonDimanche = { '15h16h' : Checkbutton( tk, text = 'de 15h à 16h', variable = horaire[ 'dimanche' ][ '15h16h' ], onvalue = True, offvalue = False ),
                                        '16h17h' : Checkbutton( tk, text = 'de 16h à 18h', variable = horaire[ 'dimanche' ][ '16h17h' ], onvalue = True, offvalue = False ),
                                        '17h18h' : Checkbutton( tk, text = 'de 17h à 18h', variable = horaire[ 'dimanche' ][ '17h18h' ], onvalue = True, offvalue = False ),
                                        '18h19h' : Checkbutton( tk, text = 'de 18h à 19h', variable = horaire[ 'dimanche' ][ '18h19h' ], onvalue = True, offvalue = False )}

BoutonSuivantNouveau = Button( tk, text = 'Suivant', command = SuivantNouveau )
BoutonRetourNouveau = Button( tk, text = 'Retour', command = RetourNouveau )
BoutonNouveau = Button( tk, text = 'Valider', command = NouveauTerminer )


######################################################### PROGRAMME
try:
        donnee = pickle.load( open( 'donnees.dr', 'rb' ) )
        Client.liste = donnee[ 0 ]
        Groupe.liste = donnee[ 1 ]
except EOFError:        pass
except FileNotFoundError:       pass

page[ 1 ] = len( Groupe.liste )

for groupe in Groupe.liste:
        groupe.charge_tkinter()

Affichage()
tk.mainloop()
