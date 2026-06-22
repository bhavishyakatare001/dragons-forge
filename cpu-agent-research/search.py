import urllib.request
import xml.etree.ElementTree as ET
import json
import os

    
    
    
    
    
    
   
    
   
    
    
       
        
            
def search_arxiv(query, max_results=3):
    """
    Connects to the free ArXiv API over the internet.
    Includes a timeout so it never freezes your terminal!
    """
    print(f"[Search API] Querying ArXiv for: '{query}'...")
    
    formatted_query = query.replace(" ", "+")
    url = f"http://export.arxiv.org/api/query?search_query=all:{formatted_query}&max_results={max_results}"
    
    try:
        # ADDED FIX: timeout=10 forces it to give up if the server is stuck
        with urllib.request.urlopen(url, timeout=10) as response:
            xml_data = response.read()
            
        root = ET.fromstring(xml_data)
        namespaces = {'atom': 'http://www.w3.org/2005/Atom'}
        
        results = []
        for entry in root.findall('atom:entry', namespaces):
            title = entry.find('atom:title', namespaces).text.strip().replace('\n', ' ')
            summary = entry.find('atom:summary', namespaces).text.strip().replace('\n', ' ')
            paper_id = entry.find('atom:id', namespaces).text.split('/abs/')[-1]
            
            results.append({
                "title": title,
                "abstract": summary,
                "source": f"ArXiv ({paper_id})"
            })
            
        return results
    except Exception as e:
        # If it times out or fails, it will print this error instead of freezing!
        print(f"[Search API] Error fetching from online API: {e}")
        return []          
            

def search_local_directory(folder_path):
    """
    Scans a local folder for text or placeholder files if you are offline.
    """
    print(f"[Search Local] Scanning folder: '{folder_path}'...")
    results = []
    
    if not os.path.exists(folder_path):
        return results
        
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                results.append({
                    "title": filename.replace(".txt", ""),
                    "abstract": content[:300], # Use the first 300 characters as an abstract
                    "source": f"Local File ({filename})"
                })
    return results

def run_search_stage(mode, query, local_folder="./my_papers"):
    """
    The master switchboard for the Search stage.
    """
    combined_results = []
    
    if mode == "api" or mode == "hybrid":
        api_data = search_arxiv(query)
        combined_results.extend(api_data)
        
    if mode == "local" or mode == "hybrid":
        local_data = search_local_directory(local_folder)
        combined_results.extend(local_data)
        
    # Deduplicate results based on title names
    seen_titles = set()
    unique_results = []
    for paper in combined_results:
        clean_title = paper["title"].lower().strip()
        if clean_title not in seen_titles:
            seen_titles.add(clean_title)
            unique_results.append(paper)
            
    print(f"[Search Stage] Completed. Found {len(unique_results)} unique papers.")
    return unique_results

# This allows us to test the file directly by running: python search.py
if __name__ == "__main__":
    # Let's run a quick mock test to see it work!
    test_results = run_search_stage(mode="api", query="CPU scheduling Round Robin")
    print("\n--- Test Results Preview ---")
    for index, paper in enumerate(test_results, 1):
        print(f"{index}. {paper['title']} [Source: {paper['source']}]")
