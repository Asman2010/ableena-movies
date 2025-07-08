import axios from 'axios';
import { ISearchResult, IMagnetLink } from '../interfaces/IStreaming';

const API_BASE_URL = 'http://localhost:8000';

/**
 * Search for movies on TamilMV
 * @param query The movie title to search for
 * @returns A promise that resolves to an array of search results
 */
export const searchTamilMV = async (query: string): Promise<ISearchResult[]> => {
  try {
    const response = await axios.get(`${API_BASE_URL}/tamilmv/search/`, {
      params: { query }
    });
    return response.data;
  } catch (error) {
    console.error('Error searching TamilMV:', error);
    return [];
  }
};

/**
 * Search for movies on PirateBay
 * @param query The movie title to search for
 * @returns A promise that resolves to an array of search results
 */
export const searchPirateBay = async (query: string): Promise<ISearchResult[]> => {
  try {
    const response = await axios.get(`${API_BASE_URL}/piratebay/search/`, {
      params: { query }
    });
    return response.data;
  } catch (error) {
    console.error('Error searching PirateBay:', error);
    return [];
  }
};

/**
 * Fetch magnet links for a specific search result
 * @param url The URL of the search result
 * @param provider The provider ID (tamilmv or piratebay)
 * @returns A promise that resolves to an array of magnet links
 */
export const fetchMagnetLinks = async (url: string, provider: string): Promise<IMagnetLink[]> => {
  try {
    const response = await axios.get(`${API_BASE_URL}/${provider}/magnet_fetcher/`, {
      params: { url }
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching magnet links:', error);
    return [];
  }
};