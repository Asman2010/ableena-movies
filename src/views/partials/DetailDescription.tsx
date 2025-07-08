// Interfaces
import { useState } from 'react'
import { IMovieDetail } from 'interfaces/IMovieDetail'
import { IStreamingProvider, ISearchResult, IMagnetLink } from 'interfaces/IStreaming'
// Images
import { Dummy } from '@/assets/images'
// Components
import ProviderModal from 'components/ProviderModal'
import SearchResultsModal from 'components/SearchResultsModal'
import MagnetModal from 'components/MagnetModal'
import LoadingSpinner from 'components/LoadingSpinner'
// Services
import { searchTamilMV, searchPirateBay, fetchMagnetLinks } from 'services/StreamingService'

// Local interface
interface IProps {
  movie: IMovieDetail
}

const DetailDescription = ({ movie }: IProps) => {
  // Variables
  const releaseDate: string | undefined = movie
    ? movie.release_date?.split('-')[0] || movie.first_air_date?.split('-')[0]
    : ''

  // Streaming state
  const [isProviderModalOpen, setIsProviderModalOpen] = useState<boolean>(false)
  const [isSearchResultsModalOpen, setIsSearchResultsModalOpen] = useState<boolean>(false)
  const [isMagnetModalOpen, setIsMagnetModalOpen] = useState<boolean>(false)
  const [selectedProvider, setSelectedProvider] = useState<IStreamingProvider | null>(null)
  const [searchResults, setSearchResults] = useState<ISearchResult[]>([])
  const [magnetLinks, setMagnetLinks] = useState<IMagnetLink[]>([])
  const [isSearching, setIsSearching] = useState<boolean>(false)
  const [isFetchingMagnets, setIsFetchingMagnets] = useState<boolean>(false)

  // Error image
  const onErrorImage = (e: any) => (e.target.src = Dummy)

  // Handler functions
  const handleWatchClick = () => {
    setIsProviderModalOpen(true)
  }

  const handleProviderSelect = async (provider: IStreamingProvider) => {
    setSelectedProvider(provider)
    setIsProviderModalOpen(false)
    setIsSearching(true)
    
    try {
      // Search for the movie in the selected provider
      const movieTitle = movie.title || movie.original_title || movie.name || movie.original_name || ''
      let results: ISearchResult[] = []
      
      if (provider.id === 'tamilmv') {
        results = await searchTamilMV(movieTitle)
      } else if (provider.id === 'piratebay') {
        results = await searchPirateBay(movieTitle)
      }
      
      setSearchResults(results)
      setIsSearchResultsModalOpen(true)
    } catch (error) {
      console.error('Error searching for movie:', error)
    } finally {
      setIsSearching(false)
    }
  }

  const handleSearchResultSelect = async (result: ISearchResult) => {
    setIsSearchResultsModalOpen(false)
    setIsFetchingMagnets(true)
    
    try {
      if (selectedProvider) {
        const magnets = await fetchMagnetLinks(result.href, selectedProvider.id)
        setMagnetLinks(magnets)
        setIsMagnetModalOpen(true)
      }
    } catch (error) {
      console.error('Error fetching magnet links:', error)
    } finally {
      setIsFetchingMagnets(false)
    }
  }

  const handleMagnetSelect = (magnet: IMagnetLink) => {
    setIsMagnetModalOpen(false)
    
    // Open the magnet link in a new tab
    window.open(magnet.magnet_link, '_blank')
  }

  return (
    <>
      {/* Banner */}
      {movie.backdrop_path && (
        <div className='relative'>
          <img
            src={`https://www.themoviedb.org/t/p/w1920_and_h800_multi_faces${movie.backdrop_path}`}
            alt={movie.name}
            className='w-full md:h-auto h-[296px] object-cover bg-center'
          />
          <div className='absolute top-0 left-0 w-full h-full bg-gradient-to-t dark:from-background from-background-light dark:via-background/90 via-background-light/20 dark:via-20% via-50% dark:to-background/10 to-background-light/5 to-70%' />
        </div>
      )}

      <div
        className={`relative container ${movie.backdrop_path ? 'md:-mt-52 -mt-28' : 'mt-32'} z-10`}
      >
        <div className='flex md:flex-row flex-col md:space-x-10 space-y-8'>
          {/* Poster */}
          <div className='relative'>
            <img
              src={`https://www.themoviedb.org/t/p/w220_and_h330_face${movie.poster_path}`}
              alt={movie.title || movie.name}
              className='rounded-xl xl:w-[220px] lg:w-[190px] md:w-[170px] w-[160px] xl:min-w-[220px] lg:min-w-[190px] md:min-w-[170px] min-w-[160px] xl:h-[330px] lg:h-[290px] md:h-[270px] h-[240px] xl:min-h-[330px] lg:min-h-[290px] md:min-h-[270px] min-h-[240px]'
              onError={onErrorImage}
            />
            <img
              src={`https://www.themoviedb.org/t/p/w220_and_h330_face${movie.poster_path}`}
              alt={movie.title || movie.name}
              className='absolute top-2 rounded-lg blur-lg -z-10 opacity-30 xl:w-[220px] lg:w-[190px] md:w-[170px] w-[160px] xl:min-w-[220px] lg:min-w-[190px] md:min-w-[170px] min-w-[160px] xl:h-[330px] lg:h-[290px] md:h-[270px] h-[240px] xl:min-h-[330px] lg:min-h-[290px] md:min-h-[270px] min-h-[240px]'
              onError={onErrorImage}
            />
          </div>

          {/* Title, release year, language, genres, description */}
          <div className='flex flex-col mt-16 space-y-3'>
            {/* Title and Watch button */}
            <div className="flex items-center justify-between">
              <h1 className='tracking-wide font-bold xl:text-3xl md:text-2xl text-slate-950 dark:text-slate-100'>
                {movie.original_name || movie.original_title}
              </h1>
              <button
                onClick={handleWatchClick}
                className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-md transition-colors"
              >
                Watch
              </button>
            </div>

            {/* Release year & language */}
            {movie.spoken_languages.length > 0 && (
              <p className='font-medium text-sm text-slate-950 dark:text-slate-100'>
                {releaseDate} &#9679; {movie.spoken_languages[0].english_name}{' '}
                {movie.first_air_date && <>&#9679; {movie.number_of_episodes} Episode</>}
              </p>
            )}

            {/* Genres */}
            <div className='flex space-x-2 overflow-x-auto no-scrollbar'>
              {movie.genres.map((genre) => (
                <div
                  key={genre.id}
                  className='px-3 py-1 dark:bg-slate-700/50 bg-slate-400/50 font-medium text-xs tracking-wide rounded dark:text-slate-100 text-slate-950 whitespace-nowrap'
                >
                  {genre.name}
                </div>
              ))}
            </div>

            {/* Description */}
            <p className='xl:max-w-[60%] lg:max-w-[70%] font-normal text-sm text-slate-950 dark:text-slate-100 leading-loose'>
              {movie.overview}
            </p>
          </div>
        </div>
      </div>
      {/* Modals */}
      <ProviderModal
        isOpen={isProviderModalOpen}
        onClose={() => setIsProviderModalOpen(false)}
        onSelectProvider={handleProviderSelect}
      />

      {/* Loading screen for searching */}
      {isSearching && (
        <div className="fixed inset-0 bg-black/50 backdrop-blur z-[999999] flex items-center justify-center">
          <div className="bg-background-light dark:bg-slate-900 p-8 rounded-xl shadow-xl flex flex-col items-center space-y-4">
            <LoadingSpinner size="lg" />
            <p className="text-lg font-medium text-slate-900 dark:text-slate-100">Searching for movie...</p>
          </div>
        </div>
      )}

      <SearchResultsModal
        isOpen={isSearchResultsModalOpen}
        results={searchResults}
        onClose={() => setIsSearchResultsModalOpen(false)}
        onSelectResult={handleSearchResultSelect}
      />

      {/* Loading screen for fetching magnet links */}
      {isFetchingMagnets && (
        <div className="fixed inset-0 bg-black/50 backdrop-blur z-[999999] flex items-center justify-center">
          <div className="bg-background-light dark:bg-slate-900 p-8 rounded-xl shadow-xl flex flex-col items-center space-y-4">
            <LoadingSpinner size="lg" />
            <p className="text-lg font-medium text-slate-900 dark:text-slate-100">Fetching magnet links...</p>
          </div>
        </div>
      )}

      <MagnetModal
        isOpen={isMagnetModalOpen}
        magnets={magnetLinks}
        onClose={() => setIsMagnetModalOpen(false)}
        onSelectMagnet={handleMagnetSelect}
      />
    </>
  )
}

export default DetailDescription
