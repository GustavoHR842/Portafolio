#Gustavo Angel Hidalgo Romero - A00835599

#Sebastian Rosas Corral – A00835870

#declaramos los colores
import colorama
from colorama import Fore
from colorama import Style
#programa para el reto 6to de primaria

#bienvenida
print('Bienvenid@ al programa para estudiar algunas materias de 6to de primaria.')

#inicializar variables, listas y diccionarios
alumnosEsp={}
alumnosMate={}
alumnosCiencias={}
continuar='si'  




while continuar in['Si','si','s','SI','sI']:
    #inicializar la lista de nuevos nombres
    nombres= []
    nomAgregar=input('Cual es tu nombre? ')
    nombres.append(nomAgregar)
  #Que materia estudiar
    print("Que materia te gustaría estudiar?")
    R1=input('a. Español, b. Matemáticas, c. Ciencias---> ')
  #seleccion de materia y su contenido
    if R1 =='a':
        print('Este es el apartado de Español')
        print('Que tema te gustaría estudiar?')
        temasEsp=['1. Lectura Comprensiva','2. Practicar teoría']
        print(temasEsp)
        RespEsp=input()
        if RespEsp=='1':
            ResutaldolecturaEsp = 0
            colorama.init()
            print(Fore.RED + Style.BRIGHT + "'Lee la siguiente lectura y responde las preguntas.'" + Style.RESET_ALL)
                    #Pregunta 1
            colorama.init()
            print(Fore.BLUE + Style.BRIGHT + "¿Se deben dejar tareas escolares?" + Style.RESET_ALL)
            print ('Salvador Guerrero (moderador): Bienvenidos a este espacio radiofónico donde abordaremos el tema de las tareas escolares. Saludemos a Marisol Luna, alumna de primaria; a Gerardo Navarrete, profesor de sexto grado; y a Israel Caballero, padre de familia. Bien, la pregunta con la que comienza el debate es: ¿debe haber o no tareas escolares?')
            print('Marisol Luna (alumna): Yo no estoy de acuerdo en que haya tareas escolares, porque cuando llegamos a casa tenemos muchas cosas que hacer como ayudar en las labores del hogar y cuidar a nuestros hermanitos. Ya tenemos suficiente con todo lo que hacemos en la escuela. ')
            print('Gerardo Navarrete (maestro): Considero que las tareas son útiles porque los tiempos de la escuela no son suficientes, siempre hay contratiempos y no podemos abordar todos los temas. Además, es una oportunidad para que los niños pongan en práctica lo que aprendieron en clase y se relacionen con sus padres.')
            print('Israel Caballero (padre de familia): Para los padres de familia es complicado estar al pendiente de las tareas. Uno viene cansado del trabajo, pero es importante supervisar las actividades que solicita la escuela, el problema es que son demasiadas y en algunos casos aburridas.')
            print('Salvador Guerrero (moderador): En términos internacionales hay diferencias entre el tiempo y tipo de tareas que se solicitan. Por ejemplo, en Francia desde 1956 no se dejan tareas escolares y en Bélgica desde 2001 se regula el tipo de tareas que se dejan, las cuales no deben exceder los 30 minutos diarios en el caso de primaria. En contraste, en México el tiempo para tareas es de una hora y media al día aproximadamente. ')
            print('Gerardo Navarrete (maestro): Es cierto que los niños tienen muchas cosas que hacer en casa, pero el problema no son las tareas, sino el tipo de tareas que debemos plantear a los alumnos y el uso educativo que se haga de ellas. Hay tareas que son de reflexión y no quitan tiempo a otras actividades. Por ejemplo, el otro día un maestro me dijo que solicitó a sus alumnos pensar en una idea que ayude a cambiar el mundo y ponerla en práctica. Eso me pareció muy bien.')
            print('Israel Caballero (padre de familia): Estoy de acuerdo con ese tipo de tareas; además, al jugar, los niños también aprenden sobre las reglas, la convivencia o cómo llegar a acuerdos. Esa tarea que mencionó el profesor me parece adecuada para que la hagan en familia.')
            print('Salvador Guerrero (moderador): Entonces, coincidimos en este debate en que las tareas escolares son benéficas siempre y cuando se valore el tipo de actividades que se solicitan, y se garantice que el tiempo destinado a las tareas no limite la participación de los niños y niñas en otras cosas que estimulan su desarrollo.')
            print(Fore.BLUE + Style.BRIGHT + "¿1. Cuál es la conclusión del debate?" + Style.RESET_ALL)
            print('A)Los maestros deben evitar dejar tareas escolares porque los niños tienen muchas cosas que hacer en el hogar.')
            print('B)Las tareas escolares son útiles porque los tiempos de la escuela no son suficientes para ver todos los temas.')
            print('C)Los niños tienen el derecho a jugar porque con ello aprenden, se divierten y reflexionan muchas cosas.')
            print('D)Las tareas escolares deben ser menos, más motivantes y propiciar la reflexión de los alumnos sobre su entorno.')
            RespEsp1=input()
            if RespEsp1 == 'D':
              print ('Respuesta Correcta')
              ResutaldolecturaEsp = ResutaldolecturaEsp + 1
            else:
              print('Respuesta Incorrecta')
              #Pregunta 2
            print(Fore.BLUE + Style.BRIGHT + "¿2. Qué concluyes a partir de las intervenciones de Marisol Luna e Israel Caballero en los fragmentos 2 y 4?" + Style.RESET_ALL)
            print('A)Es mejor dejar pocas tareas escolares a los niños porque tienen múltiples actividades que hacer y los padres de familia no tienen tiempo de revisarlas.')
            print('B)Los niños tienen muchas cosas que hacer como ayudar en las labores de la casa, cuidar a los hermanos y jugar.')
            print('C)Las tareas escolares son importantes porque los niños pueden aprender más, como en el caso de Francia.')
            print('D)Se deben dejar más tareas escolares en casa porque los niños pueden ocupar su tiempo libre y aprender; además, los padres de familia conviven más con ellos.')
            RespEsp1=input()
            if RespEsp1 == 'A':
              print ('Respuesta Correcta')
              ResutaldolecturaEsp = ResutaldolecturaEsp + 1
            else:
              print('Respuesta Incorrecta')
                         #Pregunta 3 
            print(Fore.BLUE + Style.BRIGHT + "3. En el fragmento 2 Marisol Luna expresó: “Yo no estoy de acuerdo en que haya tareas escolares porque cuando llegamos a casa tenemos muchas cosas que hacer”. ¿En qué fragmento se expresa una crítica constructiva a este comentario?" + Style.RESET_ALL)
            print('A) 1')
            print('B) 4')
            print('C) 6')
            print('D) 5')
            RespEsp1=input()
            if RespEsp1 == 'C':
              print ('Respuesta Correcta')
              ResutaldolecturaEsp = ResutaldolecturaEsp + 1
            else:
                print ('Respuesta Incorrecta')
            colorama.init()
            print(Fore.RED + Style.BRIGHT + "'Lee la siguiente lectura y responde las preguntas.'" + Style.RESET_ALL)
            colorama.init()
            print(Fore.BLUE + Style.BRIGHT + "La escuela de los espectros" + Style.RESET_ALL)
            print ('1. La mañana era soleada y las risas de los jovencitos inundaban el ambiente mientras iban entrando a la nueva secundaria. Ninguno se imaginaba que en los lejanos terrenos, luminosos y arbolados, en donde ahora estaba la flamante escuela de dos pisos antes había un antiguo cementerio. Cuando los constructores excavaban para poner los cimientos de la escuela, retiraban en secreto ataúdes, esqueletos y calaveras en camiones de volteo. Mientras tanto, algunos ancianos, mirando el avance de las obras, decían: —Esos muertitos van a reclamar su tierrita. Ya verán. ')
            print('2. El primer susto lo enfrentaron Juan y Azucena, padres de Laura. La joven mamá vio extrañada a un pequeñito que estaba solo y jugaba en la banqueta con unos caballitos de madera. Su ropa era muy antigua y calzaba huaraches. El niño levantó el rostro y le sonrió. Después, cuando le dijo a su marido, el pequeño ya no estaba. Ella se puso un poco nerviosa. ')
            print('3. Luego en casa, al arropar a Laura, le pareció ver por la ventana a un grupo de personas en harapos al otro lado de la calle, muy cerca de la escuela. Sintió que la sangre se le congelaba, tenía miedo y temblaba. Apagó la luz para evitar que la vieran y poder observar mejor. De repente, casi se desmayó cuando notó que los extraños visitantes, entre los que había niños pequeños, tenían huecos en lugar de nariz y ojos. ')
            print('4. Pasaron los días y Laura ya estaba en su nueva secundaria. A pesar de su timidez, no tardó en hacer amigas y en el primer recreo les contó lo que su madre había visto aquella noche. Poco después, Laura pidió permiso al profesor para ir al baño. El lugar estaba completamente solitario. Se metió en el último sanitario y cerró la puerta. De pronto sintió un escalofrío… Por debajo de la puerta vio un par de pies cubiertos de barro metidos en unos huaraches destruidos por el tiempo. Respiró profundamente y abrió con temor la puerta. Entonces se encontró frente a frente con un niño de tez muy pálida que vestía ropa extraña. No tenía ojos y de su boca salió un aire pestilente como el de una sepultura. —¡Vete de aquí!— le dijo el niño con voz ronca. ')
            print('5. Laura salió del baño corriendo. Cuando regresó a su salón temblaba de pánico y no podía hablar. Pasaron muchos meses antes de que pronunciara una sola palabra y les contara lo sucedido a familiares y amigos. Desde aquel día nadie en la escuela se atreve a ir a los baños sin compañía.')
           #Pregunta 4
            print ('4. En el párrafo 1, ¿para qué se describe el lugar donde se construyó la secundaria?')
            print('A)Para informar al lector las razones por las que los ancianos creen que los muertos pueden aparecerse.')
            print('B)Para explicar al lector las razones por las que se debe evitar construir secundarias sobre un cementerio.')
            print('C)Para dar a conocer al lector el lugar preciso donde vivían Laura, su madre Azucena y su padre Juan')
            print('D)Para dar a conocer al lector el tenebroso origen de la zona en la que fue construida la secundaria.')
            RespEsp1=input()
            if RespEsp1 == 'C':
              print ('Respuesta Correcta')
              ResutaldolecturaEsp = ResutaldolecturaEsp + 1
            else:
              print('Respuesta Incorrecta')
            #Pregunta 5
            print(Fore.BLUE + Style.BRIGHT + "¿5. Cuál de los siguientes enunciados que aparecen en el texto utiliza una comparación para describir un objeto, persona o evento?" + Style.RESET_ALL)
            print('A)“Luego en casa, al arropar a Laura, le pareció ver por la ventana a un grupo de personas en harapos al otro lado de la calle”.')
            print('B)“Casi se desmayó cuando notó que los extraños visitantes, entre los que había niños pequeños, tenían huecos en lugar de nariz y ojos”.')
            print('C)“Se encontró frente a frente con un niño de tez muy pálida que vestía ropa extraña. No tenía ojos y de su boca salió un aire pestilente como el de una sepultura”.')
            print('D)“Ninguno se imaginaba que en los lejanos terrenos, luminosos y arbolados, en donde ahora estaba la flamante escuela de dos pisos antes había un antiguo cementerio”.')
            RespEsp1=input()
            if RespEsp1 == 'B':
              print ('Respuesta Correcta')
              ResutaldolecturaEsp = ResutaldolecturaEsp + 1
            else:
              print('Respuesta Incorrecta')
              #Pregunta 6
            print(Fore.BLUE + Style.BRIGHT + "¿6. En cuál de los siguientes párrafos del cuento se genera mayor suspenso y tensión?" + Style.RESET_ALL)
            print('A)1')
            print('B)2')
            print('C)3')
            print('D)5')
            RespEsp1=input()
            if RespEsp1 == 'D':
              print ('Respuesta Correcta')
              ResutaldolecturaEsp = ResutaldolecturaEsp + 1
            else:
              print('Respuesta Incorrecta')
              #Pregunta 7
            print(Fore.BLUE + Style.BRIGHT + "7. Elige la opción que muestra la transformación del enunciado en negritas del párrafo 2 a obra de teatro" + Style.RESET_ALL)
            print('A) —Juan, ¿por qué ese pequeño está solo en la calle? Puede correr algún peligro, ¿a qué juega?')
            print('B) Azucena (asustada, voltea a ver a Juan): ¡Mira! ¡Ese pequeño está triste porque no encuentra a su mamá!')
            print('C) —¿Será que ese pequeño es el hijo de la conserje de la secundaria? ¿Por qué lo deja solo en la calle? ¡Qué cosa, Juan! ')
            print('D) Azucena (sorprendida, voltea a ver a Juan): ¡Mira a ese pequeño, está jugando solo en la calle! ¿Quién será?')
            RespEsp1=input()
            if RespEsp1 == 'B':
              print ('Respuesta Correcta')
              ResutaldolecturaEsp = ResutaldolecturaEsp + 1
            else:
              print('Respuesta Incorrecta')
            colorama.init()
            print(Fore.RED + Style.BRIGHT + "'Lee la siguiente lectura y responde las preguntas.'" + Style.RESET_ALL)
            colorama.init()
            print(Fore.BLUE + Style.BRIGHT + "La compra del asno" + Style.RESET_ALL)
            print ('Había una vez un zorro muy astuto que era dueño de un asno. El zorro solía pasear a su asno por la ciudad, mostrándolo hermosamente adornado. Entre todos los lujos que cargaba el burro se podían ver las más hermosas sedas, collares dorados y un gran sombrero de terciopelo, esponjoso y suave. Un día, un cerdo de la ciudad se acercó al zorro:')
            print('— ¡Qué hermoso asno llevas ahí! — le dijo el cerdo — ¿Has pensado en venderlo? — Puedo venderte a mi asno — contestó el zorro —, pero es una compra que puede dejarte en la calle. Como podrás ver, es un asno en excelentes condiciones.')
            print('El cerdo decidió comprar al asno y se encaminó a su hogar. Cuando llegó a su casa, se dedicó a presumirles a sus vecinos su gran adquisición. Los vecinos se quedaron asombrados. Solamente uno de ellos se mostró dudoso y dijo:')
            print('— ¡Qué interesante asno, vecino! Vamos a quitarle todas las telas para verlo mejor.')
            print('Cuando retiraron los adornos, la sorpresa para todos fue enorme. El asno tenía heridas en su lomo, estaba descuidado e inclusive tenía un viejo tumor. El cerdo, arrepentido de su compra, pensó: “Ahora me doy cuenta de que el asno soy yo”.')
              #Pregunta 8
            print(Fore.BLUE + Style.BRIGHT + "¿8. Qué semejanza hay entre la moraleja de la fábula y el refrán “No todo lo que brilla es oro”?" + Style.RESET_ALL)
            print('A) Cuando un burro es pequeño, parece nuevo.')
            print('B)Los zorros siempre buscan traicionar a los demás.')
            print('C) Es mejor tener algo seguro que muchas cosas inciertas.')
            print('D) No debes dejarte engañar por las apariencias.')
            RespEsp1=input()
            if RespEsp1 == 'B':
              print ('Respuesta Correcta')
              ResutaldolecturaEsp = ResutaldolecturaEsp + 1
              
            else:
              print('Respuesta Incorrecta')
              #Pregunta 9
            print(Fore.BLUE + Style.BRIGHT + "¿9. Qué refrán puede sustituir la moraleja de esta fábula?" + Style.RESET_ALL)
            print('A) Quitarle al rico y darle al pobre')
            print('B)El hábito no hace al monje. ')
            print('C) Lo que se siembra se cosecha. ')
            print('D) El miedo no anda en burro.')
            RespEsp1=input()
            if RespEsp1 == 'C':
              print ('Respuesta Correcta')
              ResutaldolecturaEsp = ResutaldolecturaEsp + 1
            else:
              print('Respuesta Incorrecta')
              #Pregunta 10
            print(Fore.BLUE + Style.BRIGHT + "¿10. Qué intención tuvo el autor cuando escribió este texto?" + Style.RESET_ALL)
            print('A) Persuadir al lector para que aprenda que la riqueza es lo más importante.')
            print('B) Informar al lector acerca de la habilidad de los zorros para engañar a otros animales. ')
            print('C) Guiar al lector para que sepa cómo adquirir animales que tienen mucho valor.')
            print('D) Hacer reflexionar al lector sobre la importancia de ver la verdadera esencia de las cosas.')
            RespEsp1=input()
            if RespEsp1 == 'D':
              print ('Respuesta Correcta')
              ResutaldolecturaEsp = ResutaldolecturaEsp + 1
            else:
              print('Respuesta Incorrecta')
            print ("Tu calificacion en lectura de comprension es la siguiente: " + str(ResutaldolecturaEsp))
            alumnosEsp[nomAgregar]=str(ResutaldolecturaEsp)
            print(alumnosEsp)
        if RespEsp=='2':
            ResutaldoteoriaEsp=0
          #Pregunta 1
            print(Fore.BLUE + Style.BRIGHT + "¿1. Cómo se llama la lista de preguntas que se deben formular para saber más sobre la vida de una persona?" + Style.RESET_ALL)
            print('A) Cuestionario ')
            print('B) Examen ')
            print('C) Entrevista')
            print('D) Interrogatorio')
            RespEsp1=input()
            if RespEsp1 == 'A':
              print ('Respuesta Correcta')
              ResutaldoteoriaEsp= ResutaldoteoriaEsp + 1
            else:
              print('Respuesta Incorrecta')
          #Pregunta 2
            print(Fore.BLUE + Style.BRIGHT + "2. Tipo de texto donde otra persona cuenta los sucesos de la vida de alguien." + Style.RESET_ALL)
            print('A) Autobiografia')
            print('B) Radiografia')
            print('C) Biografia')
            print('D) Narracion')
            RespEsp1=input()
            if RespEsp1 == 'C':
              print ('Respuesta Correcta')
              ResutaldoteoriaEsp= ResutaldoteoriaEsp + 1
            else:
              print('Respuesta Incorrecta')
          #Pregunta 3
            print(Fore.BLUE + Style.BRIGHT + "3. Es una narración breve que consiste en el relato de un suceso de pura invención." + Style.RESET_ALL)
            print('A) Cuento')
            print('B) Leyenda')
            print('C) Mito')
            print('D) Refran ')
            RespEsp1=input()
            if RespEsp1 == 'A':
              print ('Respuesta Correcta')
              ResutaldoteoriaEsp= ResutaldoteoriaEsp + 1
            else:
              print('Respuesta Incorrecta')
          #Pregunta 4
            print(Fore.BLUE + Style.BRIGHT + "4. Elige la frase escrita con adjetivos: " + Style.RESET_ALL)
            print('A) La casa en el árbol. ')
            print('B) La casona del árbol.')
            print('C) La tenebrosa casa del gran árbol.')
            print('D) La casita en el arbolito.')
            RespEsp1=input()
            if RespEsp1 == 'C':
              print ('Respuesta Correcta')
              ResutaldoteoriaEsp= ResutaldoteoriaEsp + 1
            else:
              print('Respuesta Incorrecta')
              #Pregunta 5
            print(Fore.BLUE + Style.BRIGHT + "5. ¿Cómo se le llama al personaje principal de la acción en una obra literaria o cinematográfica? " + Style.RESET_ALL)
            print('A) Protagonista ')
            print('B) Antagonista.')
            print('C) Extra')
            print('D) Personaje secundario')
            RespEsp1=input()
            if RespEsp1 == 'A':
              print ('Respuesta Correcta')
              ResutaldoteoriaEsp= ResutaldoteoriaEsp + 1
            else:
              print('Respuesta Incorrecta')
              #Pregunta 6
            print(Fore.BLUE + Style.BRIGHT + "6. ¿Cómo se le llama al personaje que se enfrenta con el personaje principal en una obra literaria o cinematográfica? " + Style.RESET_ALL)
            print('A) Protagonista ')
            print('B) Antagonista.')
            print('C) Extra')
            print('D) Personaje secundario')
            RespEsp1=input()
            if RespEsp1 == 'B':
              print ('Respuesta Correcta')
              ResutaldoteoriaEsp= ResutaldoteoriaEsp + 1
            else:
              print('Respuesta Incorrecta')
              #Pregunta 7
            print(Fore.BLUE + Style.BRIGHT + "7. Los siguientes son verbos en infinitivo, excepto:" + Style.RESET_ALL)
            print('A) Caminar')
            print('B) Correr')
            print('C) Dormir')
            print('D) Ayer')
            RespEsp1=input()
            if RespEsp1 == 'D':
              print ('Respuesta Correcta')
              ResutaldoteoriaEsp= ResutaldoteoriaEsp + 1
            else:
              print('Respuesta Incorrecta')
              #Pregunta 8
            print(Fore.BLUE + Style.BRIGHT + "8. Es un enunciado que podría ser parte de un instructivo:" + Style.RESET_ALL)
            print('A) Come frutas y verduras')
            print('B) Lanzar las fichas dentro del círculo')
            print('C) Considere saludar a sus amigos')
            print('D) Hay animales que se alimentan de pasto')
            RespEsp1=input()
            if RespEsp1 == 'B':
              print ('Respuesta Correcta')
              ResutaldoteoriaEsp= ResutaldoteoriaEsp + 1
            else:
              print('Respuesta Incorrecta')
                   #Pregunta 9
            print(Fore.BLUE + Style.BRIGHT + "9. Los adjetivos y adverbios sirven en los instructivos para:" + Style.RESET_ALL)
            print('A) Que se vea bonito el instructivo')
            print('B) Precisar las indicaciones')
            print('C) Confundir las reglas')
            print('D) Evitar el uso de imágenes')
            RespEsp1=input()
            if RespEsp1 == 'B':
              print ('Respuesta Correcta')
              ResutaldoteoriaEsp= ResutaldoteoriaEsp + 1
            else:
              print('Respuesta Incorrecta')
              #Pregunta 10
            print(Fore.BLUE + Style.BRIGHT + "10. Elige el adverbio que sea adecuado a la siguiente frase: _____________gana el que tenga más fichas" + Style.RESET_ALL)
            print('A) Finalmente')
            print('B) Despacio')
            print('C) Lentamente')
            print('D)  Alto')
            RespEsp1=input()
            if RespEsp1 == 'B':
              print ('Respuesta Correcta')
              ResutaldoteoriaEsp = ResutaldoteoriaEsp + 1
            else:
              print('Respuesta Incorrecta')
            print ("Tu calificacion en español  teorico es la siguiente: " + str(ResutaldoteoriaEsp))
            alumnosEsp[nomAgregar]=str(ResutaldoteoriaEsp)
            print(alumnosEsp)
    elif R1=='b':
        ResultadoMate = 0
        #Sección de Matemáticas
      
        print('Este es el apartado de Matemáticas')
        print('')
        print('Porcentajes')
        #Pregunta 1
        print('1. Cual es el 10% de 80? a)6  b)8  c)20 ')
        RespMate1=input()
        if RespMate1=='B':
          print('Correcta!!!')
          ResultadoMate = ResultadoMate + 1
        else:
          print('Incorrecta')

        #Pregunta 2
        print('2. Cual es el 40% de 140? a)56  b)55  c)40 ')
        RespMate2=input()
        if RespMate2=='A':
          print('Correcta!!!')
          ResultadoMate = ResultadoMate + 1
        else:
          print('Incorrecta')
        #Pregunta 3
        print('')  
        print('Fracciones')  
        print('3. Cual es el resultado de la siguiente suma: 1/2 + 2/4? a) 3/2  b)5/2  c)1')
        RespMate3= input()
        if RespMate3=='C':
          print('Correcta!!!')
          ResultadoMate = ResultadoMate + 1
        else:
          print('Incorrecta')
        #Pregunta 4
        print('4. Cual es el resultado de la siguiente resta: 4/6 - 1/3? a)2/6  b)1/3  c)1/2')
        RespMate4=input()
        if RespMate4=='A':
          print('Correcta!!!')
          ResultadoMate = ResultadoMate + 1
        else:
          print('Incorrecta')
        #Pregunta 5
        print('')  
        print('Mediana_Moda')  
        print('5. Cual es la mediana de la siguiente lista: [6 3 5 2 1]? a)3  b)6  c)5')
        RespMate5=input()
        if RespMate5=='A':
          print('Correcta!!!')
          ResultadoMate = ResultadoMate + 1
        else:
          print('Incorrecta')
        #Pregunta 6
        print('6. Cual es la moda de la siguiente lista: [4 1 8 2 4 1 4 6]? a)1  b)6  c)4')
        RespMate6=input()  
        if RespMate6=='C':
          print('Correcta!!!')
          ResultadoMate = ResultadoMate + 1
        else:
          print('Incorrecta')
        #Pregunta7
        print('')
        print('Sucesiones')
        print('7. Cual sería el siguiente número en esta sucesión: 2 4 8 16...? a)24  b)32 c)36')
        RespMate7=input()
        if RespMate7=='B':
          print('Correcta!!!')
          ResultadoMate = ResultadoMate + 1
        else:
          print('Incorrecta')
        #Pregunta 8
        print('8. Cual sería el siguiente numero en esta sucesión: 20 15 10...? a)6  b)4  c)5')
        RespMate8=input()
        if RespMate8=='C':
          print('Correcta!!!')
          ResultadoMate = ResultadoMate + 1
        else:
          print('Incorrecta')
        #Pregunta 9
        print('')
        print('Circunferencia')    
        print('9. Sabiendo que π(pi) es igual a: 3.1416, cual sería la circunferencia de un circulo cuyo diametro es de 6cm? a)18.85cm  b)20.6cm  c)12cm')
        RespMate9=input()
        if RespMate9=='A':
          print('Correcta!!!')
          ResultadoMate = ResultadoMate + 1
        else:
          print('Incorrecta')
        #pregunta 10
        print('10. Cual sería la circunferencia de un circulo cuyo diametro es de 10m? a)28.2m  b)31.42m  c)32m')
        RespMate10=input()
        if RespMate10=='B':
          print('Correcta!!!')
          ResultadoMate = ResultadoMate + 1
        else:
          print('Incorrecta')
        print ("Tu calificacion matematicas es la siguiente: " + str(ResultadoMate))
        alumnosMate[nomAgregar]=str(ResultadoMate)
        print(alumnosMate)
        
    else:
      #Sección de Ciencias
      ResultadoCiencias = 0 
      print('')
      print('Este es el apartado de Ciencias')
      print('')
      #Pregunta 1
      print('1. Cuales son los movimientos que se controlan de manera consciente? a)Involuntarios  b)Rotacional  c)Voluntarios')
      RespCiencias1=input()
      if RespCiencias1=='C':
        print('Correcta!!!')
        ResultadoCiencias = ResultadoCiencias + 1
      else:
        print('Incorrecta')
        #Pregunta 2
      print('2. Cual es el órgano mas grande del encefalo el cual esta dividido en dos hemisferios? a)Estómago  b)Cerebro  c)Pulmones')
      RespCiencias2=input()
      if RespCiencias2=='B':
        print('Correcta!!!')
        ResultadoCiencias = ResultadoCiencias + 1
      else:
        print('Incorrecta')
         #Pregunta 3
      print('3. Cual es uno de los principales mecanismos de defensa con los que contamos? a)Defensa Personal  b)Percepeción Auditiva  c)Acto Reflejo')
      RespCiencias3=input()
      if RespCiencias3=='C':
        print('Correcta!!!')
        ResultadoCiencias = ResultadoCiencias + 1
      else:
        print('Incorrecta')
         #Pregunta 4
      print('4. Cuantos huesos tiene el esqueleto humano? a)206 b) 350 c)236 ')
      RespCiencias4=input()
      if  RespCiencias4=='A':
        print('Correcta!!!')
        ResultadoCiencias = ResultadoCiencias + 1
      else:
        print('Incorrecta')
         #Pregunta 5
      print('5. En donde se concentran todos los anticuerpos que posee la madre? a)En la boca b)En la leche materna c)En la saliva ')
      RespCiencias5=input()
      if RespCiencias5=='B':
        print('Correcta!!!')
        ResultadoCiencias = ResultadoCiencias + 1
      else:
        print('Incorrecta')
         #Pregunta 6
      print('6. Cuales son los alimentos que te bridna vitaminas y minerales? a)Leguminosas  b)Verduras y Frutas  c)Cereales')
      RespCiencias6=input()
      if RespCiencias6=='B':
        print('Correcta!!!')
        ResultadoCiencias = ResultadoCiencias + 1
      else:
        print('Incorrecta')
         #Pregunta 7
      print('7. Cual es uno de los recursos que más se utilizan para controlar enfermedades como tuberculosis, hepatitis,etc? a)Vacunación  b)Pastillas  c)Capsulas')
      RespCiencias7=input()
      if RespCiencias7=='A':
        print('Correcta!!!')
        ResultadoCiencias = ResultadoCiencias + 1
      else:
        print('Incorrecta')
         #Pregunta 8
      print('8. Cual es el proceso mediante el cual se forman las distintas capaz del suelo de la Tierra? a)Meteorización  b)Intemperización  c)Estratificación')
      RespCiencias8=input()
      if RespCiencias8=='C':
        print('Correcta!!!')
        ResultadoCiencias = ResultadoCiencias + 1
      else:
        print('Incorrecta')
         #Pregunta 9
      print('9. Cual es la propiedad de algunos materiales de recobrar su forma original después de que han sido deformados? a)Elasticidad  b)Permeabilidad  c)Dureza')
      RespCiencias9=input()
      if RespCiencias9=='A':
        print('Correcta!!!')
        ResultadoCiencias = ResultadoCiencias + 1
      else:
        print('Incorrecta')
         #Pregunta 10
      print('10. Cual es el tipo de lente el cual su centro es mas grueso que los bordes? a)Lentes convexos  b)Lentes gruesos  c)Lentes convergentes')
      RespCiencias10=input()
      if RespCiencias10=='C':
        print('Correcta!!!')
        ResultadoCiencias = ResultadoCiencias + 1
      else:
        print('Incorrecta')

      print ("Tu calificacion en ciencas es la siguiente: " + str(ResultadoCiencias))
      alumnosCiencias[nomAgregar]=str(ResultadoCiencias)
      print(alumnosCiencias)
      
    continuar= input('Deseas estudiar otra materia? Si/No: ')
    print('*********************************************************') 
    
print("Sigue estudiando, vas mejorando, ten un buen dia" )