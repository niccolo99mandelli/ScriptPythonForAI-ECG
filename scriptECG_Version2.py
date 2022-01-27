import csv

def main():
	
	f= open("ECG_Version2.txt", "a+")
	f.write("""id\trelated_id\tclass\ttype/scale\tname\trelevance\ttext\thelp\tlanguage\tvalidation\tmandatory\tother\tdefault\tsame_default\tallowed_filetypes\talphasort\tanswer_width\tanswer_width_bycolumn\tarray_filter\tarray_filter_exclude\tarray_filter_style\tassessment_value\tcategory_separator\tchoice_input_columns\tchoice_title\tcode_filter\tcommented_checkbox\tcommented_checkbox_auto\tcssclass\tdate_format\tdate_max\tdate_min\tdisplay_columns\tdisplay_rows\tdisplay_type\tdropdown_dates\tdropdown_dates_minute_step\tdropdown_dates_month_style\tdropdown_prefix\tdropdown_prepostfix\tdropdown_separators\tdropdown_size\tdualscale_headerA\tdualscale_headerB\tem_validation_q\tem_validation_q_tip\tem_validation_sq\tem_validation_sq_tip\tequals_num_value\tequation\texclude_all_others\texclude_all_others_auto\thidden\thide_tip\tinput_boxes\tinput_size\tlabel_input_columns\tlocation_city\tlocation_country\tlocation_defaultcoordinates\tlocation_mapheight\tlocation_mapservice\tlocation_mapwidth\tlocation_mapzoom\tlocation_nodefaultfromip\tlocation_postal\tlocation_state\tmax_answers\tmax_filesiz""")
	f.write("""e\tmax_num_of_files\tmax_num_value\tmax_num_value_n\tmax_subquestions\tmaximum_chars\tmin_answers\tmin_num_of_files\tmin_num_value\tmin_num_value_n\tmultiflexible_checkbox\tmultiflexible_max\tmultiflexible_min\tmultiflexible_step\tnum_value_int_only\tnumbers_only\tother_comment_mandatory\tother_numbers_only\tother_replace_text\tpage_break\tparent_order\tprefix\tprintable_help\tpublic_statistics\tquestion_template\trandom_group\trandom_order\trank_title\trepeat_headings\treverse\tsamechoiceheight\tsamelistheight\tscale_export\tshow_comment\tshow_grand_total\tshow_title\tshow_totals\tshowpopups\tslider_accuracy\tslider_custom_handle\tslider_default\tslider_default_set\tslider_handle\tslider_layout\tslider_max\tslider_middlestart\tslider_min\tslider_orientation\tslider_rating\tslider_reset\tslider_reversed\tslider_separator\tslider_showminmax\tstatistics_graphtype\tstatistics_showgraph\tstatistics_showmap\tsuffix\ttext_input_columns\ttext_input_width\ttime_limit\ttime_limit_action\ttime_limit_countdown_message\ttime_limit_disable_next\ttime_limit_disable_prev\ttime_limit_mes""")
	f.write("""sage\ttime_limit_message_delay\ttime_limit_message_style\ttime_limit_timer_style\ttime_limit_warning\ttime_limit_warning_2\ttime_limit_warning_2_display_time\ttime_limit_warning_2_message\ttime_limit_warning_2_style\ttime_limit_warning_display_time\ttime_limit_warning_message\ttime_limit_warning_style\tuse_dropdown\tvalue_range_allows_missing\t\n""")
	f.write("""\t\tS\t\tsid\t\t190199\n""")
	f.write("""\t\tS\t\tgsid\t\t1\n""")
	f.write("""\t\tS\t\tadmin\t\t\n""")
	f.write("""\t\tS\t\tadminemail\t\tn.mandelli2@campus.unimib.it\n""")
	f.write("""\t\tS\t\tanonymized\t\tN\n""")
	#f.write("""\t\tS\t\tfaxto\t\t\n""")
	f.write("""\t\tS\t\tformat\t\tG\n""")
	f.write("""\t\tS\t\tsavetimings\t\tN\n""")
	f.write("""\t\tS\t\ttemplate\t\tfruity\n""")
	f.write("""\t\tS\t\tlanguage\t\tit\n""")
	f.write("""\t\tS\t\tadditional_languages\t\t\n""")
	f.write("""\t\tS\t\tdatestamp\t\tN\n""")
	f.write("""\t\tS\t\tusecookie\t\tN\n""")
	f.write("""\t\tS\t\tallowregister\t\tN\n""")
	f.write("""\t\tS\t\tallowsave\t\tY\n""")
	f.write("""\t\tS\t\tautonumber_start\t\t0\n""")
	f.write("""\t\tS\t\tautoredirect\t\tN\n""")
	f.write("""\t\tS\t\tallowprev\t\tN\n""")
	f.write("""\t\tS\t\tprintanswers\t\tN\n""")
	f.write("""\t\tS\t\tipaddr\t\tN\n""")
	f.write("""\t\tS\t\trefurl\t\tN\n""")
	f.write("""\t\tS\t\tshowsurveypolicynotice\t\t0\n""")
	f.write("""\t\tS\t\tpublicstatistics\t\tN\n""")
	f.write("""\t\tS\t\tshowdatapolicybutton\t\t0\n""")
	f.write("""\t\tS\t\tshowlegalnoticebutton\t\t0\n""")
	f.write("""\t\tS\t\tpublicgraphs\t\tN\n""")
	f.write("""\t\tS\t\tlistpublic\t\tN\n""")
	f.write("""\t\tS\t\thtmlemail\t\tY\n""")
	f.write("""\t\tS\t\tsendconfirmation\t\tY\n""")
	f.write("""\t\tS\t\ttokenanswerspersistence\t\tN\n""")
	f.write("""\t\tS\t\tassessments\t\tY\n""")
	f.write("""\t\tS\t\tusecaptcha\t\tN\n""")
	f.write("""\t\tS\t\tusetokens\t\tN\n""")
	f.write("""\t\tS\t\tbounce_email\t\tn.mandelli2@campus.unimib.it\n""")
	#f.write("""\t\tS\t\temailresponseto\t\t\n""")
	#f.write("""\t\tS\t\temailnotificationto\t\t\n""")
	f.write("""\t\tS\t\ttokenlength\t\t15\n""")
	f.write("""\t\tS\t\tshowxquestions\t\tN\n""")
	f.write("""\t\tS\t\tshowgroupinfo\t\tB\n""")
	f.write("""\t\tS\t\tshownoanswer\t\tY\n""")
	f.write("""\t\tS\t\tshowqnumcode\t\tX\n""")
	f.write("""\t\tS\t\tbounceprocessing\t\tN\n""")
	f.write("""\t\tS\t\tshowwelcome\t\tY\n""")
	f.write("""\t\tS\t\tshowprogress\t\tY\n""")
	f.write("""\t\tS\t\tquestionindex\t\t0\n""")
	f.write("""\t\tS\t\tnavigationdelay\t\t0\n""")
	f.write("""\t\tS\t\tnokeyboard\t\tN\n""")
	f.write("""\t\tS\t\talloweditaftercompletion\t\tN\n""")
	f.write("""\t\tSL\t\tsurveyls_survey_id\t\t190199\t\tit\n""")
	f.write("""\t\tSL\t\tsurveyls_language\t\tit\t\tit\n""")
	f.write("""\t\tSL\t\tsurveyls_title\t\t"Supporto di Intelligenza Artificiale Spiegabile alla lettura di ECG"\t\tit\n""")
	f.write("""\t\tSL\t\tsurveyls_description\t\t"<h4 style=""text-align:left;""><span style=""font-family:Courier New,Courier,monospace;""><br /> Benvenuto, nelle pagine seguenti il sistema le proporra' di considerare 20 elettrocardiogrammi di varia complessita' per cui e' disponibile una lettura automatica da parte di una intelligenza artificiale di ultima generazione, sviluppata con metodiche di deep learning. <br /> Per ogni ECG, lei sara' quindi invitato a confrontarsi con la intelligenza artificiale (IA) e a fornire qualora lo volesse una diagnosi testuale che, sebbene non sia ovviamente infallibile, e' pero' molto accurata (circa il 90% di accuratezza). <br /> Per ogni paziente, la IA le fornira' una breve descrizione, la diagnosi piu' probabile sulla base del suo modello computazionale e una spiegazione basata sul risultato dell'elaborazione. <br /> Lo scopo della ricerca e' comprendere l'utilita' del supporto computazionale e, soprattutto, delle spiegazioni che la IA e' in grado di proporre, affinche' essa non risulti una ""black-box"" non interpretabile. <br /> Lei potra' interrompere e riprendere il questionario in qualsiasi momento, riprendendo da dove si e' fermato. Le chiediamo di non utilizzare abbreviazioni e di essere piu' preciso possibile. <br /><br /> La ringraziamo per la collaborazione!</span></h4>"\t\tit\n""")
	#f.write("""\t\tSL\t\tsurveyls_welcome_text\t\t"<span style=""font-family:Georgia,serif;"">Benvenuto, nelle pagine seguenti ti chiederemo di rispondere ad alcune domande in merito agli ECG. Dovrai realizzare ........ </span>"\t\tit\n""")
	f.write("""\t\tSL\t\tsurveyls_endtext\t\t"<h4><span style=""font-family:Courier New,Courier,monospace; color: RGB(89,121,91);""><br />Grazie per aver partecipato! </span></h4><br/><br/>"\t\tit\n""")
	f.write("""\t\tSL\t\tsurveyls_url\t\t\t\tit\n""")
	f.write("""\t\tSL\t\tsurveyls_urldescription\t\t\t\tit\n""")
	f.write("""\t\tSL\t\tsurveyls_email_invite_subj\t\t"Invito per partecipare all'indagine"\t\tit\n""")
	f.write("""\t\tSL\t\tsurveyls_email_invite\t\t"Egregio/a {FIRSTNAME},<br /><br />e' invitato a partecipare ad un'indagine on line.<br /><br />L'indagine e' intitolata:<br />""{SURVEYNAME}""<br /><br />""{SURVEYDESCRIPTION}""<br /><br />Per partecipare fare click sul link in basso.<br /><br />Cordiali saluti,{ADMINNAME} ({ADMINEMAIL})<br /><br />----------------------------------------------<br />Fare click qui per accedere al questionario e rispondere alle domande relative:<br />{SURVEYURL}<br /><br />Se non si intende partecipare a questa indagine e non si vogliono ricevere altri inviti, si puo' cliccare sul seguente collegamento:<br />{OPTOUTURL}<br /><br />Se e' presente in blacklist ma vuole partecipare a questa indagine e ricevere inviti, vada al seguente link:<br />{OPTINURL}"\t\tit\n""")
	f.write("""\t\tSL\t\tsurveyls_email_remind_subj\t\t"Promemoria per partecipare all'indagine"\t\tit\n""")
	f.write("""\t\tSL\t\tsurveyls_email_remind\t\t"Egregio/a {FIRSTNAME},<br />Recentemente ha ricevuto un invito a partecipare ad un'indagine on line.<br /><br />Abbiamo notato che non ha ancora completato il questionario. Con l'occasione Le ricordiamo che il questionario e' ancora disponibile.<br /><br />L'indagine e' intitolata:<br />""{SURVEYNAME}""<br /><br />""{SURVEYDESCRIPTION}""<br /><br />Per partecipare fare clic sul link qui sotto.<br /><br />Cordiali saluti,<br /><br />{ADMINNAME} ({ADMINEMAIL})<br /><br />----------------------------------------------<br />Fare clic qui per accedere all'indagine e rispondere al questionario:<br />{SURVEYURL}<br /><br />Se non si intende partecipare a questa indagine e non si vogliono ricevere altri inviti, si puo' cliccare sul seguente collegamento:<br />{OPTOUTURL}""\t\tit\n""")
	f.write("""\t\tSL\t\tsurveyls_email_register_subj\t\t"Conferma di registrazione all'indagine"\t\tit\n""")
	f.write("""\t\tSL\t\tsurveyls_email_register\t\t"Egregio/a {FIRSTNAME},<br /><br />Lei (o qualcuno che ha utilizzato il suo indirizzo e-mail) si e' registrato per partecipare all'indagine on line intitolata {SURVEYNAME}.<br /><br />Per completare il questionario fare clic sul seguente indirizzo:<br /><br />{SURVEYURL}<br /><br />Se ha qualche domanda, o se non si e' registrato e ritiene che questa e-mail ti sia pervenuta per errore, la preghiamo di contattare  {ADMINNAME} all'indirizzo {ADMINEMAIL}."\t\tit\n""")
	f.write("""\t\tSL\t\tsurveyls_email_confirm_subj\t\t"Confermare la partecipazione all&#039;indagine"\t\tit\n""")
	f.write("""\t\tSL\t\tsurveyls_email_confirm\t\t"Egregio/a {FIRSTNAME},<br /><br />Questa e-mail le e' stata inviata per confermarle che ha completato correttamente il questionario intitolato {SURVEYNAME}  e che le sue risposte sono state salvate. Grazie per la partecipazione.<br /><br />Se ha ulteriori domande circa questo messaggio, la prego di contattare {ADMINNAME} all'indirizzo e-mail {ADMINEMAIL}.<br /><br />Cordiali saluti<br /><br />{ADMINNAME}"\t\tit\n""")
	f.write("""\t\tSL\t\tsurveyls_dateformat\t\t5\t\tit\n""")
	f.write("""\t\tSL\t\temail_admin_notification_subj\t\t"Invio di una risposta all'indagine {SURVEYNAME}"\t\tit\n""")
	f.write("""\t\tSL\t\temail_admin_notification\t\t"Salve,<br /><br />Una nuova risposta e' stata inviata per l'indagine '{SURVEYNAME}'.<br /><br />Fare click sul link seguente per vedere le risposte individuali:<br />{VIEWRESPONSEURL}<br /><br />Fare click sul link seguente per modificare le risposte individuali:<br />{EDITRESPONSEURL}<br /><br />Fare clic sul link seguente per visualizzare le statistiche:<br />{STATISTICSURL}"\t\tit\n""")
	f.write("""\t\tSL\t\temail_admin_responses_subj\t\t"Invio di una risposta all'indagine {SURVEYNAME} con risultati"\t\tit\n""")
	f.write("""\t\tSL\t\temail_admin_responses\t\t"Salve,<br /><br />Una nuova risposta e' stata inviata dall'indagine '{SURVEYNAME}'.<br /><br />Fare clic sul link seguente per vedere la risposta individuale:<br />{VIEWRESPONSEURL}<br /><br />Fare clic sul link seguente per modificare la risposta individuale:<br />{EDITRESPONSEURL}<br /><br />Fare clic sul link seguente per visualizzare le statistiche:<br />{STATISTICSURL}<br /><br /><br />Le seguenti risposte sono state date dal partecipante:<br />{ANSWERTABLE}"\t\tit\n""")
	f.write("""\t\tSL\t\tsurveyls_numberformat\t\t0\t\tit\n""")

	with open('configuration.csv', 'r') as file:
		reader = csv.reader(file, delimiter = "|")
		line_count=0
		f.write("""%d\t\tG\t%d\t"Prima di procedere con la compilazione le chiediamo di rispondere alla seguente domanda conoscitiva:"\t1\t"Di seguito potra' visionare una tabella in cui indicare, tramite un valore da 1 a 6, il suo livello di fiducia nella lettura automatizzata. "\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (3,3))		
		f.write("""%d\t\tQ\tF\tdom1\t1\t"Compilare la seguente tabella, dove 1 = 'Per niente' e 6 = 'Totalmente'. "\t\tit\t\tN\tN\t\t0\n""" % (93))
		f.write("""%d\t\tSQ\t\tfid1\t1\t"Fiducia nella lettura automatizzata: "\t\tit\t\tN\t\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\n""" % (94))
		f.write("""%d\t\tA\t0\t1\t\t"1"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (93))
		f.write("""%d\t\tA\t0\t2\t\t"2"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (93))
		f.write("""%d\t\tA\t0\t3\t\t"3"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (93))
		f.write("""%d\t\tA\t0\t4\t\t"4"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (93))
		f.write("""%d\t\tA\t0\t5\t\t"5"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (93))
		f.write("""%d\t\tA\t0\t6\t\t"6"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (93))		
		for row in reader:
			if(line_count != 0):
				i = int(row[0])
				case_description= row[1]
				case_diagnosis= row[2]
				case_image_url= row[3]
				case_explanation= row[4]
				case_score= int(row[5])
				f.write("""%d\t\tG\t%d\t"Paziente No. %d ~ Pagina 1"\t1\t"Di seguito potra' visionare una breve descrizione, l'immagine relativa all' ECG e la diagnosi suggerita dall'AI del paziente ID-%d. Ispezioni l'immagine, legga con attenzione e risponda alla domanda in fondo alla pagina. <br /> NB: Se lo reputa necessario, passando il puntatore del mouse sulla figura si attivera' uno zoom che le consentira' di leggere al meglio le strutture evidenziate. Se il suo browser non dovesse consentire la corretta visualizzazione delle immagini, prema il tasto destro sulla figura -> 'Apri immagine in una nuova scheda'."\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (4*i+1,4*i+1,i,i))
				f.write("""%d\t\tQ\tX\tdesc2%d\t1\t"<span style=""font-family:Georgia,serif;""><span style=""color: rgb(105, 155, 103); font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;"">Descrizione paziente: <br/>%s</span></span>"\t\tit\t\tN\tN\t\t0\n""" % (100*i+1,i,case_description))				
				f.write("""%d\t\tQ\tX\timage%d2\t1\t"<style>.magnifier { overflow: hidden; position: relative; }  .maglens { position: absolute; overflow: hidden; width: 200px; height: 200px; border: 2px solid #149414; box-shadow: inset 0 0 20px rgba(0,0,0,.5); cursor: none; }  .magsmall { position: absolute; border-style: none }  .maglarge { position: absolute; border-style: none } </style> <script type=""text/javascript"" src=""https://users.cs.northwestern.edu/~riesbeck/demo/magnifier_v3/magnifier.js""></script> <div class=""magnifier"" style=""height: 750px; width: 1100px; margin: 20px;""> <div class=""maglens""> <img src=""%s"" class=""maglarge"" alt=""ECG"" ismap=""ismap"" usemap=""#kaart"" style=""height: 1400px; width: 2100px;"" /> </div> </div>"\t\tit\t\tN\tN\t\t0\n""" % (100*i+2,i,case_image_url))												
				f.write("""%d\t\tQ\tX\tdiag1%d\t1\t"<span style=""font-family:Georgia,serif;""><span style=""color: rgb(105, 155, 103); font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;"">Il sistema di intelligenza artificiale suggerisce: <br/>%s</span></span>"\t\tit\t\tN\tN\t\t0\n""" % (100*i+3,i,case_diagnosis))								
				f.write("""%d\t\tQ\tL\tlabel1%d\t1\t"Dopo aver visionato il tracciato e la diagnosi prodottta dall'AI, quale e' la sua scelta? "\t"Se non e' sicuro della sua scelta, avra' modo di modificarla nella domanda successiva. Per inserire una nuova diagnosi utilizzo il box sottostante."\tit\t\tY\tN\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (100*i+4,i))				
				f.write("""%d\t\tA\t0\t0\t\t"Scelgo la diagnosi prodotta dall'AI"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (100*i+4))
				f.write("""%d\t\tA\t0\t1\t\t"Inserisco una nuova diagnosi..."\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (100*i+4))
				f.write("""%d\t\tQ\tT\ttext2%d\t"(((!is_empty(label1%d.NAOK) && (label1%d.NAOK == 1))))"\t"Inserisca la sua diagnosi: "\t\tit\t\tY\tN\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (100*i+5,i,i,i))
				f.write("""%d\t%d\tC\t1\tlabel1%d\t'==\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (100*i+6,100*i+4,i)) 
								
				f.write("""%d\t\tG\t%d\t"Paziente No. %d ~ Pagina 2"\t1\t"Di seguito potra' visionare tutte le informazioni della pagina precedente e la spiegazione testuale prodotta dall'AI del paziente ID-%d. Legga con attenzione e risponda alla domanda. <br />"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (4*i+2,4*i+2,i,i))
				f.write("""%d\t\tQ\tX\tdesc3%d\t1\t"<span style=""font-family:Georgia,serif;""><span style=""color: rgb(105, 155, 103); font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;"">Descrizione paziente: <br/>%s</span></span>"\t\tit\t\tN\tN\t\t0\n""" % (100*i+7,i,case_description))								
				f.write("""%d\t\tQ\tX\timage%d3\t1\t"<style>.magnifier { overflow: hidden; position: relative; }  .maglens { position: absolute; overflow: hidden; width: 200px; height: 200px; border: 2px solid #149414; box-shadow: inset 0 0 20px rgba(0,0,0,.5); cursor: none; }  .magsmall { position: absolute; border-style: none }  .maglarge { position: absolute; border-style: none } </style> <script type=""text/javascript"" src=""https://users.cs.northwestern.edu/~riesbeck/demo/magnifier_v3/magnifier.js""></script> <div class=""magnifier"" style=""height: 750px; width: 1100px; margin: 20px;""> <div class=""maglens""> <img src=""%s"" class=""maglarge"" alt=""ECG"" ismap=""ismap"" usemap=""#kaart"" style=""height: 1400px; width: 2100px;"" /> </div> </div>"\t\tit\t\tN\tN\t\t0\n""" % (100*i+8,i,case_image_url))												
				f.write("""%d\t\tQ\tX\tdiag2%d\t1\t"<span style=""font-family:Georgia,serif;""><span style=""color: rgb(105, 155, 103); font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;"">Il sistema di intelligenza artificiale suggerisce: <br/>%s</span></span>"\t\tit\t\tN\tN\t\t0\n""" % (100*i+9,i,case_diagnosis))												
				f.write("""%d\t\tQ\tX\texpl1%d\t1\t"<span style=""font-family:Georgia,serif;""><span style=""color: rgb(105, 155, 103); font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;"">Spiegazione testuale fornita dall'intelligenza artificiale: <br/>%s</span></span>"\t\tit\t\tN\tN\t\t0\n""" % (100*i+10,i,case_explanation))	
				
				f.write("""%d\t\tQ\tL\tlabel2%d\t"(((!is_empty(label1%d.NAOK) && (label1%d.NAOK == 1))))"\t"Dopo aver visionato la spiegazione testuale prodotta dall'AI, ha cambiato idea relativamente alla scelta da lei attuata in precedenza? "\t"Se desidera modificare la sua precedente diagnosi e inserirne una nuova, utilizzi il box sottostante. "\tit\t\tY\tN\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (100*i+11,i,i,i))		
				f.write("""%d\t%d\tC\t1\tlabel1%d\t'==\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (100*i+12,100*i+4,i))
				f.write("""%d\t\tA\t0\t0\t\t"Confermo la mia diagnosi: <br/><p style=""color: rgb(60,92,126)"">{list(that.text2%d.shown)}"<p/>\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t100\n""" % (100*i+11,i))
				f.write("""%d\t\tA\t0\t1\t\t"Scelgo la diagnosi prodotta dall'AI"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t%d\n""" % (100*i+11,case_score))
				f.write("""%d\t\tA\t0\t2\t\t"Inserisco una nuova diagnosi..."\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t100\n""" % (100*i+11))
				f.write("""%d\t\tQ\tT\ttext3%d\t"((label2%d == 2))"\t"Inserisca la sua nuova diagnosi: "\t\tit\t\tY\tN\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (100*i+13,i,i))
				f.write("""%d\t%d\tC\t1\tlabel2%d\t'==\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (100*i+14,100*i+11,i)) 				
				
				f.write("""%d\t\tQ\tL\tlabel3%d\t"(((!is_empty(label1%d.NAOK) && (label1%d.NAOK == 0))))"\t"Dopo aver visionato la spiegazione testuale prodotta dall'AI, ha cambiato idea relativamente alla scelta da lei attuata in precedenza? "\t"Se desidera modificare la sua precedente diagnosi e inserirne una nuova, utilizzi il box sottostante. "\tit\t\tY\tN\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (100*i+15,i,i,i))		
				f.write("""%d\t%d\tC\t1\tlabel1%d\t'==\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (100*i+16,100*i+4,i))
				f.write("""%d\t\tA\t0\t0\t\t"Scelgo la diagnosi prodotta dall'AI"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t%d\n""" % (100*i+15,case_score))
				f.write("""%d\t\tA\t0\t1\t\t"Inserisco una nuova diagnosi..."\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t100\n""" % (100*i+15))
				f.write("""%d\t\tQ\tT\ttext4%d\t"((label3%d == 1))"\t"Inserisca la sua nuova diagnosi: "\t\tit\t\tY\tN\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (100*i+17,i,i))
				f.write("""%d\t%d\tC\t1\tlabel3%d\t'==\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (100*i+18,100*i+14,i)) 				
								
							
				f.write("""%d\t\tG\t%d\t"Paziente No. %d ~ Pagina 3"\t1\t"Di seguito potra' visionare una tabella in cui indicare, tramite un valore da 1 a 6, tre dimensioni di qualita' della spiegazione fornita dall'AI. <br />Per semplicita' sono riportati la descrizione, l'ECG, la diagnosi e la spiegazione fornita nei box sottostanti. <br />"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (4*i+3, 4*i+3,i))		
				f.write("""%d\t\tQ\tX\tdesc4%d\t1\t"<span style=""font-family:Georgia,serif;""><span style=""color: rgb(105, 155, 103); font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;"">Descrizione paziente: <br/>%s</span></span>"\t\tit\t\tN\tN\t\t0\n""" % (100*i+19,i,case_description))								
				f.write("""%d\t\tQ\tX\timage%d4\t1\t"<style>.magnifier { overflow: hidden; position: relative; }  .maglens { position: absolute; overflow: hidden; width: 200px; height: 200px; border: 2px solid #149414; box-shadow: inset 0 0 20px rgba(0,0,0,.5); cursor: none; }  .magsmall { position: absolute; border-style: none }  .maglarge { position: absolute; border-style: none } </style> <script type=""text/javascript"" src=""https://users.cs.northwestern.edu/~riesbeck/demo/magnifier_v3/magnifier.js""></script> <div class=""magnifier"" style=""height: 750px; width: 1100px; margin: 20px;""> <div class=""maglens""> <img src=""%s"" class=""maglarge"" alt=""ECG"" ismap=""ismap"" usemap=""#kaart"" style=""height: 1400px; width: 2100px;"" /> </div> </div>"\t\tit\t\tN\tN\t\t0\n""" % (100*i+20,i,case_image_url))								
				f.write("""%d\t\tQ\tX\tdiag3%d\t1\t"<span style=""font-family:Georgia,serif;""><span style=""color: rgb(105, 155, 103); font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;"">Diagnosi suggerita dall'AI: <br/>%s</span></span>"\t\tit\t\tN\tN\t\t0\n""" % (100*i+21,i,case_diagnosis))
				f.write("""%d\t\tQ\tX\texpl2%d\t1\t"<span style=""font-family:Georgia,serif;""><span style=""color: rgb(105, 155, 103); font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;"">Spiegazione suggerita dall'AI: <br/>%s</span></span>"\t\tit\t\tN\tN\t\t0\n""" % (100*i+22,i,case_explanation))								
				f.write("""%d\t\tQ\tF\tconf%d\t1\t"Compilare la seguente tabella, dove 1 = 'Per niente' e 6 = 'Totalmente'. I valori sono da assegnare a ciascuna dimensione di qualita' su base della spiegazione fornita dall'AI: "\t\tit\t\tN\tN\t\t0\n""" % (100*i+23,i))
				f.write("""%d\t\tSQ\t\tappro%d\t1\t"Appropriatezza"\t\tit\t\tN\t\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\n""" % (100*i+24,i))
				f.write("""%d\t\tSQ\t\tcompr%d\t1\t"Comprensibilita'"\t\tit\t\tN\t\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\n""" % (100*i+25,i))
				f.write("""%d\t\tSQ\t\tutili%d\t1\t"Utilita'"\t\tit\t\tN\t\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\n""" % (100*i+26,i))
				f.write("""%d\t\tA\t0\t1\t\t"1"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (100*i+23))
				f.write("""%d\t\tA\t0\t2\t\t"2"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (100*i+23))
				f.write("""%d\t\tA\t0\t3\t\t"3"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (100*i+23))
				f.write("""%d\t\tA\t0\t4\t\t"4"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (100*i+23))
				f.write("""%d\t\tA\t0\t5\t\t"5"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (100*i+23))
				f.write("""%d\t\tA\t0\t6\t\t"6"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (100*i+23))
			line_count += 1
		f.write("""%d\t\tG\t%d\t"Ha completato la parte relativa agli ECG, le riproponiamo il quesito posto a inizio indagine:"\t1\t"Di seguito potra' visionare una tabella in cui indicare, tramite un valore da 1 a 6, il suo livello di fiducia nella lettura automatizzata. Ha cambiato opinione dopo lo svolgimento del questionario? "\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (4,4))		
		f.write("""%d\t\tQ\tF\tdom2\t1\t"Compilare la seguente tabella, dove 1 = 'Per niente' e 6 = 'Totalmente'. "\t\tit\t\tN\tN\t\t0\n""" % (95))
		f.write("""%d\t\tSQ\t\tfid2\t1\t"Fiducia nella lettura automatizzata: "\t\tit\t\tN\t\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\n""" % (96))
		f.write("""%d\t\tA\t0\t1\t\t"1"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (95))
		f.write("""%d\t\tA\t0\t2\t\t"2"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (95))
		f.write("""%d\t\tA\t0\t3\t\t"3"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (95))
		f.write("""%d\t\tA\t0\t4\t\t"4"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (95))
		f.write("""%d\t\tA\t0\t5\t\t"5"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (95))
		f.write("""%d\t\tA\t0\t6\t\t"6"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (95))		
		f.write("""%d\t%d\tAS\tT\t"Complimenti ha completato il questionario! Di seguito il feedback:"\t\t"<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>Ha confermato la sua diagnosi o prodotto una ulteriore in\t</var></p> 
<p id=""demo1"" style=""display:inline; font-size:18px; color: RGB(89,121,91);""><var></var></p>

<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var> casi.</var></p>
<script>
var div = parseInt({TOTAL}/100);
document.getElementById(""demo1"").innerHTML = div;
</script>
<br/>
<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>Ha selezionato la diagnosi prodotta dall'AI in\t</var></p>

<p id=""demo2"" style=""display:inline; font-size:18px; color: RGB(89,121,91);""><var></var></p>

<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var> casi di cui:</var></p>
<script>
var div = 20 - parseInt({TOTAL}/100);
document.getElementById(""demo2"").innerHTML = div;
</script>
<br/>
<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>- Ha scelto una diagnosi corretta nel\t</var></p>

<p id=""demo3"" style=""display:inline; font-size:18px; color: RGB(89,121,91);""><var></var></p>

<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>%% dei casi.</var></p>
<script>
var div = (({TOTAL}%%100)/(20 - parseInt({TOTAL}/100))*100).toFixed(2);
document.getElementById(""demo3"").innerHTML = div;
</script>
<br/>
<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>- Ha scelto una diagnosi errata nel\t</var></p>

<p id=""demo4"" style=""display:inline; font-size:18px; color: RGB(89,121,91);""><var></var></p>

<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>%% dei casi.</var></p>
<script>
var div = ((20-parseInt({TOTAL}/100)-({TOTAL}%%100))/(20 - parseInt({TOTAL}/100))*100).toFixed(2);
document.getElementById(""demo4"").innerHTML = div;
</script>"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1999\t\t\t\t\t\t100\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (90, 5))				
		f.write("""%d\t%d\tAS\tT\t"Complimenti ha completato il questionario! Di seguito il feedback:"		"<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>Ha confermato la sua diagnosi o prodotto una ulteriore in\t</var></p>

<p id=""demo1"" style=""display:inline; color: RGB(89,121,91); font-size:18px;""><var></var></p>

<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var> casi.</var></p>
<script>
var div = ({TOTAL}/100);
document.getElementById(""demo1"").innerHTML = div;
</script>
<br/>
<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>Ha selezionato la diagnosi prodotta dall'AI in\t</var></p>

<p id=""demo2"" style=""display:inline; color: RGB(89,121,91); font-size:18px;""><var></var></p>

<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var> casi.</var></p>
<script>
var div = 20-({TOTAL}/100);
document.getElementById(""demo2"").innerHTML = div;
</script>"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2000\t\t\t\t\t\t2000\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (91, 5))				
		f.write("""%d\t%d\tAS\tT\t"Complimenti ha completato il questionario! Di seguito il feedback:"		"<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>Ha confermato la sua diagnosi o prodotto una ulteriore in 0 casi.</var></p>
<br/>
<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>Ha selezionato la diagnosi prodotta dall'AI in 20 casi di cui:</var></p>
<br/>

<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>- Ha scelto una diagnosi corretta nel\t</var></p>

<p id=""demo1"" style=""display:inline; font-size:18px; color: RGB(89,121,91);""><var></var></p>

<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>%% dei casi.</var></p>
<script>
var div = ({TOTAL}/20*100).toFixed(2);
document.getElementById(""demo1"").innerHTML = div;
</script>
<br/>
<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>- Ha scelto una diagnosi errata nel\t</var></p>

<p id=""demo2"" style=""display:inline; color: RGB(89,121,91); font-size:18px;""><var></var></p>

<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>%% dei casi.</var></p>
<script>
var div = ((20-{TOTAL})/20*100).toFixed(2);
document.getElementById(""demo2"").innerHTML = div;
</script>"\t\tit\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t99\t\t\t\t\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (92, 5))				
			
															
	f.close()
if __name__=="__main__":
	main()