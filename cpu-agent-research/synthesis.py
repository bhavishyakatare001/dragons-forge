import sqlite3

def run_synthesis_stage():
    """The Writer Agent: Compiles the final academic report from the database."""
    print("\n[Synthesis Stage] Waking up Writer Agent...")
    
    try:
        # Connect to our clean data source
        conn = sqlite3.connect("synthesiser.db")
        cursor = conn.cursor()
        
        # We ask the database to group everything by the type of metric
        cursor.execute('''
            SELECT metric_name, extracted_value, paper_title 
            FROM extracted_metrics 
            ORDER BY metric_name
        ''')
        
        results = cursor.fetchall()
        
        if not results:
            print("[Synthesis Stage] Error: The database is empty! No report to write.")
            return

        print(f"  [+] Found {len(results)} verified data points. Drafting report...")
        
        # Start writing the document
        final_doc = "# Autonomous Research Report: CPU Scheduling Algorithms\n"
        final_doc += "> *Compiled entirely by local AI Agentic Pipeline*\n\n"
        
        current_metric = ""
        
        # Loop through our data and format it beautifully
        for metric_name, value, title in results:
            # If we switch to a new metric, create a new Header
            if metric_name != current_metric:
                current_metric = metric_name
                final_doc += f"## {current_metric} Optimizations\n"
            
            # Add the bullet point with strict citation
            final_doc += f"* {value}\n  * **Source Citation:** *{title}*\n\n"
            
        # Save the masterpiece to your folder
        with open("FINAL_RESEARCH_REPORT.md", "w", encoding="utf-8") as f:
            f.write(final_doc)
            
        print("[Synthesis Stage] COMPLETE! Open 'FINAL_RESEARCH_REPORT.md' to see your results.")
        
    except sqlite3.OperationalError:
        print("[Synthesis Stage] Error: Could not find 'synthesiser.db'. Did you run auditor.py first?")

# Let's run the final step!
if __name__ == "__main__":
    run_synthesis_stage()
