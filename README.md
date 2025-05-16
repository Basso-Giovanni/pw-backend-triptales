# TripTales - Diario di Gita con Intelligenza Artificiale
TripTales è un'app Android pensata per studenti in gita scolastica. Permette di documentare e condividere in modo collaborativo momenti salienti attraverso foto, commenti e geolocalizzazione, arricchiti con funzionalità smart offerte da ML Kit di Google. Questo è il backend side del progetto.

## Obiettivo del progetto
L'obiettivo è realizzare un'applicazione mobile che:

- Favorisca la collaborazione tra studenti durante una gita.
- Sfrutti intelligenza artificiale e geolocalizzazione per migliorare l'esperienza educativa.
- Permetta la documentazione multimediale tramite foto, testi, mappe e badge gamificati.

## Django Rest Framework
- Autenticazione con JWT.
- API REST per gestione utenti, gruppi, post, badge, commenti e immagini.
- Storage immagini e metadati (OCR, oggetti rilevati, ecc.). **In realtà non so se si usa**

## Endpoints
### Users
Endpoint per la gestione degli utenti.
<ul>
  <li>POST - <b>users/register/</b> -> Per registrare un nuovo utente. Body: username, email, password, bio e avatar. Restituisce il token dell'utente.</li>
  <li>POST - <b>users/login/</b> -> Per ottenere il token. Body: username e password.</li>
  <li>GET - <b>users/profile/</b> -> Per ottenere le informazioni dell'utente. Header: Authorization Token <i>token_utente</i>. Restituisce: id, username, email, bio e avatar.</li>
  <li>GET - <b>users/profile/{int:user_id}/</b> -> Per ottenere le informazioni dell'utente specificato. Header: Authorization Token <i>token_utente</i>. Restituisce: id, username, email, bio e avatar.</li>
  <li>PATCH - <b>users/profile/update/</b> -> Per aggiornare le informazioni dell'utente. Header: Authorization Token <i>token_utente</i>. Body: tutti i campi che si vogliono aggiornare.</li>
  <li>GET - <b>users/my-trips/</b> -> Per vedere i gruppi a cui l'utente è iscritto. Header: Authorization Token <i>token_utente</i>. Restituisce: un array di ID dei gruppi a cui è iscritto.</li>
</ul>

### Trips
Endpoint per la gestione dei gruppi gita.
<ul>
  <li>POST - <b>trips/create/</b> -> Per creare un nuovo gruppo gita. Header: Authorization Token <i>token_utente</i>. Body: name e description.</li>
  <li>GET - <b>trips/info/{int:id_gruppo}/</b> -> Per vedere info del gruppo specificato. Header: Authorization Token <i>token_utente</i>. Restituisce: tutte le info del gruppo gita.</li>
  <li>POST - <b>trips/join/{int:id_gruppo}/</b> -> Per unirsi ad un gruppo gita. Header: Authorization Token <i>token_utente</i>.</li>
  <li>GET - <b>trips/{int:id_gruppo}/posts/</b> -> Per ottenere post di un gruppo. Header: Authorization Token <i>token_utente</i>. Restituisce un array con i post.</li>
  <li>GET - <b>trips/{int:id_gruppo}/top-like/</b> -> Per ottenere la classifica dei post più piaciuti. Header: Authorization Token <i>token_utente</i>.</li>
  <li>GET - <b>trips/{int:id_gruppo}/top-like-user/</b> -> Per ottenere la classifica degli utenti più piaciuti. Header: Authorization Token <i>token_utente</i>.</li>
  <li>GET - <b>trips/{int:id_gruppo}/top-posters/</b> -> Per ottenere la classifica degli utenti che hanno pubblicato più post. Header: Authorization Token <i>token_utente</i>.</li>
</ul>

### Images
Endpoint per la gestione delle immagini (nei post).
<ul>
    <li>POST - <b>images/create/</b> -> Per caricare un'immagine. Header: Authorization Token <i>token_utente</i>. Body: image (file), description, latitude e longitude.</li>
    <li>GET - <b>images/{int:id_img}/</b> -> Per ottenere l'immagine. Header: Authorization Token <i>token_utente</i>.</li>
</ul>

### Post
Endpoint per la gestione dei post.
<ul>
    <li>POST - <b>posts/create/</b> -> Per creare un nuovo post. Header: Authorization Token <i>token_utente</i>. Body: title, description, image (id immagine), group (id gruppo).</li>
    <li>GET - <b>posts/{int:id_post}/</b> -> Per vedere i dettagli del post. Header: Authorization Token <i>token_utente</i>.</li>
    <li>PATCH - <b>posts/{int:id_post}/</b> -> Per modificare i dettagli del post. Header: Authorization Token <i>token_utente</i>. Body: tutti i campi da modificare.</li>
    <li>DELETE - <b>posts/{int:id_post}/</b> -> Per eliminare il post. Header: Authorization Token <i>token_utente</i>.</li>
    <li>POST - <b>posts/{int:id_post}/like/</b> -> Per mettere mi piace. Header: Authorization Token <i>token_utente</i>. Al massimo un piace per utente.</li>
    <li>POST - <b>posts/{int:id_post}/unlike/</b> -> Per togliere mi piace. Header: Authorization Token <i>token_utente</i>.</li>
    <li>GET - <b>posts/{int:id_post}/comments/</b> -> Restituisce tutti i commenti del post. Header: Authorization Token <i>token_utente</i>.</li>
    <li>POST - <b>posts/{int:id_post}/comments/</b> -> Crea nuovo commento per il post. Header: Authorization Token <i>token_utente</i>. Body: text.</li>
    <li>GET - <b>posts/{int:id_post}/comments/{int:id_commento}/</b> -> Per vedere un commento. Header: Authorization Token <i>token_utente</i>.</li>
    <li>DELETE - <b>posts/{int:id_post}/comments/{int:id_commento}/</b> -> Per cancellare un commento. Header: Authorization Token <i>token_utente</i>.</li>
</ul>

## Struttura dei repository

- [Frontend](https://github.com/AlbertooValente/pw-frontend-triptales)
- Backend

## Installazione e Setup

1. Clona il repo:

   ```bash
   git clone https://github.com/Basso-Giovanni/pw-backend-triptales.git
   ```

2. Installa le dipendenze:

   ```bash
   pip install -r requirements.txt
   ```

3. Configura `.env` con credenziali DB.

4. Migra il database:

   ```bash
   python manage.py migrate
   ```

5. Avvia il server:

   ```bash
   python manage.py runserver
   ```

## Autori
SegFault Squad: Basso Giovanni e Valente Alberto
