from mcp.server.fastmcp import FastMCP
import httpx
import os

mcp = FastMCP("Trader Journal MCP")

BASE_URL = "http://127.0.0.1:8000/api/v1"


@mcp.tool()
async def get_expectancy():
    """Get trading expectancy metrics."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/performance/expectancy"
        )
        return response.json()


@mcp.tool()
async def get_summary():
    """Get overall trading performance summary."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/performance/summary"
        )
        return response.json()


@mcp.tool()
async def get_risk_reward():
    """Get risk-reward metrics."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/performance/risk-reward"
        )
        return response.json()


@mcp.tool()
async def get_session_analysis():
    """Analyze performance by trading session."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/context/sessions"
        )
        return response.json()


@mcp.tool()
async def detect_revenge_trading():
    """Detect revenge trading behavior."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/behavior/revenge-trading"
        )
        return response.json()


@mcp.tool()
async def detect_overtrading():
    """Detect overtrading behavior."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/behavior/overtrading"
        )
        return response.json()
    
@mcp.tool()
async def get_strategy_performance():
    """Analyze trading performance by strategy."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/context/strategies"
        )
        return response.json()   

@mcp.tool()
async def get_emotion_performance():
    """Analyze trading performance by emotion."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/context/emotions"
        )
        return response.json()     
        
    
@mcp.tool()
async def get_setup_performance():
    """Analyze trading performance by setup."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/context/setups"
        )
        return response.json()
    
    
@mcp.tool()
async def get_monthly_performance():
    """Analyze trading performance by month."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/context/monthly"
        )
        return response.json()
    
    
    
@mcp.tool()
async def get_drawdown_analysis():
    """Analyze drawdown metrics."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/performance/drawdown"
        )
        return response.json()
    
@mcp.tool()
async def get_strategy_emotion_performance():
    """Analyze performance by strategy and emotion combination."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/context/strategy-emotions"
        )
        return response.json()   

@mcp.tool()
async def get_equity_curve():
    """Get trade-by-trade equity curve."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/performance/equity-curve"
        )
        return response.json() 
    
@mcp.tool()
async def analyze_my_edge():
    """Generate an AI trading coach summary of performance, edge, weaknesses, and recommendations."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/performance/coach"
        )
        return response.json()   
    

@mcp.tool()
async def get_trading_coach_report():
    """Generate a human-readable trading coach report."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/performance/coach-report"
        )
        return response.json() 
    
    
@mcp.tool()
async def analyze_trade_notes():
    """Analyze trade notes for behavioral patterns such as FOMO, early entry, revenge, discipline, fear, and confidence."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/behavior/trade-notes"
        )
        return response.json()
    

@mcp.tool()
async def get_behavioral_insights():
    """Generate behavioral trading insights from trade notes."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/behavior/insights"
        )
        return response.json()    


@mcp.tool()
async def health_check():
    """Check if the MCP server is running."""
    return {"status": "MCP server is running 🚀"}


@mcp.tool()
async def import_status():
    """Check whether the trading database exists."""
    return {
        "database_exists": os.path.exists("db/trader_journal.db"),
        "message": "Use the FastAPI upload endpoint to import MT5 CSV files."
    }


if __name__ == "__main__":
    print("🚀 MCP Server starting... waiting for client connection")
    mcp.run()