# Electronics Shop Backend

This is the **Flask-based backend** for the Electronics Shop project — a full-stack e-commerce platform for selling and delivering electronic products.

---

## Tech Stack

- **Backend**: Python + Flask
- **Database**: PostgreSQL (via SQLAlchemy)
- **Authentication**: JWT (token-based)
- **Role Management**: User/Admin
- **Testing**: Python `unittest`
- **API Schema**: Marshmallow

---

##  Features

###  Users
- Register & login
- View & update profile
- JWT-based authentication
- Role-based access (`user` or `admin`)

### 🛍 Products
- List all products
- View product details
- Admin: create, update, delete products

### Admin Analytics
- View total orders and revenue
- View top-selling products
- Manage users and assign roles

---
### Live Demo
 https://electronics-shop-frontend.onrender.com/

### Front-end repo link
 https://github.com/Electronic-Mart/electronics-shop-frontend

### Back-end deployed link
 https://electronics-shop-backend.onrender.com

---
## Admin Credentials

```env
ADMIN_EMAIL=alexnjugi11@gmail.com
ADMIN_PASSWORD=1234
You can change these in .env

 Project Structure
bash
Copy
Edit
electronics-shop-backend/
│
├── app/                  # Main Flask app
│   ├── models/           # SQLAlchemy models
│   ├── routes/           # API route controllers
│   ├── services/         # Business logic
│   ├── schemas/          # Marshmallow validation
│   ├── utils/            # JWT, role checks, invoice
│   └── config.py, __init__.py, database.py
│
├── tests/                # Unit tests
├── migrations/           # Flask-Migrate folder
├── run.py                # App runner
├── wsgi.py               # For production deployment
├── .env                  # Secrets & DB URI
├── requirements.txt
└── README.md
 Setup Instructions
 1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/Electronic-Mart/electronics-shop-backend.git
cd electronics-shop-backend
 2. Create Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
 3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
 4. Configure Environment
Create a .env file:

env
Copy
Edit
FLASK_ENV=development
SECRET_KEY=your-secret
DATABASE_URL=postgresql://postgres:password@localhost:5432/electrodb
ADMIN_EMAIL=alexnjugi11@gmail.com
ADMIN_PASSWORD=1234
 5. Initialize Database
bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
 6. Run the Server
bash
Copy
Edit
python run.py
Server will start on http://localhost:5000

 Running Tests
bash
Copy
Edit
python3 -m unittest discover tests/
 API Routes Summary
Method	Endpoint	Description	Auth
POST	/api/auth/register	Register user	
POST	/api/auth/login	Login + JWT	
GET	/api/products/	List products	
GET	/api/products/<id>	View product	
POST	/api/products/	Create product	 Admin
PUT	/api/products/<id>	Update product	 Admin
DELETE	/api/products/<id>	Delete product	 Admin
POST	/api/orders/	Place order	 User
GET	/api/users/me	My profile	 User
PUT	/api/users/me	Update my profile	 User
GET	/api/users/	Get all users	 Admin
PUT	/api/users/<id>/role	Assign user role	 Admin
GET	/api/analytics/orders	View order stats	 Admin
GET	/api/analytics/top-products	Top selling products	 Admin

 Deployment
You can deploy using:

Gunicorn + wsgi.py

Render, Railway, or Heroku

Connect to frontend at: Electronics Shop Frontend

 License
MIT License

 Author
Alex Njugi Karanja — GitHub
