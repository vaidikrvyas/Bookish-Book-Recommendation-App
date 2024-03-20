# Bookish: Book Recommendation System

## Overview
Bookish is a book recommendation system that helps users find new books based on their reading history. The system uses collaborative filtering to recommend books that similar users have liked.

## Features
- User-based recommendation: Suggests books based on the user's past reading habits.
- Large dataset: Utilizes the 'BX-Books', 'BX-Users', and 'BX-Book-Ratings' datasets for a comprehensive book list and user ratings.
- Simple GUI: A user-friendly graphical interface that allows users to easily search for and get recommendations.

## Technologies Used
- Python
- Pandas for data manipulation
- Scikit-learn for the Nearest Neighbors algorithm
- Tkinter for the GUI

## How to Run
1. Ensure you have Python installed on your computer.
2. Install the required Python packages: `pandas`, `scipy`, `sklearn`, `tkinter`.
3. Download the 'BX-Books.csv', 'BX-Users.csv', and 'BX-Book-Ratings.csv' files and place them in the same directory as the script.
4. Run the script: `python "Bookish (Book Recommendation System).py"`.

## How It Works
1. The system reads data from the provided CSV files containing books, users, and ratings.
2. It preprocesses the data to filter out users with fewer than 200 ratings and books with fewer than 50 ratings.
3. A pivot table is created to form a matrix of books and user ratings.
4. The matrix is then fed into a Nearest Neighbors model to find similar books.
5. Users can enter a book title in the GUI, and the system will display the top 5 recommendations.

## Future Work
- Improve the recommendation algorithm by implementing matrix factorization.
- Enhance the GUI with more features like user login and rating books directly from the interface.
- Expand the dataset for more comprehensive recommendations.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Thanks to the creators of the BX-Datasets for providing the data used in this project.
