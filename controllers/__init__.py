from controllers.gallery_controller import gallerys
from controllers.auth_controller import auth
from controllers.artist_controller import artists
from controllers.artwork_controller import artworks
from controllers.exhibition_controller import exhibitions
from controllers.ticket_controller import tickets


registerable_controllers = [
    gallerys, auth, artists, artworks, exhibitions, tickets
]