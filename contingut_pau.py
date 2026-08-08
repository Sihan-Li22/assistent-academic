# contingut_pau.py
CRITERIS_AVALUACIO = """
RÚBRICA DE CORRECCIÓ OFICIAL PAU CASTELLÀ:

1. EN PREGUNTAS DE PRODUCCIÓN / REDACCIÓN (Valor total: 2 puntos):
   - Contenido y coherencia: 0,5p
   - Precisión léxica: 0,5p
   - Complejidad sintáctica y cohesión: 0,5p
   - Estructura del texto y párrafos: 0,5p
   - Extensión: Penalización de 0,25p si no se ajusta al límite de palabras requerido.

2. PENALIZACIÓN GLOBAL POR ERRADAS DE NORMATIVA (Descuento final):
   - Se restará EXACTAMENTE 0,1 puntos por cada falta de ortografía o de normativa gramatical (ejemplo: omitir la 'hache' en 'haber').
   - El máximo de penalización global por ortografía en todo el examen es de 2,0 puntos.
"""
# ==============================================================================
# BLOQUE 0: DATOS GENERALES Y ESTRUCTURA DE LA PRUEBA (Serie 1)
# ==============================================================================

DATOS_GENERALES = """
Generalitat de Catalunya
Consell Interuniversitari de Catalunya
Oficina d'Accés a la Universitat
Proves d'accés a la universitat
Lengua castellana y literatura
Serie 1 / Curs 2025
"""

ESTRUCTURA_PRUEBA = """
El examen consta de CUATRO partes obligatorias:
1. Comprensión lectora (2 puntos): debe responder a TODAS las cuestiones planteadas.
2. Expresión escrita (3 puntos): debe responder a TODAS las cuestiones planteadas.
3. Saber literario (2 puntos): debe responder a CUATRO de las cinco cuestiones planteadas. Si responde a más cuestiones de las indicadas, solo se tendrán en cuenta las cuatro primeras.
4. Reflexión lingüística (3 puntos): debe responder a TODAS las cuestiones del bloque 1 y a solo DOS de las tres cuestiones planteadas en el bloque 2. Si, en el bloque 2, responde a más cuestiones de las indicadas, solo se tendrán en cuenta las dos primeras.
"""


# ==============================================================================
# BLOQUE 1: COMPRENSIÓN LECTORA [2 puntos en total]
# ==============================================================================

TEXTO_COMPRENSION_LECTORA = """
Irene VALLEJO. «Quizás, quizás, quizás». El País [en línea] (28 julio 2024)

Somos seres opinadores y, en el frenesí de comentarlo todo, es fácil precipitarse por la rampa tramposa de la generalización apresurada. Las fotos veraniegas de las redes nos convencen de que todos los demás son más felices. La rabieta de un niño conduce a sermonear sobre los padres que ya no educan a sus hijos, y de ahí al declive de la familia hay un solo paso. Nada más tentador que convertir casos aislados en causa general. Este mundo de urgencias y apocalipsis otorga más credibilidad a las afirmaciones simplificadas, contundentes y sin fisuras, incluso vociferantes, como si fuesen prueba de conocimiento y capacidad de liderazgo, mientras ignora a quienes tienen el valor de compartir sus perplejidades. Olvidamos que, a veces, las cataratas de certezas brotan de los labios más intransigentes. [...]

Los filósofos escépticos de la antigua Grecia se empeñaron en combatir esas resbaladizas creencias. Invitaban a cultivar la duda, y defendían con valentía los matices y las ambigüedades. Por supuesto, animaban a actuar razonablemente, pero sin jactarse de tener la razón. Afirmar siempre con cautela. [...]

Cuando la realidad parece sumergirse en la niebla de la complejidad y la incertidumbre, resuenan con más fuerza las voces seguras de sí mismas, las más decididas, aquellas que se abren camino a través de la jungla del mundo acorazadas con ideas rotundas. Aplomo y férrea convicción son requisitos para imponerse, mientras, para muchos, el pensamiento que matiza y duda no sirve de guía para la comunidad. En una época que pide a gritos carácter emprendedor y liderazgos rotundos, las personas introvertidas y tímidas quedan expulsadas de la carrera del éxito social en la línea de salida. Si apuestas por la meditación y la mirada contemplativa, pareces un apocado aspirante al fracaso. Con la loable intención de ayudarnos a triunfar, nos aconsejan por doquier rapidez y contundencia: vendernos bien y pensar menos. Por el contrario, Sócrates y Pirrón dejaron un legado milenario un contundente éxito- al afirmar que sus únicas certidumbres eran el filo de la duda y el destello de la curiosidad. Les interesaba el diálogo, la conversación serena entre opiniones discrepantes, donde la contradicción, lejos de despertar desconfianza, actúa como motor de conocimiento y del deseo de aprender. Sócrates, que combatía la inercia del pensamiento y el poder casi invencible de los estereotipos, pensaba que los más graves errores no los cometen los ignorantes conscientes, sino los que creen saber. Quienes vociferan convencidos suelen mostrarse poco abiertos a reflexionar y ser flexibles. En tiempos de juicios y prejuicios acelerados, vuelve a ser terapéutica la prudencia de aquellos escépticos: solo dudando adquirimos ciertas verdades, algunas certezas. Tal vez.
"""

EXAMEN_COMPRENSION_LECTORA = """
1.1. ¿Qué enunciado, de los cuatro que se presentan a continuación, corresponde a una interpretación correcta del texto?
[0,5 puntos. Si la respuesta es errónea, se descontarán 0,15 puntos; si no responde a la pregunta, no se aplicará ningún descuento.]
a) Las afirmaciones contundentes son la prueba del conocimiento.
b) Los matices y las ambigüedades no son recomendables.
c) Hoy en día, si apuestas por la duda, estás condenado a fracasar.
d) Sócrates pensaba que los más graves errores los cometen los que saben.

1.2. Explique en un máximo de veinticinco palabras cuál es la idea principal del texto.
[0,5 puntos]

1.3. ¿Qué significa la expresión subrayada en el primer párrafo del texto «las cataratas de certezas brotan de los labios más intransigentes»? Responda en un máximo de veinticinco palabras.
[0,5 puntos]

1.4. Señale qué serie, de las cuatro que se proponen, es la única correcta para sustituir todas las palabras siguientes, subrayadas en el texto: resbaladizas, férrea, inercia, vociferan.
[0,5 puntos. Si la respuesta es errónea, se descontarán 0,15 puntos; si no responde a la pregunta, no se aplicará ningún descuento.]
a) insignificantes, empecinada, pereza, graznan
b) babosas, cerril, desidia, callan
c) groseras, dura, negligencia, vocean
d) problemáticas, firme, rutina, gritan
"""

SOLUCIONARIO_COMPRENSION_LECTORA = """
RESPUESTAS BLOQUE 1:
1.1: c) Hoy en día, si apuestas por la duda, estás condenado al fracaso. [0,5 puntos]
1.2: La duda y la reflexión crítica, defendidas por los filósofos escépticos, se oponen a la búsqueda de certezas superficiales e inmediatas. [0,5 puntos]
1.3: Los intransigentes expresan constantemente sus certezas. [0,5 puntos]
1.4: d) problemáticas, firme, rutina, gritan. [0,5 puntos]
"""

# ==============================================================================
# BLOQUE 2: EXPRESIÓN ESCRITA [3 puntos en total]
# ==============================================================================

EXAMEN_EXPRESION_ESCRITA = """
2.1. Redacte un texto expositivo sobre el concepto de incertidumbre que contenga al menos los tres siguientes recursos: definición, clasificación y ejemplificación. Utilice para ello entre cien y ciento cincuenta palabras. Previamente, complete el cuadro que aparece a continuación. Este cuadro puede servirle para redactar el texto.
[2 puntos]
Definición:
Clasificación:
Ejemplificación:

2.2. Complete las secuencias con la forma correcta de entre las dos que se proponen en cada caso.
[1 punto]
a) Mi amigo me recomendó que, __________ (sobre todo / sobretodo), evitara discutir con el profesor.
b) Todavía no sé __________ (porque / por qué) no quisiste comprarte el coche eléctrico.
c) ¿Sabes ya __________ (dónde / donde) tendrá lugar la asamblea?
d) No puedo entenderlo __________ (sino / si no) me lo explicas bien.
"""

SOLUCIONARIO_EXPRESION_ESCRITA = """
RESPUESTAS BLOQUE 2:
2.1: [2 puntos] Respuesta abierta.
Criterios de corrección para 2.1:
— La extensión debe ajustarse a lo pedido. Penalización de 0,25 puntos si el texto excede en un 10% o más las 150 palabras o si no alcanza las 100 palabras.
— Parámetros de puntuación: contenido, léxico, sintaxis y estructura del texto [0,5 puntos cada uno].
— Rellenar el recuadro previo NO comporta puntuación específica.

2.2: [1 punto]
a) Mi amigo me recomendó que, sobre todo, evitara discutir con el profesor.
b) Todavía no sé por qué no quisiste comprarte el coche eléctrico.
c) ¿Sabes ya dónde tendrá lugar la asamblea?
d) No puedo entenderlo si no me lo explicas bien.
"""

# ==============================================================================
# BLOQUE 3: SABER LITERARIO [2 puntos en total]
# ==============================================================================

TEXTOS_LITERARIOS = """
Lea los siguientes textos y responda a CUATRO de las cinco cuestiones que se plantean a continuación. (Si responde a más cuestiones de las indicadas, solo se tendrán en cuenta las cuatro primeras).

Texto 1
Mi tío Antonio era un hombre escéptico y afable; llevaba una larga y fina cadena de oro que le pasaba y repasaba por el cuello; se ponía: unas veces, una gorra antigua con dos cintitas detrás, y otras, un sombrero hongo, bajo de copa y espaciado de alas. Y cuando por las mañanas salía a la compra -sin faltar una-, llevaba un carric viejo y la pequeña cesta metida debajo de las vueltas.
Era un hombre dulce: cuando se sentaba en la sala, se balanceaba en la mecedora suavemente, tarareando por lo bajo, al par que en el piano tocaban la sinfonía de una vieja ópera... Tenía la cabeza redonda y abultada, con un mostacho romo que le ocultaba la comisura de los labios, con una abundosa papada que caía sobre el cuello bajo y cerrado de la camisa. Yo no sé si mi tío Antonio había pisado alguna vez las universidades; tengo vagos barruntos de que fracasaron unos estudios comenzados. Pero tenía lo que vale más que todos los títulos una perspicacia natural, un talento práctico y, sobre todo, una bondad inquebrantable que ha dejado en mis recuerdos una suave estela de ternura.
AZORÍN. Las confesiones de un pequeño filósofo. 5.ª impresión. Barcelona: Austral, 2023, pp. 105-106

Texto 2
La madre, doña Leonarda, era mujer poco simpática; tenía la cara amarillenta, de color de membrillo; la expresión dura, falsamente amable; la nariz corva; unos cuantos lunares en la barba, y la sonrisa forzada.
La buena señora manifestaba unas ínfulas aristocráticas grotescas, y recordaba los tiempos en que su marido había sido subsecretario e iba la familia a veranear a San Juan de Luz. El que las chicas se llamaran Niní y Lulú procedía de la niñera que tuvieron por primera vez, una francesa.
Estos recuerdos de la gloria pasada, que doña Leonarda evocaba accionando con el abanico cerrado como si fuera una batuta, le hacían poner los ojos en blanco y suspirar tristemente.
Pío BAROJA. El árbol de la ciencia. Madrid: Cátedra, 2008, pp. 92-93
"""

EXAMEN_SABER_LITERARIO = """
3.1. Explique, en un máximo de cincuenta palabras, cómo se manifiesta el sentimiento de nostalgia en ambos textos.
[0,5 puntos]

3.2. Compare el simbolismo del abanico de doña Leonarda con el del carric (un tipo de abrigo) viejo del tío Antonio. Utilice un máximo de cincuenta palabras.
[0,5 puntos]

3.3. Seleccione la afirmación que mejor describe la secuencia subrayada del texto 2 «ínfulas aristocráticas grotescas» en relación con doña Leonarda.
[0,5 puntos. Si la respuesta es errónea, se descontarán 0,15 puntos; si no responde a la pregunta, no se aplicará ningún descuento.]
a) Elogia el refinamiento de doña Leonarda.
b) Critica su pretensión social.
c) Describe su elegancia natural.
d) Muestra su humildad.

3.4. Indique cuál de las siguientes figuras retóricas se emplea en el segmento subrayado del texto 1 «una suave estela de ternura».
[0,5 puntos. Si la respuesta es errónea, se descontarán 0,15 puntos; si no responde a la pregunta, no se aplicará ningún descuento.]
a) Sinestesia.
b) Símil.
c) Pleonasmo.
d) Paradoja.

3.5. Explique qué tipo de narrador aparece en el texto 2. Justifique, en un máximo de cincuenta palabras, su respuesta aportando un ejemplo extraído de este.
[0,5 puntos]
"""

SOLUCIONARIO_SABER_LITERARIO = """
RESPUESTAS BLOQUE 3:
3.1: En el primer texto, la nostalgia se manifiesta a través de los recuerdos que tiene el narrador de su tío Antonio, un hombre entrañable, bondadoso y afable, valores positivos que provocan nostalgia y melancolía en el narrador. En contraste, la nostalgia de doña Leonarda se expresa mediante la añoranza por los recuerdos de un pasado glorioso que ya no existe. [0,5 puntos]

3.2: El abanico simboliza su esfuerzo por mantener una imagen aristocrática, un estatus social que ya no tiene, y su resistencia a aceptar la realidad actual. Por el contrario, el carric viejo del tío Antonio simboliza una vida cotidiana sencilla y humilde, sin pretensiones. [0,5 puntos]

3.3: b) Critica su pretensión social. [0,5 puntos]

3.4: a) Sinestesia. [0,5 puntos]

3.5: Se trata de un narrador externo o en tercera persona y omnisciente. Este tiene un conocimiento completo y profundo de los pensamientos y sentimientos de doña Leonarda, así como de su pasado. Por ejemplo, menciona que "El que las chicas se llamaran Niní y Lulú procedía de la niñera que tuvieron por primera vez, una francesa". El narrador expresa comentarios en el que muestra su opinión mediante adjetivos y nombres valorativos. Por ejemplo, "La buena señora manifestaba unas ínfulas aristocráticas grotescas". [0,5 puntos]
"""

# ==============================================================================
# BLOQUE 4: REFLEXIÓN LINGÜÍSTICA [3 puntos en total]
# ==============================================================================

# --- Bloque 1 (Obligatorio) ---
EXAMEN_REFLEXION_LINGUISTICA_B1 = """
Bloque 1. Responda a las tres cuestiones siguientes.

4.1. Una de las dos secuencias del siguiente par mínimo es agramatical. Explique a qué se debe la agramaticalidad. La respuesta debe tener un máximo de cincuenta palabras y contener como máximo tres términos gramaticales relevantes.
[0,75 puntos]
a) Caída la noche.
b) *Llorada la niña.
(Recuadro para respuesta): Términos gramaticales relevantes (un máximo de tres) / Explicación (un máximo de cincuenta palabras).

4.2. Escriba una secuencia gramatical semánticamente coherente de no más de veinte palabras que contenga, al menos, los siguientes tres elementos en el orden que considere oportuno: nombre colectivo, perífrasis aspectual y adjetivo calificativo. La secuencia puede contener oraciones subordinadas, pero no coordinadas ni yuxtapuestas.
[0,75 puntos]
(Recuadro para respuesta): Secuencia / Escriba los elementos que se piden (Nombre colectivo, Perífrasis aspectual, Adjetivo calificativo).

4.3. A partir de las oraciones a y b, construya una secuencia en la que, mediante una estrategia propia de la subordinación, se evite la repetición del sintagma nominal la chica. Al construir dicha secuencia los cambios deben ser mínimos.
[0,5 puntos]
a) Habló con una chica.
b) No había visto a la chica desde el verano.
"""

SOLUCIONARIO_REFLEXION_LINGUISTICA_B1 = """
RESPUESTAS BLOQUE 4 (Bloque 1 obligatorio):
4.1: Términos gramaticales relevantes (un máximo de tres y un mínimo de dos): Los conceptos gramaticales relevantes para explicar la agramaticalidad son: verbo (intransitivo) inacusativo y verbo (intransitivo) inergativo. [0,25 puntos]
Explicación (un máximo de cincuenta palabras): El predicado de estas construcciones (absolutas) solo puede ser un participio formado a partir de un verbo transitivo o de un verbo intransitivo inacusativo. La gramaticalidad de la primera secuencia se explica porque caer es un verbo inacusativo y la agramaticalidad de la segunda porque llorar es un verbo inergativo. [0,5 puntos]. Total pregunta: [0,75 puntos]

4.2: Secuencia: Su numerosa familia suele reunirse a menudo. [Posible respuesta]
Elementos: Nombre colectivo (familia), Perífrasis aspectual (suele reunirse), Adjetivo calificativo (Numerosa). [0,75 puntos]

4.3: Habló con una chica que no había visto desde el verano. [0,5 puntos]
"""

# --- Bloque 2 (Elegir 2 de 3) ---
EXAMEN_REFLEXION_LINGUISTICA_B2 = """
Bloque 2. Responda a DOS de las tres cuestiones siguientes. (Si responde a más cuestiones de las indicadas, solo se tendrán en cuenta las dos primeras).

4.4. «La variación y el cambio lingüístico se deben al descuido e incultura de los hablantes».
Juan Carlos MORENO CABRERA. La dignidad e igualdad de las lenguas. Madrid: Alianza Editorial, 2000, p. 261
¿Considera que esta afirmación es correcta? Justifique su respuesta en un máximo de cincuenta palabras.
[0,5 puntos]

4.5. ¿Cuál de las siguientes afirmaciones es correcta?
[0,5 puntos. Si la respuesta es errónea, se descontarán 0,15 puntos; si no responde a la pregunta, no se aplicará ningún descuento.]
a) Todas las sociedades son diglósicas.
b) La diglosia implica la mezcla de dos idiomas o variedades en una conversación.
c) La diglosia solo afecta al vocabulario.
d) Existe diglosia en las sociedades en las que las variedades lingüísticas muestran diferencias funcionales.

4.6. Indique a qué variedad diatópica del español pertenecen las expresiones miarma y no ni ná. Justifique su respuesta en un máximo de cincuenta palabras.
[0,5 puntos]
"""

SOLUCIONARIO_REFLEXION_LINGUISTICA_B2 = """
RESPUESTAS BLOQUE 4 (Bloque 2 opcional, elegir 2):
4.4: No. Las lenguas en uso experimentan continuamente cambios que no tienen que ver con el descuido o la incultura de los hablantes. [0,5 puntos]

4.5: d) Existe diglosia en las sociedades en las que las variedades lingüísticas muestran diferencias funcionales. [0,5 puntos]

4.6: Al español meridional. Justificación: En estas expresiones podemos reconocer algunos rasgos del español meridional: simplificación de estructuras gramaticales (miarma), elisión de fonemas: (ná) y uso expresivo del lenguaje. [0,5 puntos]
"""
# Fin del archivo contingut_pau.py


# contingut_pau.py (SÈRIE 3 - SETEMBRE - TRANSCRIPCIÓ COMPLETA)

# ==============================================================================
# BLOQUE 0: DATOS GENERALES Y CRITERIOS OFICIALES DE LA PAU (Setembre)
# ==============================================================================

DATOS_GENERALES_PAU = """
Generalitat de Catalunya
Consell Interuniversitari de Catalunya
Oficina d'Accés a la Universitat
Proves d'accés a la universitat (PAU)
Lengua castellana y literatura
Curs 2025
"""

IDENTIFICACION_SERIE = "Lengua castellana y literatura. Sèrie 3. Extraordinaria (Septiembre)"

ESTRUCTURA_PRUEBA = """
El examen consta de CUATRO partes obligatorias:
1. Comprensión lectora (2 puntos): debe responder a TODAS las cuestiones planteadas.
2. Expresión escrita (3 puntos): debe responder a TODAS las cuestiones planteadas.
3. Saber literario (2 puntos): debe responder a CUATRO de las cinco cuestiones planteadas. Si responde a más cuestiones de las indicadas, solo se tendrán en cuenta las cuatro primeras.
4. Reflexión lingüística (3 puntos): debe responder a TODAS las cuestiones del bloque 1 y a solo DOS de las tres cuestiones planteadas en el bloque 2. Si, en el bloque 2, responde a más cuestiones de las indicadas, solo se tendrán en cuenta las dos primeras.
"""


# ==============================================================================
# BLOQUE 1: COMPRENSIÓN LECTORA [2 puntos en total]
# ==============================================================================

TEXTO_COMPRENSION_LECTORA = """
Juan José MILLÁS. «Sesgo y contrasesgo». El País [en línea] (29 noviembre 2024)

A la inteligencia artificial, para que sea de verdad inteligente, le falta lo que a la mayoría de las personas: una mirada propia. Ignoramos si logrará obtenerla, aunque bastaría con que lo simulara. No se trata, pues, de que carezca de yo, pero el yo no es nada sin el contrapeso del contrayó. Tal es lo que caracteriza a los seres humanos: que por debajo del yo aparente hay otro invisible que es el que manda. Llámenlo inconsciente, por ejemplo. Lo cierto es que ese yo-otro es el que marca la diferencia. El yo-otro, a veces, está representado por una enfermedad. Si yo padeciera de un daño crónico en el pie, mi yo-mismo estaría en lucha continua con ese yo-otro doloroso. Donde hay tesis y antítesis, no tarda en manifestarse la síntesis.

Gran parte de la producción literaria es producto del desencuentro entre esos dos yoes. La IA solo tiene de momento uno, pero podría, a medida que crece, surgirle ese otro capaz de provocarle una incomodidad que la dotara de un punto de vista original, de una voz propia. Una mirada singular es el resultado del choque entre aquello de lo que uno procede y su subjetividad. Si a la tradición en la que te has educado le opones lo que rechazas de ella, surge necesariamente algo nuevo. La IA se encuentra en la fase de recibir. Acepta todo cuanto le dicen sus padres (nosotros) como un niño pequeño. Tiene un sesgo, por tanto. Necesitamos que de ese sesgo nazca un contrasesgo para que escriba un buen poema. Lo hará cuando alcance la adolescencia.

A veces, discutiendo con ella, con la IA, aparecen arranques que, si no de rebelión sincera, están bien imitados. Significa que está hecha a nuestra imagen y semejanza, que la hemos construido con un pedazo de barro al que estamos a punto de dotar de alma. De momento, sabe leer y escribir correctamente, aunque no entiende lo que lee ni lo que escribe, como la mayoría de nosotros, por otra parte. Está en la época de la caligrafía y le sale muy bien.
"""

EXAMEN_COMPRENSION_LECTORA_PREGUNTAS = """
1.1. ¿Qué enunciado, de los cuatro que se presentan a continuación, corresponde a una interpretación correcta del texto?
[0,5 puntos. Si la respuesta es errónea, se descontarán 0,15 puntos; si no responde a la pregunta, no se aplicará ningún descuento.]
☐ La inteligencia artificial tiene una mirada propia.
☐ Todos los seres humanos entienden lo que leen y lo que escriben.
☐ Del rechazo a la tradición surge algo nuevo.
☐ La inteligencia artificial es capaz de escribir un buen poema.

1.2. Explique en un máximo de veinticinco palabras cuál es la idea principal del texto.
[0,5 puntos]

1.3. ¿Qué significa la expresión subrayada en el segundo párrafo del texto <<Necesitamos que de ese sesgo nazca un contrasesgo»? Responda en un máximo de veinticinco palabras.
[0,5 puntos]

1.4. Indique el antecedente del pronombre la (en <<logrará obtenerla>>), subrayado en el texto.
[0,5 puntos]
"""

SOLUCIONARIO_COMPRENSION_LECTORA = """
RESPUESTAS COMPRENSIÓN LECTORA:
1.1: c) Del rechazo a la tradición surge algo nuevo. [0,5 puntos]
1.2: La inteligencia artificial, para ser verdaderamente creativa, debería desarrollar una mirada propia. [0,5 puntos]
1.3: La inteligencia artificial necesita desarrollar un punto de vista que se oponga al sesgo con el que fue entrenada. [0,5 puntos]
1.4: una mirada propia. [0,5 puntos]
"""

# ==============================================================================
# BLOQUE 2: EXPRESIÓN ESCRITA [3 puntos en total]
# ==============================================================================

EXAMEN_EXPRESION_ESCRITA_PREGUNTAS = """
2.1. Redacte un texto argumentativo sobre los límites de la inteligencia artificial (IA). Utilice para ello entre cien y ciento cincuenta palabras. Previamente, indique, en el cuadro que aparece a continuación, la tesis que pretende defender, dos argumentos a favor de esa tesis y un contraargumento. Este cuadro puede servirle para redactar el texto.
[2 puntos]
Tesis (no más de diez palabras):
Argumento 1 (no más de diez palabras):
Argumento 2 (no más de diez palabras):
Contraargumento (no más de diez palabras):

2.2. Complete las siguientes oraciones conjugando correctamente el verbo indicado entre paréntesis.
[1 punto]
a) Dudo que tu amigo __________ (prever) el futuro.
b) Espero que tú __________ (conducir) con cuidado.
c) El año pasado aquella empresa __________ (producir) varias películas.
d) Es posible que yo __________ (errar) en mis cálculos.
"""

SOLUCIONARIO_EXPRESION_ESCRITA = """
RESPUESTAS EXPRESIÓN ESCRITA:
2.1: [2 puntos] Respuesta abierta.
Criterios de corrección para 2.1:
— La extensión debe ajustarse a lo pedido (100-150 palabras). Penalización si es muy corto o excesivamente largo.
— Parámetros de puntuación: contenido, léxico, sintaxis y estructura del texto [0,5 puntos cada uno].
— Rellenar el recuadro previo NO comporta puntuación específica, es una estrategia de planificación.

2.2: [1 punto]
a) Dudo que tu amigo prevea el futuro.
b) Espero que tú conduzcas con cuidado.
c) El año pasado aquella empresa produjo varias películas.
d) Es posible que yo yerre en mis cálculos.
"""

# ==============================================================================
# BLOQUE 3: SABER LITERARIO [2 puntos en total]
# ==============================================================================

TEXTOS_SABER_LITERARIO = """
Lea los siguientes textos y responda a CUATRO de las cinco cuestiones.

Texto 1
He cerrado mi balcón
porque no quiero oir el llanto,
pero por detrás de los grises muros
no se oye otra cosa que el llanto.
Hay muy pocos ángeles que canten,
hay muy pocos perros que ladren,
mil violines caben en la palma de mi mano.
Pero el llanto es un perro inmenso,
el llanto es un ángel inmenso,
el llanto es un violín inmenso,
las lágrimas amordazan al viento,
y no se oye otra cosa que el llanto.
Federico GARCÍA LORCA. «Casida II. Del Ilanto». Poesía completa. Barcelona: Galaxia Gutenberg, 2013, p. 553

Texto 2
[...] El llanto medio u ordinario consiste en una contracción general del rostro y un sonido espasmódico acompañado de lágrimas y mocos, estos últimos al final, pues el llanto se acaba en el momento en que uno se suena enérgicamente.
[...] Llegado el llanto, se tapará con decoro el rostro usando ambas manos con la palma hacia dentro. Los niños llorarán con la manga del saco contra la cara, y de preferencia en un rincón del cuarto. Duración media del llanto, tres minutos.
Julio CORTÁZAR. «Instrucciones para llorar». Historias de cronopios y de famas. Buenos Aires: Alfaguara, 1995, p. 3
"""

EXAMEN_SABER_LITERARIO_PREGUNTAS = """
3.1. ¿Qué contraste se presenta, en el texto 1, entre los dos primeros versos y el resto del poema?
[0,5 puntos. Si la respuesta es errónea, se descontarán 0,15 puntos; si no responde a la pregunta, no se aplicará ningún descuento.]
☐ El llanto es constante a pesar del aislamiento.
☐ El yo poético ignora el llanto y disfruta de la música.
☐ El mundo interior de la casa está lleno de alegría.
☐ El viento impide escuchar el llanto.

3.2. En ambos textos, se describe el llanto de manera distinta. Explique la diferencia en un máximo de cincuenta palabras.
[0,5 puntos]

3.3. Identifique y explique la figura retórica que aparece en el verso del texto 1 «mil violines caben en la palma de mi mano». Utilice un máximo de cincuenta palabras.
[0,5 puntos]

3.4. Argumente con ejemplos por qué el texto 2 es irónico en un máximo de cincuenta palabras.
[0,5 puntos]

3.5. Señale la opción que expresa la crítica que subyace en el texto 2.
[0,5 puntos. Si la respuesta es errónea, se descontarán 0,15 puntos; si no responde a la pregunta, no se aplicará ningún descuento.]
☐ El llanto debe ser planificado.
☐ El llanto debe seguir un protocolo.
☐ El llanto debe ser analizado científicamente.
☐ Las normas sociales reprimen la expresión del llanto.
"""

SOLUCIONARIO_SABER_LITERARIO = """
RESPUESTAS SABER LITERARIO:
3.1: a) El llanto es constante a pesar del aislamiento. [0,5 puntos]
3.2: En el poema, el llanto es un elemento que está siempre presente (omnipresente) y es imposible controlarlo, mientras que, en el texto en prosa, se reduce a un acto controlado y breve. [0,5 puntos]
3.3: Se trata de una hipérbole, pues es una exageración desmesurada. [0,5 puntos]
3.4: La complejidad y la carga emocional del llanto se reduce a una serie de instrucciones detalladas como si solo fuera un proceso físico y un acto mecánico (contracción del rostro, sonido espasmódico, el llanto acaba en el momento en que uno se suena enérgicamente). Además, la duración del llanto es absurda, pues no se trata de un acto programado y controlado. [0,5 puntos]
3.5: d) Las normas sociales reprimen la expresión del llanto. [0,5 puntos]
"""

# ==============================================================================
# BLOQUE 4: REFLEXIÓN LINGÜÍSTICA [3 puntos en total]
# ==============================================================================

# --- Bloque 1 ---
EXAMEN_REFLEXION_LINGUISTICA_B1_PREGUNTAS = """
Bloque 1. Responda a las tres cuestiones siguientes.

4.1. Explique a qué se debe el contraste semántico entre las dos secuencias del siguiente par mínimo. La respuesta debe tener un máximo de cincuenta palabras y contener como máximo tres términos gramaticales relevantes.
[0,75 puntos]
a) Fernando se tomó un café solo.
b) Fernando solo se tomó un café.
Términos gramaticales relevantes (un máximo de tres):
Explicación (un máximo de cincuenta palabras):

4.2. Escriba una secuencia gramatical semánticamente coherente de no más de veinte palabras que contenga, al menos, los siguientes tres elementos en el orden que considere oportuno: verbo inergativo, complemento predicativo orientado al sujeto y determinante posesivo. La secuencia puede contener oraciones subordinadas, pero no coordinadas ni yuxtapuestas.
[0,75 puntos]
Verbo inergativo:
Complemento predicativo orientado al sujeto:
Determinante posesivo:
Secuencia:

4.3. A partir de las oraciones a y b, construya una secuencia en la que, mediante una estrategia propia de la subordinación, se evite la repetición del sintagma nominal esta novela. Al construir dicha secuencia los cambios deben ser mínimos.
[0,5 puntos]
a) La novela se ha traducido al alemán.
b) El autor de la novela ha recibido un premio.
"""

SOLUCIONARIO_REFLEXION_LINGUISTICA_B1 = """
RESPUESTAS REFLEXIÓN LINGÜÍSTICA (Bloque 1):
4.1: Términos gramaticales relevantes: adjetivo y adverbio de foco. [0,25 puntos]
Explicación: En la primera secuencia, 'solo' es un adjetivo que puede modificar al SN 'un café' (Se tomó un café sin leche) o al SN 'Fernando' (Se tomó un café sin compañía), mientras que, en la segunda, es un adverbio de foco que puede modificar al verbo tomar (Lo único que hizo fue tomarse un café) o al SN 'un café' (Se tomó únicamente un café). [0,5 puntos]. Total pregunta: [0,75 puntos]

4.2: Secuencia: Mi hermano sonríe feliz en todas las fotografías que me mostraste. [Posible respuesta]. Verbo inergativo (sonreír), Complemento predicativo orientado al sujeto (feliz), Determinante posesivo (mi). [0,75 puntos]

4.3: La novela, cuyo autor ha recibido un premio, se ha traducido al alemán. [Posible respuesta]. [0,5 puntos]
"""

# --- Bloque 2 ---
EXAMEN_REFLEXION_LINGUISTICA_B2_PREGUNTAS = """
Bloque 2. Responda a DOS de las tres cuestiones siguientes.

4.4. «Hay lenguas útiles e inútiles».
Juan Carlos MORENO CABRERA. La dignidad e igualdad de las lenguas. Madrid: Alianza Editorial, 2000, p. 238
¿Considera que esta afirmación es correcta? Justifique su respuesta en un máximo de cincuenta palabras.
[0,5 puntos]

4.5. ¿Cuál de las siguientes afirmaciones es correcta?
[0,5 puntos. Si la respuesta es errónea, se descontarán 0,15 puntos; si no responde a la pregunta, no se aplicará ningún descuento.]
☐ Se entiende por idiolecto el estado ideal de una lengua.
☐ Se entiende por idiolecto el uso correcto de la lengua.
☐ Se entiende por idiolecto la variedad lingüística propia de un individuo.
☐ Se entiende por idiolecto un estado lingüístico intermedio.

4.6. Indique a qué variedad diatópica del español pertenecen las oraciones Vos cantás todos los días, Arregla las cosas bonito y Tomaré un matecito. Justifique su respuesta en un máximo de cincuenta palabras.
[0,5 puntos]
"""

SOLUCIONARIO_REFLEXION_LINGUISTICA_B2 = """
RESPUESTAS REFLEXIÓN LINGÜÍSTICA (Bloque 2):
4.4: No. No es la lengua en sí lo que determina su utilidad, sino las circunstancias sociales. [0,5 puntos]
4.5: c) Se entiende por idiolecto la variedad lingüística propia de un individuo. [0,5 puntos]
4.6: Al español de América. Justificación: el uso de vos en lugar de tú (vos cantás todos los días), la adverbialización del adjetivo (bonito) y el uso de diminutivos (matecito). [0,5 puntos]
"""

# contingut_pau.py (SÈRIE 1 - JUNY 2024 - TRANSCRIPCIÓ COMPLETA)

# ==============================================================================
# BLOQUE 0: DATOS GENERALES Y CRITERIOS OFICIALES PAU (Comunes a todas las Series)
# ==============================================================================

DATOS_GENERALES_PAU = """
Generalitat de Catalunya
Consell Interuniversitari de Catalunya
Oficina d'Accés a la Universitat
Proves d'accés a la universitat (PAU)
Lengua castellana y literatura
Curs 2024
"""

IDENTIFICACION_SERIE = "Lengua castellana y literatura. Sèrie 1"

ESTRUCTURA_PRUEBA = """
La prueba consta de tres partes: 1) comprensión lectora, 2) expresión escrita y 3) reflexión lingüística.
Debe escoger UNA de las dos opciones (A o B) para completar las partes 1 y 2. En cambio, la parte 3 es común a las dos opciones.
"""


# ==============================================================================
# BLOQUE 1: OPCIÓN A (Transcripción Literal del Examen y Solucionario)
# ==============================================================================

SERIE_1_OPCION_A = {
    # --- Comprensión lectora (A) ---
    "comprension_lectora_texto": """
Carlos RUIZ ZAFÓN. La sombra del viento. Barcelona: Planeta, 2016, pp. 12-14

Jamás había oído mencionar aquel título o a su autor, pero no me importó. La decisión estaba tomada. Por ambas partes. Tomé el libro con sumo cuidado y lo hojeé, dejando aletear sus páginas. Liberado de su celda en el estante, el libro exhaló una nube de polvo dorado. Satisfecho con mi elección, rehíce mis pasos en el laberinto portando mi libro bajo el brazo con una sonrisa impresa en los labios. Tal vez la atmósfera hechicera de aquel lugar había podido conmigo, pero tuve la seguridad de que aquel libro había estado allí esperándome durante años, probablemente desde antes de que yo naciese.

Aquella tarde, de vuelta en el piso de la calle Santa Ana, me refugié en mi habitación y decidí leer las primeras líneas de mi nuevo amigo. Antes de darme cuenta, me había caído dentro sin remedio. La novela relataba la historia de un hombre en busca de su verdadero padre, al que nunca había llegado a conocer y cuya existencia solo descubría merced a las últimas palabras que pronunciaba su madre en su lecho de muerte. La historia de aquella búsqueda se transformaba en una odisea fantasmagórica en la que el protagonista luchaba por recuperar una infancia y una juventud perdidas, y en la que, lentamente, descubríamos la sombra de un amor maldito cuya memoria le habría de perseguir hasta el fin de sus días. A medida que avanzaba, la estructura del relato empezó a recordarme a una de esas muñecas rusas que contienen innumerables miniaturas de sí mismas en su interior. Paso a paso, la narración se descomponía en mil historias, como si el relato hubiese penetrado en una galería de espejos y su identidad se escindiera en docenas de reflejos diferentes y al tiempo uno solo. Los minutos y las horas se deslizaron como un espejismo. Horas más tarde, atrapado en el relato, apenas advertí las campanadas de medianoche en la catedral repiqueteando a lo lejos. Enterrado en la luz de cobre que proyectaba el flexo, me sumergí en un mundo de imágenes y sensaciones como jamás las había conocido. Personajes que se me antojaron tan reales como el aire que respiraba me arrastraron en un túnel de aventura y misterio del que no quería escapar. Página a página, me dejé envolver por el sortilegio de la historia y su mundo hasta que el aliento del amanecer acarició mi ventana y mis ojos cansados se deslizaron por la última página. Me tendí en la penumbra azulada del alba con el libro sobre el pecho y escuché el rumor de la ciudad dormida goteando sobre los tejados salpicados de púrpura. El sueño y la fatiga llamaban a mi puerta, pero me resistí a rendirme. No quería perder el hechizo de la historia ni todavía decir adiós a sus personajes.

En una ocasión oí comentar a un cliente habitual en la librería de mi padre que pocas cosas marcan tanto a un lector como el primer libro que realmente se abre camino hasta su corazón. Aquellas primeras imágenes, el eco de esas palabras que creemos haber dejado atrás, nos acompañan toda la vida y esculpen un palacio en nuestra memoria al que, tarde o temprano –no importa cuántos libros leamos, cuántos mundos descubramos, cuánto aprendamos u olvidemos–, vamos a regresar. Para mí, esas páginas embrujadas siempre serán las que encontré entre los pasillos del Cementerio de los Libros Olvidados.
""",
    "comprension_lectora_preguntas": """
1.1. Resuma el texto que ha leído sin reproducir frases de este. Utilice para ello un máximo de cincuenta palabras.
[1 punto]

1.2. Señale qué serie, de las cuatro que se proponen, es la única correcta para sustituir todas las palabras siguientes, subrayadas en el texto: hechicera, fantasmagórica, sortilegio, púrpura.
[0,5 puntos. Si la respuesta es errónea, se descontarán 0,15 puntos; si no responde a la pregunta, no se aplicará ningún descuento.]
☐ repelente, aterradora, espiritismo, tinte
☐ cautivadora, sobrenatural, encanto, escarlata
☐ enloquecedora, tangible, conjuro, colorante
☐ profeta, alucinante, sorteo, dignidad

1.3. Indique los antecedentes de cuja (en «cuya memoria») y que (en «del que no quería escapar»), subrayados en el texto.
[1 punto]
a) cuja:
b) que:

1.4. Conteste únicamente DOS de las cuatro cuestiones siguientes sobre las lecturas (Nada, de Carmen Laforet, y La Fundación, de Antonio Buero Vallejo) y sobre las figuras retóricas que aparecen en el texto. Puede combinarlas como prefiera. En el caso de responder a tres o cuatro preguntas, solo se tendrán en cuenta las dos primeras.
[1,5 puntos en total. Se descontarán 0,25 puntos por cada pregunta de respuesta múltiple errónea.]

a) Sobre Nada, ¿con quién mantuvo Román una relación en su adolescencia? ¿Cómo terminó? Utilice un máximo de cincuenta palabras. [0,75 puntos]

b) Sobre La Fundación, ¿qué personaje de la obra experimenta una transformación más radical? [0,75 puntos]
☐ Max.
☐ Asel.
☐ Tomás.
☐ Lino.

c) Identifique y explique la figura retórica que aparece en el fragmento «no importa cuántos libros leamos, cuántos mundos descubramos, cuánto aprendamos u olvidemos», subrayado en el texto. Utilice un máximo de cincuenta palabras. [0,75 puntos]

d) Identifique la figura retórica que aparece en el fragmento «hasta que el aliento del amanecer acarició mi ventana», subrayado en el texto. [0,75 puntos]
☐ Oxímoron.
☐ Pleonasmo.
☐ Personificación.
☐ Zeugma.
""",
    "comprension_lectora_solucionario": """
RESPUESTAS COMPRENSIÓN LECTORA (Opción A):
1.1: Respuesta abierta. (Se admite fracción en la puntuación: 1 / 0,75 / 0,5 / 0,25).
1.2: b) cautivadora, sobrenatural, encanto, escarlata [Solucionario: línea 2] [0,5 puntos]
1.3: [1 punto. 0,5p cada uno]
    a) cuja: un amor maldito
    b) que: un túnel de aventura y misterio
1.4: [1,5 puntos. Elegir DOS]
    a) Respuesta: Con Margarita, la madre de Ena. Román acepta dinero para dejar de verla. [0,75 puntos]
    b) Respuesta: c) Tomás [Solucionario: línea 3] [0,75 puntos]
    c) Respuesta: Anáfora (o epanáfora), figura retórica de repetición al comienzo de enunciados. Si hay variación de forma o función es 'anáfora con poliptoton'. Refuerza el mensaje. [0,75 puntos]
    d) Respuesta: c) Personificación [Solucionario: línea 3] [0,75 puntos]
""",

    # --- Expresión escrita (A) ---
    "expresion_escrita_preguntas": """
2.1. ¿Comparte con el autor del texto la idea de que el primer libro que llega al corazón marca profundamente a un lector? Escriba un texto argumentativo que apoye o critique ese punto de vista. Utilice para ello entre cien y ciento cincuenta palabras. Previamente, indique, en el cuadro que aparece a continuación, la tesis que pretende defender, dos argumentos a favor de esa tesis y un contraargumento. Este cuadro puede servirle para redactar el texto.
[2 puntos]
Tesis (no más de diez palabras):
Argumento 1 (no más de diez palabras):
Argumento 2 (no más de diez palabras):
Contraargumento (no más de diez palabras):

2.2. Complete las secuencias con la forma correcta de entre las dos que se proponen en cada caso.
[1 punto]
a) Me alegro __________ (de que / que) seáis felices.
b) Tuve que subir al __________ (onceavo / undécimo) piso.
c) Consiguió que cambiara muchas ideas __________ (acerca de / a cerca de) mi profesión.
d) La víctima, un señor de cuarenta años, fue __________ (identificado / identificada) enseguida.
""",
    "expresion_escrita_solucionario": """
RESPUESTAS EXPRESIÓN ESCRITA (Opción A):
2.1: [2 puntos] Respuesta abierta. Criterios: contenido (0,5), léxico (0,5), sintaxis (0,5), estructura (0,5). Penalización por extensión incorrecta. Rellenar el cuadro no puntúa pero es estrategia.
2.2: [1 punto. 0,25p cada espacio]
    a) Me alegro de que seáis felices.
    b) Tuve que subir al undécimo piso.
    c) Consiguió que cambiara muchas ideas acerca de mi profesión.
    d) La víctima, un señor de cuarenta años, fue identificada enseguida.
"""
}

# ==============================================================================
# BLOQUE 2: OPCIÓN B (Transcripción Literal del Examen y Solucionario)
# ==============================================================================
# Nota: No se proporcionaron imágenes del texto de lectura ni enunciados de la Opción B.
# Solo se transcribe el solucionario aportado por el usuario.

SERIE_1_OPCION_B = {
    "comprension_lectora_texto": "[NO DISPONIBLE EN IMÁGENES]",
    "comprension_lectora_preguntas": "[NO DISPONIBLE EN IMÁGENES]",
    "comprension_lectora_solucionario": """
RESPUESTAS COMPRENSIÓN LECTORA (Opción B):
1.1: [1 punto] Respuesta abierta. Admite fracciones: 1 / 0,75 / 0,5 / 0,25.
1.2: [0,5 puntos] Respuesta: b) corregir, dogmatizan, asambleas, inflexibilidad [Solucionario: línea 1].
1.3: [1 punto] Cada antecedente vale 0,5 puntos.
    a) su: el fanatismo.
    b) los: al vecino, al cónyuge, al niño y al hermano.
1.4: [1,5 puntos. Elegir DOS]
    a) Respuesta: Asel es ingeniero y conoce los planos del edificio, lo que le permitirá diseñar un plan de fuga.
    b) Respuesta: c) Cincuenta [Solucionario: línea 4].
    c) Respuesta: Asíndeton, figura retórica de omisión de conjunciones. Transmite sensación de determinación.
    d) Respuesta: a) Antítesis [Solucionario: línea 1].
""",
    "expresion_escrita_preguntas": "[NO DISPONIBLE EN IMÁGENES. Se infiere que es redacción expositiva sobre la tolerancia y ejercicios gramaticales]",
    "expresion_escrita_solucionario": """
RESPUESTAS EXPRESIÓN ESCRITA (Opción B):
2.1: [2 puntos] Respuesta abierta (Texto expositivo sobre la tolerancia). Criterios: contenido (0,5), léxico (0,5), sintaxis (0,5), estructura (0,5). Rellenar el cuadro no puntúa.
2.2: [1 punto. 0,25p cada espacio]
    a) Me dijo que un mago nunca revela sus trucos.
    b) Es posible que se haya deshecho de todos los documentos.
    c) Juan tiene una vasta experiencia en estas cuestiones.
    d) Las cucarachas infestaban la casa.
"""
}

# ==============================================================================
# BLOQUE 3: PARTE COMÚN (Reflexión Lingüística - Transcripción Literal)
# ==============================================================================

SERIE_1_PARTE_COMUN = {
    "reflexion_linguistica_preguntas": """
3. Reflexión lingüística
[3 puntos en total]

3.1. Indique si una de las dos secuencias del par mínimo es agramatical o si existe un contraste semántico entre las dos secuencias del par. Si una es agramatical, especifique cuál es y explique a qué se debe la agramaticalidad. Si existe un contraste semántico, explique en qué consiste. La respuesta debe tener un máximo de cincuenta palabras y contener como máximo cuatro términos gramaticales relevantes. [1 punto]
a) Tuvimos que comprar los muebles caros.
b) Tuvimos que comprar caros los muebles.
☐ Secuencia agramatical: __________
☐ Contraste semántico
Términos gramaticales relevantes (un máximo de cuatro):
Explicación (un máximo de cincuenta palabras):

3.2. Escriba una secuencia gramatical semánticamente coherente de no más de veinte palabras que contenga, al menos, los siguientes cuatro elementos en el orden que considere oportuno: verbo transitivo, complemento locativo argumental, determinante demostrativo y adjetivo calificativo. La secuencia puede contener oraciones subordinadas, pero no coordinadas ni yuxtapuestas. [1 punto]
Secuencia: __________
Verbo transitivo: __________ / Complemento locativo argumental: __________ / Determinante demostrativo: __________ / Adjetivo calificativo: __________

3.3. Lea la siguiente lista de secuencias y, de entre las opciones que se ofrecen debajo, elija la única que identifica de manera correcta y ordenada la función sintáctica del elemento subrayado en cada una de las secuencias.
[0,5 puntos. Si la respuesta es errónea, se descontarán 0,15 puntos; si no se contesta la pregunta, no se aplicará ningún descuento.]
1. La persona con la que hablaste estaba equivocada.
2. Mete las llaves donde te dije.
3. La solución es compartir tus ideas con quienes te han apoyado.
4. Avísale antes de llegar a la estación.
☐ 1) complemento de régimen verbal, 2) complemento del nombre, 3) atributo, 4) complemento circunstancial
☐ 1) complemento de régimen verbal, 2) complemento circunstancial, 3) sujeto, 4) complemento circunstancial
☐ 1) complemento del nombre, 2) complemento locativo argumental, 3) atributo, 4) complemento del adverbio
☐ 1) complemento de régimen verbal, 2) complemento del nombre, 3) atributo, 4) término de preposición

3.4. Responda a UNA de las dos cuestiones siguientes, relacionadas con la oración compuesta y con la estructura informativa de la oración.
[0,5 puntos]
a) A partir de las oraciones 1 y 2, construya una secuencia que, mediante una estrategia propia de la subordinación, evite la repetición del sintagma nominal Luis Mateo Díez. Al construir dicha secuencia, los cambios deben ser mínimos.
1. Luis Mateo Díez nació en Villablino.
2. Entregaron el Premio Cervantes a Luis Mateo Díez.
b) Reescriba la oración Lo haré, si me lo piden, de manera que la oración subordinada pase a ser tema. Al reescribir la oración, los cambios deben ser mínimos.
""",
    "reflexion_linguistica_solucionario": """
RESPUESTAS REFLEXIÓN LINGÜÍSTICA (Parte Común):
3.1: [1 punto]
    - Opción elegida: Contraste semántico
    - Términos gramaticales relevantes (0,5p): complemento predicativo y complemento del nombre.
    - Explicación (0,5p): Existe contraste semántico. En (a) caros puede ser predicativo o complemento del nombre. En (b) solo puede ser complemento predicativo.
3.2: [1 punto. 0,25p por elemento en secuencia gramatical válida de <20 palabras]
    - Secuencia ejemplo: Este libro es tan grande que no pude ponerlo en la estantería.
    - Verbo transitivo: poner
    - Complemento locativo argumental: en la estantería
    - Determinante demostrativo: este
    - Adjetivo calificativo: grande
3.3: [0,5 puntos]
    - Respuesta correcta: c) 1) complemento del nombre, 2) complemento locativo argumental, 3) atributo, 4) complemento del adverbio [Solucionario: línea 3].
3.4: [0,5 puntos. Elegir UNA]
    - a) Entregaron el premio Cervantes a Luis Mateo Díez, nacido en Villablino.
    - b) Si me lo piden, lo haré.
"""
}

# contingut_pau.py (SÈRIE 3 - SETEMBRE 2024)

# ==============================================================================
# BLOQUE 0: DATOS GENERALES Y CRITERIOS OFICIALES PAU (Setembre 2024)
# ==============================================================================

DATOS_GENERALES_PAU = """
Generalitat de Catalunya
Consell Interuniversitari de Catalunya
Oficina d'Accés a la Universitat
Proves d'accés a la universitat (PAU)
Lengua castellana y literatura
Serie 3
Curs 2024
"""

ESTRUCTURA_PRUEBA = """
El examen consta de tres partes: 1) comprensión lectora, 2) expresión escrita y 3) reflexión lingüística.
Debe escoger UNA de las dos opciones (A o B) para completar las partes 1 y 2. En cambio, la parte 3 es común a las dos opciones.
"""


# ==============================================================================
# BLOQUE 1: OPCIÓN A (Transcripción de Alta Fidelidad del Examen y Solucionario)
# ==============================================================================

SERIE_3_OPCION_A = {
    # --- Comprensión lectora (A) ---
    "comprension_lectora_texto": """
Luis LANDERO. Lluvia fina. Barcelona: Tusquets Editores, 2019, pp. 11-13

Ahora ya sabe con certeza que los relatos no son inocentes, no del todo inocentes. Quizá tampoco lo sean las conversaciones de diario, los descuidos y equívocos verbales o el hablar por hablar. Quizá ni siquiera lo que se habla en sueños sea del todo inocente. Hay algo en las palabras que, ya de por sí, entraña un riesgo, una amenaza, y no es verdad que el viento se las lleve tan fácilmente como dicen. No es verdad. Puede ocurrir que ciertos ecos de los dichos, y hasta de los dichos más triviales, sigan como en letargo durante muchos años, latiendo débilmente en un rincón de la memoria, esperando una segunda oportunidad de regresar al presente para aumentar y corregir lo que no quedó del todo claro en su momento, y a menudo con una elocuencia y un alcance significativo que exceden con mucho a los que tuvieron en su origen. Ahí están, no hay más que verlos, llegan revestidos con extraños ropajes, al son de músicas exóticas, con trazas nunca vistas, y es que traen noticias, grandes y asombrosas noticias, de un pasado que acaso no existió jamás. Y siempre, siempre, los relatos o las palabras que vuelven de los oscuros ámbitos de la memoria llegan en son de guerra, cargados de agravios, y ansiosos de reivindicación y de discordia. Es como si en el largo exilio del olvido hubieran ahondado en sus mundos imaginarios, hurgado en sus entrañas, como el doctor Moreau con sus criaturas monstruosas, hasta sufrir una total, una fantástica metamorfosis. Y así, con su lúgubre cortejo de figuras grotescas, pero a la vez irresistiblemente seductoras, las palabras y relatos de ayer llegan a nosotros e imponen en nuestra conciencia la tiranía, la deliciosa tiranía, de sus nuevos significados y argumentos. ¡Ah!, y eso sin contar los gestos que usamos al hablar, la dimensión teatral de las palabras, y que a veces son más persuasivos que ellas mismas, y las sobreviven en la memoria, de modo que a menudo no sabemos con seguridad si estamos recordando las frases o más bien su puesta en escena, el repertorio de ademanes que las acompañaban, las sonrisas, las miradas, las manos, los hombros, las pausas, el secreto parloteo del silencio y del cuerpo.

Son negras conjeturas que cruzan y agitan la mente de Aurora y ponen un nublado de cansancio en su rostro. Y es que lleva mucho tiempo, casi toda la vida, escuchando historias, confidencias, palabras y palabras dichas siempre en voz baja y en tono airado y dolorido. Son historias que suelen venir de muy atrás, que sucedieron en un tiempo remoto, ya casi legendario, pero que se mantienen tan pujantes y vivas como entonces, si es que no más. ¿Qué habrá en Aurora que despierta enseguida la confianza de la gente y las ganas de sincerarse con ella y de contarle fragmentos antológicos de su vida, secretos que acaso el narrador no ha revelado nunca a nadie? Pero a ella sí. A ella todos le cuentan, todos la quieren, todos le agradecen su comprensión, su manera tan dulce, tan consoladora de escuchar.
""",
    "comprension_lectora_preguntas": """
1. Comprensión lectora
[4 puntos en total]

1.1. Resuma el texto que ha leído sin reproducir frases de este. Utilice para ello un máximo de cincuenta palabras.
[1 punto]

1.2. Señale qué serie, de las cuatro que se proponen, es la única correcta para sustituir todas las palabras siguientes, subrayadas en el texto: equívocos, triviales, metamorfosis, conjeturas.
[0,5 puntos. Si la respuesta es errónea, se descontarán 0,15 puntos; si no responde a la pregunta, no se aplicará ningún descuento.]
☐ malentendidos, intrascendentes, transformación, suposiciones
☐ errores, insignificantes, mejora, presunciones
☐ inequívocos, frívolos, mudanza, profecías
☐ falseamientos, vulgares, transmutación, realidades

1.3. Indique los antecedentes de los (en <<no hay más que verlos») y que (en «que se mantienen tan pujantes y vivas como entonces»), subrayados en el texto.
[1 punto]
a) los:
b) que:

1.4. Conteste únicamente DOS de las cuatro cuestiones que se plantean sobre las lecturas (Nada, de Carmen Laforet, y La Fundación, de Antonio Buero Vallejo) y sobre las figuras retóricas que aparecen en el texto. Puede combinarlas como prefiera. En el caso de responder a tres o cuatro preguntas, solo se tendrán en cuenta las dos primeras.
[1,5 puntos en total. Se descontarán 0,25 puntos por cada pregunta de respuesta múltiple errónea.]

a) Sobre Nada, ¿por qué Angustias prohíbe a Andrea ir al Barrio Chino? Utilice un máximo de cincuenta palabras.
[0,75 puntos]

b) Sobre La Fundación, ¿cuál es la profesión de Tulio en la Fundación?
[0,75 puntos]
☐ Ingeniero.
☐ Médico.
☐ Escritor.
☐ Fotógrafo.

c) Identifique la figura retórica que aparece en el fragmento «despierta enseguida la confianza de la gente y las ganas de sincerarse con ella y de contarle fragmentos antológicos de su vida», subrayado en el texto.
[0,75 puntos]
☐ Oxímoron.
☐ Asíndeton.
☐ Eufemismo.
☐ Polisíndeton.

d) Identifique la figura retórica que aparece en el fragmento «¿Qué habrá en Aurora [...]?», subrayado en el texto. Utilice un máximo de cincuenta palabras.
[0,75 puntos]
""",
    "comprension_lectora_solucionario": """
SOLUCIONARIO Comprensión lectora (Opción A):
1.1: [1 punto] Respuesta abierta. Admite fracciones (1 / 0,75 / 0,5 / 0,25).
1.2: [0,5 puntos] Respuesta: ☐ malentendidos, intrascendentes, transformación, suposiciones [Solucionario: línea 1].
1.3: [1 punto. 0,5p cada uno]
    a) los: ecos de los dichos
    b) que: historias
1.4: [1,5 puntos en total. Elegir DOS]
    a) Respuesta: Porque Angustias considera que en el Barrio Chino sólo hay «perdidas, ladrones y el brillo del demonio». [0,75 puntos]
    b) Respuesta: ☐ Fotógrafo. [Solucionario: línea 4]. [0,75 puntos]
    c) Respuesta: ☐ Polisíndeton. [Solucionario: línea 4]. [0,75 puntos]
    d) Respuesta: Pregunta retórica, figura que consiste en formular una pregunta para la cual no se espera realmente una respuesta. En este caso, la pregunta sirve para provocar una reflexión en el lector. [0,75 puntos]
""",

    # --- Expresión escrita (A) ---
    "expresion_escrita_preguntas": """
2. Expresión escrita
[3 puntos en total]

2.1. ¿Comparte la opinión del autor del texto sobre la comunicación (verbal y no verbal)? Escriba un texto argumentativo que apoye o critique ese punto de vista. Utilice para ello entre cien y ciento cincuenta palabras. Previamente, indique, en el cuadro que aparece a continuación, la tesis que pretende defender, dos argumentos a favor de esa tesis y un contraargumento. Este cuadro puede servirle para redactar el texto.
[2 puntos]
Tesis (no más de diez palabras):
Argumento 1 (no más de diez palabras):
Argumento 2 (no más de diez palabras):
Contraargumento (no más de diez palabras):

2.2. Complete las secuencias con la forma adecuada del verbo propuesto.
[1 punto]
a) Los acusados __________ (pretérito perfecto simple de argüir) que no habían estado allí.
b) Ellas __________ (pretérito perfecto simple de predecir) el resultado de la votación.
c) No creo que el resultado __________ (presente de subjuntivo de satisfacer) vuestras expectativas.
d) El doctor no es partidario de que tú __________ (presente de subjuntivo de ingerir) más de dos cápsulas.
""",
    "expresion_escrita_solucionario": """
SOLUCIONARIO Expresión escrita (Opción A):
2.1: [2 puntos] Respuesta abierta. Parámetros: contenido (0,5p), léxico (0,5p), sintaxis (0,5p), estructura (0,5p). Penalización por extensión incorrecta. El cuadro no puntúa específicamente.
2.2: [1 punto. Cada espacio vale 0,25 puntos]
    a) Los acusados arguyeron que no habían estado allí.
    b) Ellas predijeron el resultado de la votación.
    c) No creo que el resultado satisfaga vuestras expectativas.
    d) El doctor no es partidario de que tú ingieras más de dos cápsulas.
"""
}

# ==============================================================================
# BLOQUE 2: OPCIÓN B (Transcripción de Alta Fidelidad del Examen y Solucionario)
# ==============================================================================

SERIE_3_OPCION_B = {
    # --- Comprensión lectora (B) ---
    "comprension_lectora_texto": """
Rosa MONTERO. «Tiempos interesantes». El País Semanal (21 enero 2024), p. 74

Muchas veces he pensado en lo afortunada que soy al vivir en la época en la que vivo. Esto, por otra parte, es lo normal; hay una tendencia natural a sentirnos bien con lo que somos, y eso es positivo, porque favorece nuestro equilibrio psicológico. Pero mi fascinación por nuestra época quizá sea especialmente vehemente. Ya he contado alguna vez que uno de mis primeros y más poderosos recuerdos fue cuando, con seis años, me encontraba una noche de frío invierno en la avenida madrileña en la que vivía, agarrada de las manos de mis padres y mirando al cielo. Estar tan de noche en la calle ya era singular, pero es que además yo llevaba un año enferma y normalmente no salía de casa. Así que aquella velada era extraordinaria. A nuestro alrededor, para más extrañeza, había un montón de gente, todos quietos de pie y con los ojos clavados en el firmamento. Y, tras cierta espera, allí apareció una estrellita luminosa que caminaba deprisa por encima de nuestras cabezas, dibujando un arco en la negrura. Era el Sputnik ruso, el primer satélite que orbitó el planeta, el hito más importante de la carrera espacial, porque fue la primera vez que el ser humano consiguió salir del asfixiante útero de la gravedad terrestre.

Con esto quiero decir que desde muy pequeña he sido consciente de que mi vida estaba marcada por la maravilla. De que a mi generación le había tocado asistir a un progreso tecnológico extraordinario. Tan extraordinario, de hecho, que en aquel 1957 del Sputnik no podíamos ni imaginar adónde íbamos a llegar en las siguientes décadas. Siempre he sido amante de la ciencia ficción, y resulta que ahora estamos viviendo dentro de las novelas que leía en la adolescencia. O aún más allá. A veces pienso en ello y aún me pasmo. <<¡Ojalá vivas tiempos interesantes!», reza una supuesta maldición china, aunque al parecer no es china en absoluto, sino el invento de algún escritor británico del siglo xix en plena ola orientalista. En cualquier caso, y sea del origen que sea, el sentido es evidente: los tiempos agitados pueden traer mucho dolor y confusión. Y más interesantes y agitados que estos, imposible. Los avances científicos están consiguiendo cosas que parecen impensables. Como un material que otorga la invisibilidad a quien se oculte detrás (se llama Quantum Stealth y no funciona con electricidad, asi que se puede usar en cualquier sitio); o una bacteria ya conocida, la Cupriavidus metallidurans, de la que unos investigadores de la Universidad de Michigan acaban de descubrir que puede vivir en compuestos tóxicos auríferos y convertirlos en oro metálico puro de 24 quilates en pocos días. La Cupriavidus no es un producto tecnológico, pero sí lo es su observación, es decir, la manera en la que vamos desentrañando los ocultos intríngulis del universo. He escogido estos dos ejemplos, entre mil, por su conexión con lo legendario: son como la capa invisible de los cuentos de hadas o la piedra filosofal alquímica que muta en oro los metales básicos.

Pero estas cosas solo son menudencias. Hay avances infinitamente más importantes. Hace cinco años empecé a tomar notas sobre la inteligencia artificial para mi cuarta novela de Bruna Husky (una serie de libros de ciencia ficción), cuya trama tiene que ver con ese tema. Hace un año tuve que tirar todos los apuntes que tenía: la realidad los había sobrepasado. Los cambié por otros, y ahora escribo la novela mordida por la urgencia de lo que está sucediendo. Numerosos científicos piensan que alcanzaremos la inteligencia artificial general, es decir, comparable a la humana, en algún momento entre 2025 y 2031. Y de ahi, por crecimiento exponencial, a una velocidad vertiginosa que no podemos calcular (¿seis años, seis meses, seis segundos?), a la superinteligencia, es decir a algo muchísimo más inteligente que nosotros. A bastantes expertos esto les da miedo.

El neurocientífico Mariano Sigman me hizo una brillante observación el otro día: desde hace apenas algunas décadas, los seres humanos nos estamos planteando por primera vez en nuestra historia la idea de que somos capaces de acabar con la humanidad. Primero fue la energía nuclear, luego el calentamiento global, ahora la IA. Va todo tan deprisa. Sigo fascinada con los tiempos que me han tocado vivir, es más, estoy hipnotizada, turulata. Pero me empiezan a parecer un poco demasiado interesantes.
""",
    "comprension_lectora_preguntas": """
1. Comprensión lectora
[4 puntos en total]

1.1. Resuma el texto que ha leído sin reproducir frases de este. Utilice para ello un máximo de cincuenta palabras.
[1 punto]

1.2. Señale qué serie, de las cuatro que se proponen, es la única correcta para sustituir todas las palabras siguientes, subrayadas en el texto: vehemente, intringulis, mordida, exponencial.
[0,5 puntos. Si la respuesta es errónea, se descontarán 0,15 puntos; si no responde a la pregunta, no se aplicará ningún descuento.]
☐ febril, impedimentos, gastada, veloz
☐ ardiente, obstáculos, incompleta, repentino
☐ fuerte, secretos, picada, rápido
☐ irreflexiva, tejemanejes, roída, brusco

1.3. Indique los antecedentes de los (en «convertirlos en oro» y en «Los cambié por otros ), subrayados en el texto.
[1 punto]
a) los:
b) los:

1.4. Conteste únicamente DOS de las cuatro cuestiones siguientes sobre las lecturas (Nada, de Carmen Laforet, y La Fundación, de Antonio Buero Vallejo) y sobre las figuras retóricas que aparecen en el texto. Puede combinarlas como prefiera. En el caso de responder a tres o cuatro preguntas, solo se tendrán en cuenta las dos primeras.
[1,5 puntos en total. Se descontarán 0,25 puntos por cada pregunta de respuesta múltiple errónea.]

a) Sobre La Fundación, ¿cuál de las siguientes afirmaciones es incorrecta?
[0,75 puntos]
☐ La primera parte de la obra finaliza cuando el encargado descubre que el enfermo está muerto.
☐ A medida que Tomás regresa a la realidad, el escenario va cambiando.
☐ Tomás fue torturado.
☐ Max mata a Lino.

b) Sobre Nada, ¿por qué Juan y Gloria creen que Angustias se ha fugado con don Jerónimo? Utilice un máximo de cincuenta palabras.
[0,75 puntos]

c) Identifique y explique la figura retórica que aparece en el fragmento «¿seis años, seis meses, seis segundos?», subrayado en el texto. Utilice un máximo de cincuenta palabras.
[0,75 puntos]

d) Identifique la figura retórica que aparece en el fragmento «me empiezan a parecer un poco demasiado interesantes», subrayado en el texto.
[0,75 puntos]
☐ Hipérbole.
☐ Polisíndeton.
☐ Eufemismo.
☐ Metáfora.
""",
    "comprension_lectora_solucionario": """
SOLUCIONARIO Comprensión lectora (Opción B):
1.1: [1 punto] Respuesta abierta. Admite fracciones (1 / 0,75 / 0,5 / 0,25).
1.2: [0,5 puntos] Respuesta: ☐ fuerte, secretos, picada, rápido [Solucionario: línea 3].
1.3: [1 punto. 0,5p cada uno]
    a) los: compuestos tóxicos auríferos
    b) los: todos los apuntes
1.4: [1,5 puntos en total. Elegir DOS]
    a) Respuesta: ☐ Max mata a Lino. [Solucionario: línea 4]. [0,75 puntos]
    b) Respuesta: Porque en Nochebuena la han visto volver con él de madrugada. [0,75 puntos]
    c) Respuesta: Pregunta retórica, figura que consiste en formular una pregunta para la cual no se espera realmente una respuesta. En este caso, apunta a la relatividad del tiempo. [0,75 puntos]
    d) Respuesta: ☐ Eufemismo. [Solucionario: línea 3]. [0,75 puntos]
""",

    # --- Expresión escrita (B) ---
    "expresion_escrita_preguntas": """
2. Expresión escrita
[3 puntos en total]

2.1. Escriba un texto expositivo sobre el impacto de la inteligencia artificial en la sociedad contemporánea. Utilice para ello entre cien y ciento cincuenta palabras. Previamente, indique, en el cuadro que aparece a continuación, al menos los tres siguientes recursos: definición, clasificación y ejemplificación. Este cuadro puede servirle para redactar el texto.
[2 puntos]
Definición:
Clasificación:
Ejemplificación:

2.2. Complete las secuencias con la forma correcta de entre las dos que se proponen en cada caso.
[1 punto]
a) El __________ (apóstrofo / apóstrofe) es un signo ortográfico, utilizado para unir dos palabras, que indica la elisión de sonidos, generalmente una vocal.
b) No es difícil molestarte a __________ (ti / ti).
c) Por increíble que parezca, __________ (aun / aún) no ha llegado el diputado.
d) Lo cierto es que, __________ (cuanto / contra) más lo pienso, más segura estoy.
""",
    "expresion_escrita_solucionario": """
SOLUCIONARIO Expresión escrita (Opción B):
2.1: [2 puntos] Respuesta abierta (Texto expositivo). Parámetros: contenido (0,5p), léxico (0,5p), sintaxis (0,5p), estructura (0,5p). Penalización por extensión incorrecta. El cuadro no puntúa específicamente.
2.2: [1 punto. Cada espacio vale 0,25 puntos]
    a) El apóstrofo es un signo ortográfico, utilizado para unir dos palabras, que indica la elisión de sonidos, generalmente una vocal.
    b) No es difícil molestarte a ti.
    c) Por increíble que parezca, aún no ha llegado el diputado.
    d) Lo cierto es que, cuanto más lo pienso, más segura estoy.
"""
}

# ==============================================================================
# BLOQUE 3: PARTE COMÚN (Transcripción de Alta Fidelidad del Examen y Solucionario)
# ==============================================================================

SERIE_3_PARTE_COMUN = {
    "reflexion_linguistica_preguntas": """
PARTE COMÚN
3. Reflexión lingüística
[3 puntos en total]

3.1. Indique si una de las dos secuencias del par mínimo es agramatical o si existe un contraste semántico entre las dos secuencias del par. Si una es agramatical, especifique cuál es y explique a qué se debe la agramaticalidad. Si existe un contraste semántico, explique en qué consiste. La respuesta debe tener un máximo de cincuenta palabras y contener como máximo cuatro términos gramaticales relevantes. [1 punto]
a) Encontré las flores secas.
b) Encontré secas las flores.
☐ Secuencia agramatical: __________
☐ Contraste semántico
Términos gramaticales relevantes (un máximo de cuatro):
Explicación (un máximo de cincuenta palabras):

3.2. Escriba una secuencia gramatical semánticamente coherente de no más de veinte palabras que contenga, al menos, los siguientes cuatro elementos en el orden que considere oportuno: pronombre interrogativo, verbo transitivo, complemento predicativo y adverbio demostrativo. La secuencia puede contener oraciones subordinadas, pero no coordinadas ni yuxtapuestas. [1 punto]
Secuencia: __________
Pronombre interrogativo: __________ / Verbo transitivo: __________ / Complemento predicativo: __________ / Adverbio demostrativo: __________

3.3. Lea la siguiente lista de secuencias y, de entre las opciones que se ofrecen debajo, elija la única que identifica de manera correcta y ordenada la función sintáctica del elemento subrayado en cada una de las secuencias.
[0,5 puntos. Si la respuesta es errónea, se descontarán 0,15 puntos; si no se contesta la pregunta, no se aplicará ningún descuento.]
1. Sabía que las cosas no son en sí mismas alegres.
2. Los alumnos que habían aprobado estaban muy contentos.
3. Me percaté entonces de que la alegría es un estado del alma.
4. Es raro cómo se puede perder la inocencia de golpe.
☐ 1) complemento directo, 2) complemento del nombre, 3) complemento indirecto, 4) complemento circunstancial
☐ 1) complemento directo, 2) complemento del nombre, 3) complemento de régimen verbal, 4) sujeto
☐ 1) sujeto, 2) complemento circunstancial, 3) complemento de régimen verbal, 4) complemento del nombre
☐ 1) complemento directo, 2) complemento del nombre, 3) complemento indirecto, 4) sujeto

3.4. Responda a UNA de las dos cuestiones siguientes, relacionadas con la oración compuesta y con la estructura informativa de la oración.
[0,5 puntos]
a) A partir de las oraciones 1 y 2, construya una secuencia que establezca una relación ilativa entre ellas. Al construir dicha secuencia, los cambios deben ser mínimos.
1. Iremos a la playa.
2. Hace buen tiempo.
b) Reescriba la oración En su casa no admite mascotas de manera que el rema pase a ser tema. Al reescribir la oración, los cambios deben ser mínimos.
""",
    "reflexion_linguistica_solucionario": """
SOLUCIONARIO Reflexión lingüística (Parte Común):
3.1: [1 punto]
    - Opción elegida: Contraste semántico
    - Términos gramaticales relevantes (0,5p): complemento predicativo y complemento del nombre.
    - Explicación (0,5p): Existe contraste semántico entre las secuencias del par mínimo. En la primera oración el adjetivo 'secas' puede interpretarse como complemento predicativo o como complemento del nombre, mientras, en la segunda, solo puede interpretarse como complemento predicativo.
3.2: [1 punto. 0,25p por elemento en secuencia gramatical válida de <20 palabras]
    - Secuencia ejemplo: ¿Quién vio a María cansada ayer?
    - Pronombre interrogativo: quién
    - Verbo transitivo: ver
    - Complemento predicativo: cansada
    - Adverbio demostrativo: ayer
3.3: [0,5 puntos]
    - Respuesta correcta: ☐ 1) complemento directo, 2) complemento del nombre, 3) complemento de régimen verbal, 4) sujeto [Solucionario: línea 2].
3.4: [0,5 puntos. Elegir UNA]
    - Posible respuesta (a): Hace buen tiempo, así que iremos a la playa.
    - Posible respuesta (b): No admite mascotas en su casa.
"""
}