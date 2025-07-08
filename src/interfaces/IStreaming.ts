// Search result interface
export interface ISearchResult {
  href: string;
  text: string;
  title: string;
  base_domain: string;
}

// Magnet link interface
export interface IMagnetLink {
  magnet_link: string;
  display_name: string;
  info_hash: string;
  trackers: string[];
  file_size: number;
  file_size_formatted: string;
}

// Provider interface
export interface IStreamingProvider {
  id: string;
  name: string;
}