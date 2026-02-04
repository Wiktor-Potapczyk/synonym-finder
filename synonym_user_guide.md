# How to Find Synonyms

While a general dictionary helps you understand meanings, the Synonym Finder provides instructions on how to quickly discover alternative words to enhance your writing or speech.

Use this app when you need to avoid repetition or find a more precise word for your context.

## Prerequisites

- Ensure the **Synonym Finder** application is running locally.
- Ensure you have a web browser installed (Chrome, Firefox, or Edge).

## Procedure

To find synonyms for a specific word:

1.  Open your web browser and navigate to `http://127.0.0.1:5000`.
2.  In the "Synonym Finder" card, locate the input field labeled "Enter a word".
3.  Type the word you want to find synonyms for (for example, `fast`).
4.  Click the **Find Synonyms** button.
    
    The application connects to the database and retrieves a list of related words.

5.  Review the results displayed in the "Synonyms for..." section.

![Synonym Search Results](images/synonym_results.png)

## Validation

To verify that the application is working correctly and meets all requirements:

### 1. Verify Result Count
1.  Enter a common word (e.g., `happy`).
2.  Click the **Find Synonyms** button.
3.  Ensure the list contains between **3 and 10 synonyms**.

### 2. Test Word Combinations
1.  Enter a phrase such as `big house` (Note: Single words are best supported).
2.  Verify the app handles the input gracefully (e.g., by sanitizing or attempting search).

### 3. Perform Negative Testing
1.  Clear the input field.
2.  Click **Find Synonyms**.
3.  Confirm the app displays a clear prompt or error (e.g., "Word is required") and does not crash.

### 4. Simulate Connectivity Issues
1.  Briefly disconnect from the network.
2.  Attempt a search.
3.  Verify the app displays an error message explaining the connection issue (timeout or network error).
