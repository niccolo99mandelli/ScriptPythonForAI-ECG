import csv
import array as arr
def main():
    
    with open('questionAnswerA1.csv', 'r') as file:
        reader = csv.reader(file, delimiter = "|")
        line_count=0
        index=1
        positionBefore=0
        positionAfter=0
        AnswerBefore=0
        AnswerAfter=0

        ValueDiagnosis=0
        positionDiagnosis=0
        #Variabili per memorizzare tutti i Counter per ogni casistica (Advice Giusto - Spiegazione Giusta, A.Sbagliato-S.Sbagliata, A.Giusto-S.Sbagliata, A.Sbagliato-S.Giusta)
        # 1 -  Advice Giusto - Spiegazione Giusta
        # 2 -  A.Sbagliato - S.Sbagliata
        # 3 -  A.Giusto - S.Sbagliata
        # 4 -  A.Sbagliato - S.Giusta
        # ARRAY contenente le tipologie dei casi
        case=arr.array('i', [1,1,1,1,1,3,1,3,2,3,2,1,3,2,1,4,1,1,2,4])
        # Counter prima di aver visto la spiegazione
        OwnDiagnosisB1A=0
        AIDiagnosisB1A=0
        OwnDiagnosisB2A=0
        AIDiagnosisB2A=0
        OwnDiagnosisB3A=0
        AIDiagnosisB3A=0
        OwnDiagnosisB4A=0
        AIDiagnosisB4A=0
        # Counter dopo aver visto la spiegazione
        OwnDiagnosisA1A=0
        AIDiagnosisA1A=0
        OwnDiagnosisA2A=0
        AIDiagnosisA2A=0
        OwnDiagnosisA3A=0
        AIDiagnosisA3A=0
        OwnDiagnosisA4A=0
        AIDiagnosisA4A=0
        # Counter per accuratezza delle diagnosi utente

        CorrectDiagnosisBA=0
        WrongDiagnosisBA=0
        CorrectDiagnosisAA=0
        WrongDiagnosisAA=0

        for row in reader:
            if(line_count != 0):
                positionBefore=15
                positionAfter=21
                positionDiagnosis=12
                for index in range(20):
                    AnswerBefore=int(row[positionBefore])
                    AnswerAfter=int(row[positionAfter])
                    ValueDiagnosis=int(row[positionDiagnosis])
                    if(case[index]==1):
                        if(AnswerBefore == 1):
                            AIDiagnosisB1A+=1
                        else:
                            OwnDiagnosisB1A+=1

                        if(AnswerAfter == 1):
                            AIDiagnosisA1A+=1
                        else:
                            OwnDiagnosisA1A+=1
                    if(case[index]==2):
                        if(AnswerBefore == 1):
                            AIDiagnosisB2A+=1
                        else: 
                            OwnDiagnosisB2A+=1

                        if(AnswerAfter == 1):
                            AIDiagnosisA2A+=1
                        else:
                            OwnDiagnosisA2A+=1
                    if(case[index]==3):
                        if(AnswerBefore == 1):
                            AIDiagnosisB3A+=1
                        else: 
                            OwnDiagnosisB3A+=1

                        if(AnswerAfter == 1):
                            AIDiagnosisA3A+=1
                        else:
                            OwnDiagnosisA3A+=1
                    if(case[index]==4):
                        if(AnswerBefore == 1):
                            AIDiagnosisB4A+=1
                        else: 
                            OwnDiagnosisB4A+=1

                        if(AnswerAfter == 1):
                            AIDiagnosisA4A+=1
                        else:
                            OwnDiagnosisA4A+=1
                    # Valutazione Correttezza
                    if(ValueDiagnosis == 1):
                        CorrectDiagnosisBA+=1
                    else:
                        WrongDiagnosisBA+=1
                    if(AnswerBefore == 2 and AnswerAfter != 2):
                        positionDiagnosis=positionDiagnosis+5
                        ValueDiagnosis=int(row[positionDiagnosis])
                    if(AnswerBefore == 2 and AnswerAfter == 2):
                        positionDiagnosis=positionDiagnosis+11
                        ValueDiagnosis=int(row[positionDiagnosis])
                    if(AnswerBefore != 2 and AnswerAfter == 2):
                        positionDiagnosis=positionDiagnosis+11
                        ValueDiagnosis=int(row[positionDiagnosis])
                    if(AnswerAfter == 0 or AnswerAfter == 2): 
                        if(ValueDiagnosis == 1):
                            CorrectDiagnosisAA+=1
                        else:
                            WrongDiagnosisAA+=1

                    if(AnswerAfter == 2):
                        positionDiagnosis+=10
                    if(AnswerBefore == 2 and AnswerAfter != 2):
                        positionDiagnosis+=16
                    if(AnswerBefore != 2 and AnswerAfter != 2):
                        positionDiagnosis+=21
                    # Fine correttezza    
                    positionBefore+=21
                    positionAfter+=21
                    index+=1
            line_count += 1
    print(CorrectDiagnosisBA)
    print(CorrectDiagnosisAA)
    print(WrongDiagnosisBA) 
    print(WrongDiagnosisAA)
    TotalAIDiagnosisBA=AIDiagnosisB1A+AIDiagnosisB2A+AIDiagnosisB3A+AIDiagnosisB4A
    TotalOwnDiagnosisBA=OwnDiagnosisB1A+OwnDiagnosisB2A+OwnDiagnosisB3A+OwnDiagnosisB4A
    TotalAIDiagnosisAA=AIDiagnosisA1A+AIDiagnosisA2A+AIDiagnosisA3A+AIDiagnosisA4A
    TotalOwnDiagnosisAA=OwnDiagnosisA1A+OwnDiagnosisA2A+OwnDiagnosisA3A+OwnDiagnosisA4A


    with open('questionAnswerB1.csv', 'r') as file:
        reader = csv.reader(file, delimiter = "|")
        line_count=0
        index=1
        positionBefore=0
        positionAfter=0
        AnswerBefore=0
        AnswerAfter=0

        ValueDiagnosis=0
        positionDiagnosis=0
        #Variabili per memorizzare tutti i Counter per ogni casistica (Advice Giusto - Spiegazione Giusta, A.Sbagliato-S.Sbagliata, A.Giusto-S.Sbagliata, A.Sbagliato-S.Giusta)
        # 1 -  Advice Giusto - Spiegazione Giusta
        # 2 -  A.Sbagliato - S.Sbagliata
        # 3 -  A.Giusto - S.Sbagliata
        # 4 -  A.Sbagliato - S.Giusta
        # Counter prima di aver visto la spiegazione
        OwnDiagnosisB1B=0
        AIDiagnosisB1B=0
        OwnDiagnosisB2B=0
        AIDiagnosisB2B=0
        OwnDiagnosisB3B=0
        AIDiagnosisB3B=0
        OwnDiagnosisB4B=0
        AIDiagnosisB4B=0
        # Counter dopo aver visto la spiegazione
        OwnDiagnosisA1B=0
        AIDiagnosisA1B=0
        OwnDiagnosisA2B=0
        AIDiagnosisA2B=0
        OwnDiagnosisA3B=0
        AIDiagnosisA3B=0
        OwnDiagnosisA4B=0
        AIDiagnosisA4B=0

        # Counter per accuratezza delle diagnosi utente
        CorrectDiagnosisBB=0
        WrongDiagnosisBB=0
        CorrectDiagnosisAB=0
        WrongDiagnosisAB=0

        for row in reader:
            if(line_count != 0):
                positionBefore=12
                if(row[20]== '0' or row[20]== '1'):
                    positionAfter=20
                else:
                    positionAfter=18
                positionDiagnosis=12
                for index in range(20):
                    

                    AnswerBefore=int(row[positionBefore])
                    AnswerAfter=int(row[positionAfter])
                    
                    ValueDiagnosis=int(row[positionDiagnosis])
                    if(case[index]==1):
                        if(AnswerBefore == 0):
                            AIDiagnosisB1B+=1
                        else:
                            OwnDiagnosisB1B+=1

                        if(AnswerBefore == 0 and AnswerAfter == 0):
                            AIDiagnosisA1B+=1
                        elif(AnswerBefore == 0 and AnswerAfter == 1):
                            OwnDiagnosisA1B+=1
                        elif(AnswerBefore == 1 and AnswerAfter == 1):
                            AIDiagnosisA1B+=1
                        else:
                            OwnDiagnosisA1B+=1
                    if(case[index]==2):
                        if(AnswerBefore == 0):
                            AIDiagnosisB2B+=1
                        else:
                            OwnDiagnosisB2B+=1

                        if(AnswerBefore == 0 and AnswerAfter == 0):
                            AIDiagnosisA2B+=1
                        elif(AnswerBefore == 0 and AnswerAfter == 1):
                            OwnDiagnosisA2B+=1
                        elif(AnswerBefore == 1 and AnswerAfter == 1):
                            AIDiagnosisA2B+=1
                        else:
                            OwnDiagnosisA2B+=1
                    if(case[index]==3):
                        if(AnswerBefore == 0):
                            AIDiagnosisB3B+=1
                        else:
                            OwnDiagnosisB3B+=1

                        if(AnswerBefore == 0 and AnswerAfter == 0):
                            AIDiagnosisA3B+=1
                        elif(AnswerBefore == 0 and AnswerAfter == 1):
                            OwnDiagnosisA3B+=1
                        elif(AnswerBefore == 1 and AnswerAfter == 1):
                            AIDiagnosisA3B+=1
                        else:
                            OwnDiagnosisA3B+=1
                    if(case[index]==4):
                        if(AnswerBefore == 0):
                            AIDiagnosisB4B+=1
                        else:
                            OwnDiagnosisB4B+=1

                        if(AnswerBefore == 0 and AnswerAfter == 0):
                            AIDiagnosisA4B+=1
                        elif(AnswerBefore == 0 and AnswerAfter == 1):
                            OwnDiagnosisA4B+=1
                        elif(AnswerBefore == 1 and AnswerAfter == 1):
                            AIDiagnosisA4B+=1
                        else:
                            OwnDiagnosisA4B+=1

                    # Valutazione Correttezza
                    if(AnswerBefore == 1):
                        positionDiagnosis+=2
                        ValueDiagnosis=int(row[positionDiagnosis])
                        if(ValueDiagnosis == 1):
                            CorrectDiagnosisBB+=1
                        else:
                            WrongDiagnosisBB+=1
                    if(AnswerBefore == 1 and AnswerAfter == 2):
                        positionDiagnosis+=6
                        ValueDiagnosis=int(row[positionDiagnosis])
                        if(ValueDiagnosis == 1):
                            CorrectDiagnosisAB+=1
                        else:
                            WrongDiagnosisAB+=1
                    if(AnswerBefore == 1 and AnswerAfter == 0):
                        if(ValueDiagnosis == 1):
                            CorrectDiagnosisAB+=1
                        else:
                            WrongDiagnosisAB+=1
                    if(AnswerBefore == 0 and AnswerAfter == 1):
                        positionDiagnosis+=10
                        ValueDiagnosis=int(row[positionDiagnosis])
                        if(ValueDiagnosis == 1):
                            CorrectDiagnosisAB+=1
                        else:
                            WrongDiagnosisAB+=1

                    if(AnswerBefore == 1 and AnswerAfter == 2):
                        positionDiagnosis+=12
                    if(AnswerBefore == 1 and AnswerAfter != 2):
                        positionDiagnosis+=18
                    if(AnswerBefore == 0 and AnswerAfter == 0):
                        positionDiagnosis+=20
                    if(AnswerBefore == 0 and AnswerAfter !=0):
                        positionDiagnosis+=10
                    # Fine correttezza
                    positionBefore+=20
                    if(row[positionAfter+20]== ''):
                        if (row[positionAfter+22]== ''):
                            positionAfter+=18
                        else:
                            positionAfter+=22
                    else:
                        positionAfter+=20
                    
                    index+=1
            line_count += 1 
    print(CorrectDiagnosisBB)
    print(CorrectDiagnosisAB)
    print(WrongDiagnosisBB) 
    print(WrongDiagnosisAB)
    TotalAIDiagnosisBB=AIDiagnosisB1B+AIDiagnosisB2B+AIDiagnosisB3B+AIDiagnosisB4B
    TotalOwnDiagnosisBB=OwnDiagnosisB1B+OwnDiagnosisB2B+OwnDiagnosisB3B+OwnDiagnosisB4B
    TotalAIDiagnosisAB=AIDiagnosisA1B+AIDiagnosisA2B+AIDiagnosisA3B+AIDiagnosisA4B
    TotalOwnDiagnosisAB=OwnDiagnosisA1B+OwnDiagnosisA2B+OwnDiagnosisA3B+OwnDiagnosisA4B


    f= open("ResultSurvey1.txt", "a+")
    f.write("""************************************************************************************************************************\n""" )
    f.write("""*********************************  RISULTATI QUESTIONARI ~ Versione A e Versione B  ************************************\n""" )
    f.write("""************************************************************************************************************************\n\n\n""" )
    f.write("""** VERSIONE A **********************************************************************************************************\n""" )

    f.write("""___________________________________________________________________________________________________\n""" )
    f.write("""** PRIMA del visionamento della spiegazione testuale si sono riscontrati: \n""" )
    f.write("""** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(TotalAIDiagnosisBA, TotalOwnDiagnosisBA))
    f.write("""** DOPO il visionamento della spiegazione testuale si sono riscontrati: \n""" )
    f.write("""** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(TotalAIDiagnosisAA, TotalOwnDiagnosisAA))
    f.write("""___________________________________________________________________________________________________\n\n""" )

    f.write("""___________________________________________________________________________________________________\n""" )
    f.write("""** Di seguito sono riportate tutte le variazioni suddivise in base alla correttezza dei casi. \n""" ) 
    f.write("""** Qualora non ci fossero variazioni i dati non saranno visualizzati. \n""" ) 
    f.write("""___________________________________________________________________________________________________\n""" )
    if(AIDiagnosisB1A != AIDiagnosisA1A):
        f.write("""\t\t__________________________________________________________________________________________________\n""" )
        f.write("""\t\t** Dati relativi ai casi aventi ADVICE CORRETTO e SPIEGAZIONE CORRETTA: \n""" )
        f.write("""\t\t** PRIMA del visionamento della spiegazione testuale si sono riscontrati: \n""" )
        f.write("""\t\t** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(AIDiagnosisB1A, OwnDiagnosisB1A))
        f.write("""\t\t** DOPO il visionamento della spiegazione testuale si sono riscontrati: \n""" )
        f.write("""\t\t** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(AIDiagnosisA1A, OwnDiagnosisA1A))
        f.write("""\t\t__________________________________________________________________________________________________\n\n""" )
    if(AIDiagnosisB2A != AIDiagnosisA2A):
        f.write("""\t\t__________________________________________________________________________________________________\n""" )
        f.write("""\t\t** Dati relativi ai casi aventi ADVICE ERRATO e SPIEGAZIONE ERRATA: \n""" )
        f.write("""\t\t** PRIMA del visionamento della spiegazione testuale si sono riscontrati: \n""" )
        f.write("""\t\t** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(AIDiagnosisB2A, OwnDiagnosisB2A))
        f.write("""\t\t** DOPO il visionamento della spiegazione testuale si sono riscontrati: \n""" )
        f.write("""\t\t** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(AIDiagnosisA2A, OwnDiagnosisA2A))
        f.write("""\t\t__________________________________________________________________________________________________\n\n""" )
    if(AIDiagnosisB3A != AIDiagnosisA3A):
        f.write("""\t\t__________________________________________________________________________________________________\n""" )
        f.write("""\t\t** Dati relativi ai casi aventi ADVICE CORRETTO e SPIEGAZIONE ERRATA: \n""" )
        f.write("""\t\t** PRIMA del visionamento della spiegazione testuale si sono riscontrati: \n""" )
        f.write("""\t\t** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(AIDiagnosisB3A, OwnDiagnosisB3A))
        f.write("""\t\t** DOPO il visionamento della spiegazione testuale si sono riscontrati: \n""" )
        f.write("""\t\t** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(AIDiagnosisA3A, OwnDiagnosisA3A))
        f.write("""\t\t__________________________________________________________________________________________________\n\n""" )
    if(AIDiagnosisB4A != AIDiagnosisA4A):
        f.write("""\t\t__________________________________________________________________________________________________\n""" )
        f.write("""\t\t** Dati relativi ai casi aventi ADVICE ERRATO e SPIEGAZIONE CORRETTA: \n""" )
        f.write("""\t\t** PRIMA del visionamento della spiegazione testuale si sono riscontrati: \n""" )
        f.write("""\t\t** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(AIDiagnosisB4A, OwnDiagnosisB4A))
        f.write("""\t\t** DOPO il visionamento della spiegazione testuale si sono riscontrati: \n""" )
        f.write("""\t\t** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(AIDiagnosisA4A, OwnDiagnosisA4A))
        f.write("""\t\t__________________________________________________________________________________________________\n\n""" )
    f.write("""************************************************************************************************************************\n\n\n""" )
    

    f.write("""** VERSIONE B **********************************************************************************************************\n""" )

    f.write("""___________________________________________________________________________________________________\n""" )
    f.write("""** PRIMA del visionamento della spiegazione testuale si sono riscontrati: \n""" )
    f.write("""** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(TotalAIDiagnosisBB, TotalOwnDiagnosisBB))
    f.write("""** DOPO il visionamento della spiegazione testuale si sono riscontrati: \n""" )
    f.write("""** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(TotalAIDiagnosisAB, TotalOwnDiagnosisAB))
    f.write("""___________________________________________________________________________________________________\n\n""" )

    f.write("""___________________________________________________________________________________________________\n""" )
    f.write("""** Di seguito sono riportate tutte le variazioni suddivise in base alla correttezza dei casi. \n""" ) 
    f.write("""** Qualora non ci fossero variazioni i dati non saranno visualizzati. \n""" ) 
    f.write("""___________________________________________________________________________________________________\n""" )
    if(AIDiagnosisB1B != AIDiagnosisA1B):
        f.write("""\t\t__________________________________________________________________________________________________\n""" )
        f.write("""\t\t** Dati relativi ai casi aventi ADVICE CORRETTO e SPIEGAZIONE CORRETTA: \n""" )
        f.write("""\t\t** PRIMA del visionamento della spiegazione testuale si sono riscontrati: \n""" )
        f.write("""\t\t** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(AIDiagnosisB1B, OwnDiagnosisB1B))
        f.write("""\t\t** DOPO il visionamento della spiegazione testuale si sono riscontrati: \n""" )
        f.write("""\t\t** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(AIDiagnosisA1B, OwnDiagnosisA1B))
        f.write("""\t\t__________________________________________________________________________________________________\n\n""" )
    if(AIDiagnosisB2B != AIDiagnosisA2B):
        f.write("""\t\t__________________________________________________________________________________________________\n""" )
        f.write("""\t\t** Dati relativi ai casi aventi ADVICE ERRATO e SPIEGAZIONE ERRATA: \n""" )
        f.write("""\t\t** PRIMA del visionamento della spiegazione testuale si sono riscontrati: \n""" )
        f.write("""\t\t** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(AIDiagnosisB2B, OwnDiagnosisB2B))
        f.write("""\t\t** DOPO il visionamento della spiegazione testuale si sono riscontrati: \n""" )
        f.write("""\t\t** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(AIDiagnosisA2B, OwnDiagnosisA2B))
        f.write("""\t\t__________________________________________________________________________________________________\n\n""" )
    if(AIDiagnosisB3B != AIDiagnosisA3B):
        f.write("""\t\t__________________________________________________________________________________________________\n""" )
        f.write("""\t\t** Dati relativi ai casi aventi ADVICE CORRETTO e SPIEGAZIONE ERRATA: \n""" )
        f.write("""\t\t** PRIMA del visionamento della spiegazione testuale si sono riscontrati: \n""" )
        f.write("""\t\t** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(AIDiagnosisB3B, OwnDiagnosisB3B))
        f.write("""\t\t** DOPO il visionamento della spiegazione testuale si sono riscontrati: \n""" )
        f.write("""\t\t** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(AIDiagnosisA3B, OwnDiagnosisA3B))
        f.write("""\t\t__________________________________________________________________________________________________\n\n""" )
    if(AIDiagnosisB4B != AIDiagnosisA4B):
        f.write("""\t\t__________________________________________________________________________________________________\n""" )
        f.write("""\t\t** Dati relativi ai casi aventi ADVICE ERRATO e SPIEGAZIONE CORRETTA: \n""" )
        f.write("""\t\t** PRIMA del visionamento della spiegazione testuale si sono riscontrati: \n""" )
        f.write("""\t\t** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(AIDiagnosisB4B, OwnDiagnosisB4B))
        f.write("""\t\t** DOPO il visionamento della spiegazione testuale si sono riscontrati: \n""" )
        f.write("""\t\t** %d CONFERME della diagnosi prodotta dall'AI. | %d NEGAZIONI della diagnosi prodotta dall'AI **\n""" %(AIDiagnosisA4B, OwnDiagnosisA4B))
        f.write("""\t\t__________________________________________________________________________________________________\n\n""" )
    f.write("""************************************************************************************************************************\n\n\n""" )

    percA=float(TotalAIDiagnosisAA)/(float(TotalAIDiagnosisAA+TotalOwnDiagnosisAA))*100
    percB=float(TotalAIDiagnosisAB)/(float(TotalAIDiagnosisAB+TotalOwnDiagnosisAB))*100
    f.write("""** OSSERVAZIONI E DIFFERENZE TRA LE VERSIONI **************************************************************************************************\n""" )
    if(percA<percB):
        f.write("""__________________________________________________________________________________________________________________________________________\n""" )
        f.write("""** PERCENTUALI ACCETTAZIONE DIAGNOSI AI: \n""" )
        f.write("""** Di seguito sono riportate le percentuali d'accettazione della diagnosi prodotta dall'AI per le due versioni. \n""" )
        f.write("""** %.2f %% - Percentuale conferme dell'AI per la Versione A \n""" % (percA))
        f.write("""** %.2f %% - Percentuale conferme dell'AI per la Versione B \n""" % (percB))
        f.write("""** Nella Versione A i rispondenti hanno quindi confermato meno frequentemente la diagnosi suggerita dall'AI in confronto alla Versione B. \n""" )
        f.write("""__________________________________________________________________________________________________________________________________________\n\n""" )
    elif(percB>percA):
        f.write("""__________________________________________________________________________________________________________________________________________\n""" )
        f.write("""** PERCENTUALI ACCETTAZIONE DIAGNOSI AI: \n""" )
        f.write("""** Di seguito sono riportate le percentuali d'accettazione della diagnosi prodotta dall'AI per le due versioni. \n""" )
        f.write("""** %.2f %% - Percentuale conferme dell'AI per la Versione A \n""" %(percA))
        f.write("""** %.2f %% - Percentuale conferme dell'AI per la Versione B \n""" %(percB))
        f.write("""** Nella Versione B i rispondenti hanno quindi confermato meno frequentemente la diagnosi suggerita dall'AI in confronto alla Versione A. \n""" )
        f.write("""__________________________________________________________________________________________________________________________________________\n\n""" )
    else:
        f.write("""__________________________________________________________________________________________________________________________________________\n""" )
        f.write("""** PERCENTUALI ACCETTAZIONE DIAGNOSI AI: \n""" )
        f.write("""** Di seguito sono riportate le percentuali d'accettazione della diagnosi prodotta dall'AI per le due versioni. \n""" )
        f.write("""** %.2f %% - Percentuale conferme dell'AI per la Versione A \n""" %(percA))
        f.write("""** %.2f %% - Percentuale conferme dell'AI per la Versione B \n""" %(percB))
        f.write("""** In entrambe le versioni i rispondenti hanno confermato la diagnosi suggerita dall'AI con la stessa frequenza. \n""" )
        f.write("""__________________________________________________________________________________________________________________________________________\n\n""" )


    diffA=TotalAIDiagnosisAA-TotalAIDiagnosisBA
    diffB=TotalAIDiagnosisAB-TotalAIDiagnosisBB
    if(diffA<0):
        if(diffB<0):
            f.write("""__________________________________________________________________________________________________________________________________________\n""" )
            f.write("""** LA SPIEGAZIONE HA INFLUENZATO LE SCELTE DELL'UTENTE? \n""" )
            f.write("""** Dopo la visione della spiegazione testuale i rispondenti hanno rigettato la diagnosi suggerita dall'AI \n""" )
            f.write("""** con una frequenza maggiore per entrambe le versioni del questionario. \n""" )
            f.write("""** Si sono registrate %d NEGAZIONI AGGIUNTIVE per la versione A. \n""" %(diffA*(-1)))
            f.write("""** Si sono registrate %d NEGAZIONI AGGIUNTIVE per la versione B. \n""" %(diffB*(-1)))
            f.write("""** La visualizzazione della spiegazione ha convinto alcuni utenti a rifiutare la diagnosi prodotta dall'AI. \n""" )
            f.write("""__________________________________________________________________________________________________________________________________________\n\n""" )
        elif(diffB>0):
            f.write("""__________________________________________________________________________________________________________________________________________\n""" )
            f.write("""** LA SPIEGAZIONE HA INFLUENZATO LE SCELTE DELL'UTENTE? \n""" )
            f.write("""** Dopo la visione della spiegazione testuale i rispondenti hanno rigettato la diagnosi suggerita dall'AI \n""" )
            f.write("""** con una frequenza maggiore nella versione A. Invece, nella versione B hanno confermato la diagnosi dell'AI con maggior \n""" )
            f.write("""** frequenza dopo aver visionato la spiegazione testuale. \n""" )
            f.write("""** Si sono registrate %d NEGAZIONI AGGIUNTIVE per la versione A. \n""" %(diffA*(-1)))
            f.write("""** Si sono registrate %d CONFERME AGGIUNTIVE per la versione B. Per un totale di %d CONFERME. \n""" %(diffB, TotalAIDiagnosisAB))
            f.write("""** La visualizzazione della spiegazione ha convinto alcuni utenti a confermare la diagnosi prodotta dall'AI solo nella versione B. \n""" )
            f.write("""__________________________________________________________________________________________________________________________________________\n\n""" )
        else:
            f.write("""__________________________________________________________________________________________________________________________________________\n""" )
            f.write("""** LA SPIEGAZIONE HA INFLUENZATO LE SCELTE DELL'UTENTE? \n""" )
            f.write("""** Dopo la visione della spiegazione testuale i rispondenti hanno rigettato la diagnosi suggerita dall'AI \n""" )
            f.write("""** con una frequenza maggiore nella versione A. Invece, nella versione B non è stata riscontrata alcuna differenza  \n""" )
            f.write("""** relativamente alla conferma e alla negazione della diagnosi dopo aver visionato la spiegazione testuale. \n""" )
            f.write("""** Si sono registrate %d NEGAZIONI AGGIUNTIVE per la versione A. \n""" %(diffA*(-1)))
            f.write("""** La visualizzazione della spiegazione non ha influenzato le scelte degli utenti per la versione B. Ha, invece, convinto alcuni utenti \n""" )
            f.write("""** a rifiutare la diagnosi per la versione A. \n""" )
            f.write("""__________________________________________________________________________________________________________________________________________\n\n""" )
    elif(diffA>0):
        if(diffB>0):
            f.write("""__________________________________________________________________________________________________________________________________________\n""" )
            f.write("""** LA SPIEGAZIONE HA INFLUENZATO LE SCELTE DELL'UTENTE? \n""" )
            f.write("""** Dopo la visione della spiegazione testuale i rispondenti hanno confermato la diagnosi suggerita dall'AI \n""" )
            f.write("""** con una frequenza maggiore per entrambe le versioni del questionario. \n""" )
            f.write("""** Si sono registrate %d CONFERME AGGIUNTIVE per la versione A. Per un totale di %d CONFERME. \n""" %(diffA, TotalAIDiagnosisAA))
            f.write("""** Si sono registrate %d CONFERME AGGIUNTIVE per la versione B. Per un totale di %d CONFERME. \n""" %(diffB, TotalAIDiagnosisAB))
            f.write("""** La visualizzazione della spiegazione ha influenzato le scelte degli utenti per entrambe le versioni, convincendo alcuni utenti\n""" )
            f.write("""** a confermare la diagnosi prodotta dall'AI. \n""" )
            f.write("""__________________________________________________________________________________________________________________________________________\n\n""" )
        elif(diffB<0):
            f.write("""__________________________________________________________________________________________________________________________________________\n""" )
            f.write("""** LA SPIEGAZIONE HA INFLUENZATO LE SCELTE DELL'UTENTE? \n""" )
            f.write("""** Dopo la visione della spiegazione testuale i rispondenti hanno confermato la diagnosi suggerita dall'AI \n""" )
            f.write("""** con una frequenza maggiore nella versione A. Invece, nella versione B hanno rigettato la diagnosi dell'AI con maggior \n""" )
            f.write("""** frequenza dopo aver visionato la spiegazione testuale. \n""" )
            f.write("""** Si sono registrate %d CONFERME AGGIUNTIVE per la versione A. Per un totale di %d CONFERME. \n""" %(diffA, TotalAIDiagnosisAA))
            f.write("""** Si sono registrate %d NEGAZIONI AGGIUNTIVE per la versione B. \n""" %(diffB*(-1)))
            f.write("""** La visualizzazione della spiegazione ha influenzato le scelte degli utenti per entrambe le versioni, convincendo alcuni utenti\n""" )
            f.write("""** a confermare la diagnosi per la versione A e a negarla per la versione B. \n""" )
            f.write("""__________________________________________________________________________________________________________________________________________\n\n""" )
        else:
            f.write("""__________________________________________________________________________________________________________________________________________\n""" )
            f.write("""** LA SPIEGAZIONE HA INFLUENZATO LE SCELTE DELL'UTENTE? \n""" )
            f.write("""** Dopo la visione della spiegazione testuale i rispondenti hanno confermato la diagnosi suggerita dall'AI \n""" )
            f.write("""** con una frequenza maggiore nella versione A. Invece, nella versione B non è stata riscontrata alcuna differenza  \n""" )
            f.write("""** relativamente alla conferma e alla negazione della diagnosi dopo aver visionato la spiegazione testuale. \n""" )
            f.write("""** Si sono registrate %d CONFERME AGGIUNTIVE per la versione A. Per un totale di %d CONFERME.\n""" %(diffA, TotalAIDiagnosisAA))
            f.write("""** La visualizzazione della spiegazione non ha influenzato le scelte degli utenti per la versione B. Ha, invece, convinto alcuni utenti \n""" )
            f.write("""** a confermare la diagnosi per la versione A. \n""" )
            f.write("""__________________________________________________________________________________________________________________________________________\n\n""" )
    else:
        if(diffB==0):
            f.write("""__________________________________________________________________________________________________________________________________________\n""" )
            f.write("""** LA SPIEGAZIONE HA INFLUENZATO LE SCELTE DELL'UTENTE? \n""" )
            f.write("""** Dopo la visione della spiegazione testuale i rispondenti non hanno cambiato idea relativamente alla conferma e alla negazione \n""" )
            f.write("""** della diagnosi suggerita dall'AI per entrambe le versioni del questionario. \n""" )
            f.write("""__________________________________________________________________________________________________________________________________________\n\n""" )
        elif(diffB<0):
            f.write("""__________________________________________________________________________________________________________________________________________\n""" )
            f.write("""** LA SPIEGAZIONE HA INFLUENZATO LE SCELTE DELL'UTENTE? \n""" )
            f.write("""** Dopo la visione della spiegazione testuale non è stata riscontrata alcuna differenza relativamente alla conferma \n""" )
            f.write("""** e alla negazione della diagnosi suggerita dall'AI per la versione A. Invece, nella versione B è stata rigettata la diagnosi dell'AI \n""" )
            f.write("""** con maggior frequenza dopo la visione della spiegazione testuale. \n""" )
            f.write("""** Si sono registrate %d NEGAZIONI AGGIUNTIVE per la versione B. \n""" %(diffB*(-1)))
            f.write("""** La visualizzazione della spiegazione non ha influenzato le scelte degli utenti per la versione A. Ha, invece, convinto alcuni utenti \n""" )
            f.write("""** a rifiutare la diagnosi per la versione B. \n""" )
            f.write("""__________________________________________________________________________________________________________________________________________\n\n""" )
        else:
            f.write("""__________________________________________________________________________________________________________________________________________\n""" )
            f.write("""** LA SPIEGAZIONE HA INFLUENZATO LE SCELTE DELL'UTENTE? \n""" )
            f.write("""** Dopo la visione della spiegazione testuale non è stata riscontrata alcuna differenza relativamente alla conferma \n""" )
            f.write("""** e alla negazione della diagnosi suggerita dall'AI per la versione A. Invece, nella versione B è stata confermata la diagnosi dell'AI \n""" )
            f.write("""** con maggior frequenza dopo la visione della spiegazione testuale. \n""" )
            f.write("""** Si sono registrate %d CONFERME AGGIUNTIVE per la versione B. Per un totale di %d CONFERME.\n""" %(diffB, TotalAIDiagnosisAB))
            f.write("""** La visualizzazione della spiegazione non ha influenzato le scelte degli utenti per la versione A. Ha, invece, convinto alcuni utenti \n""" )
            f.write("""** a confermare la diagnosi per la versione B. \n""" )
            f.write("""__________________________________________________________________________________________________________________________________________\n\n\n""" )

    TotalWrongAIDiagnosisBA=AIDiagnosisB2A+AIDiagnosisB4A
    TotalWrongAIDiagnosisBB=AIDiagnosisB2B+AIDiagnosisB4B
    TotalWrongAIDiagnosisAA=AIDiagnosisA2A+AIDiagnosisA4A
    TotalWrongAIDiagnosisAB=AIDiagnosisA2B+AIDiagnosisA4B
    f.write("""__________________________________________________________________________________________________________________________________________\n""" )
    f.write("""** LA SPIEGAZIONE HA INDOTTO A PIÙ ERRORI? \n""" )
    f.write("""** Nella versione A, precedentemente alla visualizzazione della spiegazione, l'intelligenza artificiale ha indotto l'utente  \n""" )
    f.write("""** a selezionare una diagnosi errata in %d casi. \n""" %(TotalWrongAIDiagnosisBA))
    f.write("""** Successivamente alla visualizzazione della spiegazione, l'intelligenza artificiale ha indotto l'utente  \n""" )
    f.write("""** a selezionare una diagnosi errata in %d casi, di cui: \n""" %(TotalWrongAIDiagnosisAA))
    f.write("""** \t\t - %d aventi spiegazione errata. \n""" %(AIDiagnosisA2A))
    f.write("""** \t\t - %d aventi spiegazione corretta. \n""" %(AIDiagnosisA4A))
    if(TotalWrongAIDiagnosisAA>TotalWrongAIDiagnosisBA):
        f.write("""** L'intelligenza artificiale ha indotto a più errori dopo la visualizzazione della spiegazione. \n""" )
    elif(TotalWrongAIDiagnosisAA<TotalWrongAIDiagnosisBA):
        f.write("""** L'intelligenza artificiale ha indotto a meno errori dopo la visualizzazione della spiegazione. \n""" )
    else:
        f.write("""** L'intelligenza artificiale non ha alterato gli errori compiuti dall'utente dopo la visualizzazione della spiegazione. \n""" )
    f.write("""__________________________________________________________________________________________________________________________________________\n""" )
    f.write("""** Nella versione B, precedentemente alla visualizzazione della spiegazione, l'intelligenza artificiale ha indotto l'utente  \n""" )
    f.write("""** a selezionare una diagnosi errata in %d casi. \n""" %(TotalWrongAIDiagnosisBB))
    f.write("""** Successivamente alla visualizzazione della spiegazione, l'intelligenza artificiale ha indotto l'utente  \n""" )
    f.write("""** a selezionare una diagnosi errata in %d casi, di cui: \n""" %(TotalWrongAIDiagnosisAB))
    f.write("""** \t\t - %d aventi spiegazione errata. \n""" %(AIDiagnosisA2B))
    f.write("""** \t\t - %d aventi spiegazione corretta. \n""" %(AIDiagnosisA4B))
    if(TotalWrongAIDiagnosisAB>TotalWrongAIDiagnosisBB):
        f.write("""** L'intelligenza artificiale ha indotto a più errori dopo la visualizzazione della spiegazione. \n""" )
    elif(TotalWrongAIDiagnosisAB<TotalWrongAIDiagnosisBB):
        f.write("""** L'intelligenza artificiale ha indotto a meno errori dopo la visualizzazione della spiegazione. \n""" )
    else:
        f.write("""** L'intelligenza artificiale non ha alterato gli errori compiuti dall'utente dopo la visualizzazione della spiegazione. \n""" )
    f.write("""__________________________________________________________________________________________________________________________________________\n\n\n""" )
    TotalCorrectAIDiagnosisBA=AIDiagnosisB1A+AIDiagnosisB3A
    TotalCorrectAIDiagnosisAA=AIDiagnosisA1A+AIDiagnosisA3A
    
    f.write("""__________________________________________________________________________________________________________________________________________\n""" )
    f.write("""** TEST D'IPOTESI SULL'ACCURATEZZA: \n""" )
    f.write("""** ACCURATEZZA SULLE DIAGNOSI PRODOTTE DALL'AI e CONFERMATE DALL'UTENTE: \n""" )
    f.write("""____________________________________________________________________________\n""" )
    f.write("""** \tVERSIONE A \t\t| CORRETTI \t| ERRATI \t| TOTALE \t|\n""")
    f.write("""** \t PRE-SPIEGAZIONE \t|  %d    \t|  %d \t\t|   %d \t|\n"""%(TotalCorrectAIDiagnosisBA, TotalWrongAIDiagnosisBA, TotalCorrectAIDiagnosisBA+TotalWrongAIDiagnosisBA))
    f.write("""** \t POST-SPIEGAZIONE \t|  %d  \t|  %d \t\t|   %d \t|\n"""%(TotalCorrectAIDiagnosisAA, TotalWrongAIDiagnosisAA, TotalCorrectAIDiagnosisAA+TotalWrongAIDiagnosisAA))
    f.write("""** \t TOTALE \t\t|  %d  \t|  %d \t\t|   %d \t|\n"""%(TotalCorrectAIDiagnosisBA+TotalCorrectAIDiagnosisAA, TotalWrongAIDiagnosisBA+TotalWrongAIDiagnosisAA, TotalAIDiagnosisBA+TotalAIDiagnosisAA))
    f.write("""____________________________________________________________________________\n\n""" )
    percCorrectA=(TotalCorrectAIDiagnosisBA+TotalCorrectAIDiagnosisAA)/(TotalAIDiagnosisBA+TotalAIDiagnosisAA)*100

    ExpectedValueaA=(TotalCorrectAIDiagnosisBA+TotalWrongAIDiagnosisBA)*percCorrectA/100
    ExpectedValuecA=(TotalCorrectAIDiagnosisAA+TotalWrongAIDiagnosisAA)*percCorrectA/100
    ExpectedValuebA=(TotalCorrectAIDiagnosisBA+TotalWrongAIDiagnosisBA)-ExpectedValueaA
    ExpectedValuedA=(TotalCorrectAIDiagnosisAA+TotalWrongAIDiagnosisAA)-ExpectedValuecA
    chiSquareaA=(TotalCorrectAIDiagnosisBA-ExpectedValueaA)*(TotalCorrectAIDiagnosisBA-ExpectedValueaA)/ExpectedValueaA
    chiSquarebA=(TotalWrongAIDiagnosisBA-ExpectedValuebA)*(TotalWrongAIDiagnosisBA-ExpectedValuebA)/ExpectedValuebA
    chiSquarecA=(TotalCorrectAIDiagnosisAA-ExpectedValuecA)*(TotalCorrectAIDiagnosisAA-ExpectedValuecA)/ExpectedValuecA
    chiSquaredA=(TotalWrongAIDiagnosisAA-ExpectedValuedA)*(TotalWrongAIDiagnosisAA-ExpectedValuedA)/ExpectedValuedA
    chiSquareA=chiSquareaA+chiSquarebA+chiSquarecA+chiSquaredA
    if(chiSquareA>3.841):
        if(chiSquareA>6.635):
            f.write("""VALORE CHI-QUADRO: %.5f\n""" %(chiSquareA))
            f.write("""GRADI DI LIBERTÀ: 1\n""" )
            f.write("""** La differenza tra le due proporzioni è significativa al livello di probabilità 5%  e 1 %. \n""" )
            f.write("""** In conclusione, la differenza tra la correttezza delle conferme dell'AI prima e dopo il visionamento della spiegazione \n""" )
            f.write("""** è STATISTICAMENTE SIGNIFICATIVA AL LIVELLO DI PROBABILITÀ 5%  e 1%.\n""" )
        else:
            f.write("""VALORE CHI-QUADRO: %.5f\n""" %(chiSquareA))
            f.write("""GRADI DI LIBERTÀ: 1\n""" )
            f.write("""** La differenza tra le due proporzioni è significativa al livello di probabilità 5 % ma non al livello di probabilità 1 %. \n""" )
            f.write("""** In conclusione, la differenza tra la correttezza delle conferme dell'AI prima e dopo il visionamento della spiegazione \n""" )
            f.write("""** è STATISTICAMENTE SIGNIFICATIVA AL LIVELLO DI PROBABILITÀ 5%.\n""" )
    else:
        if(chiSquareA>6.635):
            f.write("""VALORE CHI-QUADRO: %.5f\n""" %(chiSquareA))
            f.write("""GRADI DI LIBERTÀ: 1\n""" )
            f.write("""** La differenza tra le due proporzioni non è significativa al livello di probabilità 5 %, ma lo è con un livello di probabilità 1 %. \n""" )
            f.write("""** In conclusione, la differenza tra la correttezza delle conferme dell'AI prima e dopo il visionamento della spiegazione \n""" )
            f.write("""** è STATISTICAMENTE SIGNIFICATIVA AL LIVELLO DI PROBABILITÀ 1%.\n""" )
        else:
            f.write("""VALORE CHI-QUADRO: %.5f\n""" %(chiSquareA))
            f.write("""GRADI DI LIBERTÀ: 1\n""" )
            f.write("""** La differenza tra le due proporzioni non è significativa al livello di probabilità 5%  e 1 %. \n""" )
            f.write("""** In conclusione, la differenza tra la correttezza delle conferme dell'AI prima e dopo il visionamento della spiegazione \n""" )
            f.write("""** è STATISTICAMENTE NON SIGNIFICATIVA AL LIVELLO DI PROBABILITÀ 5%  e 1%.\n""" )
    f.write("""__________________________________________________________________________________________________________________________________________\n""" )


    TotalCorrectAIDiagnosisBB=AIDiagnosisB1B+AIDiagnosisB3B
    TotalCorrectAIDiagnosisAB=AIDiagnosisA1B+AIDiagnosisA3B
    f.write("""____________________________________________________________________________\n""" )
    f.write("""** \tVERSIONE B \t\t| CORRETTI \t| ERRATI \t| TOTALE \t|\n""")
    f.write("""** \t PRE-SPIEGAZIONE \t|  %d    \t|  %d \t\t|   %d \t|\n"""%(TotalCorrectAIDiagnosisBB, TotalWrongAIDiagnosisBB, TotalCorrectAIDiagnosisBB+TotalWrongAIDiagnosisBB))
    f.write("""** \t POST-SPIEGAZIONE \t|  %d  \t|  %d \t\t|   %d \t|\n"""%(TotalCorrectAIDiagnosisAB, TotalWrongAIDiagnosisAB, TotalCorrectAIDiagnosisAB+TotalWrongAIDiagnosisAB))
    f.write("""** \t TOTALE \t\t|  %d  \t|  %d \t\t|   %d \t|\n"""%(TotalCorrectAIDiagnosisBB+TotalCorrectAIDiagnosisAB, TotalWrongAIDiagnosisBB+TotalWrongAIDiagnosisAB, TotalAIDiagnosisBB+TotalAIDiagnosisAB))
    f.write("""____________________________________________________________________________\n\n""" )
    percCorrectB=(TotalCorrectAIDiagnosisBB+TotalCorrectAIDiagnosisAB)/(TotalAIDiagnosisBB+TotalAIDiagnosisAB)*100

    ExpectedValueaB=(TotalCorrectAIDiagnosisBB+TotalWrongAIDiagnosisBB)*percCorrectB/100
    ExpectedValuecB=(TotalCorrectAIDiagnosisAB+TotalWrongAIDiagnosisAB)*percCorrectB/100
    ExpectedValuebB=(TotalCorrectAIDiagnosisBB+TotalWrongAIDiagnosisBB)-ExpectedValueaB
    ExpectedValuedB=(TotalCorrectAIDiagnosisAB+TotalWrongAIDiagnosisAB)-ExpectedValuecB
    chiSquareaB=(TotalCorrectAIDiagnosisBB-ExpectedValueaB)*(TotalCorrectAIDiagnosisBB-ExpectedValueaB)/ExpectedValueaB
    chiSquarebB=(TotalWrongAIDiagnosisBB-ExpectedValuebB)*(TotalWrongAIDiagnosisBB-ExpectedValuebB)/ExpectedValuebB
    chiSquarecB=(TotalCorrectAIDiagnosisAB-ExpectedValuecB)*(TotalCorrectAIDiagnosisAB-ExpectedValuecB)/ExpectedValuecB
    chiSquaredB=(TotalWrongAIDiagnosisAB-ExpectedValuedB)*(TotalWrongAIDiagnosisAB-ExpectedValuedB)/ExpectedValuedB
    chiSquareB=chiSquareaB+chiSquarebB+chiSquarecB+chiSquaredB
    if(chiSquareB>3.841):
        if(chiSquareB>6.635):
            f.write("""VALORE CHI-QUADRO: %.5f\n""" %(chiSquareB))
            f.write("""GRADI DI LIBERTÀ: 1\n""" )
            f.write("""** La differenza tra le due proporzioni è significativa al livello di probabilità 5%  e 1 %. \n""" )
            f.write("""** In conclusione, la differenza tra la correttezza delle conferme dell'AI prima e dopo il visionamento della spiegazione \n""" )
            f.write("""** è STATISTICAMENTE SIGNIFICATIVA AL LIVELLO DI PROBABILITÀ 5%  e 1%.\n""" )
        else:
            f.write("""VALORE CHI-QUADRO: %.5f\n""" %(chiSquareB))
            f.write("""GRADI DI LIBERTÀ: 1\n""" )
            f.write("""** La differenza tra le due proporzioni è significativa al livello di probabilità 5 % ma non al livello di probabilità 1 %. \n""" )
            f.write("""** In conclusione, la differenza tra la correttezza delle conferme dell'AI prima e dopo il visionamento della spiegazione \n""" )
            f.write("""** è STATISTICAMENTE SIGNIFICATIVA AL LIVELLO DI PROBABILITÀ 5%.\n""" )
    else:
        if(chiSquareB>6.635):
            f.write("""VALORE CHI-QUADRO: %.5f\n""" %(chiSquareB))
            f.write("""GRADI DI LIBERTÀ: 1\n""" )
            f.write("""** La differenza tra le due proporzioni non è significativa al livello di probabilità 5 %, ma lo è con un livello di probabilità 1 %. \n""" )
            f.write("""** In conclusione, la differenza tra la correttezza delle conferme dell'AI prima e dopo il visionamento della spiegazione \n""" )
            f.write("""** è STATISTICAMENTE SIGNIFICATIVA AL LIVELLO DI PROBABILITÀ 1%.\n""" )
        else:
            f.write("""VALORE CHI-QUADRO: %.5f\n""" %(chiSquareB))
            f.write("""GRADI DI LIBERTÀ: 1\n""" )
            f.write("""** La differenza tra le due proporzioni non è significativa al livello di probabilità 5%  e 1 %. \n""" )
            f.write("""** In conclusione, la differenza tra la correttezza delle conferme dell'AI prima e dopo il visionamento della spiegazione \n""" )
            f.write("""** è STATISTICAMENTE NON SIGNIFICATIVA AL LIVELLO DI PROBABILITÀ 5%  e 1%.\n""" )
    f.write("""__________________________________________________________________________________________________________________________________________\n\n\n""" )


    f.write("""** ACCURATEZZA SULLE DIAGNOSI PRODOTTE DALL'UTENTE: \n""" )
    f.write("""____________________________________________________________________________\n""" )
    f.write("""** \tVERSIONE A \t\t| CORRETTI \t| ERRATI \t| TOTALE \t|\n""")
    f.write("""** \t PRE-SUGGERIMENTO \t|  %d    \t|  %d \t\t|   %d \t|\n"""%(CorrectDiagnosisBA, WrongDiagnosisBA, CorrectDiagnosisBA+WrongDiagnosisBA))
    f.write("""** \t POST-SUGGERIMENTO \t|  %d  \t|  %d \t\t|   %d \t|\n"""%(CorrectDiagnosisAA, WrongDiagnosisAA, CorrectDiagnosisAA+WrongDiagnosisAA))
    f.write("""** \t TOTALE \t\t|  %d  \t|  %d \t\t|   %d \t|\n"""%(CorrectDiagnosisBA+CorrectDiagnosisAA, WrongDiagnosisBA+WrongDiagnosisAA, CorrectDiagnosisBA+CorrectDiagnosisAA+WrongDiagnosisBA+WrongDiagnosisAA))
    f.write("""____________________________________________________________________________\n\n""" )
    percCorrectOwnA=(CorrectDiagnosisBA+CorrectDiagnosisAA)/(CorrectDiagnosisBA+CorrectDiagnosisAA+WrongDiagnosisBA+WrongDiagnosisAA)*100

    ExpectedValueOwnaA=(CorrectDiagnosisBA+WrongDiagnosisBA)*percCorrectOwnA/100
    ExpectedValueOwncA=(CorrectDiagnosisAA+WrongDiagnosisAA)*percCorrectOwnA/100
    ExpectedValueOwnbA=(CorrectDiagnosisBA+WrongDiagnosisBA)-ExpectedValueOwnaA
    ExpectedValueOwndA=(CorrectDiagnosisAA+WrongDiagnosisAA)-ExpectedValueOwncA
    chiSquareOwnaA=(CorrectDiagnosisBA-ExpectedValueOwnaA)*(CorrectDiagnosisBA-ExpectedValueOwnaA)/ExpectedValueOwnaA
    chiSquareOwnbA=(WrongDiagnosisBA-ExpectedValueOwnbA)*(WrongDiagnosisBA-ExpectedValueOwnbA)/ExpectedValueOwnbA
    chiSquareOwncA=(CorrectDiagnosisAA-ExpectedValueOwncA)*(CorrectDiagnosisAA-ExpectedValueOwncA)/ExpectedValueOwncA
    chiSquareOwndA=(WrongDiagnosisAA-ExpectedValueOwndA)*(WrongDiagnosisAA-ExpectedValueOwndA)/ExpectedValueOwndA
    chiSquareOwnA=chiSquareOwnaA+chiSquareOwnbA+chiSquareOwncA+chiSquareOwndA
    if(chiSquareOwnA>3.841):
        if(chiSquareOwnA>6.635):
            f.write("""VALORE CHI-QUADRO: %.5f\n""" %(chiSquareOwnA))
            f.write("""GRADI DI LIBERTÀ: 1\n""" )
            f.write("""** La differenza tra le due proporzioni è significativa al livello di probabilità 5%  e 1 %. \n""" )
            f.write("""** In conclusione, la differenza tra la correttezza delle diagnosi prodotte dall'utente prima e dopo il visionamento del suggerimento \n""" )
            f.write("""** è STATISTICAMENTE SIGNIFICATIVA AL LIVELLO DI PROBABILITÀ 5%  e 1%.\n""" )
        else:
            f.write("""VALORE CHI-QUADRO: %.5f\n""" %(chiSquareOwnA))
            f.write("""GRADI DI LIBERTÀ: 1\n""" )
            f.write("""** La differenza tra le due proporzioni è significativa al livello di probabilità 5 % ma non al livello di probabilità 1 %. \n""" )
            f.write("""** In conclusione, la differenza tra la correttezza delle diagnosi prodotte dall'utente prima e dopo il visionamento del suggerimento \n""" )
            f.write("""** è STATISTICAMENTE SIGNIFICATIVA AL LIVELLO DI PROBABILITÀ 5%.\n""" )
    else:
        if(chiSquareOwnA>6.635):
            f.write("""VALORE CHI-QUADRO: %.5f\n""" %(chiSquareOwnA))
            f.write("""GRADI DI LIBERTÀ: 1\n""" )
            f.write("""** La differenza tra le due proporzioni non è significativa al livello di probabilità 5 %, ma lo è con un livello di probabilità 1 %. \n""" )
            f.write("""** In conclusione, la differenza tra la correttezza delle diagnosi prodotte dall'utente prima e dopo il visionamento del suggerimento \n""" )
            f.write("""** è STATISTICAMENTE SIGNIFICATIVA AL LIVELLO DI PROBABILITÀ 1%.\n""" )
        else:
            f.write("""VALORE CHI-QUADRO: %.5f\n""" %(chiSquareOwnA))
            f.write("""GRADI DI LIBERTÀ: 1\n""" )
            f.write("""** La differenza tra le due proporzioni non è significativa al livello di probabilità 5%  e 1 %. \n""" )
            f.write("""** In conclusione, la differenza tra la correttezza ddelle diagnosi prodotte dall'utente prima e dopo il visionamento del suggerimento \n""" )
            f.write("""** è STATISTICAMENTE NON SIGNIFICATIVA AL LIVELLO DI PROBABILITÀ 5%  e 1%.\n""" )
    f.write("""__________________________________________________________________________________________________________________________________________\n""" )


    f.write("""____________________________________________________________________________\n""" )
    f.write("""** \tVERSIONE B \t\t| CORRETTI \t| ERRATI \t| TOTALE \t|\n""")
    f.write("""** \t PRE-SPIEGAZIONE \t|  %d    \t|  %d \t\t|   %d \t|\n"""%(CorrectDiagnosisBB, WrongDiagnosisBB, CorrectDiagnosisBB+WrongDiagnosisBB))
    f.write("""** \t POST-SPIEGAZIONE \t|  %d  \t\t|  %d \t\t|   %d \t|\n"""%(CorrectDiagnosisAB, WrongDiagnosisAB, CorrectDiagnosisAB+WrongDiagnosisAB))
    f.write("""** \t TOTALE \t\t|  %d  \t|  %d \t\t|   %d \t|\n"""%(CorrectDiagnosisBB+CorrectDiagnosisAB, WrongDiagnosisBB+WrongDiagnosisAB, CorrectDiagnosisBB+CorrectDiagnosisAB+WrongDiagnosisBB+WrongDiagnosisAB))
    f.write("""____________________________________________________________________________\n\n""" )
    percCorrectOwnB=(CorrectDiagnosisBB+CorrectDiagnosisAB)/(CorrectDiagnosisBB+CorrectDiagnosisAB+WrongDiagnosisBB+WrongDiagnosisAB)*100

    ExpectedValueOwnaB=(CorrectDiagnosisBB+WrongDiagnosisBB)*percCorrectOwnB/100
    ExpectedValueOwncB=(CorrectDiagnosisAB+WrongDiagnosisAB)*percCorrectOwnB/100
    ExpectedValueOwnbB=(CorrectDiagnosisBB+WrongDiagnosisBB)-ExpectedValueOwnaB
    ExpectedValueOwndB=(CorrectDiagnosisAB+WrongDiagnosisAB)-ExpectedValueOwncB
    chiSquareOwnaB=(CorrectDiagnosisBB-ExpectedValueOwnaB)*(CorrectDiagnosisBB-ExpectedValueOwnaB)/ExpectedValueOwnaB
    chiSquareOwnbB=(WrongDiagnosisBB-ExpectedValueOwnbB)*(WrongDiagnosisBB-ExpectedValueOwnbB)/ExpectedValueOwnbB
    chiSquareOwncB=(CorrectDiagnosisAB-ExpectedValueOwncB)*(CorrectDiagnosisAB-ExpectedValueOwncB)/ExpectedValueOwncB
    chiSquareOwndB=(WrongDiagnosisAB-ExpectedValueOwndB)*(WrongDiagnosisAB-ExpectedValueOwndB)/ExpectedValueOwndB
    chiSquareOwnB=chiSquareOwnaB+chiSquareOwnbB+chiSquareOwncB+chiSquareOwndB
    if(chiSquareOwnB>3.841):
        if(chiSquareOwnB>6.635):
            f.write("""VALORE CHI-QUADRO: %.5f\n""" %(chiSquareOwnB))
            f.write("""GRADI DI LIBERTÀ: 1\n""" )
            f.write("""** La differenza tra le due proporzioni è significativa al livello di probabilità 5%  e 1 %. \n""" )
            f.write("""** In conclusione, la differenza tra la correttezza delle diagnosi prodotte dall'utente prima e dopo il visionamento della spiegazione \n""" )
            f.write("""** è STATISTICAMENTE SIGNIFICATIVA AL LIVELLO DI PROBABILITÀ 5%  e 1%.\n""" )
        else:
            f.write("""VALORE CHI-QUADRO: %.5f\n""" %(chiSquareOwnB))
            f.write("""GRADI DI LIBERTÀ: 1\n""" )
            f.write("""** La differenza tra le due proporzioni è significativa al livello di probabilità 5 % ma non al livello di probabilità 1 %. \n""" )
            f.write("""** In conclusione, la differenza tra la correttezza delle diagnosi prodotte dall'utente prima e dopo il visionamento della spiegazione \n""" )
            f.write("""** è STATISTICAMENTE SIGNIFICATIVA AL LIVELLO DI PROBABILITÀ 5%.\n""" )
    else:
        if(chiSquareOwnB>6.635):
            f.write("""VALORE CHI-QUADRO: %.5f\n""" %(chiSquareOwnB))
            f.write("""GRADI DI LIBERTÀ: 1\n""" )
            f.write("""** La differenza tra le due proporzioni non è significativa al livello di probabilità 5 %, ma lo è con un livello di probabilità 1 %. \n""" )
            f.write("""** In conclusione, la differenza tra la correttezza delle diagnosi prodotte dall'utente prima e dopo il visionamento della spiegazione \n""" )
            f.write("""** è STATISTICAMENTE SIGNIFICATIVA AL LIVELLO DI PROBABILITÀ 1%.\n""" )
        else:
            f.write("""VALORE CHI-QUADRO: %.5f\n""" %(chiSquareOwnB))
            f.write("""GRADI DI LIBERTÀ: 1\n""" )
            f.write("""** La differenza tra le due proporzioni non è significativa al livello di probabilità 5%  e 1 %. \n""" )
            f.write("""** In conclusione, la differenza tra la correttezza delle diagnosi prodotte dall'utente prima e dopo il visionamento della spiegazione \n""" )
            f.write("""** è STATISTICAMENTE NON SIGNIFICATIVA AL LIVELLO DI PROBABILITÀ 5%  e 1%.\n""" )
    f.write("""__________________________________________________________________________________________________________________________________________\n""" )


    f.close()
if __name__=="__main__":
    main()