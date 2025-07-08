import { useEffect, useState } from 'react'
// Services
import { discoverMovies } from 'services/MovieApi'
// Interfaces
import type { IMovie } from 'interfaces/IMovie'
// Components
import MovieCard from 'components/MovieCard'
import MovieCardSkeleton from 'components/skeleton/MovieCardSkeleton'

const Home = () => {
  // Variables
  const apiKey: string = import.meta.env.VITE_API_KEY
  const [isLoading, setIsLoading] = useState<boolean>(true)
  const [movies, setMovies] = useState<IMovie[]>([])
  const [filter, setFilter] = useState('en')
  const [page, setPage] = useState(1)

  const languageFilters = [
    { key: 'en', label: 'English' },
    { key: 'ta', label: 'Tamil' },
    { key: 'ml', label: 'Malayalam' },
  ]

  // Get data
  const getData = async () => {
    setIsLoading(true)

    const params = {
      api_key: apiKey,
      page: 1,
      with_original_language: filter,
    }

    const { data } = await discoverMovies({ ...params, page })

    if (data) {
      setMovies((prev) => (page === 1 ? data.results : [...prev, ...data.results]))
      setIsLoading(false)
    }
  }

  // Get data when filter changes
  useEffect(() => {
    setPage(1)
    getData()
  }, [filter])

  useEffect(() => {
    if (page > 1) getData()
  }, [page])

  return (
    <div className='container py-8'>
      <div className='flex items-center justify-center space-x-4 mb-8'>
        {languageFilters.map(({ key, label }) => (
          <button
            key={key}
            onClick={() => setFilter(key)}
            className={`px-4 py-2 rounded-full font-semibold transition-colors ${
              filter === key
                ? 'bg-blue-600 text-white'
                : 'bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-gray-200'
            }`}
          >
            {label}
          </button>
        ))}
      </div>

      <div className='grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-8'>
        {!isLoading &&
          movies.map((movie) => (
            <MovieCard
              key={movie.id}
              movie={movie}
            />
          ))}
        {isLoading &&
          Array.from({ length: 12 }).map((_, i) => <MovieCardSkeleton key={i} />)}
      </div>

      <div className='flex justify-center mt-8'>
        <button
          onClick={() => setPage((prev) => prev + 1)}
          className='px-6 py-3 bg-blue-600 text-white font-semibold rounded-full hover:bg-blue-700 transition-colors disabled:opacity-50'
          disabled={isLoading}
        >
          {isLoading ? 'Loading...' : 'Load More'}
        </button>
      </div>
    </div>
  )
}

export default Home
