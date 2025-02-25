# Shutterstar 📸  
**Capturing the band's best moments!**  

## Description  
Shutterstar is a Flask-based microservice dedicated to managing and displaying the band's pictures. It provides APIs for uploading, storing, and optimizing images to ensure high-quality delivery.  

## Features  
- Upload and organize images efficiently.  
- Fetch and display pictures with optimized resolution.  
- Secure API endpoints to manage and retrieve images.  

## Installation  
```bash
git clone https://github.com/yourusername/Shutterstar.git
cd Shutterstar
pip install -r requirements.txt
python app.py
```
## API Endpoints 

| Method | Endpoint       | Description               |
|--------|--------------|---------------------------|
| GET    | `/health`    | Check the service health   |
| GET    | `/count` | Retrieve the pictures count |
| GET   | `/picture`    | Retrieve all pictures from DB  |
| GET | `/picture/<int:id>` | Search for specific picture with ID |
| POST | `/picture` | Create new pictures |
| PUT | `/picture/<int:id>` | Update picture with ID |
| DELETE | `/picture/<int:id>` | Delete picture with ID | 


## Technologies Used
- Flask
- PostgreSQL / SQLite
- Cloud Storage Integration