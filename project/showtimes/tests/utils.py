from pytz import timezone
from random import choice

from moviebase.settings import TIME_ZONE
from movielist.models import Movie
from movielist.tests.utils import faker
from showtimes.models import Cinema, Screening

TZ = timezone(TIME_ZONE)


def fake_cinema_data():
    """Generate a dict of cinema data.

    The format is compatible with serializers.
    """
    cinema_data = {
        "name": f"{faker.street_name()} Cinema",
        "city": faker.city(),
    }
    return cinema_data


def create_fake_cinema():
    """Generate new fake object `Cinema` and save to database.

    Return the created object.
    """
    cinema_data = fake_cinema_data()
    new_cinema = Cinema.objects.create(**cinema_data)
    return new_cinema


def fake_screening_data():
    """Generate a dict of screening data

    The format is compatible with serializers.
    """
    screening_data = {
        "movie": choice(Movie.objects.all()).title,
        "cinema": choice(Cinema.objects.all()).name,
        "date": faker.future_datetime(
            end_date='+30d',
            tzinfo=TZ
        ).strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    return screening_data


def find_cinema_by_name(name):
    """Return the first `Cinema` object that matches `name`."""
    return Cinema.objects.filter(name=name).first()


def find_movie_by_title(title):
    """Return the first `Movie` object that matches `title`."""
    return Movie.objects.filter(title=title).first()


def create_fake_screening():
    """Generate new fake screenings into object 'cinema' and save to database.

    Return the created object.
    """
    screening_data = fake_screening_data()
    screening_data['movie'] = find_movie_by_title(screening_data['movie'])
    screening_data['cinema'] = find_cinema_by_name(screening_data['cinema'])
    Screening.objects.create(**screening_data)
