# Dynamic_trading
Flask Based project for stock trading
Sure, here's an example of a README file you could include with your Flask app for the stock charts viewer:

---

# Stock Charts Viewer using Flask and Yahoo Finance API

This Flask application provides a simple web interface to visualize stock charts using the Yahoo Finance API and Plotly library.

## Prerequisites

Before running the application, ensure you have Python installed on your system. You'll also need to install the required Python libraries:

```bash
pip install Flask plotly yfinance
```

## Usage

1. Clone or download this repository to your local machine.
2. Navigate to the project directory.
3. Run the Flask app:

    ```bash
    python app.py
    ```

4. Open a web browser and go to `http://127.0.0.1:5000/`.
5. Enter a stock ticker symbol in the provided form and click "Show Chart" to view the stock's closing price chart for the past year.

## File Structure

- `app.py`: Main Flask application file containing routes and logic to fetch and display stock charts.
- `templates/`: Directory containing HTML templates for the user interface.
  - `index.html`: Homepage with a form to enter stock ticker symbols.
  - `stock_chart.html`: Template to display the stock chart.

## Dependencies

- Flask: Web framework for creating the application.
- Plotly: Library for creating interactive and visually appealing charts.
- yfinance: Python module to fetch stock data from Yahoo Finance.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- This application uses the Yahoo Finance API for fetching stock data.
- Special thanks to the Plotly and Flask communities for their libraries and resources.

---

Feel free to adjust and expand this README to include any additional instructions, acknowledgments, or information specific to your application.