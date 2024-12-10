using System;
using System.Collections;
using System.Collections.Generic;

// Класс, представляющий фильм
public class Movie
{
    public string Title { get; set; }
    public string Director { get; set; }
    public int ReleaseYear { get; set; }

    public Movie(string title, string director, int releaseYear)
    {
        Title = title;
        Director = director;
        ReleaseYear = releaseYear;
    }

    public override string ToString()
    {
        return $"{Title} ({ReleaseYear}) by {Director}";
    }
}

// Класс, представляющий коллекцию фильмов с итератором
public class MovieCollection : IEnumerable<Movie>
{
    private List<Movie> movies;

    public MovieCollection()
    {
        movies = new List<Movie>();
    }

    public void AddMovie(Movie movie)
    {
        movies.Add(movie);
    }

    public IEnumerator<Movie> GetEnumerator()
    {
        return new MovieEnumerator(movies);
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }

    // Вложенный класс, реализующий итератор
    private class MovieEnumerator : IEnumerator<Movie>
    {
        private List<Movie> movies;
        private int position = -1;
        private int filterYear;

        public MovieEnumerator(List<Movie> movies)
        {
            this.movies = movies;
            this.filterYear = -1; // По умолчанию без фильтрации
        }

        public MovieEnumerator(List<Movie> movies, int filterYear)
        {
            this.movies = movies;
            this.filterYear = filterYear;
        }

        public Movie Current
        {
            get
            {
                if (position == -1 || position >= movies.Count)
                    throw new InvalidOperationException();
                return movies[position];
            }
        }

        object IEnumerator.Current => Current;

        public bool MoveNext()
        {
            position++;
            if (filterYear != -1)
            {
                while (position < movies.Count && movies[position].ReleaseYear != filterYear)
                {
                    position++;
                }
            }
            return position < movies.Count;
        }

        public void Reset()
        {
            position = -1;
        }

        public void Dispose()
        {
            // Нет ресурсов для освобождения
        }
    }

    // Метод для получения итератора с фильтрацией по году выпуска
    public IEnumerable<Movie> GetMoviesByYear(int year)
    {
        return new MovieEnumerable(movies, year);
    }

    // Вложенный класс, реализующий IEnumerable для фильтрации
    private class MovieEnumerable : IEnumerable<Movie>
    {
        private List<Movie> movies;
        private int filterYear;

        public MovieEnumerable(List<Movie> movies, int filterYear)
        {
            this.movies = movies;
            this.filterYear = filterYear;
        }

        public IEnumerator<Movie> GetEnumerator()
        {
            return new MovieEnumerator(movies, filterYear);
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }
}

// Пример использования
class Program
{
    static void Main(string[] args)
    {
        var movieCollection = new MovieCollection();
        movieCollection.AddMovie(new Movie("Inception", "Christopher Nolan", 2010));
        movieCollection.AddMovie(new Movie("The Dark Knight", "Christopher Nolan", 2008));
        movieCollection.AddMovie(new Movie("Interstellar", "Christopher Nolan", 2014));
        movieCollection.AddMovie(new Movie("The Matrix", "The Wachowskis", 1999));

        Console.WriteLine("All movies:");
        foreach (var movie in movieCollection)
        {
            Console.WriteLine(movie);
        }

        Console.WriteLine("\nMovies released in 2010:");
        foreach (var movie in movieCollection.GetMoviesByYear(2010))
        {
            Console.WriteLine(movie);
        }
    }
}
