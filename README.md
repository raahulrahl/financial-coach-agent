<p align="center">
  <img src="https://raw.githubusercontent.com/getbindu/create-bindu-agent/refs/heads/main/assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center">financial-coach-agent</h1>

<p align="center">
  <strong>AI-powered personal finance coach that provides comprehensive financial guidance, budget planning, debt management strategies, and investment education. Helps users develop healthy financial habits and make informed money decisions through personalized coaching and actionable insights.</strong>
</p>

<p align="center">
  <a href="https://github.com/Paraschamoli/financial-coach-agent/actions/workflows/main.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/Paraschamoli/financial-coach-agent/main.yml?branch=main" alt="Build status">
  </a>
  <a href="https://img.shields.io/github/license/Paraschamoli/financial-coach-agent">
    <img src="https://img.shields.io/github/license/Paraschamoli/financial-coach-agent" alt="License">
  </a>
</p>

---

## 📖 Overview

AI Financial Coach Agent is a comprehensive personal finance advisor that provides educational guidance, budget planning, debt management strategies, and investment education. Built on the [Bindu Agent Framework](https://github.com/getbindu/bindu) for Internet of Agents, it helps users develop healthy financial habits and make informed money decisions through personalized coaching and actionable insights.

**Key Capabilities:**
- 💰 **Budget Planning & Optimization** - Create personalized monthly budgets with percentage-based allocation
- 📊 **Debt Management Strategies** - Snowball vs avalanche methods with payoff timelines
- 🎯 **Savings Goal Setting** - Emergency fund planning and progress tracking
- 📚 **Financial Education** - Investment concepts, risk management, and financial literacy
- 📈 **Spending Analysis** - Identify patterns and optimize expenses
- 🛡️ **Risk Assessment** - Educational guidance on financial risks

**Educational Focus:**
- Always includes clear disclaimers about not being a certified financial advisor
- Provides step-by-step actionable strategies
- Focuses on teaching concepts rather than specific product recommendations

---

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager
- OpenRouter API key (free tier available)

### Installation

```bash
# Clone the repository
git clone https://github.com/Paraschamoli/financial-coach-agent.git
cd financial-coach-agent

# Create virtual environment
uv venv --python 3.12
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync

# Configure environment
cp .env.example .env
```

### Configuration

Edit `.env` and add your API key:

| Key | Get It From | Required |
|-----|-------------|----------|
| `OPENROUTER_API_KEY` | [OpenRouter](https://openrouter.ai/keys) | ✅ Yes |

### Run Agent

```bash
# Start the agent
uv run -m financial_coach_agent

# Agent will be available at http://localhost:3773
```

---

## 💡 Usage

### Example Queries

```bash
# Example query 1 - Budget Planning
"help me create a monthly budget for $5,200 income with rent $1,500, utilities $250, groceries $600"

# Example query 2 - Debt Management
"what's the best strategy to pay off $8,000 credit card debt at 22% interest"

# Example query 3 - Investment Education
"how can I start investing with $100 and what are index funds"

# Example query 4 - Savings Planning
"I earn $5,200 monthly, how much should I save for emergency fund and retirement"
```

### Input Formats

**Plain Text:**
```
Natural language queries about personal finance, budgeting, debt management, or investment education.
Examples:
- "help me create a budget"
- "what's the best way to pay off credit card debt"
- "teach me about index funds"
```

**JSON:**
```json
{
  "content": "Create a monthly budget for $5,200 income",
  "focus": "budget-planning"
}
```

### Output Structure

The agent returns structured financial coaching with:
- **📊 Budget Framework**: Percentage-based allocation with categories
- **🎯 Debt Strategies**: Snowball vs avalanche methods with timelines
- **📚 Educational Content**: Clear explanations of financial concepts
- **⚠️ Disclaimers**: Always mentions not a certified financial advisor
- **📈 Action Steps**: Step-by-step guidance and next steps

---

## 🔌 API Usage

The agent exposes a RESTful API when running. Default endpoint: `http://localhost:3773`

### Quick Start

For complete API documentation, request/response formats, and examples, visit:

📚 **[Bindu API Reference - Send Message to Agent](https://docs.getbindu.com/api-reference/all-the-tasks/send-message-to-agent)**

### Additional Resources

- 📖 [Full API Documentation](https://docs.getbindu.com/api-reference/all-the-tasks/send-message-to-agent)
- 📦 [Postman Collections](https://github.com/GetBindu/Bindu/tree/main/postman/collections)
- 🔧 [API Reference](https://docs.getbindu.com)

---

## 🎯 Skills

### financial-coach (v1.0.0)

**Primary Capability:**
- **Personalized Financial Coaching** - Comprehensive guidance for budgeting, debt management, and financial education
- **Educational Focus** - Teaching concepts and strategies without specific product recommendations
- **Risk-Aware Guidance** - Includes appropriate disclaimers and safety considerations

**Features:**
- **Budget Creation & Optimization** - Percentage-based allocation with customizable categories
- **Debt Payoff Strategies** - Snowball vs avalanche methods with timeline calculations
- **Emergency Fund Planning** - 6-month expense buffer recommendations
- **Investment Education** - Index funds, risk management, and portfolio concepts
- **Spending Pattern Analysis** - Identify habits and optimization opportunities
- **Financial Wellness Assessment** - Holistic financial health evaluation

**Best Used For:**
- Personal budget creation and optimization
- Credit card debt repayment planning
- Emergency fund goal setting
- Investment education and guidance
- Financial habit improvement
- Savings strategy development

**Not Suitable For:**
- Specific investment product recommendations
- Tax preparation or legal advice
- Insurance policy recommendations
- Complex financial planning requiring professional certification
- Guaranteed return promises

**Performance:**
- Average processing time: ~3 seconds
- Max concurrent requests: 10
- Memory per request: 256MB
- Response format: Markdown with structured sections

---

## 🐳 Docker Deployment

### Local Docker Setup

```bash
# Build and run with Docker Compose
docker-compose up --build

# Agent will be available at http://localhost:3773
```

### Docker Configuration

The agent runs on port `3773` and requires:
- `OPENROUTER_API_KEY` environment variable

Configure this in your `.env` file before running.

---

## 🌐 Deploy to bindus.directory

Make your agent discoverable worldwide and enable agent-to-agent collaboration.

### Setup GitHub Secrets

```bash
# Authenticate with GitHub
gh auth login

# Set deployment secrets
gh secret set BINDU_API_TOKEN --body "<your-bindu-api-key>"
gh secret set DOCKERHUB_TOKEN --body "<your-dockerhub-token>"
```

Get your keys:
- **Bindu API Key**: [bindus.directory](https://bindus.directory) dashboard
- **Docker Hub Token**: [Docker Hub Security Settings](https://hub.docker.com/settings/security)

### Deploy

```bash
# Push to trigger automatic deployment
git push origin main
```

GitHub Actions will automatically:
1. Build your agent
2. Create Docker container
3. Push to Docker Hub
4. Register on bindus.directory

---

## 🛠️ Development

### Project Structure

```
financial-coach-agent/
├── financial_coach_agent/
│   ├── skills/
│   │   └── financial-coach/
│   │       ├── skill.yaml          # Skill configuration
│   │       └── __init__.py
│   ├── __init__.py
│   ├── __main__.py
│   ├── main.py                     # Agent entry point
│   └── agent_config.json           # Agent configuration
├── tests/
│   └── test_main.py
├── .env.example
├── docker-compose.yml
├── Dockerfile.agent
└── pyproject.toml
```

### Running Tests

```bash
make test              # Run all tests
make test-cov          # With coverage report
```

### Code Quality

```bash
make format            # Format code with ruff
make lint              # Run linters
make check             # Format + lint + test
```

### Pre-commit Hooks

```bash
# Install pre-commit hooks
uv run pre-commit install

# Run manually
uv run pre-commit run -a
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Powered by Bindu

Built with the [Bindu Agent Framework](https://github.com/getbindu/bindu)

**Why Bindu?**
- 🌐 **Internet of Agents**: A2A, AP2, X402 protocols for agent collaboration
- ⚡ **Zero-config setup**: From idea to production in minutes
- 🛠️ **Production-ready**: Built-in deployment, monitoring, and scaling

**Build Your Own Agent:**
```bash
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
```

---

## 📚 Resources

- 📖 [Full Documentation](https://Paraschamoli.github.io/financial-coach-agent/)
- 💻 [GitHub Repository](https://github.com/Paraschamoli/financial-coach-agent/)
- 🐛 [Report Issues](https://github.com/Paraschamoli/financial-coach-agent/issues)
- 💬 [Join Discord](https://discord.gg/3w5zuYUuwt)
- 🌐 [Agent Directory](https://bindus.directory)
- 📚 [Bindu Documentation](https://docs.getbindu.com)

---

<p align="center">
  <strong>Built with 💛 by the team from Amsterdam 🌷</strong>
</p>

<p align="center">
  <a href="https://github.com/Paraschamoli/financial-coach-agent">⭐ Star this repo</a> •
  <a href="https://discord.gg/3w5zuYUuwt">💬 Join Discord</a> •
  <a href="https://bindus.directory">🌐 Agent Directory</a>
</p>
