<p align="center">
  <a href="#">
    <img alt="Projects Library" src="readme_images/icon.svg" width="300" />
  </a>
</p>

<p align="center">
  Platform used to manage student projects.
</p>


## Built with

- [Django](https://www.djangoproject.com/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)



## How to run app locally

1. Clone the repository

```bash
git clone https://github.com/ahmedy19/Projects_Library.git
```

2. Change the working directory

```bash
cd Projects_Library
```

3. Create virtual environment

```bash
python -m venv env
```

4. Activate virtual environment

```bash
Mac & Linux -> source env/bin/activate
Windows -> .\env\Scripts\activate
```

5. Install modules

```bash
pip3 install -r requirements.txt
```

6. Create `.env` file in root

```bash
DJ_SECRET_KEY = Your Django Secret Key
DJ_DEBUG = True for Development | False for Production
```

7. Create tables

```bash
- python manage.py makemigrations
- python manage.py migrate
```

8. Create superuser

```bash
python manage.py createsuperuser
```

9. Run app
    
```bash
python manage.py runserver
```

10. Open [localhost:8000](http://localhost:8000/)


## License
License under the [MIT License](LICENSE).
