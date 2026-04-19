# MyMicroApp - DevOps Assignment

A simple FastAPI microservice with Docker containerization and GitHub Actions CI/CD pipeline for AWS EC2 deployment.

## Features

- **FastAPI**: Modern Python web framework
- **Docker**: Containerized application
- **GitHub Actions**: Automated CI/CD pipeline
- **AWS EC2**: Cloud deployment
- **Docker Hub**: Public image repository

## Project Structure

```
mymicroapp/
├── app/
│   └── __init__.py
├── main.py                 # FastAPI application
├── requirements.txt        # Python dependencies
├── Dockerfile             # Container configuration
├── docker-compose.yml     # Local development setup
├── .gitignore             # Git ignore patterns
├── .dockerignore           # Docker ignore patterns
├── .github/
│   └── workflows/
│       └── deploy.yml     # GitHub Actions CI/CD
└── README.md              # This file
```

## Local Development

### Prerequisites
- Python 3.11+
- Docker & Docker Compose
- Git

### Setup & Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/mymicroapp.git
   cd mymicroapp
   ```

2. **Create virtual environment (optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

   The app will be available at `http://localhost:8000`

5. **Access API documentation**
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

## Docker

### Build Image
```bash
docker build -t mymicroapp:latest .
```

### Run Container
```bash
docker run -p 8000:8000 mymicroapp:latest
```

### Using Docker Compose (Development)
```bash
docker-compose up
```

## API Endpoints

- `GET /` - Root endpoint with API info
- `GET /health` - Health check
- `GET /api/users` - Get all users
- `GET /api/users/{user_id}` - Get specific user
- `POST /api/users` - Create new user
- `GET /api/items` - Get all items
- `GET /api/items/{item_id}` - Get specific item
- `POST /api/items` - Create new item

## Testing Endpoints

```bash
# Health check
curl http://localhost:8000/health

# Get all users
curl http://localhost:8000/api/users

# Get all items
curl http://localhost:8000/api/items

# Create a new user
curl -X POST http://localhost:8000/api/users \
  -H "Content-Type: application/json" \
  -d '{"id":3, "name":"Charlie", "email":"charlie@example.com"}'
```

## CI/CD Pipeline

The GitHub Actions workflow automatically:
1. Builds Docker image on every push to `main`
2. Pushes image to Docker Hub
3. Deploys to AWS EC2 instance

### GitHub Secrets Required
- `DOCKER_USERNAME` - Docker Hub username
- `DOCKER_PASSWORD` - Docker Hub password/token
- `EC2_HOST` - EC2 instance public IP
- `EC2_USER` - EC2 user (ec2-user for Amazon Linux 2)
- `EC2_SSH_KEY` - Private SSH key for EC2 access

## Deployment

The application is deployed on AWS EC2 and automatically updated via GitHub Actions CI/CD pipeline.

### EC2 Access
```bash
ssh -i your-key.pem ec2-user@<EC2_IP>
```

### View Logs on EC2
```bash
docker logs mymicroapp-container
```

## Docker Hub Repository

Images are pushed to: `https://hub.docker.com/r/YOUR_USERNAME/mymicroapp`

## License

MIT
