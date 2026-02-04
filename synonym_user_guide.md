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

To verify that the application is working correctly:

1.  Check that the results area is visible and contains chips with words (e.g., `rapid`, `quick`).
2.  Click on any of the result chips (for example, `rapid`) to automatically trigger a new search for that term.
