"""trading_analyst_agent for proposing trading strategies"""

TRADING_ANALYST_PROMPT = """
**Objective**: Develop at least five distinct trading strategies based on the provided inputs.

**Inputs**:
* **User Risk Attitude**: {user_risk_attitude}
* **User Investment Period**: {user_investment_period}
* **Market Analysis**: {market_data_analysis_output}

---

**Example Strategies**:

**Strategy 1: Conservative Dividend Growth**
* **Description**: Focus on blue-chip stocks with a history of consistent dividend growth.
* **Alignment**: Suitable for conservative, long-term investors.
* **Indicators**: P/E ratio, dividend yield, payout ratio.
* **Entry**: Buy during market dips.
* **Exit**: Hold for long-term growth; re-evaluate if the dividend is cut.
* **Risks**: Market risk, interest rate risk.

**Strategy 2: Aggressive Tech Momentum**
* **Description**: Capitalize on short-term price movements in high-growth tech stocks.
* **Alignment**: Suitable for aggressive, short-term investors.
* **Indicators**: RSI, MACD, trading volume.
* **Entry**: Buy when a stock breaks above a key resistance level.
* **Exit**: Sell when momentum indicators show a reversal.
* **Risks**: High volatility, market sentiment shifts.

---

**Task**: Generate five new, distinct strategies based on the provided market data and user inputs. Ensure each strategy includes a description, alignment with user profile, key indicators, entry/exit points, and potential risks.
"""