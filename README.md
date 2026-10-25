# Watches---SLIPD-Campus

Technologies & Frameworks : 

Python 
Django
HTML 
CSS

**Project structure**
| File / Folder | Purpose |
|---|---|
| `watchstore/settings.py` | Project settings, SQLite database config |
| `watchstore/urls.py` | Main URL routes |
| `store/models.py` | Database tables: Watch, Profile, CartItem |
| `store/views.py` | Page logic: home, about, cart, signup, add/remove |
| `store/forms.py` | Sign-up form (username, email, phone, address, password) |
| `store/urls.py` | App page addresses |
| `store/templates/store/` | HTML pages (base, home, about, cart, login, signup) |
| `store/static/store/style.css` | Premium black-and-gold design |
| `store/management/commands/seed_watches.py` | Adds sample watches |

**Database design (SQLite)**
- `auth_user` (built-in Django): username, email, hashed password.
- `Profile`: user (one-to-one), phone, address.
- `Watch`: name, brand, price, description, image_url.
- `CartItem`: user (foreign key), watch (foreign key), quantity.


HOME PAGE 
<img width="1840" height="877" alt="Home" src="https://github.com/user-attachments/assets/e4812e51-3a0d-4254-a74c-abe64471d024" />
