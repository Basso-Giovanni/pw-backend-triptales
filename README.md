# Backend del progetto TripTales
## Endpoints
### Users
<ul>
  <li><b>users/register/</b> -> Per registrare un nuovo utente. Parametri: username, email, password, bio e avatar (per il momento). Restituisce il token dell'utente.</li>
  <li><b>users/login/</b> -> Per ottenere il token passando username e password.</li>
  <li><b>users/profile/</b> -> Per ottenere le informazioni dell'utente passando il token.</li>
  <li><b>users/profile/update/</b> -> Per aggiornare le informazioni dell'utente passando il token.</li>
</ul>

### Trips
<ul>
  <li><b>trips/create/</b> -> Per creare un nuovo gruppo gita. Parametri: name e description. Nell'header ci deve essere il token.</li>
  <li><b>trips/join/</b> -> Per unirsi ad un gruppo gita.</li>
</ul>

### Images
<ul>
    <li><b>trips/images/</b> -> Carica immagine (POST, image-description, Authorization: token)</li>
    <li><b>trips/images/{pk}/</b> -> Ottiene immagine (GET) oppure elimina/aggiorna immagine (DELETE/PATCH o PUT)</li>
</ul>

### Post
<ul>
    <li><b>posts/create/</b> -> Per creare un nuovo post</li>
    <li><b>posts/{pk}/</b> -> Per visualizzare un post (GET), per cancellarlo (solo il proprietario) (DELETE), per aggiornarlo (PATCH)</li>
    <li><b>posts/{pk}/like/</b> -> Per mettere mi piace</li>
    <li><b>posts/{pk}/unlike/</b> -> Per togliere mi piace</li>
    <li><b>posts/{pk}/comments/</b> -> Restituisce tutti i commenti del post</li>
    <li><b>posts/{pk}/comments/create/</b> -> Crea nuovo commento per il post</li>
    <li><b>posts/{pk}/comments/{pk}/</b> -> Vedi commento (GET) o elimina commento (DELETE)</li>
</ul>