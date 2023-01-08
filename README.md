# Übe

Übe is a philosophy-based chat room website and app where users can build communities, debate and discuss philosophical ideas, play games, and ponder dilemmas.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7+
- Django 3.1+

### Installation

1. Clone the repository:

```sh
git clone https://github.com/your-username/ube.git
```

2. Navigate to the project directory:

```sh
cd ube
```


3. Install the required packages:

```sh
pip install -r requirements.txt
```

4. Create a new file called `.env` in the project root, and add the following variables:

```sh
SECRET_KEY=<your-secret-key>
DEBUG=<True|False>
```

5. Migrate the database:

```sh
python manage.py migrate
```

6. Start the development server:

```sh
python manage.py runserver
```

## Usage

To use the app, create a superuser account:

```sh
python manage.py createsuperuser
```


Then, visit `http://localhost:8000/admin/` to log in and access the site's administration panel. From here, you can create rooms and moderate discussions.

Users can access the chat rooms at `http://localhost:8000/rooms/`

## Contribution
To contribute to the project, follow these steps:

1. Fork the project
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
