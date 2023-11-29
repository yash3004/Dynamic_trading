from flask import Flask, render_template, request
import yfinance as yf
import plotly.graph_objs as go

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stock_chart', methods=['POST'])
def stock_chart():
    if request.method == 'POST':
        ticker = request.form['ticker']
        data = yf.download(ticker, period='1y')

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name=f'{ticker} Close Price'))
        fig.update_layout(title=f'{ticker} Stock Chart', xaxis_title='Date', yaxis_title='Price')

        graph = fig.to_html(full_html=False)
        return render_template('stock_chart.html', graph=graph)

if __name__ == '__main__':
    app.run(debug=True)
