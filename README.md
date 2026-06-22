# Trader Journal MCP

AI-powered trading analytics and coaching platform built with FastAPI, SQLite, and MCP.

## Overview

Trader Journal MCP helps traders discover their trading edge by analyzing historical trades and exposing insights through an MCP server that can be used by AI assistants.

Instead of only recording trades, the system identifies:

- Best-performing strategies
- Best-performing setups
- Emotional trading patterns
- Drawdown and recovery metrics
- Trading expectancy
- Risk-reward performance
- Behavioral mistakes such as revenge trading and overtrading

The ultimate goal is to provide an AI Trading Coach that helps traders improve decision-making based on real historical data.

---

## Architecture

MT5 CSV
↓
Importer
↓
SQLite Database
↓
Analytics Engine
↓
FastAPI API
↓
MCP Server
↓
AI Assistant

---

## Features

### Performance Analytics

- Trading Summary
- Expectancy Analysis
- Risk-Reward Analysis
- Monthly Performance
- Drawdown Analysis
- Equity Curve

### Behavioral Analytics

- Revenge Trading Detection
- Overtrading Detection

### Context Analytics

- Pair Performance
- Session Performance
- Day of Week Analysis
- Trade Duration Analysis
- Strategy Performance
- Emotion Performance
- Setup Performance
- Strategy + Emotion Analysis

### AI Trading Coach

The AI coach combines all analytics and identifies:

- Strongest trading edge
- Weakest trading behavior
- Best strategy
- Best setup
- Best emotional state
- Personalized recommendations

---

## API Endpoints

### Performance

- GET /api/v1/performance/summary
- GET /api/v1/performance/expectancy
- GET /api/v1/performance/risk-reward
- GET /api/v1/performance/drawdown
- GET /api/v1/performance/equity-curve
- GET /api/v1/performance/coach

### Behavior

- GET /api/v1/behavior/revenge-trading
- GET /api/v1/behavior/overtrading

### Context

- GET /api/v1/context/pairs
- GET /api/v1/context/sessions
- GET /api/v1/context/days
- GET /api/v1/context/duration
- GET /api/v1/context/strategies
- GET /api/v1/context/emotions
- GET /api/v1/context/setups
- GET /api/v1/context/monthly
- GET /api/v1/context/strategy-emotions

---

## MCP Tools

### Performance

- get_summary()
- get_expectancy()
- get_risk_reward()
- get_monthly_performance()
- get_drawdown_analysis()
- get_equity_curve()

### Behavior

- detect_revenge_trading()
- detect_overtrading()

### Context

- get_session_analysis()
- get_strategy_performance()
- get_emotion_performance()
- get_setup_performance()
- get_strategy_emotion_performance()

### AI Coach

- analyze_my_edge()

---

## Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pandas
- FastMCP
- HTTPX

---

## Future Roadmap

- Live MT5 integration
- Automated trade journaling
- Equity curve visualizations
- AI trade reviews
- Trade screenshots
- RAG-powered trading memory
- Portfolio analytics
- Multi-account support
- Telegram integration
- Voice-based trading coach

---

## Author

Cephars Bonacci