"""
vw602- Gabriel Sanchez

"""
import tkinter as tk
import requests
from bs4 import BeautifulSoup
import re

# Function to fetch and scrape the website content
def fetch_summary(url):
    try:
        # Send a GET request to fetch the website content
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        soup = BeautifulSoup(response.text, 'html.parser')

        # Try to extract the most important part (usually paragraphs or content section)
        paragraphs = soup.find_all('p')  # Get all paragraph tags
        if paragraphs:
            # Collect the first 5 paragraphs as a detailed summary
            text = ""
            for i in range(min(5, len(paragraphs))):
                text += paragraphs[i].get_text() + "\n"
            # Clean up the text to remove unwanted characters or excess spaces
            text = re.sub(r'\s+', ' ', text).strip()
            return text
        return "No content found or invalid webpage."
    except Exception as e:
        return f"Error occurred: {str(e)}"

# GUI function to create the interface
def create_window():
    window = tk.Tk()
    window.title("Web Scraper & Summary")
    
    # Label for instructions
    label = tk.Label(window, text="Enter the website URL to scrape:", font=("Arial", 12))
    label.pack(pady=10)
    
    # Entry field for URL input
    url_entry = tk.Entry(window, font=("Arial", 12), width=40)
    url_entry.pack(pady=10)
    
    # Text area to display the summary
    result_text = tk.Text(window, height=10, width=50, wrap=tk.WORD, font=("Arial", 12))
    result_text.pack(pady=10)

    # Function to fetch summary when "Get Summary" is clicked
    def get_summary():
        url = url_entry.get()  # Get the URL from the entry field
        if url:
            summary = fetch_summary(url)
            result_text.delete(1.0, tk.END)  # Clear any previous results
            result_text.insert(tk.END, summary)  # Insert new summary into the text area

    # Button to trigger scraping and summary generation
    scrape_button = tk.Button(window, text="Get Summary", command=get_summary, font=("Arial", 12))
    scrape_button.pack(pady=20)
    
    # Start the Tkinter window
    window.mainloop()

if __name__ == "__main__":
    create_window()