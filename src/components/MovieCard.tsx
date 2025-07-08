import { BaseSyntheticEvent } from 'react'
import { Link } from 'react-router-dom'
// Interfaces
import { IMovie } from 'interfaces/IMovie'
// Components
import { LazyLoadImage, trackWindowScroll } from 'react-lazy-load-image-component'
// Images
import { Dummy } from '@/assets/images'
// Icons
import { IconStarFilled } from '@tabler/icons-react'
// Style effect
import 'react-lazy-load-image-component/src/effects/black-and-white.css'

// Local Interfaces
interface IProps {
  movie: IMovie
}

const MovieCard = ({ movie }: IProps) => {
  return (
    <Link
      to={`/${movie.first_air_date ? 'tv' : 'movie'}/detail/${movie.id}`}
      className='flex flex-col group text-slate-900 dark:text-slate-100'
    >
      <div className='w-full rounded-lg overflow-hidden shadow-lg'>
        <LazyLoadImage
          src={`https://image.tmdb.org/t/p/w440_and_h660_face${movie.poster_path}`}
          alt={movie.title || movie.original_title || movie.original_name}
          useIntersectionObserver={true}
          threshold={100}
          placeholderSrc={Dummy} // Using a dummy image as placeholder
          onError={(event: BaseSyntheticEvent) => {
            event.currentTarget.onerror = null
            event.currentTarget.src = Dummy
          }}
          effect='black-and-white'
          width='100%'
          className='w-full h-auto object-cover transform transition-transform duration-300 group-hover:scale-110'
        />
      </div>
      <div className='mt-3'>
        <h3 className='text-base font-semibold truncate'>
          {movie.title || movie.name}
        </h3>
        <div className='flex justify-between items-center mt-1 text-sm text-slate-600 dark:text-zinc-400'>
          <p>{movie.release_date?.split('-')[0] || movie.first_air_date?.split('-')[0]}</p>
          {Number(movie.vote_average) > 0 && (
            <div className='flex items-center space-x-1'>
              <IconStarFilled className='w-4 h-4 text-yellow-500' />
              <p>{String(movie.vote_average).substring(0, 3)}</p>
            </div>
          )}
        </div>
      </div>
    </Link>
  )
}

export default trackWindowScroll(MovieCard)
