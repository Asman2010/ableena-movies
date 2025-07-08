from typing import List, Dict



def search(links_data: Dict, search_term: str = None, keywords: List[str] = None) -> List[Dict]:
    """
    Search through internal links for given term(s).
    
    Args:
        links_data: Dictionary containing 'internal' and 'external' links
        search_term: Single term to search for
        keywords: List of keywords to search for (OR logic)
        
    Returns:
        List of matching links
    """
    internal_links = links_data.get('internal', [])
    
    if not internal_links:
        return []
    
    # Determine what to search for
    search_terms = []
    if search_term:
        search_terms.append(search_term.lower())
    if keywords:
        search_terms.extend([keyword.lower() for keyword in keywords])
    
    if not search_terms:
        return []
    
    results = []
    
    for link in internal_links:
        text = link.get('text', '').lower()
        
        # Check if any search term is in the text
        for term in search_terms:
            if term in text:
                results.append(link)
                break  # Don't add the same link multiple times
    
    return results

