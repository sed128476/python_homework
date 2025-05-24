import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import json
import pandas as pd
import time
import os
import sys

def setup_driver():
    try:
        print("Setting up Chrome driver...")
        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-extensions')
        return webdriver.Chrome(service=service, options=options)
    except Exception as e:
        print(f"Error setting up Chrome driver: {str(e)}")
        raise

def wait_for_element(driver, by, value, timeout=30):
    """Helper function to wait for an element with better error handling"""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except TimeoutException:
        print(f"Timeout waiting for element: {value}")
        return None

def get_book_info():
    try:
        # Initialize the driver
        driver = setup_driver()
        
        # Navigate to the search page
        url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
        print(f"Navigating to {url}")
        driver.get(url)
        
        # Initialize results list
        results = []
        page_num = 1
        max_retries = 3
        
        while True:
            print(f"\nProcessing page {page_num}...")
            
            # Wait for search results with retry logic
            retry_count = 0
            while retry_count < max_retries:
                try:
                    # Wait for the search results container
                    search_results = wait_for_element(driver, By.CLASS_NAME, "cp-search-results-list")
                    if search_results:
                        break
                    retry_count += 1
                    print(f"Retry {retry_count} of {max_retries}...")
                    time.sleep(5)  # Wait before retrying
                except Exception as e:
                    print(f"Error waiting for search results: {str(e)}")
                    retry_count += 1
                    if retry_count == max_retries:
                        raise
            
            # Find all search result items on current page
            result_items = driver.find_elements(By.CSS_SELECTOR, "li.cp-search-result-item")
            print(f"Found {len(result_items)} results on page {page_num}")
            
            if not result_items:
                print("No results found on this page")
                break
            
            # Process each result on the current page
            for i, item in enumerate(result_items, 1):
                try:
                    print(f"Processing result {i} on page {page_num}...")
                    
                    # Get title with explicit wait
                    title_element = wait_for_element(item, By.CLASS_NAME, "title-content")
                    title = title_element.text if title_element else "No title found"
                    print(f"Found title: {title}")
                    
                    # Get authors
                    authors = []
                    author_elements = item.find_elements(By.CLASS_NAME, "author-name")
                    for author in author_elements:
                        if author.text:
                            authors.append(author.text)
                    author_text = "; ".join(authors) if authors else "No author found"
                    print(f"Found authors: {author_text}")
                    
                    # Get format and year
                    details_element = wait_for_element(item, By.CLASS_NAME, "cp-search-result-item-details")
                    details = details_element.text if details_element else "No details found"
                    print(f"Found details: {details}")
                    
                    # Create dictionary for this result
                    book_info = {
                        "Title": title,
                        "Author": author_text,
                        "Format-Year": details
                    }
                    
                    # Add to results list
                    results.append(book_info)
                    
                except Exception as e:
                    print(f"Error processing item {i} on page {page_num}: {str(e)}")
                    continue
            
            # Check for next page button
            try:
                next_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Next page']")
                if not next_button.is_enabled():
                    print("No more pages available")
                    break
                    
                print("Moving to next page...")
                next_button.click()
                
                # Add a delay between pages
                time.sleep(5)  # Increased delay to 5 seconds
                page_num += 1
                
            except NoSuchElementException:
                print("No more pages available")
                break
            except Exception as e:
                print(f"Error navigating to next page: {str(e)}")
                break
        
        # Create DataFrame
        if results:
            df = pd.DataFrame(results)
            print("\nDataFrame created successfully!")
            print(f"\nTotal books collected: {len(df)}")
            print("\nFirst few rows of the DataFrame:")
            print(df.head())
            
            # Save to CSV
            try:
                df.to_csv("book_results.csv", index=False, encoding='utf-8')
                print("\nResults saved to book_results.csv")
            except Exception as e:
                print(f"Error saving CSV file: {str(e)}")
            
            # Save to JSON
            try:
                with open("book_results.json", "w", encoding="utf-8") as f:
                    json.dump(results, f, indent=4, ensure_ascii=False)
                print("Results saved to book_results.json")
            except Exception as e:
                print(f"Error saving JSON file: {str(e)}")
            
            return df
        else:
            print("No results were collected")
            return None
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        print(f"Error details: {sys.exc_info()}")
        return None
        
    finally:
        if 'driver' in locals():
            driver.quit()
            print("\nBrowser closed.")

if __name__ == "__main__":
    print("Starting book information collection...")
    df = get_book_info()
    if df is not None:
        print("\nTotal books collected:", len(df))