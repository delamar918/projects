    # Balancing Your Budget with Python
    #### Author: Mariel Dela Cruz
    #### Completed and submitted: May 5, 2023
    #### Video Demo:  https://youtu.be/7uY_9PdxLVA
    #### Description:
    This program presents a simple tool that allows the user to get an idea of whether or not he or she is on budget for the current month.

    #### Program Functions
    The program has 3 functions.

    1. The first function asks the user to enter his or her budget for 4 different categories: housing, utilities, food and miscellaneous. The program converts inputs into integers so any input that cannot be converted to an integer will raise a TypeError error.

    2. The second function asks the user for expenses for each of the 4 categories. The user can add as many expenses as possible. The while loop creates a running total of all expenses entered for each of the four categories. Similarly, the program also converts expense inputs into integers and would raise a TypeError if the input cannot be converted into an integer.

    3. Once the user is done inputting expenses, the program asks the user if he or she would like an itemized summary or not. If the user says yes to itemization, the program will produce a line summary for each category, stating whether or not the user is under budget, over budget or at budget and by how much. Itemization will also order categories from most under budget to most over budget. The itemize_it function creates a dictionary that contains the 4 expense categories and their corresponding remainders (budget minus expense). This dictionary is returned back to the main() function. If the user chooses not to have an itemized summary, the program will show a line summary that shows the difference between the total budget and total expenses.


