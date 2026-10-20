package com.paulrosero.laboratorio1

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

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge() // Configuracion Edge-to-Edge requerida
        setContent {
            Laboratorio1Theme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    LoginScreen(modifier = Modifier.padding(innerPadding))
                }
            }
        }
    }
}

@Composable
fun LoginScreen(modifier: Modifier = Modifier) {
    // 1. Definicion del Estado: 'remember' hace que la variable sobreviva a la recomposicion
    var username by remember { mutableStateOf("") }

    Column(
        modifier = modifier
            .fillMaxSize()
            .padding(24.dp),
        verticalArrangement = Arrangement.Center
    ) {
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

        // 2. Construccion del DSL (Domain Specific Language) de UI
        OutlinedTextField(
            value = username,
            onValueChange = { username = it }, // Actualiza el estado al escribir
            label = { Text("Nombre de Usuario") },
            placeholder = { Text("Ingresa tu nombre...") },
            singleLine = true,
            modifier = Modifier.fillMaxWidth()
        )

        Spacer(modifier = Modifier.height(8.dp))

        // 3. Logica Declarativa: El sistema decide que mostrar segun el estado
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

        // 4. Desafio Extra: Boton que se habilite solo si el nombre tiene 5 o mas caracteres
        val isButtonEnabled = username.length >= 5
        val context = LocalContext.current

        Button(
            onClick = {
                Toast.makeText(context, "¡Credenciales válidas! Bienvenido $username", Toast.LENGTH_SHORT).show()
            },
            enabled = isButtonEnabled,
            modifier = Modifier.fillMaxWidth()
        ) {
            Text("Iniciar Sesión", fontSize = 16.sp)
        }

        Spacer(modifier = Modifier.height(8.dp))

        // Indicador explicativo del estado del reto
        Text(
            text = if (isButtonEnabled) {
                "✓ Reto Cumplido: Botón habilitado (${username.length} caracteres >= 5)"
            } else {
                "ⓘ Desafío Extra: Requiere mín. 5 caracteres para habilitar (${username.length}/5)"
            },
            style = MaterialTheme.typography.bodySmall,
            color = if (isButtonEnabled) Color(0xFF2E7D32) else MaterialTheme.colorScheme.outline
        )
    }
}
