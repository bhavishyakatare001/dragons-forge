import os
import shutil
import search
import validator
import auditor
import synthesis

def clean_workspace():
    """Wipes old data so we always start with a clean slate."""
    print("[System] Sweeping the workspace...")
    if os.path.exists("synthesiser.db"):
        os.remove("synthesiser.db")
        print("  -> Deleted old database.")
    
    if os.path.exists("refined_papers"):
        shutil.rmtree("refined_papers")
        print("  -> Deleted old refined papers.")
    print("[System] Workspace is clean!\n")

def run_pipeline():
    print("==================================================")
    print("   STARTING AUTONOMOUS RESEARCH PIPELINE          ")
    print("==================================================")
    
    # 1. Clean the environment
    clean_workspace()
    
    # 2. Define your research goal here!
    research_query = "CPU scheduling Round Robin"
    
    # 3. Trigger Stage 1: The Hunter
    raw_papers = search.run_search_stage(mode="api", query=research_query)
    
    # 4. Trigger Stage 2: The Gatekeeper
    if raw_papers:
        valid_papers = validator.run_validator_stage(raw_papers)
    else:
        print("[System] No papers found. Exiting.")
        return

    # 5. Trigger Stage 3: The Analyst
    if valid_papers:
        auditor.run_auditor_stage(valid_papers)
    else:
        print("[System] No relevant CPU papers passed the gate. Exiting.")
        return
        
    # 6. Trigger Stage 4: The Writer
    synthesis.run_synthesis_stage()
    
    print("\n==================================================")
    print(" ALL DONE! Run 'cat FINAL_RESEARCH_REPORT.md'     ")
    print("==================================================")

if __name__ == "__main__":
    run_pipeline()
