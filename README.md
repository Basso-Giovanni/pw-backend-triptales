# Backend del progetto TripTales
## Endpoints
### Users
<ul>
  <li><b>api/users/register/</b> -> Per registrare un nuovo utente. Parametri: username, email, password, bio e avatar (per il momento). Restituisce il token dell'utente.</li>
  <li><b>api/users/login/</b> -> Per ottenere il token passando username e password.</li>
  <li><b>api/users/profile/</b> -> Per ottenere le informazioni dell'utente passando il token.</li>
  <li><b>api/users/profile/update/</b> -> Per aggiornare le informazioni dell'utente passando il token.</li>
</ul>

### Trips
<ul>
  <li><b>api/trips/create/</b> -> Per creare un nuovo gruppo gita. Parametri: name e description. Nell'header ci deve essere il token.</li>
  <li><b>api/trips/join/</b> -> Per unirsi ad un gruppo gita.</li>
</ul>

### Images
<ul>
    <li><b>api/trips/images/</b> -> Carica immagine (POST, image-description, Authorization: token)</li>
    <li><b>api/trips/images/{pk}</b> -> Ottiene immagine (GET)</li>
</ul>