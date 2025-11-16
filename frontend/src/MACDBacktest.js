import React, { useState } from 'react';
import axios from 'axios';

function MACDBacktest() {
    const [ticker, setTicker] = useState('AAPL');
    const [startDate, setStartDate] = useState('2020-01-01');
    const [endDate, setEndDate] = useState('2021-01-01');
    const [ma1, setMa1] = useState(10);
    const [ma2, setMa2] = useState(21);
    const [plot, setPlot] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/api/macd/', {
                ticker,
                start_date: startDate,
                end_date: endDate,
                ma1,
                ma2,
            });
            setPlot(response.data.plot);
        } catch (error) {
            console.error('Error running backtest:', error);
        }
    };

    return (
        <div>
            <h1>MACD Backtest</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    Ticker:
                    <input type="text" value={ticker} onChange={(e) => setTicker(e.target.value)} />
                </label>
                <label>
                    Start Date:
                    <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} />
                </label>
                <label>
                    End Date:
                    <input type="date" value={endDate} onChange={(e) => setEndDate(e.target.value)} />
                </label>
                <label>
                    MA1:
                    <input type="number" value={ma1} onChange={(e) => setMa1(e.target.value)} />
                </label>
                <label>
                    MA2:
                    <input type="number" value={ma2} onChange={(e) => setMa2(e.target.value)} />
                </label>
                <button type="submit">Run Backtest</button>
            </form>
            {plot && <img src={`data:image/png;base64,${plot}`} alt="Backtest Plot" />}
        </div>
    );
}

export default MACDBacktest;
