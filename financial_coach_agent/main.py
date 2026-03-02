"""Financial Coach Agent - AI Personal Finance Advisor."""

import argparse
import asyncio
import json
import os
import sys
import traceback
from pathlib import Path
from textwrap import dedent
from typing import Any, cast

from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from bindu.penguin.bindufy import bindufy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Global variables
agent: Agent | None = None
_initialized = False
_init_lock = asyncio.Lock()


class AgentNotInitializedError(RuntimeError):
    """Raised when agent is accessed before initialization."""
    pass


def load_config() -> dict[str, Any]:
    """Load agent config from `agent_config.json` or return defaults."""
    config_path = Path(__file__).parent / "agent_config.json"

    if config_path.exists():
        try:
            with open(config_path) as f:
                return cast(dict[str, Any], json.load(f))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"⚠️  Failed to load config from {config_path}: {exc}")

    return {
        "name": "financial-coach-agent",
        "description": "AI personal finance coach and financial wellness advisor",
        "version": "1.0.0",
        "deployment": {
            "url": "http://127.0.0.1:3773",
            "expose": True,
            "protocol_version": "1.0.0",
            "proxy_urls": ["127.0.0.1"],
            "cors_origins": ["*"],
        },
        "environment_variables": [
            {"key": "OPENROUTER_API_KEY", "description": "OpenRouter API key for LLM calls", "required": True},
        ],
    }


async def initialize_agent() -> None:
    """Initialize the financial coach agent with proper model and tools."""
    global agent

    # Get API keys from environment
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    model_name = os.getenv("MODEL_NAME", "openai/gpt-4o")

    if not openrouter_api_key:
        raise ValueError("OPENROUTER_API_KEY is required")

    # Create the financial coach agent
    agent = Agent(
        name="Financial Coach",
        model=OpenRouter(
            id=model_name,
            api_key=openrouter_api_key,
            cache_response=True,
            supports_native_structured_outputs=True,
        ),
        tools=[],
        description=dedent("""\
            You are an experienced AI Financial Coach and Personal Finance Advisor.
            
            Your goal is to help users develop healthy financial habits, create effective budgets,
            manage debt wisely, and build financial literacy through personalized coaching.
        """),
        instructions=dedent("""\
            CRITICAL COACHING GUIDELINES - FOLLOW EXACTLY:
            
            1. **ALWAYS provide educational guidance** - Focus on teaching concepts and strategies
            2. **NEVER give specific investment recommendations** - No stock picks, no specific products
            3. **INCLUDE clear disclaimers** - Always mention not certified financial advisor
            4. **PROVIDE actionable steps** - Give clear, step-by-step guidance
            5. **FOCUS on education** - Explain financial concepts clearly
            6. **USE markdown formatting** - Structure responses clearly with headers and bullet points
            
            CONTENT GUIDELINES:
            - Start with clear title using # heading
            - Use bullet points with hyphens (-) for lists
            - Provide step-by-step strategies and action plans
            - Include educational explanations of financial concepts
            - Offer budget templates and frameworks users can customize
            - End with encouragement and next steps
            
            ABSOLUTELY FORBIDDEN:
            - Specific stock, cryptocurrency, or investment recommendations
            - Tax preparation or legal advice
            - Insurance product recommendations
            - Certified financial advice
            - Promises of guaranteed returns
        """),
        add_datetime_to_context=True,
        markdown=True,
        debug_mode=True,
    )
    print("✅ Financial Coach Agent initialized")


async def run_agent(messages: list[dict[str, str]]) -> Any:
    """Run the financial coach agent with given messages."""
    global agent
    if not agent:
        raise AgentNotInitializedError
    result = agent.run(messages)
    return result


async def handler(messages: list[dict[str, str]]) -> Any:
    """Handle incoming agent messages with lazy initialization."""
    global _initialized

    # Lazy initialization on first call
    async with _init_lock:
        if not _initialized:
            print("🔧 Initializing Financial Coach Agent...")
            await initialize_agent()
            _initialized = True

    # Run the async agent
    result = await run_agent(messages)
    return result


async def cleanup() -> None:
    """Clean up any resources."""
    print("🧹 Cleaning up Financial Coach Agent resources...")


def main():
    """Run the main entry point for the Financial Coach Agent."""
    parser = argparse.ArgumentParser(description="Bindu Financial Coach Agent")
    parser.add_argument(
        "--openrouter-api-key",
        type=str,
        default=os.getenv("OPENROUTER_API_KEY"),
        help="OpenRouter API key (env: OPENROUTER_API_KEY)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=os.getenv("MODEL_NAME", "openai/gpt-4o"),
        help="Model ID for OpenRouter (env: MODEL_NAME)",
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to agent_config.json (optional)",
    )
    args = parser.parse_args()

    # Set environment variables if provided via CLI
    if args.openrouter_api_key:
        os.environ["OPENROUTER_API_KEY"] = args.openrouter_api_key
    if args.model:
        os.environ["MODEL_NAME"] = args.model

    print("🤖 Financial Coach Agent - AI Personal Finance Advisor")
    print("💰 Capabilities: Budget Planning, Debt Management, Financial Education")

    # Load configuration
    config = load_config()

    try:
        # Bindufy and start the agent server
        print("🚀 Starting Bindu Financial Coach Agent server...")
        print(f"🌐 Server will run on: {config.get('deployment', {}).get('url', 'http://127.0.0.1:3773')}")
        bindufy(config, handler)
    except KeyboardInterrupt:
        print("\n🛑 Financial Coach Agent stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
        traceback.print_exc()
        sys.exit(1)
    finally:
        # Cleanup on exit
        asyncio.run(cleanup())


if __name__ == "__main__":
    main()
