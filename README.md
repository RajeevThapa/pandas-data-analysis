# Excel Data Analysis with Pandas

This Python script analyzes data from an Excel file and generates a CSV file containing the percentages of responses for each question.

## Overview

The script reads an Excel file with survey data, calculates the percentage of each response for each question, and outputs the results to a CSV file.

## Dependencies

- Python 3.x
- pandas

## Installation

1. Clone the repository to your local machine:

    ```
    git clone <repository_url.git>
    ```

2. Install the required dependencies using pip:

    ```
    pip install pandas
    ```

## Usage

1. Ensure that your Excel file (`sample.xlsx`) is in the same directory as the Python script.
2. Run the script using the following command:

    ```
    python data_analysis.py
    ```

3. After execution, the script will generate a CSV file named `response_percentages.csv` containing the results.

## Input

- `sample.xlsx`: Excel file containing survey data. The data should be organized such that each column represents a question, and each row represents a respondent's answer to those questions.

## Output

- `response_percentages.csv`: CSV file containing the percentages of responses for each question.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
