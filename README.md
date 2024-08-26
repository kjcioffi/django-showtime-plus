# ShowTime+ Application

## Project Overview

**Ever wonder what's currently in theaters?**

While Google, Rotten Tomatoes, and IMDb provide movie information, they can sometimes be cumbersome and overwhelming when you need quick, concise details to make an informed decision.

**ShowTime+** is a streamlined platform designed for users who want just enough information about movies currently in theaters, all in one place. Our goal is to offer an experience that is both informative and easy to navigate, helping you make an informed decision without the clutter.

The platform features a list of popular movies, and users can click on each movie to view more details.

## Running the Project

To run the ShowTime+ project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone [repository-url]
    cd django-showtime-plus
    ```

2. **Create an account** on [The Movie Database (TMDB)](https://developer.themoviedb.org/docs/getting-started) and request an API key.

3. **Set up environment variables**:
    - At the root of the directory, create a `.env` file with the following configurations:
        ```env
        DEBUG=TRUE
        ALLOWED_HOSTS=localhost,127.0.0.1
        
        SECRET_KEY=<your-secret-key>  # Optionally create one using: python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

        TMDB_API_KEY=<your-tmdb-api-key>
        ```

4. **(Optional) Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

5. **Install dependencies**:
    ```bash
    pip install piptools
    pip-sync requirements/requirements.txt requirements/dev/requirements-dev.txt
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

You should now be able to access the application at `http://localhost:8000`.

---

## Running the project containerized

1. At the root of the directory, ensure you have your .env file. Optionally, you can use the ```.env-template``` file to fill out the required variables and renamed it to ```.env```.

2. In your .env file, toggle ```DEBUG=false```.

3. To run the project, execute:

    ```bash
    docker compose up
    ```

    optionally, if you wish to rebuild from scratch (without any caching)

    ```bash
    docker compose up --build
    ```

The Dockerfile is designed to be used with Docker compose and will pull environment variable info from .env.

4. Navigate to ```localhost``` on port 80.