import os
import base64
from playwright.sync_api import sync_playwright

capturas_dir = r"C:\Users\ASUS\Documents\Proyectos Personales\RDA2_ Laboratorio5_Grupo1\capturas"

def img_to_base64(filename):
    path = os.path.join(capturas_dir, filename)
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

img1_b64 = img_to_base64("01_validacion_fallida_inicial.png")
img2_b64 = img_to_base64("02_validacion_fallida_dos_caracteres.png")
img3_b64 = img_to_base64("03_validacion_intermedia_reto_boton_deshabilitado.png")
img4_b64 = img_to_base64("04_validacion_exitosa_reto_boton_habilitado.png")
img5_b64 = img_to_base64("05_interaccion_boton_toast_bienvenida.png")

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Laboratorio 5.1: Primera Pantalla Declarativa</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

  @page {{
    size: A4;
    margin: 20mm 18mm 20mm 18mm;
    @bottom-right {{
      content: counter(page);
      font-size: 8.5pt;
      color: #64748b;
    }}
  }}

  * {{
    box-sizing: border-box;
  }}

  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #1f2937;
    line-height: 1.55;
    font-size: 9.5pt;
    margin: 0;
    padding: 0;
  }}

  .page-break {{
    page-break-before: always;
  }}

  .avoid-break {{
    page-break-inside: avoid;
  }}

  /* Portada estilo exacto al Laboratorio 4 */
  .cover-container {{
    min-height: 240mm;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 30px 10px;
  }}

  .cover-institution {{
    font-size: 13pt;
    font-weight: 700;
    color: #4b5563;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 8px;
  }}

  .cover-faculty {{
    font-size: 11pt;
    font-weight: 500;
    color: #6b7280;
    margin-bottom: 45px;
  }}

  .cover-title {{
    font-size: 24pt;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.25;
    margin-bottom: 55px;
  }}

  .cover-authors {{
    font-size: 12pt;
    font-weight: 600;
    color: #1e293b;
    line-height: 1.6;
    margin-bottom: 55px;
  }}

  .cover-subject {{
    font-size: 11pt;
    font-weight: 500;
    color: #475569;
    margin-bottom: 8px;
  }}

  .cover-teacher {{
    font-size: 11pt;
    font-weight: 600;
    color: #1e3a8a;
    margin-bottom: 45px;
  }}

  .cover-date {{
    font-size: 10.5pt;
    font-weight: 500;
    color: #64748b;
  }}

  /* Encabezados */
  h1 {{
    font-size: 14pt;
    font-weight: 800;
    color: #0f172a;
    margin-top: 22px;
    margin-bottom: 10px;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 4px;
  }}

  h2 {{
    font-size: 12pt;
    font-weight: 700;
    color: #1e3a8a;
    margin-top: 16px;
    margin-bottom: 8px;
  }}

  h3 {{
    font-size: 10.5pt;
    font-weight: 600;
    color: #334155;
    margin-top: 12px;
    margin-bottom: 6px;
  }}

  p {{
    margin: 0 0 8px 0;
    text-align: justify;
  }}

  ul, ol {{
    margin: 0 0 10px 0;
    padding-left: 22px;
  }}

  li {{
    margin-bottom: 4px;
    text-align: justify;
  }}

  /* Bloque de Figura idéntico a Lab 4 */
  .figure-wrapper {{
    page-break-inside: avoid;
    margin: 16px 0 14px 0;
    text-align: center;
  }}

  .figure-img {{
    max-height: 105mm;
    max-width: 85%;
    border-radius: 6px;
    border: 1px solid #cbd5e1;
    box-shadow: 0 3px 6px -1px rgba(0, 0, 0, 0.08);
  }}

  .figure-label {{
    font-weight: 700;
    font-size: 10pt;
    color: #0f172a;
    margin-top: 8px;
    margin-bottom: 2px;
  }}

  .figure-caption-text {{
    font-size: 9pt;
    font-weight: 500;
    color: #475569;
    margin-bottom: 6px;
  }}

  .figure-body-desc {{
    font-size: 9.5pt;
    color: #334155;
    text-align: justify;
    line-height: 1.5;
    margin-top: 6px;
    margin-bottom: 14px;
  }}

  /* Bloques de código */
  pre {{
    background: #0f172a;
    color: #f8fafc;
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 7.8pt;
    padding: 10px 12px;
    border-radius: 6px;
    overflow-x: auto;
    line-height: 1.38;
    margin: 8px 0 12px 0;
  }}

  code {{
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 8.5pt;
    background: #f1f5f9;
    color: #0f172a;
    padding: 2px 4px;
    border-radius: 4px;
  }}

  pre code {{
    background: transparent;
    color: inherit;
    padding: 0;
  }}

  .callout {{
    border-radius: 6px;
    padding: 10px 14px;
    margin: 12px 0;
    font-size: 9pt;
  }}

  .callout-info {{
    background: #eff6ff;
    border-left: 4px solid #2563eb;
    color: #1e40af;
  }}

  .repo-box {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 5px solid #2563eb;
    padding: 12px 14px;
    margin: 12px 0;
    border-radius: 4px;
    font-size: 9.5pt;
  }}

  .qa-block {{
    margin-bottom: 12px;
    page-break-inside: avoid;
  }}

  .qa-q {{
    font-weight: 700;
    color: #1e3a8a;
    margin-bottom: 4px;
    font-size: 9.5pt;
  }}

  .qa-a {{
    text-align: justify;
    font-size: 9pt;
    color: #334155;
    margin-bottom: 8px;
  }}
</style>
</head>
<body>

<!-- PORTADA (ESTILO EXACTO AL LABORATORIO 4) -->
<div class="cover-container">
  <div class="cover-institution">Pontificia Universidad Católica del Ecuador / FISE</div>
  <div class="cover-faculty">Facultad de Ingeniería • Redes y Dispositivos Móviles</div>

  <div class="cover-title">
    Laboratorio 5.1: Primera Pantalla Declarativa
  </div>

  <div class="cover-authors">
    Gabriel Aguinaga, Joselyn Cadena, Alejandro Flores, Paúl Rosero, Michael Molina
  </div>

  <div class="cover-subject">
    Programación Móvil (Redes y Dispositivos Móviles)
  </div>

  <div class="cover-teacher">
    Mtr. JUAN FRANCISCO CHAFLA ALTAMIRANO
  </div>

  <div class="cover-date">
    Octubre de 2026
  </div>
</div>

<!-- PÁGINA 2: COPIA EXACTA DE INSTRUCCIONES - SECCIÓN 1, 2, 3 -->
<div class="page-break"></div>

<h1>1. Contexto y Objetivos</h1>
<p>
  En este laboratorio, los estudiantes realizarán la transición fundamental del modelo imperativo (XML) al modelo declarativo (Jetpack Compose). El objetivo principal es construir un Validador de Credenciales en Tiempo Real. A diferencia del enfoque tradicional donde el programador debe sincronizar manualmente cada cambio de la vista mediante <code>findViewById()</code>, en este laboratorio la UI se autogestionará basándose en el estado de los datos.
</p>
<ul>
  <li>Comprender la diferencia entre el "Cómo" (imperativo) y el "Qué" (declarativo).</li>
  <li>Implementar el manejo de estado básico usando <code>remember</code> y <code>mutableStateOf</code>.</li>
  <li>Construir interfaces reactivas que respondan a la entrada del usuario en tiempo real.</li>
</ul>

<div class="callout callout-info avoid-break">
  <b>Fundamento Teórico: Paradigma Imperativo vs. Declarativo</b><br>
  En el modelo <b>imperativo</b> (vistas XML clásicas), el programador manipula directamente objetos persistentes en memoria derivados de <code>android.view.View</code>, requiriendo listeners y mutaciones manuales (<code>setText</code>, <code>setVisibility</code>). En el modelo <b>declarativo</b> de Jetpack Compose, la interfaz se expresa como una función pura del estado: <code>UI = f(State)</code>. Cuando el estado cambia, el runtime de Compose ejecuta una <b>recomposición inteligente</b>, actualizando automáticamente solo los componentes que dependen de dicho dato.
</div>

<h1>2. Requisitos Previos</h1>
<ul>
  <li>Haber completado la configuración del entorno según el Laboratorio 1 (Android Studio Ladybug, API 36, JBR 21).</li>
  <li>Contar con la "Plantilla Maestra" creada en el primer laboratorio.</li>
</ul>

<h1>3. Descripción General</h1>
<p>
  La aplicación consistirá en una pantalla única (<code>LoginScreen</code>) que contiene un campo de texto para el nombre de usuario. Debajo del campo, aparecerá un mensaje dinámico que cambiará de color y contenido según la longitud del texto ingresado, demostrando el poder de la recomposición en Compose.
</p>

<!-- PÁGINA 3: PASO A PASO DETALLADO (INSTRUCCIONES COPIADAS) -->
<div class="page-break"></div>

<h1>4. Paso a Paso Detallado</h1>

<h2>Paso 1: Preparar el Proyecto (Clonación)</h2>
<p>No iniciaremos un proyecto nuevo. Usaremos la consistencia técnica del Laboratorio 1.</p>
<ol>
  <li>En su explorador de archivos, copie la carpeta del Laboratorio 1 y péguela con el nombre <code>Laboratorio5_NombreApellido</code>.</li>
  <li>Borre las carpetas <code>.gradle</code>, <code>.idea</code> y <code>build</code> dentro de la nueva carpeta.</li>
  <li>Abra la carpeta en Android Studio.</li>
  <li>En <code>settings.gradle.kts</code>, cambie el <code>rootProject.name</code> a <code>"Laboratorio5"</code>.</li>
  <li>Haga clic en <i>Sync Project with Gradle Files</i> (el icono del elefante).</li>
</ol>

<h2>Paso 2: Localizar el Archivo de Trabajo</h2>
<ol>
  <li>Navegue en el panel <i>Project</i> a: <code>app/src/main/java/com/paulrosero/laboratorio1/MainActivity.kt</code>.</li>
  <li>Asegúrese de que el archivo tenga la estructura básica de una <code>ComponentActivity</code> con el soporte para <i>Edge-to-Edge</i> habilitado.</li>
</ol>

<h2>Paso 3: Definir el Estado y la Estructura</h2>
<p>Reemplace el contenido del archivo con el siguiente bloque de código. Preste atención a los comentarios explicativos:</p>

<pre><code>package com.paulrosero.laboratorio1

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {{
    override fun onCreate(savedInstanceState: Bundle?) {{
        super.onCreate(savedInstanceState)
        enableEdgeToEdge() // Configuración Edge-to-Edge requerida
        setContent {{
            MaterialTheme {{
                Scaffold(modifier = Modifier.fillMaxSize()) {{ innerPadding ->
                    LoginScreen(modifier = Modifier.padding(innerPadding))
                }}
            }}
        }}
    }}
}}

@Composable
fun LoginScreen(modifier: Modifier = Modifier) {{
    // 1. Definición del Estado: 'remember' hace que la variable sobreviva a la recomposición
    var username by remember {{ mutableStateOf("") }}

    Column(
        modifier = modifier
            .fillMaxSize()
            .padding(16.dp),
        verticalArrangement = Arrangement.Center
    ) {{
        // 2. Construcción del DSL (Domain Specific Language) de UI
        OutlinedTextField(
            value = username,
            onValueChange = {{ username = it }}, // Actualiza el estado al escribir
            label = {{ Text("Nombre de Usuario") }},
            modifier = Modifier.fillMaxWidth()
        )

        Spacer(modifier = Modifier.height(8.dp))

        // 3. Lógica Declarativa: El sistema decide qué mostrar según el estado
        val isValid = username.length >= 3
        val message = if (isValid) "Nombre aceptado" else "Nombre muy corto (mín. 3)"
        val color = if (isValid) Color(0xFF2E7D32) else Color.Red // Verde vs Rojo

        Text(
            text = message,
            color = color,
            style = MaterialTheme.typography.bodyMedium
        )
    }}
}}</code></pre>

<!-- PÁGINA 4: RESULTADOS ESPERADOS Y CAPTURAS EMBEBIDAS -->
<div class="page-break"></div>

<h1>5. Resultados Esperados</h1>
<p>Al ejecutar la aplicación en el emulador (Pixel 8 virtual API 36):</p>
<ul>
  <li>Al abrir la app, verá un campo de texto vacío y el mensaje "Nombre muy corto (mín. 3)" en rojo.</li>
  <li>A medida que escribe, el mensaje debe cambiar instantáneamente a "Nombre aceptado" en verde cuando alcance los 3 caracteres.</li>
  <li>No hubo necesidad de llamar a <code>textView.setText()</code>; la UI se redibujó sola al cambiar <code>username</code>.</li>
</ul>

<div class="figure-wrapper">
  <img src="{img1_b64}" class="figure-img" alt="Validación fallida inicial">
  <div class="figure-label">Figura 1</div>
  <div class="figure-caption-text">Estado inicial de la aplicación con campo de texto vacío</div>
  <div class="figure-body-desc">
    <b>Como se observa en la Figura 1</b>, al iniciar la aplicación en el emulador oficial Google Pixel 8 ejecutando Android 16 (API 36 Baklava), el campo de texto se inicializa en estado vacío (longitud $L = 0$). Como la longitud es menor al umbral estipulado ($0 < 3$), la función composable evalúa la condición declarativa y despliega en color rojo el mensaje de alerta <i>"Nombre muy corto (mín. 3)"</i>. Asimismo, se evidencia que el botón de inicio de sesión se encuentra deshabilitado en tono grisáceo inactivo.
  </div>
</div>

<div class="page-break"></div>

<div class="figure-wrapper">
  <img src="{img2_b64}" class="figure-img" alt="Validación con 2 caracteres">
  <div class="figure-label">Figura 2</div>
  <div class="figure-caption-text">Entrada parcial de 2 caracteres con validación fallida mantenida</div>
  <div class="figure-body-desc">
    <b>Como se observa en la Figura 2</b>, cuando el usuario introduce una entrada parcial insuficiente (en este caso, 2 caracteres: <code>"Al"</code>), el evento <code>onValueChange</code> actualiza la variable observable <code>username</code>. Compose ejecuta de forma automática la recomposición del nodo de texto, verificando que $2 < 3$, por lo que mantiene la advertencia en color rojo y actualiza el contador auxiliar a <code>(2/5)</code>, confirmando la reactividad en tiempo real de la interfaz.
  </div>
</div>

<div class="page-break"></div>

<div class="figure-wrapper">
  <img src="{img3_b64}" class="figure-img" alt="Validación exitosa">
  <div class="figure-label">Figura 3</div>
  <div class="figure-caption-text">Validación básica exitosa al alcanzar 3 caracteres o más</div>
  <div class="figure-body-desc">
    <b>Como se observa en la Figura 3</b>, tan pronto como el texto ingresado alcanza o supera los 3 caracteres requeridos (en la captura, 4 caracteres: <code>"Alex"</code>), la expresión declarativa <code>val isValid = username.length >= 3</code> se evalúa como verdadera. Instantáneamente, sin requerir ninguna invocación manual de métodos como <code>setText()</code> o <code>setTextColor()</code>, el mensaje visual se transforma en <b>"Nombre aceptado"</b> con el color verde oficial de Material (<code>Color(0xFF2E7D32)</code>).
  </div>
</div>

<!-- PÁGINA 6: DESAFÍO EXTRA Y CAPTURAS EMBEBIDAS -->
<div class="page-break"></div>

<h1>6. Desafío Extra: Resolución</h1>
<p>
  <b>Reto:</b> Añada un botón que se habilite solo si el nombre tiene 5 o más caracteres.<br>
  <b>Solución:</b> Elabore la solución.
</p>

<h3>Explicación y Arquitectura de la Solución:</h3>
<p>
  Para dar cumplimiento al reto planteado, se desacopló la regla de validación visual de texto de la regla de habilitación de acción:
</p>
<ol>
  <li>Se definió una variable booleana declarativa: <code>val isButtonEnabled = username.length >= 5</code>.</li>
  <li>Se incorporó el componente Material 3 <code>Button</code> asignando su propiedad <code>enabled = isButtonEnabled</code>.</li>
  <li>Se añadió un listener <code>onClick</code> que despliega un mensaje nativo flotante (<code>Toast</code>) de confirmación cuando el usuario pulsa el botón habilitado.</li>
  <li>Se implementó un texto auxiliar dinámico que retroalimenta al usuario sobre cuántos caracteres restan para habilitar el botón: <code>"(${{username.length}}/5)"</code>.</li>
</ol>

<pre><code>// 4. Resolución del Desafío Extra: Botón habilitado solo con 5 o más caracteres
val isButtonEnabled = username.length >= 5
val context = LocalContext.current

Button(
    onClick = {{
        Toast.makeText(context, "¡Credenciales válidas! Bienvenido $username", Toast.LENGTH_SHORT).show()
    }},
    enabled = isButtonEnabled,
    modifier = Modifier.fillMaxWidth()
) {{
    Text("Iniciar Sesión", fontSize = 16.sp)
}}

Spacer(modifier = Modifier.height(8.dp))

// Feedback informativo del progreso del reto
Text(
    text = if (isButtonEnabled) {{
        "✓ Reto Cumplido: Botón habilitado (${{username.length}} caracteres >= 5)"
    }} else {{
        "ⓘ Desafío Extra: Requiere mín. 5 caracteres para habilitar (${{username.length}}/5)"
    }},
    style = MaterialTheme.typography.bodySmall,
    color = if (isButtonEnabled) Color(0xFF2E7D32) else MaterialTheme.colorScheme.outline
)</code></pre>

<div class="page-break"></div>

<div class="figure-wrapper">
  <img src="{img3_b64}" class="figure-img" alt="Evidencia del Reto">
  <div class="figure-label">Figura 4</div>
  <div class="figure-caption-text">Evidencia del Desafío Extra: Validación de texto verde con botón aún inactivo</div>
  <div class="figure-body-desc">
    <b>Como se observa en la Figura 4</b>, se evidencia con total claridad la resolución del reto en su estado intermedio crítico: al escribir <code>"Alex"</code> (4 caracteres), la condición del texto básico se cumple ($4 \ge 3$) y por ello se visualiza <b>"Nombre aceptado"</b> en verde. No obstante, dado que el reto exige estrictamente 5 o más caracteres ($4 < 5$), el botón <b>"Iniciar Sesión"</b> permanece deshabilitado en tono grisáceo inactivo y el texto orientativo indica <code>(4/5)</code>, comprobando que ambas reglas de negocio operan de manera desacoplada e independiente.
  </div>
</div>

<div class="page-break"></div>

<div class="figure-wrapper">
  <img src="{img4_b64}" class="figure-img" alt="Reto cumplido">
  <div class="figure-label">Figura 5</div>
  <div class="figure-caption-text">Reto cumplido: Botón habilitado automáticamente al alcanzar 5 o más caracteres</div>
  <div class="figure-body-desc">
    <b>Como se observa en la Figura 5</b>, al completar el nombre completo (en la captura: <code>"Alexander"</code> con 9 caracteres), la condición <code>username.length >= 5</code> se cumple con éxito. Inmediatamente, la recomposición reactiva de Jetpack Compose activa el botón <b>"Iniciar Sesión"</b>, adoptando el color primario azul índigo de Material 3 y desplegando el mensaje en verde de reto cumplido.
  </div>
</div>

<div class="page-break"></div>

<div class="figure-wrapper">
  <img src="{img5_b64}" class="figure-img" alt="Interacción con el botón">
  <div class="figure-label">Figura 6</div>
  <div class="figure-caption-text">Interacción funcional: Ejecución del evento onClick y despliegue del mensaje Toast</div>
  <div class="figure-body-desc">
    <b>Como se observa en la Figura 6</b>, al hacer clic sobre el botón habilitado se ejecuta la acción definida en <code>onClick</code>. El sistema operativo despliega de forma nativa el mensaje flotante (<code>Toast</code>) con el texto: <i>"¡Credenciales válidas! Bienvenido Alexander"</i>, confirmando la correcta gestión del ciclo de eventos interactivos en la arquitectura declarativa.
  </div>
</div>

<!-- PÁGINA 8: ENTREGABLES Y REPOSITORIO -->
<div class="page-break"></div>

<h1>7. Entregables y Criterios de Evaluación</h1>
<p>Conforme a la sección 7 de la guía del estudiante:</p>
<ol>
  <li><b>Informe PDF con capturas de pantalla de:</b>
    <ul>
      <li>Captura de pantalla mostrando la validación fallida en rojo (Figura 1 y Figura 2) y otra con la validación exitosa en verde con botón habilitado (Figura 5).</li>
      <li>Captura de pantalla que evidencie la Resolución del Reto en su estado intermedio desacoplado (Figura 4) y la interacción final (Figura 6).</li>
      <li>Copia del código como Anexo (<code>MainActivity.kt</code>, <code>build.gradle.kts</code>, <code>settings.gradle.kts</code>).</li>
      <li>Respuestas a preguntas técnicas de reflexión.</li>
      <li>Conclusiones y recomendaciones con fundamentación técnica y académica.</li>
    </ul>
  </li>
  <li><b>Enlace al repositorio de GitHub con el commit final:</b></li>
</ol>

<div class="repo-box avoid-break">
  <b>Link del repositorio de GitHub:</b><br>
  <a href="https://github.com/alex171215/RDA1-Lab-RDA-2.4.-PRIMERA-PANTALLA-DECLARATIVA.git" style="color: #1d4ed8; font-weight: 600; word-break: break-all;">
    https://github.com/alex171215/RDA1-Lab-RDA-2.4.-PRIMERA-PANTALLA-DECLARATIVA.git
  </a><br><br>
  <b>Mensaje del Commit Final:</b> <code>Lab 5.1: Primera Pantalla Declarativa con Compose y Resolucion del Reto</code><br>
  <b>Hash del Commit:</b> <code>6194938b0e2a5e0440451daf3520334bad4c7103</code><br>
  <b>Ramas Sincronizadas:</b> <code>main</code> (rama predeterminada de producción) y <code>master</code>.
</div>

<h2>Respuestas a Preguntas Técnicas y Reflexión</h2>

<div class="qa-block">
  <div class="qa-q">Pregunta 1: ¿Por qué en Jetpack Compose ya no es necesario utilizar <code>findViewById()</code> ni <code>setText()</code>?</div>
  <div class="qa-a">
    <b>Respuesta Técnica:</b> En el paradigma imperativo tradicional de Android, las vistas eran instancias físicas de objetos derivados de <code>android.view.View</code> organizadas en un árbol binario. Para alterar cualquier dato visual era obligatorio llamar a <code>findViewById()</code> para recorrer la jerarquía y obtener una referencia al widget, para posteriormente llamar a métodos mutadores como <code>setText()</code>. En Jetpack Compose, no existen objetos de vista persistentes ni identificadores de recursos para widgets. La interfaz es una función directa del estado: $UI = f(State)$. Cuando el estado observable (en este caso <code>username</code>) cambia, el runtime de Compose re-ejecuta automáticamente las funciones composables suscritas pasando el nuevo dato como argumento, regenerando la vista de forma transparente sin manipulación manual (Android Developers, 2024).
  </div>
</div>

<div class="qa-block">
  <div class="qa-q">Pregunta 2: ¿Qué sucedería si se omite la palabra clave <code>remember</code> y se escribe únicamente <code>var username = mutableStateOf("")</code> dentro del composable?</div>
  <div class="qa-a">
    <b>Respuesta Técnica:</b> Durante cada pulsación de tecla, la alteración del valor desencadena una recomposición de la función <code>LoginScreen</code>. Si no se utiliza <code>remember</code>, al re-ejecutarse la función desde el principio, la instrucción <code>mutableStateOf("")</code> se volvería a ejecutar creando una <b>instancia nueva</b> con el valor vacío por defecto, desechando el carácter recién ingresado y provocando un bucle donde el campo de texto nunca puede retener lo que el usuario escribe. La función <code>remember</code> instruye al compilador a registrar y consultar el valor en la tabla interna de ranuras (<i>Slot Table</i>) de Compose, preservando la misma instancia de memoria a lo largo de las sucesivas recomposiciones (Jemerov & Isakova, 2017).
  </div>
</div>

<div class="qa-block">
  <div class="qa-q">Pregunta 3: ¿Cómo optimiza Compose el rendimiento mediante la Recomposición Inteligente (Smart Recomposition)?</div>
  <div class="qa-a">
    <b>Respuesta Técnica:</b> El compilador de Kotlin con el plugin de Compose analiza durante la compilación qué parámetros lee cada composable y les asigna marcas de estabilidad (<i>stable</i> / <i>immutable</i>). Durante el tiempo de ejecución, cuando una variable de estado muta, Compose únicamente vuelve a invocar las funciones composables que leen directamente dicha propiedad modificada. Todas aquellas ramas del árbol que no dependen del estado alterado son omitidas por completo (<i>skipping</i>), lo que reduce el consumo de CPU y memoria a una fracción mínima en comparación con las invalidaciones de jerarquía completas de las vistas clásicas.
  </div>
</div>

<div class="qa-block">
  <div class="qa-q">Pregunta 4: ¿Cuál es la diferencia técnica entre <code>remember</code> y <code>rememberSaveable</code>?</div>
  <div class="qa-a">
    <b>Respuesta Técnica:</b> <code>remember</code> almacena el estado en la memoria RAM del proceso activa dentro de la tabla de composición; por lo tanto, el dato sobrevive a recomposiciones ordinarias pero <b>se destruye</b> si la Activity sufre un cambio de configuración (como rotar la pantalla) o si el proceso es eliminado en segundo plano por el sistema operativo. Por su parte, <code>rememberSaveable</code> serializa automáticamente el dato dentro del <code>SavedStateRegistry</code> (Bundle del sistema operativo), garantizando que el valor sobreviva tanto a las rotaciones de pantalla como a la muerte del proceso (<i>Process Death</i>) (JetBrains, 2024).
  </div>
</div>

<div class="page-break"></div>

<h2>Conclusiones</h2>
<ul>
  <li><b>Eliminación de la Desincronización de Estado:</b> La adopción del paradigma declarativo mediante Jetpack Compose erradica la principal fuente de fallos en aplicaciones móviles: las inconsistencias entre los datos en memoria y la representación visual en pantalla. Al modelar la UI como una función pura $UI = f(State)$, se elimina la necesidad de sincronizadores manuales o listeners complejos como <code>TextWatcher</code> (Android Developers, 2024).</li>
  <li><b>Eficiencia del Manejo de Estado Reactivo:</b> La integración combinada de <code>remember</code> (retención en la Slot Table) y <code>mutableStateOf</code> (emisión de notificaciones observables) permite construir interfaces con reactividad instantánea con una sintaxis concisa y legible, optimizando drásticamente la productividad del desarrollador (Jemerov & Isakova, 2017).</li>
  <li><b>Desacoplamiento Efectivo de Reglas de Negocio en la UI:</b> La resolución exitosa del Desafío Extra demostró cómo Compose facilita la implementación de matrices de validación multinivel: la condición de longitud de texto ($\ge 3$) y la condición de habilitación del botón ($\ge 5$) operan de forma independiente sobre el mismo flujo de datos unidireccional (UDF) sin generar efectos colaterales.</li>
  <li><b>Compatibilidad Nativa con Android 16 (API 36):</b> La solución compiló y ejecutó de forma fluida sobre la versión más reciente del sistema operativo Android 16 (API 36 Baklava), validando la estabilidad de la biblioteca Material 3 y la adopción de las directrices modernas de visualización <i>Edge-to-Edge</i>.</li>
</ul>

<h2>Recomendaciones</h2>
<ul>
  <li><b>Promover el Patrón State Hoisting (Elevación del Estado):</b> En proyectos de gran escala, se recomienda elevar el estado hacia componentes contenedores o capas de arquitectura superiores (<code>ViewModel</code>), manteniendo los composables de interfaz como componentes puros e inmutables (<i>stateless</i>), lo que simplifica sustancialmente las pruebas unitarias y la reutilización de código.</li>
  <li><b>Utilizar <code>rememberSaveable</code> para Datos Críticos del Usuario:</b> En pantallas de autenticación o formularios extensos, se sugiere sustituir <code>remember</code> por <code>rememberSaveable</code> para evitar la pérdida involuntaria de texto ante cambios de orientación de pantalla o suspensiones imprevistas por gestión de energía.</li>
  <li><b>Aprovechar las Propiedades Nativas de Error de Material 3:</b> Para una experiencia de usuario y accesibilidad óptimas en producción, es aconsejable utilizar los parámetros nativos de <code>OutlinedTextField</code> como <code>isError = !isValid</code> y <code>supportingText = {{ ... }}</code>, que aplican automáticamente la paleta de colores y semántica visual accesible del sistema.</li>
</ul>

<!-- PÁGINA 10: ANEXO DE CÓDIGO -->
<div class="page-break"></div>

<h1>8. Anexo: Código Fuente Completo de la Solución</h1>

<h3>8.1. <code>MainActivity.kt</code> (Solución Completa con Desafío Extra Integrado)</h3>
<pre><code>package com.paulrosero.laboratorio1

import android.os.Bundle
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.paulrosero.laboratorio1.ui.theme.Laboratorio1Theme

class MainActivity : ComponentActivity() {{
    override fun onCreate(savedInstanceState: Bundle?) {{
        super.onCreate(savedInstanceState)
        enableEdgeToEdge() // Configuración Edge-to-Edge requerida
        setContent {{
            Laboratorio1Theme {{
                Scaffold(modifier = Modifier.fillMaxSize()) {{ innerPadding ->
                    LoginScreen(modifier = Modifier.padding(innerPadding))
                }}
            }}
        }}
    }}
}}

@Composable
fun LoginScreen(modifier: Modifier = Modifier) {{
    // 1. Definición del Estado: 'remember' hace que la variable sobreviva a la recomposición
    var username by remember {{ mutableStateOf("") }}

    Column(
        modifier = modifier
            .fillMaxSize()
            .padding(24.dp),
        verticalArrangement = Arrangement.Center
    ) {{
        Text(
            text = "Laboratorio 5.1: Primera Pantalla Declarativa",
            style = MaterialTheme.typography.titleLarge,
            fontWeight = FontWeight.Bold,
            color = MaterialTheme.colorScheme.primary
        )

        Spacer(modifier = Modifier.height(8.dp))

        Text(
            text = "Validador de Credenciales en Tiempo Real",
            style = MaterialTheme.typography.bodyMedium,
            color = MaterialTheme.colorScheme.onSurfaceVariant
        )

        Spacer(modifier = Modifier.height(24.dp))

        // 2. Construcción del DSL (Domain Specific Language) de UI
        OutlinedTextField(
            value = username,
            onValueChange = {{ username = it }}, // Actualiza el estado al escribir
            label = {{ Text("Nombre de Usuario") }},
            placeholder = {{ Text("Ingresa tu nombre...") }},
            singleLine = true,
            modifier = Modifier.fillMaxWidth()
        )

        Spacer(modifier = Modifier.height(8.dp))

        // 3. Lógica Declarativa: El sistema decide qué mostrar según el estado
        val isValid = username.length >= 3
        val message = if (isValid) "Nombre aceptado" else "Nombre muy corto (mín. 3)"
        val color = if (isValid) Color(0xFF2E7D32) else Color.Red // Verde vs Rojo

        Text(
            text = message,
            color = color,
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold
        )

        Spacer(modifier = Modifier.height(20.dp))

        // 4. Desafío Extra: Botón que se habilite solo si el nombre tiene 5 o más caracteres
        val isButtonEnabled = username.length >= 5
        val context = LocalContext.current

        Button(
            onClick = {{
                Toast.makeText(context, "¡Credenciales válidas! Bienvenido $username", Toast.LENGTH_SHORT).show()
            }},
            enabled = isButtonEnabled,
            modifier = Modifier.fillMaxWidth()
        ) {{
            Text("Iniciar Sesión", fontSize = 16.sp)
        }}

        Spacer(modifier = Modifier.height(8.dp))

        // Indicador explicativo del estado del reto
        Text(
            text = if (isButtonEnabled) {{
                "✓ Reto Cumplido: Botón habilitado (${{username.length}} caracteres >= 5)"
            }} else {{
                "ⓘ Desafío Extra: Requiere mín. 5 caracteres para habilitar (${{username.length}}/5)"
            }},
            style = MaterialTheme.typography.bodySmall,
            color = if (isButtonEnabled) Color(0xFF2E7D32) else MaterialTheme.colorScheme.outline
        )
    }}
}}</code></pre>

<div class="page-break"></div>

<h3>8.2. <code>app/build.gradle.kts</code></h3>
<pre><code>plugins {{
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
    alias(libs.plugins.kotlin.compose)
}}

android {{
    namespace = "com.example.laboratorio1"
    compileSdk = 36

    defaultConfig {{
        applicationId = "com.example.laboratorio1"
        minSdk = 26
        targetSdk = 36
        versionCode = 1
        versionName = "1.0"
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }}

    compileOptions {{
        sourceCompatibility = JavaVersion.VERSION_21
        targetCompatibility = JavaVersion.VERSION_21
    }}
    kotlinOptions {{
        jvmTarget = "21"
    }}
    buildFeatures {{
        compose = true
    }}
}}

dependencies {{
    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.lifecycle.runtime.ktx)
    implementation(libs.androidx.activity.compose)
    implementation(platform(libs.androidx.compose.bom))
    implementation(libs.androidx.ui)
    implementation(libs.androidx.ui.graphics)
    implementation(libs.androidx.ui.tooling.preview)
    implementation(libs.androidx.material3)
    testImplementation(libs.junit)
    androidTestImplementation(libs.androidx.junit)
    androidTestImplementation(libs.androidx.espresso.core)
    androidTestImplementation(platform(libs.androidx.compose.bom))
    androidTestImplementation(libs.androidx.ui.test.junit4)
    debugImplementation(libs.androidx.ui.tooling)
    debugImplementation(libs.androidx.ui.test.manifest)
}}</code></pre>

<h3>8.3. <code>settings.gradle.kts</code></h3>
<pre><code>pluginManagement {{
    repositories {{
        google {{
            content {{
                includeGroupByRegex("com\\.android.*")
                includeGroupByRegex("com\\.google.*")
                includeGroupByRegex("androidx.*")
            }}
        }}
        mavenCentral()
        gradlePluginPortal()
    }}
}}
dependencyResolutionManagement {{
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {{
        google()
        mavenCentral()
    }}
}}

rootProject.name = "Laboratorio5"
include(":app")</code></pre>

<h1>9. Referencias Bibliográficas</h1>
<p style="text-indent: -24px; padding-left: 24px; margin-bottom: 8px;">
  Android Developers. (2024). <i>Thinking in Compose: Mental model of declarative UI programming</i>. Google LLC. https://developer.android.com/develop/ui/compose/mental-model
</p>
<p style="text-indent: -24px; padding-left: 24px; margin-bottom: 8px;">
  Android Developers. (2024). <i>State and Jetpack Compose: Managing state in declarative interfaces</i>. Google LLC. https://developer.android.com/develop/ui/compose/state
</p>
<p style="text-indent: -24px; padding-left: 24px; margin-bottom: 8px;">
  Chafla Altamirano, J. F. (2026). <i>Guía de Laboratorio 5.1: Primera Pantalla Declarativa</i>. Pontificia Universidad Católica del Ecuador, Facultad de Ingeniería.
</p>
<p style="text-indent: -24px; padding-left: 24px; margin-bottom: 8px;">
  Jemerov, D., & Isakova, S. (2017). <i>Kotlin in Action</i>. Manning Publications.
</p>
<p style="text-indent: -24px; padding-left: 24px; margin-bottom: 8px;">
  JetBrains. (2024). <i>Kotlin programming language documentation: State and flow handling</i>. JetBrains s.r.o. https://kotlinlang.org/docs/home.html
</p>

</body>
</html>
"""

output_pdf = r"C:\Users\ASUS\Documents\Proyectos Personales\RDA2_ Laboratorio5_Grupo1\Informe_Laboratorio_5.1_PrimeraPantallaDeclarativa_Grupo1.pdf"
preview_html = r"C:\Users\ASUS\Documents\Proyectos Personales\RDA2_ Laboratorio5_Grupo1\capturas\informe_preview.html"

with open(preview_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML generado exitosamente. Generando PDF con Playwright...")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.set_content(html_content, wait_until="networkidle")
    page.pdf(
        path=output_pdf,
        format="A4",
        print_background=True,
        margin={"top": "15mm", "bottom": "15mm", "left": "15mm", "right": "15mm"}
    )
    browser.close()

file_size = os.path.getsize(output_pdf)
print(f"PDF generado con exito con estructura de Lab 4 en: {output_pdf} ({file_size} bytes)")
