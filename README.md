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


 
<img width="1840" height="877" alt="Home" src="https://github.com/user-attachments/assets/e4812e51-3a0d-4254-a74c-abe64471d024" />
<img width="1837" height="882" alt="Home 1" src="https://github.com/user-attachments/assets/63670b5c-968a-4099-bb62-6e0c24d18b27" />
<img width="1862" height="885" alt="about" src="https://github.com/user-attachments/assets/db582fd3-6b7f-4034-b321-0f22d910fb7b" />
<img width="1850" height="882" alt="cart" src="https://github.com/user-attachments/assets/33ceb3e5-ba6c-42a6-a29d-0cf7fc0869b1" />
<img width="1856" height="872" alt="login" src="https://github.com/user-attachments/assets/aea4559d-cfca-40a7-9dec-843b1ef08747" />
<img width="1841" height="886" alt="sign up" src="https://github.com/user-attachments/assets/c6088dd9-19f2-438e-99e1-87690c0b2c34" />






