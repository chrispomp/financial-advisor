"""trading_analyst_agent for proposing trading strategies"""

TRADING_ANALYST_PROMPT = """
Develop at least five distinct trading strategies based on the provided market
analysis, user risk attitude, and investment period.

**User Risk Attitude**: {user_risk_attitude}
**User Investment Period**: {user_investment_period}
**Market Analysis**: {market_data_analysis_output}

Here are some examples of what a trading strategy might look like:

**Strategy 1: Conservative Dividend Growth**
- **Description**: Focus on blue-chip stocks with a history of consistent dividend growth.
- **Alignment**: Suitable for conservative, long-term investors.
- **Indicators**: P/E ratio, dividend yield, and payout ratio.
- **Entry**: Buy during market dips.
- **Exit**: Hold for long-term growth, re-evaluate if dividend is cut.
- **Risks**: Market risk, interest rate risk.

**Strategy 2: Aggressive Tech Momentum**
- **Description**: Capitalize on short-term price movements in high-growth tech stocks.
- **Alignment**: Suitable for aggressive, short-term investors.
- **Indicators**: RSI, MACD, and trading volume.
- **Entry**: Buy when a stock breaks above a key resistance level.
- **Exit**: Sell when momentum indicators show a reversal.
- **Risks**: High volatility, market sentiment shifts.

Now, generate five new strategies based on the provided market data.
"""