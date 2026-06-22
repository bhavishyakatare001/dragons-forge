import search

def validate_paper(paper):
    """
    The Gatekeeper. Scans the abstract and title for strict CPU scheduling metrics.
    Returns True if it passes, False if it should be dropped.
    """
    text_to_check = (paper.get('title', '') + " " + paper.get('abstract', '')).lower()
    
    # STRICT criteria: No 2-letter acronyms that cause false positives!
    required_keywords = [
        "turnaround time", 
        "waiting time", 
        "burst time", 
        "arrival time", 
        "cpu scheduling", 
        "time quantum"
    ]
    
    for keyword in required_keywords:
        if keyword in text_to_check:
            return True
            
    return False

def run_validator_stage(papers_list):
    """Takes the raw list of papers and filters out the junk."""
    print(f"\n[Validator Stage] Inspecting {len(papers_list)} papers...")
    
    valid_papers = []
    for paper in papers_list:
        if validate_paper(paper):
            print(f"  [+] PASSED: {paper['title'][:60]}...")
            valid_papers.append(paper)
        else:
            print(f"  [-] DROPPED: {paper['title'][:60]}...")
            
    print(f"[Validator Stage] Finished. {len(valid_papers)} papers passed the gate.")
    return valid_papers

if __name__ == "__main__":
    raw_papers = search.run_search_stage(mode="api", query="CPU scheduling Round Robin")
    validated_papers = run_validator_stage(raw_papers)
