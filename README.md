##Telegram Birthday Reminder Bot

Este bot se encargará de recordarte dia a dia los cumpleaños de un calendario de Google. El archivo `main.py` deberá configurarse en el servidor con un crontab diario, de forma que solo te notifique los cumpleaños una sola vez.
El archivo `bot.py` deberá estar ejecutandose de forma contínua para poder interactuar con el Bot.

Para poder usar el BOT necesitamos tener:
- [ ] Una clave API de Google Calendar
- [ ] Un calendario de Google Calendar exclusivo para los eventos
- [ ] Un bot de Telegram
- [ ] Tu Chat ID. (En caso de usarse en un grupo, el Chat ID del grupo) 

### ¿Cómo crear una API de Google Calendar?
Proximamente ...

### ¿Cómo crear un Bot de Telegram?
Proximamente ...

### ¿Cómo obtener mi Chat ID?
Para encontrar tu Chat ID, envia `/start` a [@chatid_echo_bot](https://t.me/chatid_echo_bot). El número que te devuelve es tu Chat ID.
Si necesitas el Chat ID de un grupo, simplemente añade el bot al grupo y envia `/start`

### ¿Cómo crear un calendario en Google Calendar?
- Abre [Google Calendar](https://calendar.google.com/calendar/u/0/r?hl=es&pli=1) en un ordenador.
- A la izquierda, junto a "Otros calendarios", haz clic en Añadir otros calendarios Añadir y luego Crear un calendario.
- Escribe un nombre para tu calendario
- Haz clic en Crear calendario.

### ¿Cómo hacer público un calendario en Google Calendar?
Para que el bot pueda acceder a los eventos, necesita que sea un calendario público. 
- Abre [Google Calendar](https://calendar.google.com/calendar/u/0/r?hl=es&pli=1) en un ordenador.
- Arriba a la derecha, haz clic en Configuración 
- Haz clic en el nombre del calendario que quieras compartir.
- Abre Permisos de acceso.
- Marca la casilla que verás junto a "Compartir públicamente". 

### ¿Cuál es la ID de mi calendario?
- Abre [Google Calendar](https://calendar.google.com/calendar/u/0/r?hl=es&pli=1) en un ordenador.
- Arriba a la derecha, haz clic en Configuración 
- Haz clic en el nombre del calendario que quieras compartir.
- Busca el campo "ID del calendario".

### ¿Cómo añadir un cumpleaños en Google Calendar? (ORDENADOR)
- Abre [Google Calendar](https://calendar.google.com/calendar/u/0/r?hl=es&pli=1) en un ordenador.
- En la esquina superior izquierda, haz clic en Crear Añadir.
- Selecciona el calendario que creamos anteriormente para los cumpleaños.
- Escribe el título del evento, en este caso el nombre del cumpelañero.
- Selecciona "Repetir Anualmente"
- Selecciona "Todo el día" como duración del evento.
- Al principio de la página, haz clic en Guardar.

### ¿Cómo añadir un cumpleaños en Google Calendar? (TELÉFONO)
- Abre Google Calendar en tu teléfono
- Selecciona la opción de recordatorio, situada en la parte inferior derecha de la aplicación.
- Escribe el título del evento, en este caso el nombre del cumpelañero.
- Selecciona el calendario que creamos anteriormente para los cumpleaños.
- Selecciona "Repetir Anualmente"
- Selecciona "Todo el día" como duración del evento.
- Pulsa en guardar para crear dicho recordatorio.

