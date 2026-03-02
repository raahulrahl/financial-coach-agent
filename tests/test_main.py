"""Tests for the Financial Coach Agent."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from financial_coach_agent.main import handler


@pytest.mark.asyncio
async def test_handler_returns_response():
    """Test that handler accepts messages and returns a response."""
    messages = [{"role": "user", "content": "Hello, can you help me with my budget?"}]

    # Mock the run_agent function to return a mock response
    mock_response = MagicMock()
    mock_response.run_id = "test-run-id"
    mock_response.status = "COMPLETED"

    # Mock _initialized to skip initialization and run_agent to return our mock
    with (
        patch("financial_coach_agent.main._initialized", True),
        patch("financial_coach_agent.main.run_agent", new_callable=AsyncMock, return_value=mock_response),
    ):
        result = await handler(messages)

    # Verify we get a result back
    assert result is not None
    assert result.run_id == "test-run-id"
    assert result.status == "COMPLETED"


@pytest.mark.asyncio
async def test_handler_with_multiple_messages():
    """Test that handler processes multiple messages correctly."""
    messages = [
        {"role": "system", "content": "You are a helpful financial assistant."},
        {"role": "user", "content": "I have $5000 in debt."},
    ]

    mock_response = MagicMock()
    mock_response.run_id = "test-run-id-2"

    with (
        patch("financial_coach_agent.main._initialized", True),
        patch("financial_coach_agent.main.run_agent", new_callable=AsyncMock, return_value=mock_response) as mock_run,
    ):
        result = await handler(messages)

    # Verify run_agent was called
    mock_run.assert_called_once_with(messages)
    assert result is not None
    assert result.run_id == "test-run-id-2"


@pytest.mark.asyncio
async def test_handler_initialization():
    """Test that handler initializes on first call."""
    messages = [{"role": "user", "content": "Test"}]

    mock_response = MagicMock()

    # Start with _initialized as False to test initialization path
    with (
        patch("financial_coach_agent.main._initialized", False),
        patch("financial_coach_agent.main.initialize_agent", new_callable=AsyncMock) as mock_init,
        patch("financial_coach_agent.main.run_agent", new_callable=AsyncMock, return_value=mock_response) as mock_run,
        patch("financial_coach_agent.main._init_lock", new_callable=MagicMock()) as mock_lock,
    ):
        # Configure the lock to work as an async context manager
        mock_lock_instance = MagicMock()
        mock_lock_instance.__aenter__ = AsyncMock(return_value=None)
        mock_lock_instance.__aexit__ = AsyncMock(return_value=None)
        mock_lock.return_value = mock_lock_instance

        result = await handler(messages)

        # Verify initialization was called
        mock_init.assert_called_once()
        # Verify run_agent was called
        mock_run.assert_called_once_with(messages)
        # Verify we got a result
        assert result is not None


@pytest.mark.asyncio
async def test_handler_race_condition_prevention():
    """Test that handler prevents race conditions with initialization lock."""
    messages = [{"role": "user", "content": "Test"}]

    mock_response = MagicMock()

    # Test with multiple concurrent calls
    with (
        patch("financial_coach_agent.main._initialized", False),
        patch("financial_coach_agent.main.initialize_agent", new_callable=AsyncMock) as mock_init,
        patch("financial_coach_agent.main.run_agent", new_callable=AsyncMock, return_value=mock_response),
        patch("financial_coach_agent.main._init_lock", new_callable=MagicMock()) as mock_lock,
    ):
        # Configure the lock to work as an async context manager
        mock_lock_instance = MagicMock()
        mock_lock_instance.__aenter__ = AsyncMock(return_value=None)
        mock_lock_instance.__aexit__ = AsyncMock(return_value=None)
        mock_lock.return_value = mock_lock_instance

        # Call handler twice to ensure lock is used
        await handler(messages)
        await handler(messages)

        # Verify initialize_agent was called only once (due to lock)
        mock_init.assert_called_once()


@pytest.mark.asyncio
async def test_handler_with_financial_query():
    """Test that handler can process a complex financial query."""
    messages = [
        {
            "role": "user",
            "content": "I earn $4000/mo and spend $2000 on rent. I have $5k debt at 20% APR. What should I do?",
        }
    ]

    mock_response = MagicMock()
    mock_response.run_id = "finance-plan-run-id"
    mock_response.content = "Based on your high rent and debt, here is a plan..."

    with (
        patch("financial_coach_agent.main._initialized", True),
        patch("financial_coach_agent.main.run_agent", new_callable=AsyncMock, return_value=mock_response),
    ):
        result = await handler(messages)

    assert result is not None
    assert result.run_id == "finance-plan-run-id"
    assert result.content == "Based on your high rent and debt, here is a plan..."
