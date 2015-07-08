##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################


def missing_filter(_file):
     """This filter sorts a CSV."""

     import csv 

     with open('../'+_file+'.csv', 'rU') as f:
          for row in csv.reader(f):

               #Filter Professors


               if 'Alan' in row[0] and 'Kolata' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Alice' in row[0] and 'Yao' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Bruce' in row[0] and 'Lincoln' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Constantine' in row[0] and 'Nakassis' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Francois' in row[0] and 'Richard' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Joseph' in row[0] and 'Masco' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Judy' in row[0] and 'Farquhar' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Julie' in row[0] and 'Chu' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Justin' in row[0] and 'Richland' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Kathleen' in row[0] and 'Morrison' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Kaushik' in row[0] and 'Sunder' in row[0] and 'Rajan' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Susan' in row[0] and 'Gal' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Michael' in row[0] and 'Dietler' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Russell' in row[0] and 'Tuttle' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Shannon' in row[0] and 'Dawdy' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Karin' in row[0] and 'Knorr' in row[0] and 'Cetina' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Stephen' in row[0] and 'Palmie' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'William' in row[0] and 'Mazzarella' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Aden' in row[0] and 'Kumler' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Elizabeth' in row[0] and 'Helsinger' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Martha' in row[0] and 'Ward' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Matthew' in row[0] and 'Jesse' in row[0] and 'Jackson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Cecile' in row[0] and 'Fromont' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Chelsea' in row[0] and 'Foxwell' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Christine' in row[0] and 'Mehring' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Claudia' in row[0] and 'Brittenham' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Charles' in row[0] and 'Cohen' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Richard' in row[0] and 'Neer' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Yuri' in row[0] and 'Tsivian' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Tom' in row[0] and 'Gunning' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Foong' in row[0] and 'Ping' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Wu' in row[0] and 'Hung' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'WJT' in row[0] and 'Mitchell' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Niall' in row[0] and 'Atkinson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Patrick' in row[0] and 'Crowley' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Persis' in row[0] and 'Berlekamp' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Rebecca' in row[0] and 'Zorach' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Catherine' in row[0] and 'Sullivan' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'David' in row[0] and 'Schutter' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Geof' in row[0] and 'Oppenheimer' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jason' in row[0] and 'Salavon' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jessica' in row[0] and 'Stockholder' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Laura' in row[0] and 'Letinsky' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'William' in row[0] and 'Pope' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'David' in row[0] and 'Martinez' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Margaret' in row[0] and 'Mitchell' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jeffrey' in row[0] and 'Stackert' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Abigail' in row[0] and 'Sussman' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'A' in row[0] and 'David' in row[0] and 'Nussbaum' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'A' in row[0] and 'Kerem' in row[0] and 'Cosar' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Amanda' in row[0] and 'Sharkey' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Amir' in row[0] and 'Sufi' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Amit' in row[0] and 'Seru' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Anastasia' in row[0] and 'Zakolyukina' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Anil' in row[0] and 'Kashyap' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Anita' in row[0] and 'Rao' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Ann' in row[0] and 'McGill' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Anuj' in row[0] and 'Shah' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Austan' in row[0] and 'Goolsbee' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Brent' in row[0] and 'Neiman' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Bryan' in row[0] and 'Kelly' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Burhaneddin' in row[0] and 'Sandikci' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Chad' in row[0] and 'Syverson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Chang' in row[0] and 'Tai' in row[0] and 'Hsieh' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Che' in row[0] and 'Lin' in row[0] and 'Su' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Chris' in row[0] and 'Nosko' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Christian' in row[0] and 'Hansen' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Christian' in row[0] and 'Leuz' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Christopher' in row[0] and 'Hsee' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Christopher' in row[0] and 'Yenkey' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Dacheng' in row[0] and 'Xiu' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Dan' in row[0] and 'Adelman' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Daniel' in row[0] and 'Bartels' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Devin' in row[0] and 'Pope' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Donald' in row[0] and 'Eisenstein' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Douglas' in row[0] and 'Diamond' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Douglas' in row[0] and 'Skinner' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Drew' in row[0] and 'Creal' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Elena' in row[0] and 'Belavina' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Elizabeth' in row[0] and 'Pontikes' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Ellen' in row[0] and 'Engel' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Emily' in row[0] and 'Oster' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Emir' in row[0] and 'Kamenica' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Eric' in row[0] and 'Budish' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Erik' in row[0] and 'Hurst' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Eugene' in row[0] and 'Caruso' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Eugene' in row[0] and 'Fama' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'George' in row[0] and 'Constantinides' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'George' in row[0] and 'Wu' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Gregor' in row[0] and 'Matvos' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Hans' in row[0] and 'Christensen' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Haresh' in row[0] and 'Sapra' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Hoyt' in row[0] and 'Bleakley' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jacopo' in row[0] and 'Ponticelli' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jane' in row[0] and 'Risen' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jeffrey' in row[0] and 'Russell' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jesse' in row[0] and 'Shapiro' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jing' in row[0] and 'Cynthia' in row[0] and 'Wu' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'John' in row[0] and 'Birge' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'John' in row[0] and 'Cochrane' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Joseph' in row[0] and 'Gerakos' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Joseph' in row[0] and 'Pagliari' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Joseph' in row[0] and 'Vavra' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Juhani' in row[0] and 'Linnainmaa' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Kathleen' in row[0] and 'Fitzgerald' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Kelly' in row[0] and 'Shue' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Kinda' in row[0] and 'Hachem' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Lars' in row[0] and 'Stole' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Laurens' in row[0] and 'Debo' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Linda' in row[0] and 'Ginzel' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Loukas' in row[0] and 'Karabarbounis' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Lubos' in row[0] and 'Pastor' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Luigi' in row[0] and 'Zingales' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Luis' in row[0] and 'Garicano' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Margarita' in row[0] and 'Tsoutsoura' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Marianne' in row[0] and 'Bertrand' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Mark' in row[0] and 'Maffett' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Matthew' in row[0] and 'Gentzkow' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Matthew' in row[0] and 'Notowidigdo' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Matt' in row[0] and 'Taddy' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Michael' in row[0] and 'Gibbs' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Michael' in row[0] and 'Minnis' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Milton' in row[0] and 'Harris' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Mladen' in row[0] and 'Kolar' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'N' in row[0] and 'Bora' in row[0] and 'Keskin' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Neale' in row[0] and 'Mahoney' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Nicholas' in row[0] and 'Epley' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Nicholas' in row[0] and 'Polson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Oleg' in row[0] and 'Urminksy' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Philip' in row[0] and 'Berger' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Pietro' in row[0] and 'Veronesi' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Pingyang' in row[0] and 'Gao' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Pradeep' in row[0] and 'Chintagunta' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Raghuram' in row[0] and 'Rajan' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Ralph' in row[0] and 'Ossa' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Randall' in row[0] and 'Kroszner' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Ray' in row[0] and 'Ball' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Reid' in row[0] and 'Hastie' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Richard' in row[0] and 'Thaler' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Robert' in row[0] and 'Gramacy' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Robert' in row[0] and 'Topel' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Robert' in row[0] and 'Vishny' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Rodney' in row[0] and 'Parker' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Ronald' in row[0] and 'Burt' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Sarah' in row[0] and 'Zechman' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Stavros' in row[0] and 'Panageas' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Stefano' in row[0] and 'Giglio' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Stephen' in row[0] and 'Morrissette' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Steven' in row[0] and 'Davis' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Steven' in row[0] and 'Kaplan' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Thomas' in row[0] and 'Chevrier' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Tobias' in row[0] and 'Moskowitz' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Valeri' in row[0] and 'Nikolaev' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Veronica' in row[0] and 'Guerrieri' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Zheng' in row[0] and 'Song' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Zhiguo' in row[0] and 'He' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jill' in row[0] and 'Mateo' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jill' in row[0] and 'Mateo' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Dario' in row[0] and 'Maestripieri' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Guanglei' in row[0] and 'Hong' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jennifer' in row[0] and 'Cole' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Margaret' in row[0] and 'Beale' in row[0] and 'Spencer' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Martha' in row[0] and 'McClintock' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Richard' in row[0] and 'Shweder' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Susan' in row[0] and 'Goldin' in row[0] and 'Meadow' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Susan' in row[0] and 'Levine' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'William' in row[0] and 'Goldstein' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Richard' in row[0] and 'Taub' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Robert' in row[0] and 'Richards' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Alain' in row[0] and 'Bresson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Christopher' in row[0] and 'Faraone' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'David' in row[0] and 'Wray' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Elisabeth' in row[0] and 'Asmis' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Shadi' in row[0] and 'Bartsch' in row[0] and 'Zimmer' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Helma' in row[0] and 'Dik' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jonathan' in row[0] and 'Hall' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Clifford' in row[0] and 'Ando' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Michael' in row[0] and 'Allen' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Michele' in row[0] and 'Lowrie' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Peter' in row[0] and 'White' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Sarah' in row[0] and 'Nooter' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Mark' in row[0] and 'Payne' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Arnold' in row[0] and 'Davidson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Francoise' in row[0] and 'Meltzer' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Haun' in row[0] and 'Saussy' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Joshua' in row[0] and 'Scodel' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Lawrence' in row[0] and 'Rothfield' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Loren' in row[0] and 'Kruger' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'David' in row[0] and 'Wellbery' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Frederick' in row[0] and 'de' in row[0] and 'Armas' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Boris' in row[0] and 'Maslov' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'John' in row[0] and 'Goldsmith' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Dan' in row[0] and 'Morgan' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'D' in row[0] and 'N' in row[0] and 'Rodowick' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'David' in row[0] and 'Levin' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jacqueline' in row[0] and 'Stewart' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jennifer' in row[0] and 'Wild' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Judy' in row[0] and 'Hoffman' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Noa' in row[0] and 'Steimatsky' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Rebecca' in row[0] and 'West' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Rochona' in row[0] and 'Majumdar' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Robert' in row[0] and 'Bird' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Xinyu' in row[0] and 'Dong' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Daniel' in row[0] and 'Arnold' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Donald' in row[0] and 'Harper' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Edward' in row[0] and 'Shaughnessy' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jacob' in row[0] and 'Eyferth' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Hoyt' in row[0] and 'Long' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Judith' in row[0] and 'Zeitlin' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Kyeong' in row[0] and 'Hee' in row[0] and 'Choi' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Michael' in row[0] and 'Bourdaghs' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Paola' in row[0] and 'Iovene' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Paul' in row[0] and 'Copp' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Reginald' in row[0] and 'Jackson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Alessandra' in row[0] and 'Voena' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Ali' in row[0] and 'Hortacsu' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Azeem' in row[0] and 'Shaikh' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Brent' in row[0] and 'Hickman' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Kevin' in row[0] and 'Murphy' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Casey' in row[0] and 'Mulligan' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'David' in row[0] and 'Galenson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Derek' in row[0] and 'Neal' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Felix' in row[0] and 'Tintelnot' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Fernando' in row[0] and 'Enrique' in row[0] and 'Alvarez' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Glen' in row[0] and 'Weyl' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Harald' in row[0] and 'Uhlig' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Hugo' in row[0] and 'Sonnenschein' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'John' in row[0] and 'List' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Lars' in row[0] and 'Peter' in row[0] and 'Hansen' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Magne' in row[0] and 'Mogstad' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Melissa' in row[0] and 'Tartari' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Nancy' in row[0] and 'Stokey' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Philip' in row[0] and 'Reny' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'James' in row[0] and 'Heckman' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Roger' in row[0] and 'Myerson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Rafael' in row[0] and 'Lopes'in row[0] and 'de' in row[0] and 'Melo' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Richard' in row[0] and 'VanWeelden' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Robert' in row[0] and 'Lucas' in row[0] and 'Jr' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Robert' in row[0] and 'Shimer' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Sebastien' in row[0] and 'Gay' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Stephane' in row[0] and 'Bonhomme' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Stephen' in row[0] and 'Levitt' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Adrienne' in row[0] and 'Brown' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Hillary' in row[0] and 'Chute' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Benjamin' in row[0] and 'Morgan' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Bill' in row[0] and 'Brown' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Christina' in row[0] and 'von' in row[0] and 'Nolcken' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Christopher' in row[0] and 'Taylor' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'David' in row[0] and 'Simon' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Deborah' in row[0] and 'Nelson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Elaine' in row[0] and 'Hadley' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Eric' in row[0] and 'Slauter' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Frances' in row[0] and 'Ferguson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Heather' in row[0] and 'Keenleyside' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jennifer' in row[0] and 'Scappettone' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'John' in row[0] and 'Muse' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'John' in row[0] and 'Wilkinson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Julie' in row[0] and 'Orlemanski' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Kenneth' in row[0] and 'Warren' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Lauren' in row[0] and 'Berlant' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Leela' in row[0] and 'Gandhi' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Lisa' in row[0] and 'Ruddick' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Mark' in row[0] and 'Miller' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Maud' in row[0] and 'Ellmann' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Patrick' in row[0] and 'Jagoda' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Richard' in row[0] and 'So' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Laura' in row[0] and 'Gandolfi' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Sonali' in row[0] and 'Thakkar' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Srikanth' in row[0] and 'Reddy' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Timothy' in row[0] and 'Campbell' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Leora' in row[0] and 'Auslander' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Catherine' in row[0] and 'Baumann' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Christopher' in row[0] and 'Wild' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Eric' in row[0] and 'Santner' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Florian' in row[0] and 'Klinger' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Kimberly' in row[0] and 'Kenny' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Willemien' in row[0] and 'Otten' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'James' in row[0] and 'Robinson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Adrian' in row[0] and 'Johns' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Amy' in row[0] and 'Lippert' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Cameron' in row[0] and 'Hawkins' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Constantin' in row[0] and 'Fasolt' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Dain' in row[0] and 'Borges' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'James' in row[0] and 'Hevia' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Julie' in row[0] and 'Savile' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Kenneth' in row[0] and 'Pomeranz' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Mauricio' in row[0] and 'Tenorio' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Moishe' in row[0] and 'Postone' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'John' in row[0] and 'Woods' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Ramon' in row[0] and 'Gutierrez' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'David' in row[0] and 'Nirenberg' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Dipesh' in row[0] and 'Chakrabarty' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Wendy' in row[0] and 'Doniger' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Michael' in row[0] and 'Sells' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Michael' in row[0] and 'Fishbane' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Alison' in row[0] and 'Siegler' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Anthony' in row[0] and 'Casey' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Anup' in row[0] and 'Malani' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Brian' in row[0] and 'Leiter' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Craig' in row[0] and 'Futterman' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Daniel' in row[0] and 'Abebe' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Daniel' in row[0] and 'Fischel' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'David' in row[0] and 'Strauss' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'David' in row[0] and 'Weisbach' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Douglas' in row[0] and 'Baird' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Eduardo' in row[0] and 'Penalver' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Edward' in row[0] and 'Morrison' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Elizabeth' in row[0] and 'Frankel' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Elizabeth' in row[0] and 'Kregor' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Erica' in row[0] and 'Zunkel' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Eric' in row[0] and 'Posner' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Geoffrey' in row[0] and 'Stone' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jeff' in row[0] and 'Leslie' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jennifer' in row[0] and 'Nou' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jonathan' in row[0] and 'Masur' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Kenneth' in row[0] and 'Dam' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Laura' in row[0] and 'Weinrib' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Lee' in row[0] and 'Fennell' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Lior' in row[0] and 'Strahilevitz' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Lisa' in row[0] and 'Bernstein' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Maria' in row[0] and 'Woltjen' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Mark' in row[0] and 'Heyrman' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Mary' in row[0] and 'Anne' in row[0] and 'Case' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Michael' in row[0] and 'Schill' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'M' in row[0] and 'Todd' in row[0] and 'Henderson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Nicholas' in row[0] and 'Stephanopoulos' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Omri' in row[0] and 'Ben' in row[0] and 'Shahar' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Bernard' in row[0] and 'Harcourt' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Randall' in row[0] and 'Picker' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Randall' in row[0] and 'Schmidt' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Randolph' in row[0] and 'Stone' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'R' in row[0] and 'H' in row[0] and 'Helmholz' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Richard' in row[0] and 'McAdams' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Saul' in row[0] and 'Levmore' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Sital' in row[0] and 'Kalantry' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Thomas' in row[0] and 'Miles' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Tom' in row[0] and 'Ginsburg' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'William' in row[0] and 'Hubbard' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'William' in row[0] and 'Landes' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Alan' in row[0] and 'Yu' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Amy' in row[0] and 'Dahlstrom' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Anastasia' in row[0] and 'Giannakidou' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Diane' in row[0] and 'Brentari' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Gregory' in row[0] and 'Kobele' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Itamar' in row[0] and 'Francez' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jason' in row[0] and 'Merchant' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jason' in row[0] and 'Riggle' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Karlos' in row[0] and 'Arregi' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Ming' in row[0] and 'Xiang' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Salikoko' in row[0] and 'Mufewene' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Victor' in row[0] and 'Friedman' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Anne' in row[0] and 'Robertson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Anthony' in row[0] and 'Cheung' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Berthold' in row[0] and 'Hoeckner' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Kaley' in row[0] and 'Mason' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Larry' in row[0] and 'Zbikowski' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Marta' in row[0] and 'Ptaszynska' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Melvin' in row[0] and 'Butler' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Philip' in row[0] and 'Bohlman' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Augusta' in row[0] and 'Read' in row[0] and 'Thomas' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Martha' in row[0] and 'Feldman' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Robert' in row[0] and 'Kendrick' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Seth' in row[0] and 'Brodsky' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Shulamit' in row[0] and 'Ran' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Steven' in row[0] and 'Rings' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Thomas' in row[0] and 'Christensen' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Travis' in row[0] and 'Jackson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Ahmed' in row[0] and 'El' in row[0] and 'Shamsy' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Brian' in row[0] and 'Muhs' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Christopher' in row[0] and 'Woods' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Dennis' in row[0] and 'Pardee' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Franklin' in row[0] and 'Lewis' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Gil' in row[0] and 'Stein' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Hakan' in row[0] and 'Karateke' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Janet' in row[0] and 'Johnson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'J' in row[0] and 'David' in row[0] and 'Schloen' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Martha' in row[0] and 'Roth' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Matthew' in row[0] and 'Stolper' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'McGuire' in row[0] and 'Gibson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Naama' in row[0] and 'Rokem' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Nadine' in row[0] and 'Moeller' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Orit' in row[0] and 'Bashkin' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Petra' in row[0] and 'Goedegebuure' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Rebecca' in row[0] and 'Hasselbach' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Richard' in row[0] and 'Payne' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Robert' in row[0] and 'Ritner' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Scott' in row[0] and 'Branting' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Tahera' in row[0] and 'Qutbuddin' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Theo' in row[0] and 'van'in row[0] and 'den' in row[0] and 'Hout' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Walter' in row[0] and 'Farber' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'W' in row[0] and 'Raymond' in row[0] and 'Johnson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Agnes' in row[0] and 'Callard' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Anat' in row[0] and 'Schechtman' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Anton' in row[0] and 'Ford' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Anubav' in row[0] and 'Vasudevan' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Bart' in row[0] and 'Schultz' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Benjamin' in row[0] and 'Callard' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Ben' in row[0] and 'Laurence' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Candace' in row[0] and 'Vogler' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Daniel' in row[0] and 'Brudney' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'James' in row[0] and 'Conant' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jason' in row[0] and 'Bridges' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Josef' in row[0] and 'Stern' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Kevin' in row[0] and 'Davey' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Malte' in row[0] and 'Willer' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Marko' in row[0] and 'Malink' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Michael' in row[0] and 'Forster' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Michael' in row[0] and 'Kremer' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Raoul' in row[0] and 'Moati' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Gabriel' in row[0] and 'Lear' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jonathan' in row[0] and 'Lear' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Robert' in row[0] and 'Pippin' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Alberto' in row[0] and 'Simpser' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Dali' in row[0] and 'Yang' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Dan' in row[0] and 'Slater' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Gary' in row[0] and 'Herrigel' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Iza' in row[0] and 'Hussin' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'John' in row[0] and 'Padgett' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Linda' in row[0] and 'Zerilli' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Lisa' in row[0] and 'Weeden' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Patchen' in row[0] and 'Markell' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Nathan' in row[0] and 'Tarcov' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Stanislav' in row[0] and 'Markus' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Tianna' in row[0] and 'Paschel' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Alicia' in row[0] and 'Menendez' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Anthony' in row[0] and 'Fowler' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Ariel' in row[0] and 'Kalil' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Benjamin' in row[0] and 'Keys' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Boris' in row[0] and 'Shor' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Bruce' in row[0] and 'Meyer' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Christopher' in row[0] and 'Berry' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Damon' in row[0] and 'Jones' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Dan' in row[0] and 'Black' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Daniel' in row[0] and 'Bennett' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'David' in row[0] and 'Meltzer' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Ethan' in row[0] and 'Bueno'in row[0] and 'de' in row[0] and 'Mesquita' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Ioana' in row[0] and 'Marinescu' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'James' in row[0] and 'Sallee' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jeffrey' in row[0] and 'Grogger' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Ofer' in row[0] and 'Malamud' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Pablo' in row[0] and 'Montagnes' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'William' in row[0] and 'Howell' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Rebecca' in row[0] and 'Sive' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Robert' in row[0] and 'LaLonde' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Robert' in row[0] and 'Michael' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Robert' in row[0] and 'Weissbourd' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Scott' in row[0] and 'Ashworth' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jens' in row[0] and 'Ludwig' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Steve' in row[0] and 'Cicala' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Susan' in row[0] and 'Mayer' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Tomas' in row[0] and 'Philipson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Willard' in row[0] and 'Manning' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Amanda' in row[0] and 'Woodward' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Boaz' in row[0] and 'Keysar' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Brian' in row[0] and 'Prendergast' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Daniel' in row[0] and 'Casasanto' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Daniel' in row[0] and 'Margoliash' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'David' in row[0] and 'Gallo' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Greg' in row[0] and 'Norman' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Howard' in row[0] and 'Nusbaum' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Jasmin' in row[0] and 'Cloutier' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'John' in row[0] and 'Cacioppo' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Katherine' in row[0] and 'Kinzler' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Leslie' in row[0] and 'Kay' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Sarah' in row[0] and 'London' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Sian' in row[0] and 'Beilock' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Steven' in row[0] and 'Shevell' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'William' in row[0] and 'Schweiker' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Agnes' in row[0] and 'Lugo' in row[0] and 'Ortiz' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Alfredo' in row[0] and 'de' in row[0] and 'Melo' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Alison' in row[0] and 'James' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Armando' in row[0] and 'Maggi' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Daisy' in row[0] and 'Delogu' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Daniel' in row[0] and 'Desormeaux' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Justin' in row[0] and 'Steinberg' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Larry' in row[0] and 'Norman' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Mario' in row[0] and 'Santana' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Miguel' in row[0] and 'Martinez' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Philippe' in row[0] and 'Desan' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Robert' in row[0] and 'Morrissey' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Rocco' in row[0] and 'Rubini' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Gary' in row[0] and 'Tubb' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Muzaffar' in row[0] and 'Alam' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Sascha' in row[0] and 'Ebeling' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Steven' in row[0] and 'Collins' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Thibaut' in row[0] and 'dHubert' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Ulrike' in row[0] and 'Stark' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Vasudha' in row[0] and 'Paramasivan' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Whitney' in row[0] and 'Cox' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Glenn' in row[0] and 'Most' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Heinrich' in row[0] and 'Meier' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Lorraine' in row[0] and 'Daston' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Ralph' in row[0] and 'Lerner' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Rosanna' in row[0] and 'Warren' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Hans' in row[0] and 'Joas' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Adam' in row[0] and 'Zagajewski' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Andreas' in row[0] and 'Glaeser' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Andrew' in row[0] and 'Abbott' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Cheol' in row[0] and 'Sung' in row[0] and 'Lee' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Dingxin' in row[0] and 'Zhao' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Edward' in row[0] and 'Laumann' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Elisabeth' in row[0] and 'Clemens' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Forrest' in row[0] and 'Stuart' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'James' in row[0] and 'Evans' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'John' in row[0] and 'Martin' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Kazuo' in row[0] and 'Yamaguchi' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Linda' in row[0] and 'Waite' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Omar' in row[0] and 'McRoberts' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Ross' in row[0] and 'Stolzenberg' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Stephen' in row[0] and 'Raudenbush' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Terry' in row[0] and 'Clark' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Bozena' in row[0] and 'Shallcross' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Lina' in row[0] and 'Steiner' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'William' in row[0] and 'Nickell' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Yaroslav' in row[0] and 'Gorbachov' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Alida' in row[0] and 'Bouris' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Dexter' in row[0] and 'Voisin' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Gina' in row[0] and 'Samuels' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Heather' in row[0] and 'Hill' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Matthew' in row[0] and 'Epperson' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Scott' in row[0] and 'Allard' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Virginia' in row[0] and 'Parks' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
               elif 'Dwight' in row[0] and 'Hopkins' in row[0]:
                    with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))



                              #Filter Everthing Else
               else:
                    with open('../__MISSING.csv', 'a') as f2: f2.write("{}\n".format(row[0]))

#Unhash to run
#missing_filter("__NAMES___CLEANED_Faculty_Deans_Provosts__")
missing_filter("__CLEANED_Faculty_Deans_Provosts_")

