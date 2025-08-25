| Video | Audio |
| --- | --- |
| FADE IN:   Ver referencia 1 | Esta es la función que más usarás de un asistente IA de programación: recibir sugerencias en el editor mientras escribes tu código. |
| INS.WIPE: Tipos de sugerencias  INS.BULLETS: Finalizaciones de código  Ver referencia 2       Sugerencias de próxima edición (NES)  Ver referencia 3  Ver video | Los asistentes online ofrecen dos tipos de sugerencias:  Finalizaciones de código,  completan la línea actual o varios renglones y se adaptan a tu estilo de programación considerando el código que escribes. Además te permiten aceptar toda la sugerencia, solo una parte o ignorarla.  Sugerencias de próxima edición, predicen el siguiente cambio que podrías realizar, desde un símbolo hasta una función completa, basándose en lo que has escrito, te ayuda a anticipar ubicaciones y contenido de futuras modificaciones.  En ambos casos, las sugerencias se muestran como texto fantasma en un espacio de código. |
| INS.WIPE: Espacio de código      INS.NUMS: Selecciona ‘Crear repositorio’    Llena el formulario      Crea el espacio de código       Busca la extensión     Activa el asistente   Ver video | Un espacio de código es el entorno donde administras proyectos, editas archivos y utilizas al asistente IA. Sigue estos pasos para crearlo y configurarlo:  Haz clic en Crear repositorio en la página de inicio de la plataforma.  Completa los campos de nombre y descripción, mantén la configuración por defecto y presiona Crear repositorio.  Haz clic en Crear un espacio de código, y confirma la acción. A continuación la plataforma te redireccionará al espacio de código.  Selecciona la opción Extensiones del menú lateral, busca copilot en la barra de búsqueda.  Elige el primer resultado y haz clic en instalar para activar el asistente IA.  Ahora tu espacio de código está listo. |
| INS.WIPE: Recibe las sugerencias    INS.NUMS: Crea un archivo INS.TXT: calculadora.py     Escribe código     Acepta sugerencias completas   Acepta palabra por palabra    Navega entre alternativas  Ver video   Explora ediciones NES  Ver video | Para recibir sugerencias mientras desarrollas, realiza lo siguiente:  Crea un archivo nuevo con la extensión del lenguaje de programación que quieras usar. Por ejemplo calculadora punto pe i griega para Python.  Empieza a escribir tu código. El asistente mostrará las sugerencias en texto fantasma.  Haz clic en Aceptar para aceptar toda la sugerencia.  Selecciona Aceptar palabra para aceptar palabra por palabra mientras analizas la propuesta.  Usa las flechas de navegación para moverte entre las alternativas que ofrece el asistente.    Explora la flecha verde cuando aparezca en el margen, significa que hay una sugerencia de próxima edición NES. Ahí puedes analizar, aceptar o rechazar la sugerencia. |
| FADE OUT | A medida que avances en tu desarrollo, el asistente te ofrecerá distintos tipos de sugerencias. Analízalas con tu criterio de programador y selecciona únicamente las que te resulten útiles. |


Referencias gráficas
Referencia 1

Las sugerencias son el texto que aparece en gris. Para animación puede ser texto simulado para diferenciar entre código y sugerencias.

Referencia 2

En el cuadro rojo se observan las opciones para Aceptar toda la sugerencia (Accept) y aceptar solo una parte (Accept World).

Referencia 3

En el cuadro rojo se muestran las opciones del NES, el menú aparece cuando el cursor pasa por la flecha azul

Código 1
def suma(a, b):
return a + b

def resta(a, b):
return a - b

def multiplicacion(a, b):
resultado = 0
resultado = a * b
return resultado

def division(a, b):
if b == 0:
raise ValueError("No se puede dividir por cero")
return a / b

def potencia(base, exponente):
resultado = 1
for _ in range(exponente):
resultado *= base
return resultado

def raiz_cuadrada(numero):
if numero < 0:
raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
return numero ** 0.5

Código 2
def suma(a, b):
return a + b

def resta(a, b):
return a - b

def multiplicacion(a, b):
return a * b

def division(a, b):
if b != 0:
return a / b
else:
return "Error: División por cero no permitida."

def potencia(a, b):
return a ** b

Fuentes:
https://code.visualstudio.com/blogs/2025/02/12/next-edit-suggestions
https://code.visualstudio.com/docs/copilot/ai-powered-suggestions#_next-edit-suggestions
https://www.youtube.com/@code/videos
https://code.visualstudio.com/docs/editing/userdefinedsnippets
https://docs.github.com/es/copilot/how-tos/get-code-suggestions/get-code-suggestions
