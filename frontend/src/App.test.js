import { render, screen } from '@testing-library/react';
import App from './App';

test('renders macd backtest heading', () => {
  render(<App />);
  const headingElement = screen.getByText(/macd backtest/i);
  expect(headingElement).toBeInTheDocument();
});
