import csv

def main():
	
	f= open("ECG_VersionPT.txt", "a+")
	f.write("""id\trelated_id\tclass\ttype/scale\tname\trelevance\ttext\thelp\tlanguage\tvalidation\tmandatory\tother\tdefault\tsame_default\tallowed_filetypes\talphasort\tanswer_width\tanswer_width_bycolumn\tarray_filter\tarray_filter_exclude\tarray_filter_style\tassessment_value\tcategory_separator\tchoice_input_columns\tchoice_title\tcode_filter\tcommented_checkbox\tcommented_checkbox_auto\tcssclass\tdate_format\tdate_max\tdate_min\tdisplay_columns\tdisplay_rows\tdisplay_type\tdropdown_dates\tdropdown_dates_minute_step\tdropdown_dates_month_style\tdropdown_prefix\tdropdown_prepostfix\tdropdown_separators\tdropdown_size\tdualscale_headerA\tdualscale_headerB\tem_validation_q\tem_validation_q_tip\tem_validation_sq\tem_validation_sq_tip\tequals_num_value\tequation\texclude_all_others\texclude_all_others_auto\thidden\thide_tip\tinput_boxes\tinput_size\tlabel_input_columns\tlocation_city\tlocation_country\tlocation_defaultcoordinates\tlocation_mapheight\tlocation_mapservice\tlocation_mapwidth\tlocation_mapzoom\tlocation_nodefaultfromip\tlocation_postal\tlocation_state\tmax_answers\tmax_filesiz""")
	f.write("""e\tmax_num_of_files\tmax_num_value\tmax_num_value_n\tmax_subquestions\tmaximum_chars\tmin_answers\tmin_num_of_files\tmin_num_value\tmin_num_value_n\tmultiflexible_checkbox\tmultiflexible_max\tmultiflexible_min\tmultiflexible_step\tnum_value_int_only\tnumbers_only\tother_comment_mandatory\tother_numbers_only\tother_replace_text\tpage_break\tparent_order\tprefix\tprintable_help\tpublic_statistics\tquestion_template\trandom_group\trandom_order\trank_title\trepeat_headings\treverse\tsamechoiceheight\tsamelistheight\tscale_export\tshow_comment\tshow_grand_total\tshow_title\tshow_totals\tshowpopups\tslider_accuracy\tslider_custom_handle\tslider_default\tslider_default_set\tslider_handle\tslider_layout\tslider_max\tslider_middlestart\tslider_min\tslider_orientation\tslider_rating\tslider_reset\tslider_reversed\tslider_separator\tslider_showminmax\tstatistics_graphtype\tstatistics_showgraph\tstatistics_showmap\tsuffix\ttext_input_columns\ttext_input_width\ttime_limit\ttime_limit_action\ttime_limit_countdown_message\ttime_limit_disable_next\ttime_limit_disable_prev\ttime_limit_mes""")
	f.write("""sage\ttime_limit_message_delay\ttime_limit_message_style\ttime_limit_timer_style\ttime_limit_warning\ttime_limit_warning_2\ttime_limit_warning_2_display_time\ttime_limit_warning_2_message\ttime_limit_warning_2_style\ttime_limit_warning_display_time\ttime_limit_warning_message\ttime_limit_warning_style\tuse_dropdown\tvalue_range_allows_missing\t\n""")
	f.write("""\t\tS\t\tsid\t\t200199\n""")
	f.write("""\t\tS\t\tgsid\t\t1\n""")
	f.write("""\t\tS\t\tadmin\t\t\n""")
	f.write("""\t\tS\t\tadminemail\t\tn.mandelli2@campus.unimib.it\n""")
	f.write("""\t\tS\t\tanonymized\t\tN\n""")
	#f.write("""\t\tS\t\tfaxto\t\t\n""")
	f.write("""\t\tS\t\tformat\t\tG\n""")
	f.write("""\t\tS\t\tsavetimings\t\tN\n""")
	f.write("""\t\tS\t\ttemplate\t\tfruity\n""")
	f.write("""\t\tS\t\tlanguage\t\tpt\n""")
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
	f.write("""\t\tSL\t\tsurveyls_survey_id\t\t200199\t\tpt\n""")
	f.write("""\t\tSL\t\tsurveyls_language\t\tpt\t\tpt\n""")
	f.write("""\t\tSL\t\tsurveyls_title\t\t"Suporte de inteligencia artificial explicado para leitura de ECG"\t\tpt\n""")
	f.write("""\t\tSL\t\tsurveyls_description\t\t"<h4 style=""text-align:left;""><span style=""font-family:Courier New,Courier,monospace;""><br /> Bem-vindo, nas paginas seguintes o sistema ira' propor que considere 20 eletrocardiogramas de complexidade variavel para os quais esta' disponivel uma leitura automatica por inteligencia artificial de ultima geracao, desenvolvida com metodos de deep learning. <br /> Para cada ECG, voce sera' solicitado a fornecer um diagnostico textual e a lidar com a inteligencia artificial (IA) que, embora obviamente nao seja infalivel, e', no entanto, muito precisa (cerca de 90% de precisao). <br /> Para cada paciente, o AI fornecera' uma breve descricao, o diagnstico mais provavel baseado em seu modelo computacional e uma explicacao baseada no resultado do processamento. <br /> O objetivo da pesquisa e' compreender a utilidade do suporte computacional e, sobretudo, das explicacoes que a IA e' capaz de propor, para que nao resulte em uma "" caixa-preta "" nao interpretavel <br /> Voce pode parar e retomar o questionario a qualquer momento, continuando de onde parou. Pedimos que voce nao use abreviacoes e seja o mais preciso possivel. <br /> <br /> Obrigado pela sua cooperacao!</span></h4>"\t\tpt\n""")
	#f.write("""\t\tSL\t\tsurveyls_welcome_text\t\t"<span style=""font-family:Georgia,serif;"">Benvenuto, nelle pagine seguenti ti chiederemo di rispondere ad alcune domande in merito agli ECG. Dovrai realizzare ........ </span>"\t\tpt\n""")
	f.write("""\t\tSL\t\tsurveyls_endtext\t\t"<h4><span style=""font-family:Courier New,Courier,monospace; color: RGB(89,121,91);""><br />Obrigado por participar! </span></h4><br/><br/>"\t\tpt\n""")
	f.write("""\t\tSL\t\tsurveyls_url\t\t\t\tpt\n""")
	f.write("""\t\tSL\t\tsurveyls_urldescription\t\t\t\tpt\n""")
	f.write("""\t\tSL\t\tsurveyls_email_invite_subj\t\t"Convite para participar num inquerito"\t\tpt\n""")
	f.write("""\t\tSL\t\tsurveyls_email_invite\t\t"Caro(a) {FIRSTNAME},<br /><br />Foi convidado para participar num inquerito.<br /><br />O inquerito e intitulado de:<br />""{SURVEYNAME}""<br /><br />""{SURVEYDESCRIPTION}""<br /><br />Para participar, por favor, utilize o endereco abaixo.<br /><br />Com os melhores cumprimentos,<br /><br />{ADMINNAME} ({ADMINEMAIL})<br /><br />----------------------------------------------<br />Clique aqui para aceder ao inquerito:<br />{SURVEYURL}<br /><br />Se nao quer participar deste inquerito e nao deseja receber mais convites clique p.f. na seguinte ligacao:<br />{OPTOUTURL}<br /><br />Se estiver na lista negra mas quiser participar neste inquerito e pretender receber convites, por favor clique no seguinte link:<br /> {OPTINURL}"\t\tpt\n""")
	f.write("""\t\tSL\t\tsurveyls_email_remind_subj\t\t"Lembrete para participar num inquerito"\t\tpt\n""")
	f.write("""\t\tSL\t\tsurveyls_email_remind\t\t"Caro(a) {FIRSTNAME}<br /><br />Recentemente, foi convidado a participar num inquerito.<br /><br />Notamos que ainda nao completou o inquerito, e queremos relembrar que o inquerito ainda esta disponivel, caso queira tomar parte dele.<br /><br />O inquerito tem o titulo:<br />""{SURVEYNAME}""<br /><br />""{SURVEYDESCRIPTION}""<br /><br />Para participar, por favor, carregue no endereco abaixo.<br /><br />Com os melhores cumprimentos,<br /><br />{ADMINNAME} ({ADMINEMAIL})<br /><br />----------------------------------------------<br />Clique aqui para aceder ao inquerito:<br />{SURVEYURL}<br /><br />Se nao quer participar deste inquerito e nao deseja receber mais convites clique p.f. na seguinte ligacao:<br />{OPTOUTURL}""\t\tpt\n""")
	f.write("""\t\tSL\t\tsurveyls_email_register_subj\t\t"Confirmacao do registo no inquerito"\t\tpt\n""")
	f.write("""\t\tSL\t\tsurveyls_email_register\t\t"Caro(a) {FIRSTNAME},<br /><br />Registou-se, ou alguem utilizando o seu endereco de correio, para participar no inquerito com o titulo {SURVEYNAME}.<br /><br />Para completar este inquerito, carregue no endereco:<br /><br />{SURVEYURL}<br /><br />Se tiver alguma pergunta sobre este inquerito, ou se nao fez o registo para participar e considera este email um erro, por favor contacte {ADMINNAME} atraves do endereco electronico {ADMINEMAIL}."\t\tpt\n""")
	f.write("""\t\tSL\t\tsurveyls_email_confirm_subj\t\t"Confirmacao da sua participacao no nosso inquerito"\t\tpt\n""")
	f.write("""\t\tSL\t\tsurveyls_email_confirm\t\t"Caro(a) {FIRSTNAME},<br /><br />Este email confirma que completou o inquerito intitulado {SURVEYNAME} e que as suas respostas foram gravadas. Agradecemos a sua participacao.<br /><br />Se tiver outras perguntas relacionadas com este email, por favor, contacte {ADMINNAME} atraves do endereco electronico {ADMINEMAIL}.<br /><br />Com os melhores cumprimentos,<br /><br />{ADMINNAME}"\t\tpt\n""")
	f.write("""\t\tSL\t\tsurveyls_dateformat\t\t5\t\tpt\n""")
	f.write("""\t\tSL\t\temail_admin_notification_subj\t\t"Resposta a submissao do inquerito {SURVEYNAME}"\t\tpt\n""")
	f.write("""\t\tSL\t\temail_admin_notification\t\t"Hello,<br /><br />A new response was submitted for your survey '{SURVEYNAME}'.<br /><br />Click the following link to see the individual response:<br />{VIEWRESPONSEURL}<br /><br />Click the following link to edit the individual response:<br />{EDITRESPONSEURL}<br /><br />View statistics by clicking here:<br />{STATISTICSURL}"\t\tpt\n""")
	f.write("""\t\tSL\t\temail_admin_responses_subj\t\t"Resposta a submissao do inquerito {SURVEYNAME} incluindo resultados"\t\tpt\n""")
	f.write("""\t\tSL\t\temail_admin_responses\t\t"Hello,<br /><br />A new response was submitted for your survey '{SURVEYNAME}'.<br /><br />Click the following link to see the individual response:<br />{VIEWRESPONSEURL}<br /><br />Click the following link to edit the individual response:<br />{EDITRESPONSEURL}<br /><br />View statistics by clicking here:<br />{STATISTICSURL}<br /><br /><br />The following answers were given by the participant:<br />{ANSWERTABLE}"\t\tpt\n""")
	f.write("""\t\tSL\t\tsurveyls_numberformat\t\t0\t\tpt\n""")

	with open('configuration_pt.csv','r') as file:
		reader = csv.reader(file, delimiter = "|")
		line_count=0
		f.write("""%d\t\tG\t%d\t"Antes de prosseguir com a compilacao, pedimos que voce responda a' seguinte questao cognitiva:"\t1\t"Abaixo voce podera' visualizar uma tabela na qual indicara', usando um valor de 1 a 6, seu nivel de confianca na leitura automatizada . "\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (3,3))		
		f.write("""%d\t\tQ\tF\tdom1\t1\t"Preencha a seguinte tabela, onde 1 = 'Nem um pouco' e 6 = 'Totalmente'. "\t\tpt\t\tN\tN\t\t0\n""" % (93))
		f.write("""%d\t\tSQ\t\tfid1\t1\t"Confianca na leitura automatizada:"\t\tpt\t\tN\t\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\n""" % (94))
		f.write("""%d\t\tA\t0\t1\t\t"1"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (93))
		f.write("""%d\t\tA\t0\t2\t\t"2"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (93))
		f.write("""%d\t\tA\t0\t3\t\t"3"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (93))
		f.write("""%d\t\tA\t0\t4\t\t"4"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (93))
		f.write("""%d\t\tA\t0\t5\t\t"5"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (93))
		f.write("""%d\t\tA\t0\t6\t\t"6"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (93))		
		for row in reader:
			if(line_count != 0):
				i = int(row[0])
				case_description= row[1]
				case_diagnosis= row[2]
				case_image_url= row[3]
				case_explanation= row[4]
				case_score= int(row[5])
				example= row[6]
				f.write("""%d\t\tG\t%d\t"Paciente No.%d ~ Pagina 1"\t1\t" Abaixo voce podera' ver uma breve descricao da ID do paciente-%d e a imagem de seu ECG. Observe-os com atencao e, por fim, responda a' pergunta no final da pagina. <br /> NOTA: Caso julgue necessario, passar o cursor do mouse sobre a figura ativara' um zoom que permitira' uma melhor leitura das estruturas destacadas. Se o seu navegador nao permitir a exibicao correta das imagens, pressione o botao direito na figura -> 'Abrir imagem em uma nova aba'."\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (4*i+1,4*i+1,i,i))
				#f.write("""%d\t\tQ\tX\timage%d1\t1\t"<style text=""text/css"">.zoom { padding: 50px; background-color: white; transition: transform .2s; width: 20px; height: 20px; margin: 0 ;} .zoom:hover { transform: scale(1.3);} </style><p style=""text-align:center;""><img alt=""ECG paziente %d"" class=""zoom"" src=""%s"" style=""height: 750px; width: 1100px;""></p>"\t\tpt\t\tN\tN\t\t0\n""" % (100*i+1,i,i,case_image_url))
				f.write("""%d\t\tQ\tX\timage%d1\t1\t"<style>.magnifier { overflow: hidden; position: relative; }  .maglens { position: absolute; overflow: hidden; width: 200px; height: 200px; border: 2px solid #149414; box-shadow: inset 0 0 20px rgba(0,0,0,.5); cursor: none; }  .magsmall { position: absolute; border-style: none }  .maglarge { position: absolute; border-style: none } </style> <script type=""text/javascript"" src=""https://users.cs.northwestern.edu/~riesbeck/demo/magnifier_v3/magnifier.js""></script> <div class=""magnifier"" style=""height: 750px; width: 1100px; margin: 20px;""> <div class=""maglens""> <img src=""%s"" class=""maglarge"" alt=""ECG"" ismap=""ismap"" usemap=""#kaart"" style=""height: 1400px; width: 2100px;"" /> </div> </div>"\t\tpt\t\tN\tN\t\t0\n""" % (100*i+1,i,case_image_url))				
				f.write("""%d\t\tQ\tX\tdesc1%d\t1\t"<span style=""font-family:Georgia,serif;""><span style=""color: rgb(105, 155, 103); font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;"">Descricao do paciente: <br/>%s</span></span>"\t\tpt\t\tN\tN\t\t0\n""" % (100*i+2,i,case_description))				
				f.write("""%d\t\tQ\tT\ttext1%d\t1\t"A luz do rastreamento de ID-%d do paciente, forneca seu diagnostico: "\t" Se voce nao tiver certeza de sua escolha, podera' modifica-la nas seguintes questoes."\tpt\t\tY\tN\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (100*i+3,i,i))
				
				f.write("""%d\t\tG\t%d\t"Paciente No.%d ~ Pagina 2"\t1\t" Abaixo voce podera' ver a descricao, o ECG e o diagnostico sugerido pelo IA do paciente ID-%d. Leia com atencao e responda a' pergunta."\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (4*i+2,4*i+2,i,i))
				f.write("""%d\t\tQ\tX\tdesc2%d\t1\t"<span style=""font-family:Georgia,serif;""><span style=""color: rgb(105, 155, 103); font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;"">Descricao do paciente: <br/>%s</span></span>"\t\tpt\t\tN\tN\t\t0\n""" % (100*i+4,i,case_description))				
				f.write("""%d\t\tQ\tX\timage%d2\t1\t"<style>.magnifier { overflow: hidden; position: relative; }  .maglens { position: absolute; overflow: hidden; width: 200px; height: 200px; border: 2px solid #149414; box-shadow: inset 0 0 20px rgba(0,0,0,.5); cursor: none; }  .magsmall { position: absolute; border-style: none }  .maglarge { position: absolute; border-style: none } </style> <script type=""text/javascript"" src=""https://users.cs.northwestern.edu/~riesbeck/demo/magnifier_v3/magnifier.js""></script> <div class=""magnifier"" style=""height: 750px; width: 1100px; margin: 20px;""> <div class=""maglens""> <img src=""%s"" class=""maglarge"" alt=""ECG"" ismap=""ismap"" usemap=""#kaart"" style=""height: 1400px; width: 2100px;"" /> </div> </div>"\t\tpt\t\tN\tN\t\t0\n""" % (100*i+5,i,case_image_url))												
				f.write("""%d\t\tQ\tX\tdiag1%d\t1\t"<span style=""font-family:Georgia,serif;""><span style=""color: rgb(105, 155, 103); font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;"">O sistema de inteligencia artificial sugere: <br/>%s</span></span>"\t\tpt\t\tN\tN\t\t0\n""" % (100*i+6,i,case_diagnosis))								
				f.write("""%d\t\tQ\tL\tlabel1%d\t1\t"Apos visualizar o diagnostico produzido pela IA, qual a sua escolha? "\t" Se voce deseja alterar seu diagnostico anterior e inserir um novo, use a caixa abaixo."\tpt\t\tY\tN\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (100*i+7,i))				
				f.write("""%d\t\tA\t0\t0\t\t"Eu confirmo meu diagnostico:<br/> <p style=""color: rgb(60,92,126)"">{list(that.text1%d.shown)}"<p/>\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (100*i+7,i))
				f.write("""%d\t\tA\t0\t1\t\t"Eu escolho o diagnostico produzido pela IA"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (100*i+7))
				f.write("""%d\t\tA\t0\t2\t\t"Eu entro um novo diagnostico ..."\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (100*i+7))
				f.write("""%d\t\tQ\tT\ttext2%d\t"(((!is_empty(label1%d.NAOK) && (label1%d.NAOK == 2))))"\t"Insira seu novo diagnostico:"\t\tpt\t\tY\tN\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (100*i+8,i,i,i))
				f.write("""%d\t%d\tC\t1\tlabel1%d\t'==\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (100*i+9,100*i+7,i)) 
								
				f.write("""%d\t\tG\t%d\t"Paciente No.%d ~ Pagina 3"\t1\t" Abaixo voce podera' ver todas as informacoes das paginas anteriores e a explicacao textual produzida pelo IA do paciente ID-%d. Leia com atencao e responda a' pergunta. <br />"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (4*i+3,4*i+3,i,i))
				f.write("""%d\t\tQ\tX\tdesc3%d\t1\t"<span style=""font-family:Georgia,serif;""><span style=""color: rgb(105, 155, 103); font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;"">Descricao do paciente: <br/>%s</span></span>"\t\tpt\t\tN\tN\t\t0\n""" % (100*i+10,i,case_description))								
				f.write("""%d\t\tQ\tX\timage%d3\t1\t"<style>.magnifier { overflow: hidden; position: relative; }  .maglens { position: absolute; overflow: hidden; width: 200px; height: 200px; border: 2px solid #149414; box-shadow: inset 0 0 20px rgba(0,0,0,.5); cursor: none; }  .magsmall { position: absolute; border-style: none }  .maglarge { position: absolute; border-style: none } </style> <script type=""text/javascript"" src=""https://users.cs.northwestern.edu/~riesbeck/demo/magnifier_v3/magnifier.js""></script> <div class=""magnifier"" style=""height: 750px; width: 1100px; margin: 20px;""> <div class=""maglens""> <img src=""%s"" class=""maglarge"" alt=""ECG"" ismap=""ismap"" usemap=""#kaart"" style=""height: 1400px; width: 2100px;"" /> </div> </div>"\t\tpt\t\tN\tN\t\t0\n""" % (100*i+11,i,case_image_url))												
				f.write("""%d\t\tQ\tX\tdiag2%d\t1\t"<span style=""font-family:Georgia,serif;""><span style=""color: rgb(105, 155, 103); font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;"">O sistema de inteligencia artificial sugere: <br/>%s</span></span>"\t\tpt\t\tN\tN\t\t0\n""" % (100*i+12,i,case_diagnosis))												
				f.write("""%d\t\tQ\tX\texpl1%d\t1\t"<span style=""font-family:Georgia,serif;""><span style=""color: rgb(105, 155, 103); font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;"">Explicacao textual fornecida por inteligencia artificial: <br/>%s</span></span>"\t\tpt\t\tN\tN\t\t0\n""" % (100*i+13,i,case_explanation))	
				f.write("""%d\t\tQ\tL\tlabel2%d\t1\t"Depois de ver a explicacao textual produzida pela IA, voce mudou de ideia em relacao ao diagnostico que idealizou anteriormente? "\t" Se voce deseja alterar seu diagnostico anterior e inserir um novo, use a caixa abaixo."\tpt\t\tY\tN\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (100*i+14,i))		
				f.write("""%d\t\tA\t0\t0\t\t"Eu confirmo meu diagnostico: <br/><p style=""color: rgb(60,92,126)"">{if(!is_empty(text2%d),list(that.text2%d.shown),list(that.text1%d.shown))}"<p/>\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t100\n""" % (100*i+14,i,i,i))
				f.write("""%d\t\tA\t0\t1\t\t"Eu escolho o diagnostico produzido pela IA"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t%d\n""" % (100*i+14,case_score))
				f.write("""%d\t\tA\t0\t2\t\t"Eu entro um novo diagnostico ..."\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t100\n""" % (100*i+14))
				f.write("""%d\t\tQ\tT\ttext3%d\t"((label2%d == 2))"\t"Insira seu novo diagnostico: "\t\tpt\t\tY\tN\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (100*i+15,i,i))
				f.write("""%d\t%d\tC\t1\tlabel2%d\t'==\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (100*i+16,100*i+14,i)) 				
				
							
				f.write("""%d\t\tG\t%d\t"Paciente No.%d ~ Pagina 4"\t1\t" Abaixo voce podera' visualizar uma tabela na qual podera' indicar, atraves de um valor de 1 a 6, tres dimensoes de qualidade da explicacao fornecida pela IA. <br /> Para simplificar, sao relatados a descricao, o ECG, o diagnostico e a explicacao fornecida nos quadros abaixo.<br />"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (4*i+4, 4*i+4,i))		
				f.write("""%d\t\tQ\tX\tdesc4%d\t1\t"<span style=""font-family:Georgia,serif;""><span style=""color: rgb(105, 155, 103); font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;"">Descricao do paciente: <br/>%s</span></span>"\t\tpt\t\tN\tN\t\t0\n""" % (100*i+17,i,case_description))								
				f.write("""%d\t\tQ\tX\timage%d4\t1\t"<style>.magnifier { overflow: hidden; position: relative; }  .maglens { position: absolute; overflow: hidden; width: 200px; height: 200px; border: 2px solid #149414; box-shadow: inset 0 0 20px rgba(0,0,0,.5); cursor: none; }  .magsmall { position: absolute; border-style: none }  .maglarge { position: absolute; border-style: none } </style> <script type=""text/javascript"" src=""https://users.cs.northwestern.edu/~riesbeck/demo/magnifier_v3/magnifier.js""></script> <div class=""magnifier"" style=""height: 750px; width: 1100px; margin: 20px;""> <div class=""maglens""> <img src=""%s"" class=""maglarge"" alt=""ECG"" ismap=""ismap"" usemap=""#kaart"" style=""height: 1400px; width: 2100px;"" /> </div> </div>"\t\tpt\t\tN\tN\t\t0\n""" % (100*i+18,i,case_image_url))								
				f.write("""%d\t\tQ\tX\tdiag3%d\t1\t"<span style=""font-family:Georgia,serif;""><span style=""color: rgb(105, 155, 103); font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;"">Diagnostico sugerido pela AI: <br/>%s</span></span>"\t\tpt\t\tN\tN\t\t0\n""" % (100*i+19,i,case_diagnosis))
				f.write("""%d\t\tQ\tX\texpl2%d\t1\t"<span style=""font-family:Georgia,serif;""><span style=""color: rgb(105, 155, 103); font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: pre-wrap; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;"">Explicacao textual fornecida por inteligencia artificial: <br/>%s</span></span>"\t\tpt\t\tN\tN\t\t0\n""" % (100*i+20,i,case_explanation))								
				f.write("""%d\t\tQ\tF\tconf%d\t1\t"Preencha a seguinte tabela, onde 1 = 'Nem um pouco' e 6 = 'Totalmente'. Os valores devem ser atribuidos a cada dimensao da qualidade com base na explicacao fornecida pela IA:"\t\tpt\t\tN\tN\t\t0\n""" % (100*i+21,i))
				f.write("""%d\t\tSQ\t\tappro%d\t1\t"Adequacao"\t\tpt\t\tN\t\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\n""" % (100*i+22,i))
				f.write("""%d\t\tSQ\t\tcompr%d\t1\t"Compreensibilidade"\t\tpt\t\tN\t\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\n""" % (100*i+23,i))
				f.write("""%d\t\tSQ\t\tutili%d\t1\t"Utilitario"\t\tpt\t\tN\t\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\n""" % (100*i+24,i))
				f.write("""%d\t\tA\t0\t1\t\t"1"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (100*i+21))
				f.write("""%d\t\tA\t0\t2\t\t"2"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (100*i+21))
				f.write("""%d\t\tA\t0\t3\t\t"3"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (100*i+21))
				f.write("""%d\t\tA\t0\t4\t\t"4"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (100*i+21))
				f.write("""%d\t\tA\t0\t5\t\t"5"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (100*i+21))
				f.write("""%d\t\tA\t0\t6\t\t"6"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (100*i+21))
			line_count += 1
		f.write("""%d\t\tG\t%d\t"Voce completou a parte relativa aos ECGs, propomos novamente a pergunta colocada no inicio da invest"\t1\t"Abaixo voce podera' visualizar uma tabela para indicar, usando um valor de 1 a 6 , o seu nivel de confianca na leitura automatizada. Voce mudou de ideia apos o questionario? "\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (4,4))		
		f.write("""%d\t\tQ\tF\tdom2\t1\t"Preencha a seguinte tabela, onde 1 = 'Nem um pouco' e 6 = 'Totalmente'. "\t\tpt\t\tN\tN\t\t0\n""" % (95))
		f.write("""%d\t\tSQ\t\tfid2\t1\t"Confianca na leitura automatizada:"\t\tpt\t\tN\t\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1\n""" % (96))
		f.write("""%d\t\tA\t0\t1\t\t"1"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (95))
		f.write("""%d\t\tA\t0\t2\t\t"2"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (95))
		f.write("""%d\t\tA\t0\t3\t\t"3"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (95))
		f.write("""%d\t\tA\t0\t4\t\t"4"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (95))
		f.write("""%d\t\tA\t0\t5\t\t"5"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (95))
		f.write("""%d\t\tA\t0\t6\t\t"6"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t0\n""" % (95))		
		f.write("""%d\t%d\tAS\tT\t"Parabens, voce completou o questionario! Feedback abaixo:"\t\t"<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>Ele confirmou seu diagnostico ou produziu outro em\t</var></p> 
<p id=""demo1"" style=""display:inline; font-size:18px; color: RGB(89,121,91);""><var></var></p>

<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var> casos.</var></p>
<script>
var div = parseInt({TOTAL}/100);
document.getElementById(""demo1"").innerHTML = div;
</script>
<br/>
<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>Ele selecionou o diagnostico produzido pela AI em\t</var></p>

<p id=""demo2"" style=""display:inline; font-size:18px; color: RGB(89,121,91);""><var></var></p>

<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var> casos dos quais:</var></p>
<script>
var div = 20 - parseInt({TOTAL}/100);
document.getElementById(""demo2"").innerHTML = div;
</script>
<br/>
<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>- Ele escolheu um diagnostico correto em\t</var></p>

<p id=""demo3"" style=""display:inline; font-size:18px; color: RGB(89,121,91);""><var></var></p>

<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>%% de casos.</var></p>
<script>
var div = (({TOTAL}%%100)/(20 - parseInt({TOTAL}/100))*100).toFixed(2);
document.getElementById(""demo3"").innerHTML = div;
</script>
<br/>
<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>- Ele escolheu um diagnostico errado em\t</var></p>

<p id=""demo4"" style=""display:inline; font-size:18px; color: RGB(89,121,91);""><var></var></p>

<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>%% de casos.</var></p>
<script>
var div = ((20-parseInt({TOTAL}/100)-({TOTAL}%%100))/(20 - parseInt({TOTAL}/100))*100).toFixed(2);
document.getElementById(""demo4"").innerHTML = div;
</script>"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1999\t\t\t\t\t\t100\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (90, 5))				
		f.write("""%d\t%d\tAS\tT\t"Parabens, voce completou o questionario! Feedback abaixo:"		"<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>Ele confirmou seu diagnostico ou produziu outro em\t</var></p>

<p id=""demo1"" style=""display:inline; color: RGB(89,121,91); font-size:18px;""><var></var></p>

<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var> casos.</var></p>
<script>
var div = ({TOTAL}/100);
document.getElementById(""demo1"").innerHTML = div;
</script>
<br/>
<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>Ele selecionou o diagnostico produzido pela AI em\t</var></p>

<p id=""demo2"" style=""display:inline; color: RGB(89,121,91); font-size:18px;""><var></var></p>

<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var> casos.</var></p>
<script>
var div = 20-({TOTAL}/100);
document.getElementById(""demo2"").innerHTML = div;
</script>"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2000\t\t\t\t\t\t2000\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (91, 5))				
		f.write("""%d\t%d\tAS\tT\t"Parabens, voce completou o questionario! Feedback abaixo:"		"<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>Ele confirmou seu diagnostico ou produziu outro em 0 casos.</var></p>
<br/>
<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>Ele selecionou o diagnostico produzido pela AI em 20 casos, dos quais:</var></p>
<br/>

<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>- Ele escolheu um diagnostico correto em\t</var></p>

<p id=""demo1"" style=""display:inline; font-size:18px; color: RGB(89,121,91);""><var></var></p>

<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>%% de casos.</var></p>
<script>
var div = ({TOTAL}/20*100).toFixed(2);
document.getElementById(""demo1"").innerHTML = div;
</script>
<br/>
<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>- Ele escolheu um diagnostico errado em\t</var></p>

<p id=""demo2"" style=""display:inline; color: RGB(89,121,91); font-size:18px;""><var></var></p>

<p style=""display:inline; color: RGB(89,121,91); font-family:verdana; font-size:18px;""><var>%% de casos.</var></p>
<script>
var div = ((20-{TOTAL})/20*100).toFixed(2);
document.getElementById(""demo2"").innerHTML = div;
</script>"\t\tpt\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t99\t\t\t\t\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n""" % (92, 5))				
			
															
	f.close()
if __name__=="__main__":
	main()